# python
import os
import re
import sys
from importlib import import_module
from typing import List, Union
from click import FileError
# framework
from .verify_result import VerifyResult
from .rule_ifc import RuleIFC
from .rule_unit_controller import RuleUnitController
from ..ifc import IFCReader

import pandas as pd

class RuleIFCController():
    def __init__(
        self,
        path = 'rules',
        rule_units: RuleUnitController = None,
        mode = 'local'
    ):
        self.rule_ifcs: List[RuleIFC] = []
        regex = r"class (.*)\(.*RuleIFC\):"
        path_dir = os.path.abspath(path)
        # RuleUnit 경로를 sys.path에 추가합니다.
        backup_sys_path = [path for path in sys.path]
        sys.path = [path_dir]
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
                                    relative_path = os.path.relpath(curpath, path)
                                    import_name = os.path.join(relative_path, filename).lstrip('./').replace(os.path.sep, '.')[:-3]
                                    rule = getattr(import_module(import_name), cls_name)(rule_units=rule_units)
                                    rule.filename = filename
                                    self.rule_ifcs.append(rule)
        sys.path = [path for path in backup_sys_path]
        self._prioritize()
        self._set_index()
    
    @property
    def rules_df(self):
        return pd.DataFrame([{ 
            "filename": rule.filename,
            "priority": rule.priority,
            "ref_code": rule.ref_code,
            "title": rule.title,
            "author": rule.author,
            "ref_url": rule.ref_url
        } for rule in self.rule_ifcs])

    def add_rule(
        self,
        code: str
    ):
        # TODO : rule 코드를 입력받아 rule-set에 추가
        raise NotImplementedError
    
    @classmethod
    def _is_valid_filename(
        cls,
        filename: str
    ) -> bool:
        if filename.count('.') > 1:
            # 파일명에 .이 여러개 있는지 확인. 여러개 있으면 import가 안됨
            raise FileError("rule 파일명에 . 글자는 허용되지 않습니다. 파일명에서 . 을 제거해주시기 바랍니다.")
        return True
    
    def _prioritize(
        self
    ):
        """RuleIFC 리스트를 priority에 따라 오름차순으로 정렬한다.
        """
        self.rule_ifcs = sorted(self.rule_ifcs, key=lambda r: r.priority)
    
    def _set_index(
        self
    ):
        for idx, rule_ifc in enumerate(self.rule_ifcs):
            rule_ifc._index = idx
    
    @classmethod
    def _verify(
        cls,
        reader: IFCReader,
        rule_ifc: RuleIFC,
        guid: str = None,
    ) -> List[VerifyResult]:
        results = list(cls._verify_iter(reader, rule_ifc, guid))
        return results
    
    @classmethod
    def _verify_iter(
        cls,
        reader: IFCReader,
        rule_ifc: RuleIFC,
        guid: str = None,
    ) -> VerifyResult:
        entities = rule_ifc.retrieve_entities(reader, guid)
        print(len(entities))
        for entity in entities:
            try:
                rule_ifc.pre_process(entity)
                rule_ifc.process(entity)
                rule_ifc.post_process(entity)
                result = rule_ifc.make_result(entity)
                rule_ifc.save_result(entity, result)
                yield VerifyResult(rule_ifc, result, entity)
            except Exception as ex:
                yield VerifyResult(rule_ifc, 'ERROR : ' + str(ex), entity)

    def verify_all(
        self,
        reader: IFCReader,
        guid: str = None,
        return_results: bool = False
    ):
        # TODO : result_strs는 임시로 만든 것임. logger를 이용하도록 변경
        results = []
        result_strs = []
        result_strs.append('검사 시작')
        for rule_ifc in self.rule_ifcs:
            result_strs.append('룰 제목 : {0}'.format(rule_ifc.title))
            for verify_result in self._verify_iter(reader, rule_ifc, guid):
                results.append(verify_result)
                result_str = repr(verify_result)
                # print(result_str)
                result_strs.append(result_str)
        result_strs.append('검사 완료')
        if return_results:
            return results, result_strs
        else:
            return result_strs

    def verify(
            self,
            reader: IFCReader,
            idxs : Union[int, List],
            guid: str = None,
            return_results: bool = False
    ):
        # TODO : result_strs는 임시로 만든 것임. logger를 이용하도록 변경
        results = []
        result_strs = []
        result_strs.append('선택된 인덱스에 대해 검사 시작')
        if type(idxs) is int:
            idxs = [idxs]
        for idx in idxs:
            rule_ifc = self.rule_ifcs[idx]
            result_strs.append('룰 제목 : {0}'.format(rule_ifc.title))
            # print("Rule_index : ", idx)
            for verify_result in self._verify_iter(reader, rule_ifc, guid):
                results.append(verify_result)
                result_str = repr(verify_result)
                # print(result_str)
                result_strs.append(result_str)
        result_strs.append('검사 완료')
        if return_results:
            return results, result_strs
        else:
            return result_strs

    def verify_rule(
        self,
        reader: IFCReader,
        rule_ifc: RuleIFC,
        guid: str = None,
    ) -> VerifyResult:
        verify_result = self._verify_iter(reader, rule_ifc, guid)
        # print(repr(verify_result))
        return verify_result

    def show_rule(self,
                  idx = None):
        if idx is None:
            print(self.rules_df)
        else:
            print(self.rules_df.loc[idx])