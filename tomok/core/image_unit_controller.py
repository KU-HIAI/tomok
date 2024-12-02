# python
import os
import re
import sys
from importlib import import_module
from typing import List
from click import FileError

# framework
from .image_unit import ImageUnit
from .repo import prepare_tf_repo, TF_REPO_ID


class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


class ImageUnitController:
    _instance = None  # class level 인스턴스 저장 변수

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ImageUnitController, cls).__new__(cls)
        return cls._instance

    def __init__(self, TF_REPO_TOKEN, path=TF_REPO_ID, mode="github"):
        if "initialized" not in self.__dict__:
            if mode == "github":
                prepare_tf_repo(True, TF_REPO_TOKEN)
            self.initialized = True
            self.imageunits: List[ImageUnit] = []
            self.imageunits_dict = AttrDict()
            regex = r"class (.*)\(.*ImageUnit\):"
            path_dir = os.path.abspath(path)
            # ImageUnit 경로를 sys.path에 추가합니다.
            backup_sys_path = [path for path in sys.path]
            sys.path = [path_dir]
            if mode in ["local", "github"]:
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
                                        imageunit = getattr(
                                            import_module(import_name), cls_name
                                        )()
                                        imageunit.filename = filename
                                        imageunit.filepath = os.path.join(
                                            curpath, filename
                                        )
                                        self.imageunits.append(imageunit)

                                        # Adding object to imageunits_dict
                                        keys = relative_path.split(os.path.sep) + [
                                            module_name
                                        ]
                                        current_dict = self.imageunits_dict
                                        for key in keys:
                                            if key not in current_dict:
                                                current_dict[key] = AttrDict()
                                            current_dict = current_dict[key]
                                        current_dict[cls_name] = imageunit
            sys.path = [path for path in backup_sys_path]
            print("Table unit controller instance has been created.")

    def __getattr__(self, name):
        if name in self.imageunits_dict["ImageUnits"]:
            return self.imageunits_dict["ImageUnits"][name]
        else:
            raise AttributeError(f"No such attribute: {name}")

    def __getitem__(self, name):
        if name in self.imageunits_dict["ImageUnits"]:
            return self.imageunits_dict["ImageUnits"][name]
        else:
            raise KeyError(f"No such key: {name}")

    @classmethod
    def _is_valid_filename(cls, filename: str) -> bool:
        if filename.count(".") > 1:
            # 파일명에 .이 여러개 있는지 확인. 여러개 있으면 import가 안됨
            raise FileError(
                "image 파일명에 . 글자는 허용되지 않습니다. 파일명에서 . 을 제거해주시기 바랍니다."
            )
        return True

    @classmethod
    def instance(cls, TF_REPO_TOKEN):
        if cls._instance is None:
            cls._instance = cls(TF_REPO_TOKEN)
        return cls._instance
