import os
from os.path import join
import json
import yaml
import requests
from collections import defaultdict, deque
import pandas as pd
from typing import List, Dict, Any

# from acc_utils import ACCEngine, RuleUnitCallingDescriptor
from ..ifc import IFCReader


class RuleUnitCallingDescriptor:
    def __init__(self, rule_file, module_file):
        self.df = pd.read_csv(rule_file, index_col=False).drop_duplicates()
        self.module_df = pd.read_csv(
            module_file, index_col=False
        ).drop_duplicates()  # module csv 에서 가져옴. 라이브러리에서 가져오면 정보 더 많을 것. 이후 수정 필요
        self.module_df["code"] = self.module_df["code"].apply(self.convert_code_format)
        self.graph, self.reverse_graph = self.build_graph(self.df)
        self.sccs = self.tarjan_scc(self.graph)
        print("SCCs found:", self.sccs)
        self.dag, self.scc_map = self.build_scc_dag(self.sccs, self.graph)
        self.topo_order = self.topological_sort(self.dag)
        self.execution_orders = self.get_execution_orders()

    def convert_code_format(self, code):
        parts = code.split("_")
        prefix = parts[0].replace(" ", "")
        parts[1] = parts[1].replace(".", "")
        middle = "".join(["0" + char for char in parts[1]])
        suffix = "0" + parts[2][1]
        return f"{prefix}_{middle}_{suffix}"

    def build_graph(self, df):
        graph = defaultdict(list)
        reverse_graph = defaultdict(list)
        nodes = set(self.module_df["code"])

        for _, row in df.iterrows():
            if row["parent_code"] in nodes and row["child_code"] in nodes:
                graph[row["parent_code"]].append(row["child_code"])
                reverse_graph[row["child_code"]].append(row["parent_code"])

        return graph, reverse_graph

    def get_roots(self):
        roots = []
        for node in self.graph:
            if not self.reverse_graph[node]:
                roots.append(node)
        return roots

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
        resource_path,
        openapi_file="../api_server/openapi/tomok-api.yaml",
    ):
        self.var_cache = {"pass_fail": 0}
        self.openapi_spec = None
        rule_file_path = join(resource_path, rule_file)
        module_file_path = join(resource_path, module_file)
        self.rule_unit_descriptor = RuleUnitCallingDescriptor(
            rule_file_path, module_file_path
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
            else:
                self.run_unit(order)

    def run_scc(self, scc):
        while True:
            for unit in scc:
                print(f"Executing unit: {unit}")
                self.run_unit(unit)
            if self.var_cache.get("pass_fail") == -9999:
                print(f"SCC {scc} 재실행 중...")
            else:
                break

    def run_unit(self, unit):
        try:
            input_value = self.get_input_values(self.current_entity, unit)
            print(f"Input values for {unit}: {input_value}")
            path = self.get_api_path(unit)
            result = self.ruleunit_call(path, **input_value)
            for k, v in result.items():
                self.var_cache[k] = v
            print(f"API result for {unit}: {result}")
        except Exception as e:
            print(f"Error executing unit {unit}: {e}")


class ACCController:
    def __init__(
        self,
        resource_path,
        rule_file="tree_temp2.csv",
        module_file="module_temp.csv",
    ):
        self.rule_file = rule_file
        self.module_file = module_file
        self.reader = None
        self.entities = []
        self.subtype = ""
        self.flag = False
        self.engine = ACCEngine(
            rule_file=self.rule_file,
            module_file=self.module_file,
            resource_path=resource_path,
        )
        self.log = []
    
    def list_ifc_files(self):
        return os.listdir(self.ifc_dir)

    def load_ifc_file(self, ifc_filepath):
        self.reader = IFCReader(ifc_filepath)
        return self.reader is not None

    def set_subtype(self, subtype):
        self.subtype = subtype

    def search_entities(self):
        if self.reader and self.subtype:
            self.entities = self.reader.get_products_by_subtype(self.subtype)
        return self.entities

    def run_verification(self) -> List[Dict[str, Any]]:
        if not self.entities:
            return []

        self.flag = True
        results = []
        for entity_index, entity in enumerate(self.entities):
            entity_result = {"index": entity_index, "result": {"ccc_results": []}}
            self.engine.current_entity = entity  # 엔진에 현재 엔티티를 설정
            for order_index, order in enumerate(self.engine.execution_orders):
                ccc_result = {"ccc_index": order_index, "log": []}
                if isinstance(order, list):
                    while True:
                        for code in order:
                            ccc_result["log"].append(f"룰유닛 {code} 실행")
                            try:
                                input_value = self.engine.get_input_values(entity, code)
                                ccc_result["log"].append(f"입력 변수: {input_value}")
                                path = self.engine.get_api_path(code)
                                result = self.engine.ruleunit_call(path, **input_value)
                                for k, v in result.items():
                                    self.engine.var_cache[k] = v
                                ccc_result["log"].append(f"API 반환 결과: {result}")
                            except Exception as e:
                                ccc_result["log"].append(
                                    f"Error executing code {code}: {e}"
                                )
                        if self.engine.var_cache.get("pass_fail") == -9999:
                            ccc_result["log"].append("\n--- CCC 재실행 ---\n")
                        else:
                            break
                else:
                    code = order
                    ccc_result["log"].append(f"룰유닛 {code} 실행")
                    try:
                        input_value = self.engine.get_input_values(entity, code)
                        ccc_result["log"].append(f"입력 변수: {input_value}")
                        path = self.engine.get_api_path(code)
                        result = self.engine.ruleunit_call(path, **input_value)
                        for k, v in result.items():
                            self.engine.var_cache[k] = v
                        ccc_result["log"].append(f"API 반환 결과: {result}")
                    except Exception as e:
                        ccc_result["log"].append(f"Error executing code {code}: {e}")
                entity_result["result"]["ccc_results"].append(ccc_result)
            results.append(entity_result)
        return results

    def display_log(self, selected_entity_index):
        if selected_entity_index < len(self.log):
            return self.log[selected_entity_index]
        return []

    def get_execution_orders(self):
        return self.engine.execution_orders


# Example usage
if __name__ == "__main__":
    acc_controller = ACCController()

    # List IFC files
    ifc_files = acc_controller.list_ifc_files()
    print("Available IFC files:", ifc_files)

    # Load an IFC file
    if ifc_files:
        file_loaded = acc_controller.load_ifc_file(ifc_files[0])
        print(f"File loaded: {file_loaded}")

        # Set subtype and search entities
        acc_controller.set_subtype("RC_STIFFENINGGIRDER")
        entities = acc_controller.search_entities()
        print(f"Found entities: {entities}")

        # Specify the execution order index to run
        execution_order_index = 0  # 예시로 0번째 실행 오더를 사용
        try:
            verification_results = acc_controller.run_verification(
                execution_order_index
            )
            print("Verification results:", json.dumps(verification_results, indent=2))
        except IndexError as e:
            print(f"Error: {e}")

        # Get execution orders
        execution_orders = acc_controller.get_execution_orders()
        print("Execution orders:", execution_orders)
