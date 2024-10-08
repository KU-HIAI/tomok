# python
import os
import re
import sys
from importlib import import_module
from typing import List
from click import FileError

# framework
from .table_unit import TableUnit


class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


class TableUnitController:
    def __init__(self, path="tableunits", mode="local"):
        self.tableunits: List[TableUnit] = []
        self.tableunits_dict = AttrDict()
        regex = r"class (.*)\(.*TableUnit\):"
        path_dir = os.path.abspath(path)
        # TableUnit 경로를 sys.path에 추가합니다.
        backup_sys_path = [path for path in sys.path]
        sys.path = [path_dir]
        if mode == "local":
            for curpath, subdirs, filenames in os.walk(path):
                for filename in filenames:
                    if filename.endswith(".py"):
                        code = open(
                            os.path.join(curpath, filename), encoding="utf-8"
                        ).read()  # encoding= 추가!
                        matches = re.findall(regex, code, re.MULTILINE)
                        if len(matches) > 0:
                            if self._is_valid_filename(filename):
                                for match in matches:
                                    cls_name = match.strip()
                                    module_name = filename[:-3]
                                    relative_path = os.path.relpath(curpath, path)
                                    import_name = (
                                        os.path.join(relative_path, filename)
                                        .lstrip("./")
                                        .replace(os.path.sep, ".")[:-3]
                                    )
                                    tableunit = getattr(
                                        import_module(import_name), cls_name
                                    )()
                                    tableunit.filename = filename
                                    tableunit.filepath = os.path.join(curpath, filename)
                                    self.tableunits.append(tableunit)

                                    # Adding object to tableunits_dict
                                    keys = relative_path.split(os.path.sep) + [
                                        module_name
                                    ]
                                    current_dict = self.tableunits_dict
                                    for key in keys:
                                        if key not in current_dict:
                                            current_dict[key] = AttrDict()
                                        current_dict = current_dict[key]
                                    current_dict[cls_name] = tableunit
        sys.path = [path for path in backup_sys_path]

    def __getattr__(self, name):
        if name in self.tableunits_dict:
            return self.tableunits_dict[name]
        else:
            raise AttributeError(f"No such attribute: {name}")

    def __getitem__(self, name):
        if name in self.tableunits_dict:
            return self.tableunits_dict[name]
        else:
            raise KeyError(f"No such key: {name}")

    @classmethod
    def _is_valid_filename(cls, filename: str) -> bool:
        if filename.count(".") > 1:
            # 파일명에 .이 여러개 있는지 확인. 여러개 있으면 import가 안됨
            raise FileError(
                "table 파일명에 . 글자는 허용되지 않습니다. 파일명에서 . 을 제거해주시기 바랍니다."
            )
        return True
