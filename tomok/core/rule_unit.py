import inspect
import requests
import json
import base64
import zlib
from .util import typename, import_check

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
        