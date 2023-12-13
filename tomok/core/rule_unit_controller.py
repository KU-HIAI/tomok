# python
import os
import re
from importlib import import_module
from typing import List
from click import FileError
# framework
from .rule_unit import RuleUnit


class RuleUnitController():
    def __init__(
        self,
        path = 'ruleunits',
        mode = 'local'
    ):
        self.ruleunits: List[RuleUnit] = []
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
                                    cls_name = match
                                    import_name = os.path.join(curpath, filename).replace(os.path.sep, '.')[:-3]
                                    rule = getattr(import_module(import_name), cls_name)()
                                    rule.filename = filename
                                    self.ruleunits.append(rule)
    
    @classmethod
    def _is_valid_filename(
        cls,
        filename: str
    ) -> bool:
        if filename.count('.') > 1:
            # 파일명에 .이 여러개 있는지 확인. 여러개 있으면 import가 안됨
            raise FileError("rule 파일명에 . 글자는 허용되지 않습니다. 파일명에서 . 을 제거해주시기 바랍니다.")
        return True