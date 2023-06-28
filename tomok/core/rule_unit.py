import inspect
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

    def render_markdown(self):
        if not import_check('IPython'):
            return
        from IPython.display import display, Markdown
        display(Markdown(self.content))
        