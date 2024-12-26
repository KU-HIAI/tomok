import os
from os.path import join
import json
import yaml
import socket
import requests
import urllib.parse
from collections import defaultdict, deque
import pandas as pd
from typing import List, Dict, Any

from ..ifc import IFCReader


class RuleUnitCallingDescriptor:
    def __init__(self, rule_file, module_files):
        self.df = pd.read_csv(rule_file, index_col=False).drop_duplicates()
        self.module_dfs = [
            pd.read_csv(module_file, index_col=False).drop_duplicates()
            for module_file in module_files
        ]
        self.results = []
        for module_df in self.module_dfs:
            module_df["code"] = module_df["code"].apply(self.convert_code_format)
            graph, reverse_graph = self.build_graph(self.df, module_df)
            sccs = self.tarjan_scc(graph)

            # 모든 노드가 연결된 경우, 실행 순서에 포함되도록 처리
            if len(sccs) != len(module_df):
                sccs = self.ensure_all_nodes_in_scc(sccs, graph)

            print("SCCs found:", sccs)
            dag, scc_map = self.build_scc_dag(sccs, graph)
            topo_order = self.topological_sort(dag)
            execution_orders = self.get_execution_orders(module_df, topo_order, sccs)
            self.results.append(
                {
                    "module_df": module_df,
                    "graph": graph,
                    "reverse_graph": reverse_graph,
                    "sccs": sccs,
                    "dag": dag,
                    "scc_map": scc_map,
                    "topo_order": topo_order,
                    "execution_orders": execution_orders,
                }
            )

    def convert_code_format(self, code):
        replacements = {
            "①": "_01",
            "②": "_02",
            "③": "_03",
            "④": "_04",
            "⑤": "_05",
            "⑥": "_06",
            "⑦": "_07",
            "⑧": "_08",
            "⑨": "_09",
        }
        parts = code.split("_")
        prefix = parts[0].replace(" ", "")
        parts[1] = parts[1].split(".")
        middle = ""
        for x in parts[1]:
            if len(x) > 1:
                middle += x
            else:
                middle += "0" + x
        suffix = "0" + parts[2][1]
        if any(key in code for key in replacements):
            suffix += replacements[code[-1]]

        return f"{prefix}_{middle}_{suffix}"

    def build_graph(self, df, module_df):
        graph = defaultdict(list)
        reverse_graph = defaultdict(list)
        nodes = set(module_df["code"])

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

    def ensure_all_nodes_in_scc(self, sccs, graph):
        """
        그래프의 모든 노드가 SCC에 포함되도록 보장
        """
        all_nodes = set(graph.keys())
        scc_nodes = set(node for scc in sccs for node in scc)
        missing_nodes = all_nodes - scc_nodes

        # 모든 노드를 포함하도록 SCC 재구성
        if missing_nodes:
            sccs.append(list(missing_nodes))

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

    def get_execution_orders(self, module_df, topo_order, sccs):
        module_codes = set(module_df["code"])
        rule_codes = set(self.df["child_code"]) | set(self.df["parent_code"])

        independent_rules = [code for code in module_codes if code not in rule_codes]

        dependent_execution_order = []

        if (
            len(module_codes) == len(sccs) and len(sccs) > 1
        ):  # 순환참조가 존재하지 않으면 하나로 묶어버리기
            dependent_execution_order.append(list(module_codes))
        else:
            for scc_index in topo_order:
                scc = sccs[scc_index]
                if len(scc) > 1:
                    dependent_execution_order.append(scc)
                else:
                    dependent_execution_order.extend(scc)

        return independent_rules + dependent_execution_order


