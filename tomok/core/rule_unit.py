import inspect

def typename(obj):
    """
    Get the typename of object.

    :param obj: Target object.
    :return: Typename of the obj.
    """
    if not isinstance(obj, type):
        obj = obj.__class__
    try:
        return f'{obj.__module__}.{obj.__name__}'
    except AttributeError:
        return str(obj)

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
        print('_register_ru')
        print(dir(self))
        method_list = [attr for attr in dir(self) if inspect.isfunction(getattr(self, attr))]
        print(method_list)
        print([getattr(self, attr) for attr in dir(self)])
        typename