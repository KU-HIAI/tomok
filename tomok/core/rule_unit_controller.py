# python
import os
import re
from importlib import import_module
from typing import List
from click import FileError
# framework
from .rule_unit import RuleUnit


class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

class RuleUnitController():
    def __init__(
        self,
        path = 'ruleunits',
        mode = 'local'
    ):
        self.ruleunits: List[RuleUnit] = []
        self.ruleunits_dict = AttrDict()
        regex = r"class (.*)\(.*RuleUnit\):"
        if mode == 'local':
            for curpath, subdirs, filenames in os.walk(path):
                for filename in filenames:
                    if filename.endswith('.py'):
                        code = open(os.path.join(curpath, filename), encoding="utf-8").read() # encoding= 추가!
                        matches = re.findall(regex, code, re.MULTILINE)
                        if len(matches) > 0:
                            if self._is_valid_filename(filename):
                                for match in matches:
                                    cls_name = match.strip()
                                    module_name = filename[:-3]
                                    import_name = os.path.join(curpath, filename).replace(os.path.sep, '.')[:-3]
                                    relative_path = os.path.relpath(curpath, path)
                                    ruleunit = getattr(import_module(import_name), cls_name)()
                                    ruleunit.filename = filename
                                    self.ruleunits.append(ruleunit)

                                    # Adding object to ruleunits_dict
                                    keys = relative_path.split(os.path.sep) + [module_name]
                                    current_dict = self.ruleunits_dict
                                    for key in keys:
                                        if key not in current_dict:
                                            current_dict[key] = AttrDict()
                                        current_dict = current_dict[key]
                                    current_dict[cls_name] = ruleunit
    

    def __getattr__(self, name):
        if name in self.ruleunits_dict:
            return self.ruleunits_dict[name]
        else: 
            raise AttributeError(f"No such attribute: {name}")
    
    def __getitem__(self, name):
        if name in self.ruleunits_dict:
            return self.ruleunits_dict[name]
        else: 
            raise KeyError(f"No such key: {name}")
    
                       
    
    @classmethod
    def _is_valid_filename(
        cls,
        filename: str
    ) -> bool:
        if filename.count('.') > 1:
            # 파일명에 .이 여러개 있는지 확인. 여러개 있으면 import가 안됨
            raise FileError("rule 파일명에 . 글자는 허용되지 않습니다. 파일명에서 . 을 제거해주시기 바랍니다.")
        return True