class ACCEngine:
    def __init__(
        self,
        rule_file,
        resource_path,
        module_file_path,
        ruleunit_api_url="https://tomokapi.hiai.kr/v1.0",
    ):
        self.var_cache = {"pass_fail": 0}
        self.openapi_spec = None
        
        def build_new_local_ip_url():
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
            s.close()
            parsed_url = urllib.parse.urlparse(ruleunit_api_url)
            port = parsed_url.port
            return f"http://{ip}:{port}/v1.0"
        
        # 로컬 IP 계산해서 새로운 주소 생성
        if False:
            self.ruleunit_api_url = build_new_local_ip_url()
        else:
            self.ruleunit_api_url = "https://tomokapi.hiai.kr/v1.0/"
            
        self.openapi_url = join(self.ruleunit_api_url, "openapi.json")
        rule_file_path = join(resource_path, rule_file)
        module_files = [
            join(module_file_path, f)
            for f in sorted(os.listdir(module_file_path))
            if f.endswith(".csv")
        ]
        self.rule_unit_descriptor = RuleUnitCallingDescriptor(
            rule_file_path, module_files
        )
        self.execution_orders = [
            result["execution_orders"] for result in self.rule_unit_descriptor.results
        ]
        self.openapi_spec = self.load_openapi_spec(self.openapi_url)

        self.module_names = [
            f.split("_")[-1].replace(".csv", "")
            for f in sorted(os.listdir(module_file_path))
            if f.endswith(".csv")
        ]
        self.ruleunit_api_url = ruleunit_api_url

    def load_openapi_spec(self, openapi_url):
        import requests

        try:
            response = requests.get(openapi_url)
            response.raise_for_status()
            openapi_spec = response.json()
            return openapi_spec
        except requests.exceptions.RequestException as e:
            print(f"Error fetching OpenAPI spec: {e}")
            return {}

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
            replacements = {
                "01": " ①",
                "02": " ②",
                "03": " ③",
                "04": " ④",
                "05": " ⑤",
                "06": " ⑥",
                "07": " ⑦",
                "08": " ⑧",
                "09": " ⑨",
            }
            temp = rule_code.split("_")
            template = "KRPset_{} {} {} {}_{} ({})"
            if len(temp[1]) > 6:
                code = template.format(
                    temp[0][:3],
                    temp[0][3:5],
                    temp[0][5:7],
                    temp[0][7:],
                    f"{temp[1][1]}.{temp[1][3]}.{temp[1][5]}.{temp[1][7]}",
                    temp[2][-1],
                )
            else:
                middle = [temp[1][i : i + 2] for i in range(0, len(temp[1]), 2)]
                middle = [str(int(x)) for x in middle]
                code = template.format(
                    temp[0][:3],
                    temp[0][3:5],
                    temp[0][5:7],
                    temp[0][7:],
                    ".".join(middle),
                    temp[2][-1],
                )
            if len(temp) == 4:
                code += replacements[temp[-1]]
            return code

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
        base_uri = self.ruleunit_api_url if self.ruleunit_api_url else "http://tomokapi.hiai.kr/v1.0"
        headers = {"X-Auth": key}
        api_uri = base_uri + path
        response = requests.post(api_uri, headers=headers, data=kwargs)
        return response.json()

    def run_execution_orders(self):
        for execution_order in self.execution_orders:
            for order in execution_order:
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
        module_file_path,
        rule_file="tree_temp2.csv",
        ruleunit_api_url="https://tomokapi.hiai.kr/v1.0",
    ):
        self.rule_file = rule_file
        self.reader = None
        self.entities = []
        self.subtype = ""
        self.flag = False
        self.engine = ACCEngine(
            rule_file=self.rule_file,
            resource_path=resource_path,
            module_file_path=module_file_path,
            ruleunit_api_url=ruleunit_api_url,
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

    def run_verification(self, module_index: int) -> List[Dict[str, Any]]:
        """
        특정 모듈 인덱스를 사용하여 검증을 수행합니다.
        :param module_index: 사용하려는 모듈의 인덱스
        :return: 검증 결과 리스트
        """
        if not self.entities:
            return []

        # Check if the module index is within the valid range
        if module_index < 0 or module_index >= len(self.engine.execution_orders):
            raise IndexError(
                f"Invalid module index: {module_index}. Available range is 0 to {len(self.engine.execution_orders) - 1}."
            )

        self.flag = True
        results = []
        execution_orders = self.engine.execution_orders[module_index]

        for entity_index, entity in enumerate(self.entities):
            entity_result = {
                "index": entity_index,
                "ccc_results": [],
                "api_results": {},
            }
            self.engine.current_entity = entity  # 엔진에 현재 엔티티를 설정

            for order_index, order in enumerate(execution_orders):
                ccc_result = {"index": order_index, "log": []}
                if isinstance(order, list):
                    while True:
                        for code in order:
                            ccc_result["log"].append(f"룰유닛 [{code}] 실행")
                            try:
                                input_value = self.engine.get_input_values(entity, code)
                                ccc_result["log"].append(f"입력 변수: {input_value}")
                                path = self.engine.get_api_path(code)
                                result = self.engine.ruleunit_call(path, **input_value)
                                for k, v in result.items():
                                    self.engine.var_cache[k] = v
                                ccc_result["log"].append(f"API 반환 결과: {result}")
                                entity_result["api_results"][code] = result
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
                        entity_result["api_results"][code] = result
                    except Exception as e:
                        ccc_result["log"].append(f"Error executing code {code}: {e}")
                entity_result["ccc_results"].append(ccc_result)
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
    acc_controller = ACCController(
        resource_path="path_to_resource", module_directory="path_to_module_directory"
    )

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

        # Run verification with a specific module index
        try:
            module_index = 0  # 예시로 첫 번째 모듈 파일을 사용
            verification_results = acc_controller.run_verification(module_index)
            print("Verification results:", json.dumps(verification_results, indent=2))
        except IndexError as e:
            print(f"Error: {e}")

        # Get execution orders
        execution_orders = acc_controller.get_execution_orders()
        print("Execution orders:", execution_orders)
