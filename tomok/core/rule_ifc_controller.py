# python
import os
import re
from importlib import import_module
from typing import List, Union
from click import FileError
# framework
from .verify_result import VerifyResult
from .rule_ifc import RuleIFC
from ..ifc import IFCReader

import pandas as pd

class RuleIFCController():
    def __init__(
        self,
        path = 'rules',
        mode = 'local'
    ):
        self.rules: List[RuleIFC] = []
        regex = r"class (.*)\(.*RuleIFC\):"
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
                                    self.rules.append(rule)

        self._prioritize()
        self._set_index()
    
    @property
    def rules_df(self):
        return pd.DataFrame([{ 
            "filename": rule.filename,
            "priority": rule.priority,
            "ref_code": rule.ref_code,
            "title": rule.title,
            "type": rule.rule_type.name,
            "author": rule.author,
            "ref_url": rule.ref_url
        } for rule in self.rules])

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
        self.rules = sorted(self.rules, key=lambda r: r.priority)
    
    def _set_index(
        self
    ):
        for idx, rule in enumerate(self.rules):
            rule._index = idx
    
    @classmethod
    def _verify(
        cls,
        reader: IFCReader,
        rule: RuleIFC
    ) -> List[VerifyResult]:
        results = list(cls._verify_iter(reader, rule))
        return results
    
    @classmethod
    def _verify_iter(
        cls,
        reader: IFCReader,
        rule: RuleIFC
    ) -> VerifyResult:
        entities = rule.retrieve_entities(reader)
        print(len(entities))
        for entity in rule.retrieve_entities(reader):
            try:
                rule.pre_process(entity)
                rule.process(entity)
                rule.post_process(entity)
                result = rule.make_result(entity)
                rule.save_result(entity, result)
                yield VerifyResult(rule, result, entity)
            except Exception as ex:
                yield VerifyResult(rule, 'ERROR : ' + str(ex), entity)

    def verify_all(
        self,
        reader: IFCReader,
        return_results: bool = False
    ):
        # TODO : result_strs는 임시로 만든 것임. logger를 이용하도록 변경
        results = []
        result_strs = []
        result_strs.append('검사 시작')
        for rule in self.rules:
            result_strs.append('룰 제목 : {0}'.format(rule.title))
            for verify_result in self._verify_iter(reader, rule):
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
            return_results: bool = False
    ):
        # TODO : result_strs는 임시로 만든 것임. logger를 이용하도록 변경
        results = []
        result_strs = []
        result_strs.append('선택된 인덱스에 대해 검사 시작')
        if type(idxs) is int:
            idxs = [idxs]
        for idx in idxs:
            rule = self.rules[idx]
            result_strs.append('룰 제목 : {0}'.format(rule.title))
            # print("Rule_index : ", idx)
            for verify_result in self._verify_iter(reader, rule):
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
        rule: RuleIFC
    ) -> VerifyResult:
        verify_result = self._verify_iter(reader, rule)
        # print(repr(verify_result))
        return verify_result

    def show_rule(self,
                  idx = None):
        if idx is None:
            print(self.rules_df)
        else:
            print(self.rules_df.loc[idx])