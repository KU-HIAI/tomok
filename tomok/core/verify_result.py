# python
from typing import Union, List
from enum import Enum
# 3rd-party
from ifcopenshell import entity_instance
# framework
from .rule_unit import RuleUnit
from .results import OKNGResult
from ..ifc import Product


class VerifyResult():
    def __init__(
            self,
            ruleunit: RuleUnit,
            result: Union[str, OKNGResult],
            entity: Union[Product, entity_instance],
            log: List[str] = []
    ):
        self.ruleunit = ruleunit
        self.result = result
        self.entity = entity
        self.log = log

    def __repr__(
            self
    ) -> str:
        result_str = self.result
        if isinstance(self.result, Enum):
            result_str = self.result.name
        return "[{0} 검사] 결과 : {3} / (#{2}, {1})".format(
            self.ruleunit.title,
            self.entity.entity.Name,
            self.entity.entity.id(),
            result_str
        )

    def to_json(self):
        result_str = self.result
        if isinstance(self.result, Enum):
            result_str = self.result.name
        return {
            'rule': {
                'index': self.ruleunit._index,
                'title': self.ruleunit.title,
                'ref_code': self.ruleunit.ref_code,
                'ref_date': self.ruleunit.ref_date
            },
            'entity': str(self.entity),
            'process_log': self.log,
            'result': result_str
        }
