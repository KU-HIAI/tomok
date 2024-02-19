from typing import Optional
from itertools import product, islice
import inspect
import requests
import json
import base64
import zlib
import re
import ast
import textwrap
import random
from .util import typename, import_check
from .results import ResultBase


class RuleUnit:
    priority: int = 1
    version: float = 1.0
    acc_able: Optional[bool] = None
    author: str = "unknown"
    ref_code: str = "KDS # # #"
    ref_date: str = "YYYY-MM-DD"
    identification_code: str = "D # # #"
    rule_type: str = "TBD"
    title: str = ""
    description: str = """
    descriptions about this rule.
    """
    ref_url: str = "https://www.kcsc.re.kr/"
    filename: str = ""
    _index: int = 0
    flowchart: str = ""
    content: str = ""

    def __init__(self):
        self.rule_methods = self._register_rule_methods()

    def _register_rule_methods(self):
        method_list = [
            getattr(self, attr)
            for attr in dir(self)
            if typename(getattr(self, attr)) == "tomok.core.decorator.RuleMethod"
            or typename(getattr(self, attr)) == "tomok.tomok.core.decorator.RuleMethod"
        ]
        return method_list

    def _get_mermaid_ink_url(self, flowchart_str, theme="default"):
        json_obj = {"code": flowchart_str, "mermaid": {"theme": theme}}
        pako_str = self._encode_pako(json_obj)
        url = f"https://mermaid.ink/img/pako:{pako_str}"
        return url

    def _encode_pako(self, json_obj):
        json_str = json.dumps(json_obj, ensure_ascii=False)
        decoded_str = bytes(json_str, encoding="utf-8")
        compressed_data = zlib.compress(decoded_str, level=9)
        base64_encoded_data = base64.urlsafe_b64encode(compressed_data).decode("utf-8")
        safe_encoded_str = base64_encoded_data.replace("+", "-").replace("/", "_")
        safe_encoded_str = safe_encoded_str.rstrip("=")

        return safe_encoded_str

    def render_flowchart(self):
        img_url = self._get_mermaid_ink_url(self.flowchart)
        from IPython.display import display, Markdown

        display(Markdown(f"![]({img_url})"))

    def _get_filename(self, filename=None, saved_directory=None, extension='png'):
        # 파일 이름이 제공되지 않은 경우, 클래스 이름과 '.png' 확장자를 사용합니다.
        if not filename:
            class_name = self.__class__.__name__
            if class_name == "__main__":
                class_name = "saved_image"
            filename = f"{class_name}.{extension}"
        if saved_directory is not None:
            import os

            filename = os.path.join(saved_directory, filename)
        return filename

    def save_flowchart(self, filename=None, saved_directory=None):
        filename = self._get_filename(filename, saved_directory, 'png')

        response = requests.get(self._get_mermaid_ink_url(self.flowchart))
        if response.status_code == 200:
            with open(filename, "wb") as file:
                file.write(response.content)
            print(f"이미지가 {filename}으로 저장되었습니다.")
        else:
            print("이미지를 다운로드할 수 없습니다.")

    def render_content(self):
        if not import_check("IPython"):
            return
        from IPython.display import display, Markdown

        display(Markdown(self.content))
    
    def save_content_md(self, filename=None, saved_directory=None):
        filename = self._get_filename(filename, saved_directory, 'md')
        with open(filename, "w") as file:
            file.write(self.content)
            print(f"건설기준문서내용이 {filename}으로 저장되었습니다.")
    
    def save_content_html(self, filename=None, saved_directory=None):
        filename = self._get_filename(filename, saved_directory, 'html')
        from markdown import markdown
        with open(filename, "w") as file:
            file.write(markdown(self.content))
            print(f"건설기준문서내용이 {filename}으로 저장되었습니다.")

    def _find_docstring_variables(self, func):
        """Find variables in the given function's docstring."""
        docstring = inspect.getdoc(func)

        # Define regex patterns for args and variable names/descriptions
        arg_pattern = re.compile(r"Args:\n(.+?)(\n\n|$)", re.S)
        var_pattern = re.compile(r"(\w+)\s\(([\w.]+)\)")

        arg_block_match = arg_pattern.search(docstring)

        if arg_block_match:
            arg_block = arg_block_match.group(1)
            return var_pattern.findall(arg_block)
        else:
            return []
    
    def _find_return_docstring_variables(self, func):
        """Find return variables in the given function's docstring."""
        docstring = inspect.getdoc(func)
    
        # Define regex patterns for returns and variable names/descriptions
        return_pattern = re.compile(r"Returns:\n(.+?)(\n\n|$)", re.S)
        var_pattern = re.compile(r"(\w+)\s\(([\w.]+)\)")
    
        return_block_match = return_pattern.search(docstring)
    
        if return_block_match:
            return_block = return_block_match.group(1)
            return var_pattern.findall(return_block)
        else:
            return []
    

    def _get_source_body(self, func):
        source = inspect.getsource(func)

        index = source.find('"""')
        if index != -1:  # '"""' 가 존재하는 경우라면,
            # 다음 '"""' 의 위치 찾기
            end_index = source.find('"""', index + 3)
            if end_index != -1:  # 이것도 존재한다면,
                # 첫번째 '"""' 와 두번째 '"""' 사이에 있는 것을 모두 제거
                source = source[end_index + 3 :]
                return source

    def _get_source_vars(self, source):
        source = textwrap.dedent(source).strip()

        class VarExtractor(ast.NodeVisitor):
            def __init__(self):
                self.names = set()

            def visit_Name(self, node):
                self.names.add(node.id)

        extractor = VarExtractor()
        extractor.visit(ast.parse(source))
        return extractor.names

    def wrap_value(self, type_str, value):
        def parse_bool(s):
            s = s.strip().lower()
            if s == 'true':
                return True
            elif s == 'false':
                return False
            else:
                raise ValueError("bool 타입 변수에는 True 또는 False를 입력해야 합니다.")

        type_dict = {
            "int": int,
            "float": float,
            "str": str,
            "bool": parse_bool,  # since bool('False') is True
            "list": list,
            "tuple": tuple,
            "dict": dict,
            "set": set,
            # 더 많은 타입들을 이곳에 추가하면 됩니다.
        }
        return type_dict[type_str](value)

    def verify(self, with_stdin=True):
        error_flag = 0  # 하나라도 오류가 있으면 1를 반환

        # 메타 데이터 검증
        print("\033[1m[메타 데이터 검증]\033[0m")
        print("acc_able: ", self.acc_able)
        if self.acc_able is not None:
            print("\033[92m" + "[통과]" + "\033[0m" + " acc 가능여부가 설정되어 있습니다.")
        else:
            print(
                "\033[91m"
                + "[오류]"
                + "\033[0m"
                + " 메타데이터에 acc_able (ACC 가능여부)가 설정되어야 합니다. ACC 가능일 경우 True 아닌 경우 False 값을 설정해야 합니다."
            )
            error_flag = 1
        print("")

        print("\033[1m[룰 유닛 함수 목록]\033[0m")
        print(self.rule_methods)
        print("")

        for rule_method in self.rule_methods:
            # 기반 데이터 준비
            func = rule_method.fn
            docstring = inspect.getdoc(func)
            body = inspect.getsource(func)
            source = self._get_source_body(func)

            # 룰 인자 검증
            print("\033[1m[룰 입력 인자 검증]\033[0m")
            params = inspect.signature(func).parameters
            input_list = list(params.keys())
            print("- 함수에 정의된 인자 리스트: ", input_list)
            docstring_params = self._find_docstring_variables(func)
            docstring_params = {var[0]: var[1] for var in docstring_params}
            print("- docstring에 정의된 인자 리스트: ", docstring_params.keys())
            is_variables_matched = set(docstring_params.keys()) == set(input_list)
            if is_variables_matched:
                print("\033[92m" + "[통과]" + "\033[0m" + " 함수와 docstring 인자 일치")
            else:
                print("\033[91m" + "[오류]" + "\033[0m" + " 함수와 docstring 인자 불일치.\n")
                print("맞는데도 이 오류가 발생한다면 docstring의 띄어쓰기를 확인하세요.")
                error_flag = 1

            # 입력 인자에 userdefined 있는지 여부
            has_userdefined = False
            for input_name in input_list:
                if "userdefined" in input_name.lower():
                    has_userdefined = True
            if not has_userdefined:
                print("\033[92m" + "[통과]" + "\033[0m" + " UserDefined 인자 불검출")
            else:
                print("\033[91m" + "[오류]" + "\033[0m" + " UserDefined 인자 검출")
                error_flag = 1

            # 모든 입력 인자의 사용 여부 검사
            source_vars = self._get_source_vars(source)
            print("- 소스코드에 사용된 인자 리스트: ", source_vars)
            all_variable_used = len(set(input_list).difference(set(source_vars))) == 0
            if all_variable_used:
                print("\033[92m" + "[통과]" + "\033[0m" + " 입력 인자 모두 사용")
            else:
                print("\033[91m" + "[오류]" + "\033[0m" + " 미사용 입력 인자 존재")
                print(
                    "\033[91m" + "[미사용 인자]" + "\033[0m",
                    set(input_list).difference(set(source_vars)),
                )
                error_flag = 1
            print("")

            # 룰 실행여부 검증
            print("\033[1m[룰 실행 여부 검증]\033[0m")
            if(len(set(input_list).difference(set(docstring_params.keys()))) > 0):
                print('\033[91m' + '[오류]' + '\033[0m' + ' 입력 인자 중 일부가 docstring에 기재되어 있지 않습니다. 자료형(예: float, str, int)을 알 수 없으므로 룰 실행 여부 검정이 불가합니다.')
                print(set(input_list).difference(set(docstring_params.keys())))
                print('\033[91m' + '위 인자에 대한 docstring 작성 후 다시 실행 해주시기 바랍니다.' + '\033[0m')
                return 1
            if with_stdin:  # input()의 stdin 입력 없이 검토하는 기능 추가
                user_input = {}
                for param in input_list:
                    user_input[param] = input(f"{param} ({docstring_params[param]}) 인자의 값을 넣어주세요 : ")
                    try:
                        user_input[param] = self.wrap_value(
                            docstring_params[param], user_input[param]
                        )
                        print(f"{param}: {user_input[param]}")
                    except Exception as ex:
                        print("\033[91m" + "[오류]" + "\033[0m" + " 인자 형 변환 실패")
                        print(ex)
                        error_flag = 1
                try:
                    result = func(**user_input)
                    print("\033[92m" + "[통과]" + "\033[0m" + " 룰 실행 확인")
                except Exception as ex:
                    print("\033[91m" + "[오류]" + "\033[0m" + " 룰 실행 실패")
                    print(ex)
                    error_flag = 1

                # 룰 반환형 검사
                print("\033[1m[룰 반환 데이터 검증]\033[0m")
                print("결과:", result)
                if isinstance(result, ResultBase):
                    print("\033[92m" + "[통과]" + "\033[0m" + " 반환 자료형 확인")
                else:
                    # print('\033[91m' + '[오류]' + '\033[0m' + ' 반환 자료는 ResultBase, PassFailResult, SingleValueResult, MultiValueResult 등 이어야 합니다.')
                    print(
                        "\033[91m" + "[오류]" + "\033[0m" + " 반환 자료형은 RuleUnitResult 이어야 합니다."
                    )
                    return 1
            else:
                print("건너뜁니다... (입력값 없이 진행)")
            print("")

            docstring_return_params = self._find_return_docstring_variables(func)
            docstring_return_params = {var[0]: var[1] for var in docstring_return_params}

            def validate_return_docstring(returned_value):
                if len(set(returned_value.result_variables.keys()).difference(set(docstring_return_params))) > 0:
                    print('\033[91m' + '[오류]' + '\033[0m' + ' 반환 인자 중 일부가 docstring에 기재되어 있지 않습니다.')
                    print(set(returned_value.result_variables.keys()).difference(set(docstring_return_params)))
                    print('\033[91m' + '위 인자의 변수명이 docstring에 기록되어 있는지, 변수명에 오류가 없는지 확인 바랍니다.' + '\033[0m')
                    print("")
                    return 1
                else:
                    return 0

            if with_stdin:
                if validate_return_docstring(result) == 1:
                    error_flag = 1

            # 경곗값 테스트 (Boundary Value Test) - 입력변수에 극단적인 값이 들어와도 안전한지 검증
            print("\033[1m[다양한 입력값 대응 여부 검증]\033[0m")
            value_dict = {  # 임의로 설정한 극단적 값
                "int": [-1, 0, 10, 100, 99999],
                "float": [-1.0, 0.0, 10.0, 100.0, 99999.9],
                "str": ['', '테스트', 'Test!Test!Test!Test!Test!Test!\nTest!'],
                "bool": [True, False],
                "list": [[1.0], [1.0, 999.9]],
                "dict": [{"1": 1}],
                "set": [{1.0}, {1.0, 999.9}],
            }
            arg_to_type = {k: docstring_params[k] for k in input_list}
            candidates = [value_dict[v] for v in arg_to_type.values()]

            for extreme_args in islice(product(*candidates), 10000):  # 나중에 product의 순서가 랜덤으로 되도록 해야 함
                try:
                    output = func(*extreme_args)

                    # docstring 검사
                    if validate_return_docstring(output) == 1:
                        raise TypeError

                    # return type 검사
                    if not isinstance(output, ResultBase):
                        print("\033[91m" + "[오류]" + "\033[0m" + " RuleUnitResult를 반환하지 않는 경우 존재")
                        raise TypeError("RuleUnit 반환형 오류")

                except AssertionError:
                    pass  # no problem with AssertionError when given extreme arguments
                except TypeError:
                    # print("\033[91m" + "[오류]" + "\033[0m" + " 룰 안전하지 않음")
                    print('\033[1m' + f"오류 당시 입력변수" + '\033[0m' + f": {str({k:v for k, v in zip(input_list, extreme_args)})}")
                    raise
            print("\033[92m" + "[통과]" + "\033[0m" + " 극단적 입력값 테스트 완료")

        return error_flag

