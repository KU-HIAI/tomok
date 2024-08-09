from os.path import join
import requests
import yaml
from tomok import IFCReader
from collections import defaultdict, deque
import pandas as pd
import re


resource_path = "./resources"


class RuleUnitCallingDescriptor:
    def __init__(self, rule_file, module_file, target_rule):
        self.df = pd.read_csv(rule_file, index_col=False).drop_duplicates()
        self.module_df = pd.read_csv(module_file, index_col=False).drop_duplicates()
        self.module_df["code"] = self.module_df["code"].apply(self.convert_code_format)
        self.target_rule = target_rule
        self.graph, self.reverse_graph = self.build_graph(self.df)
        self.sccs = self.tarjan_scc(self.graph)
        print("SCCs found:", self.sccs)
        self.dag, self.scc_map = self.build_scc_dag(self.sccs, self.graph)
        self.topo_order = self.topological_sort(self.dag)
        self.execution_orders = self.get_execution_orders()

    def convert_code_format(self, code):
        # Convert 'KDS 24 14 21_4.1.2.3_(1)' to 'KDS241421_04010203_01'
        parts = code.split("_")
        prefix = parts[0].replace(" ", "")
        parts[1] = parts[1].replace(".", "")
        middle = "".join(["0" + char for char in parts[1]])
        suffix = "0" + parts[2][1]
        return f"{prefix}_{middle}_{suffix}"

    def build_graph(self, df):
        graph = defaultdict(list)
        reverse_graph = defaultdict(list)

        # Create nodes from module file
        nodes = set(self.module_df["code"])

        # Use rule file to create edges
        for _, row in df.iterrows():
            if row["parent_code"] in nodes and row["child_code"] in nodes:
                graph[row["parent_code"]].append(row["child_code"])
                reverse_graph[row["child_code"]].append(row["parent_code"])

        return graph, reverse_graph

    def tarjan_scc(self, graph):
        index = 0
        stack = []
        indices = {}
        lowlinks = {}
        on_stack = defaultdict(bool)
        sccs = []

        def strongconnect(node):
            nonlocal index
            indices[node] = index
            lowlinks[node] = index
            index += 1
            stack.append(node)
            on_stack[node] = True

            for neighbor in list(graph[node]):
                if neighbor not in indices:
                    strongconnect(neighbor)
                    lowlinks[node] = min(lowlinks[node], lowlinks[neighbor])
                elif on_stack[neighbor]:
                    lowlinks[node] = min(lowlinks[node], indices[neighbor])

            if lowlinks[node] == indices[node]:
                scc = []
                while True:
                    w = stack.pop()
                    on_stack[w] = False
                    scc.append(w)
                    if w == node:
                        break
                sccs.append(scc)

        for node in list(graph):
            if node not in indices:
                strongconnect(node)

        return sccs

    def build_scc_dag(self, sccs, graph):
        scc_map = {}
        for idx, scc in enumerate(sccs):
            for node in scc:
                scc_map[node] = idx

        dag = defaultdict(list)
        for node in list(graph):
            for neighbor in graph[node]:
                if scc_map[node] != scc_map[neighbor]:
                    dag[scc_map[node]].append(scc_map[neighbor])

        return dag, scc_map

    def topological_sort(self, dag):
        in_degree = {node: 0 for node in dag}
        for node in list(dag):
            for neighbor in dag[node]:
                if neighbor not in in_degree:
                    in_degree[neighbor] = 0
                in_degree[neighbor] += 1

        queue = deque([node for node in dag if in_degree[node] == 0])
        topo_order = []

        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for neighbor in dag[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(topo_order) == len(dag):
            return topo_order
        else:
            raise Exception("Graph has at least one cycle")

    def get_execution_orders(self):
        module_codes = set(self.module_df["code"])
        rule_codes = set(self.df["child_code"]) | set(self.df["parent_code"])

        independent_rules = [code for code in module_codes if code not in rule_codes]

        dependent_execution_order = []
        for scc_index in self.topo_order:
            scc = self.sccs[scc_index]
            if len(scc) > 1:
                dependent_execution_order.append(scc)
            else:
                dependent_execution_order.extend(scc)

        return independent_rules + dependent_execution_order


class ACCEngine:
    def __init__(
        self,
        rule_file,
        module_file,
        openapi_file="../api_server/openapi/tomok-api.yaml",
        target_rule="KDS241421_04010201_01",
    ):
        self.var_cache = {"pass_fail": 0}
        self.openapi_spec = None
        rule_file_path = join(resource_path, rule_file)
        module_file_path = join(resource_path, module_file)
        self.rule_unit_descriptor = RuleUnitCallingDescriptor(
            rule_file_path, module_file_path, target_rule
        )
        self.execution_orders = self.rule_unit_descriptor.execution_orders
        self.load_openapi_spec(openapi_file)

    def load_openapi_spec(self, openapi_file):
        with open(openapi_file, "r") as fp:
            self.openapi_spec = yaml.safe_load(fp)

    def get_api_path(self, code):
        temp = "/".join([code[:3].lower(), code[3:9], code[10:]])
        temp_keys = list(self.openapi_spec["paths"])
        for k in temp_keys:
            if temp in k:
                return k
        return None

    def get_properties(self, path):
        return list(
            self.openapi_spec["paths"][path]["post"]["requestBody"]["content"][
                "multipart/form-data"
            ]["schema"]["properties"].keys()
        )

    def get_input_variables(self, path):
        properties = self.get_properties(path)
        return [x for x in properties if "fI" in x]

    def get_input_values(self, entity, rule_code: str):
        def build_KRP_string(rule_code: str):
            template = "KRPset_{} {} {} {}_{} ({})"
            temp = rule_code.split("_")
            return template.format(
                temp[0][:3],
                temp[0][3:5],
                temp[0][5:7],
                temp[0][7:],
                f"{temp[1][1]}.{temp[1][3]}.{temp[1][5]}.{temp[1][7]}",
                temp[2][-1],
            )

        path = self.get_api_path(rule_code)
        krp_string = build_KRP_string(rule_code)
        input_vars = self.get_input_variables(path)

        input_values = {}
        for item in input_vars:
            input_values[item] = entity[krp_string][item]
            if input_values[item] == "":
                temp_item = item.replace("I", "O")
                if temp_item in self.var_cache:
                    input_values[item] = self.var_cache[temp_item]
                else:
                    input_values[item] = -9999
                    print(
                        "참조가 필요한 입력변수 {} 가 아직 계산되지 않음.".format(item)
                    )

        return input_values

    def get_child_code(self):
        return list(set(self.rule_unit_descriptor.df["child_code"]))

    def ruleunit_call(self, path: str, **kwargs):
        key = "f234cf784e7c9669929122343a808bcf9607e425"
        base_uri = "http://tomokapi.hiai.kr/v1.0"
        headers = {"X-Auth": key}
        api_uri = base_uri + path
        response = requests.post(api_uri, headers=headers, data=kwargs)
        return response.json()

    def run_execution_orders(self):
        for order in self.execution_orders:
            if isinstance(order, list):
                self.run_scc(order)

    def run_scc(self, scc):
        while True:
            for unit in scc:
                print(f"Executing unit: {unit}")
            if self.var_cache.get("pass_fail") == -9999:
                print(f"SCC {scc} 재실행 중...")
            else:
                break


if __name__ == "__main__":
    ifcpath = join(resource_path, "(KDS) ED_extension_case10_v2.ifc")
    reader = IFCReader(ifcpath)
    subtype = "RC_STIFFENINGGIRDER"

    engine = ACCEngine(
        rule_file="tree_temp2.csv",
        module_file="module_temp.csv",
        target_rule="KDS241421_04010201_01",
    )

    entity = reader.get_products_by_subtype(subtype)[0]

    for order in engine.execution_orders:
        if isinstance(order, list):
            while True:
                for code in order:
                    print("target code:", code)
                    try:
                        input_value = engine.get_input_values(entity, code)
                        print(input_value)
                        path = engine.get_api_path(code)
                        result = engine.ruleunit_call(path, **input_value)
                        for k, v in result.items():
                            engine.var_cache[k] = v
                        print("result", result)
                    except Exception as e:
                        print(f"Error executing code {code}: {e}")
                if engine.var_cache.get("pass_fail") == -9999:
                    print(f"SCC {order} 재실행 중...")
                else:
                    break
        else:
            code = order
            print("target code:", code)
            try:
                input_value = engine.get_input_values(entity, code)
                print(input_value)
                path = engine.get_api_path(code)
                result = engine.ruleunit_call(path, **input_value)
                for k, v in result.items():
                    engine.var_cache[k] = v
                print("result", result)
            except Exception as e:
                print(f"Error executing code {code}: {e}")
