import inspect
import re
import textwrap
import ast
import json
import base64
import zlib
import requests
from .util import typename, import_check



class BaseUnit:
    #######################
    # content 렌더링 및 저장
    #######################
    def render_content(self):
        if not import_check("IPython"):
            return
        from IPython.display import display, Markdown

        display(Markdown(self.content))
    
    def save_content_md(self, filename=None, saved_directory=None):
        filename = self._get_filename(filename, saved_directory, "md")
        with open(filename, "w") as file:
            file.write(self.content)
            print(f"건설기준문서내용이 {filename}으로 저장되었습니다.")

    def save_content_html(self, filename=None, saved_directory=None):
        filename = self._get_filename(filename, saved_directory, "html")
        from markdown import markdown

        with open(filename, "w") as file:
            file.write(markdown(self.content))
            print(f"건설기준문서내용이 {filename}으로 저장되었습니다.")
    
    
    #################################
    # mermaid flowchart 렌더링 및 저장
    #################################
    def _get_mermaid_ink_url(self, flowchart_str, theme="default", bgColor="!white"):
        json_obj = {"code": flowchart_str, "mermaid": {"theme": theme}}
        pako_str = self._encode_pako(json_obj)
        url = f"https://mermaid.ink/img/pako:{pako_str}?bgColor={bgColor}"
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

    def _get_filename(self, filename=None, saved_directory=None, extension="png"):
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
        filename = self._get_filename(filename, saved_directory, "png")

        response = requests.get(self._get_mermaid_ink_url(self.flowchart))
        if response.status_code == 200:
            with open(filename, "wb") as file:
                file.write(response.content)
            print(f"이미지가 {filename}으로 저장되었습니다.")
        else:
            print("이미지를 다운로드할 수 없습니다.")


    ############
    # 함수부 분석
    ############
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
            if s == "true":
                return True
            elif s == "false":
                return False
            else:
                raise ValueError(
                    "bool 타입 변수에는 True 또는 False를 입력해야 합니다."
                )

        def parse_list(s):
            if isinstance(s, list):
                return s
            elif isinstance(s, str):
                s = s.strip()
                assert re.fullmatch(
                    r"\[\d+(\.\d+)?(,\s?\d+(\.\d+)?)*]", s
                ), "[1, 2, 3]과 같은 식으로 입력해야 합니다."
                return list(map(float, s[1:-1].split(",")))
            else:
                raise ValueError("list 형식으로 파싱할 수 없습니다.")

        type_dict = {
            "int": int,
            "float": float,
            "str": str,
            "bool": parse_bool,  # since bool('False') is True
            "list": parse_list,
            "tuple": tuple,
            "dict": dict,
            "set": set,
            # 더 많은 타입들을 이곳에 추가하면 됩니다.
        }
        return type_dict[type_str](value)