# python
from typing import Union
from enum import Enum
# 3rd-party
from ifcopenshell import entity_instance
# framework
from .rule import Rule, RuleType
from .results import OKNGResult
from ..ifc import Product


class VerifyResult():
    def __init__(
            self,
            rule: Rule,
            result: Union[str, OKNGResult],
            entity: Union[Product, entity_instance],
    ):
        self.rule = rule
        self.result = result
        self.entity = entity

    def __repr__(
            self
    ) -> str:
        result_str = self.result
        if isinstance(self.result, Enum):
            result_str = self.result.name
        return "[{4} : {0} 검사] 결과 : {3} / (#{2}, {1})".format(
            self.rule.title,
            self.entity.entity.Name,
            self.entity.entity.id(),
            result_str,
            self.rule.rule_type.name
        )
    
    def to_json(self):
        result_str = self.result
        if isinstance(self.result, Enum):
            result_str = self.result.name
        return {
            'rule': {
                'index': self.rule._index,
                'title': self.rule.title,
                'ref_code': self.rule.ref_code,
                'ref_date': self.rule.ref_date
            },
            'entity': str(self.entity),
            'result': result_str
        }