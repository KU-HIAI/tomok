import inspect
import requests
import json
import base64
import zlib
import re
import ast
import textwrap
from .util import typename, import_check
from .results import ResultBase

class RuleUnit():
    priority = 1
    version = 1.0
    author = 'unknown'
    ref_code = 'KDS # # #'
    ref_date = 'YYYY-MM-DD'
    identification_code = 'D # # #'
    rule_type = 'TBD'
    title = ''
    description = """
    descriptions about this rule.
    """
    ref_url = "https://www.kcsc.re.kr/"
    filename = ""
    _index = 0
    flowchart = ""
    content = ""


    def __init__(self):
        self.rule_methods = self._register_rule_methods()
    

    def _register_rule_methods(self):
        method_list = [getattr(self, attr) for attr in dir(self) if typename(getattr(self, attr)) == 'tomok.core.decorator.RuleMethod']
        return method_list


    def _get_mermaid_ink_url(self, flowchart_str, theme='default'):
        json_obj = {
            'code': flowchart_str,
            'mermaid':{
                'theme': theme
            }
        }
        pako_str = self._encode_pako(json_obj)
        url = f"https://mermaid.ink/img/pako:{pako_str}"
        return url


    def _encode_pako(self, json_obj):
        json_str = json.dumps(json_obj, ensure_ascii=False)
        decoded_str = bytes(json_str, encoding='utf-8')
        compressed_data = zlib.compress(decoded_str, level=9)
        base64_encoded_data = base64.urlsafe_b64encode(compressed_data).decode('utf-8')
        safe_encoded_str = base64_encoded_data.replace('+', '-').replace('/', '_')
        safe_encoded_str = safe_encoded_str.rstrip('=')

        return safe_encoded_str


    def render_flowchart(self):
        img_url = self._get_mermaid_ink_url(self.flowchart)
        from IPython.display import display, Markdown
        display(Markdown(f"![]({img_url})"))


    def save_flowchart(self, filename=None, saved_directory=None):
        # 파일 이름이 제공되지 않은 경우, 클래스 이름과 '.png' 확장자를 사용합니다.
        if not filename:
            class_name = self.__class__.__name__
            if class_name == '__main__':
                class_name = 'saved_image'
            filename = f"{class_name}.png"
        if saved_directory is not None:
            import os
            filename = os.path.join(saved_directory, filename)
        
        response = requests.get(self._get_mermaid_ink_url(self.flowchart))
        if response.status_code == 200:
            with open(filename, 'wb') as file:
                file.write(response.content)
            print(f"이미지가 {filename}으로 저장되었습니다.")
        else:
            print("이미지를 다운로드할 수 없습니다.")
    

    def render_markdown(self):
        if not import_check('IPython'):
            return
        from IPython.display import display, Markdown
        display(Markdown(self.content))
    

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

    def _get_source_body(self, func):
        source = inspect.getsource(func)

        index = source.find('"""')
        if index != -1:  # '"""' 가 존재하는 경우라면,
            # 다음 '"""' 의 위치 찾기
            end_index = source.find('"""', index + 3) 
            if end_index != -1: # 이것도 존재한다면,
                # 첫번째 '"""' 와 두번째 '"""' 사이에 있는 것을 모두 제거
                source = source[end_index + 3:]
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
        type_dict = {
            'int': int,
            'float': float,
            'str': str,
            'bool': bool,
            'list': list,
            'tuple': tuple,
            'dict': dict,
            'set': set,
            # 더 많은 타입들을 이곳에 추가하면 됩니다.
        }
        return type_dict[type_str](value)


    def verify(self):
        # 메타 데이터 검증
        print("\033[1m[메타 데이터 검증]\033[0m")
        print("...under construction...")
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
            docstring_params = {var[0]:var[1] for var in docstring_params}
            print("- docstring에 정의된 인자 리스트: ", docstring_params)
            is_variables_matched = set(docstring_params.keys()) == set(input_list)
            if(is_variables_matched):
                print('\033[92m' + '[통과]' + '\033[0m' + ' 함수와 docstring 인자 일치')
            else:
                print('\033[91m' + '[오류]' + '\033[0m' + ' 함수와 docstring 인자 불일치')
            
            # 입력 인자에 userdefined 있는지 여부
            has_userdefined = False
            for input_name in input_list:
                if "userdefined" in input_name.lower():
                    has_userdefined = True
            if(not has_userdefined):
                print('\033[92m' + '[통과]' + '\033[0m' + ' UserDefined 인자 불검출')
            else:
                print('\033[91m' + '[오류]' + '\033[0m' + ' UserDefined 인자 검출')
            
            # 모든 입력 인자의 사용 여부 검사
            source_vars = self._get_source_vars(source)
            print("- 소스코드에 사용된 인자 리스트: ", source_vars)
            all_variable_used = len(set(input_list).difference(set(source_vars))) == 0
            if(all_variable_used):
                print('\033[92m' + '[통과]' + '\033[0m' + ' 입력 인자 모두 사용')
            else:
                print('\033[91m' + '[오류]' + '\033[0m' + ' 미사용 입력 인자 존재')
                print('\033[91m' + '[미사용 인자]' + '\033[0m', set(input_list).difference(set(source_vars)))
            print("")

            # 룰 실행여부 검증
            print("\033[1m[룰 실행 여부 검증]\033[0m")
            user_input = {}
            for param in input_list:
                user_input[param] = input(f"{param} 인자의 값을 넣어주세요 : ")
                try:
                    user_input[param] = self.wrap_value(docstring_params[param], user_input[param])
                    print(f"{param}: {user_input[param]}")
                except Exception as ex:
                    print('\033[91m' + '[오류]' + '\033[0m' + ' 인자 형 변환 실패')
                    print(ex)
            try:
                result = func(**user_input)
                print('\033[92m' + '[통과]' + '\033[0m' + ' 룰 실행 확인')
            except Exception as ex:
                print('\033[91m' + '[오류]' + '\033[0m' + ' 룰 실행 실패')
                print(ex)
            print("")
            
            # 룰 반환형 검사
            print("\033[1m[룰 반환 데이터 검증]\033[0m")
            print("결과:", result)
            if isinstance(result, ResultBase):
                print('\033[92m' + '[통과]' + '\033[0m' + ' 반환 자료형 확인')
            else:
                print('\033[91m' + '[오류]' + '\033[0m' + ' 반환 자료은 ResultBase, PassFailResult, SingleValueResult, MultiValueResult 등 이어야 합니다.')
        