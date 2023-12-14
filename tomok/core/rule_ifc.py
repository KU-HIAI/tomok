# python
from typing import List, Union
from enum import IntEnum
# framework
from .results import OKNGResult
from ..ifc.entity import Product
from ..ifc.reader import IFCReader


class RuleIFC():
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
    content = "markdown"
    flowchart = "mermaid"
    _index = 0

    def retrieve_entities(
            self,
            reader: IFCReader
    ) -> List[Product]:
        raise NotImplementedError

    def pre_process(
            self,
            entity: Product
    ):
        pass

    def process(
            self,
            entity: Product
    ):
        raise NotImplementedError

    def post_process(
            self,
            entity: Product
    ):
        pass

    def make_result(
            self,
            entity: Product
    ) -> Union[str, OKNGResult]:
        raise NotImplementedError

    def save_result(
            self,
            entity: Product,
            result: Union[str, OKNGResult]
    ):
        pass


class RuleType(IntEnum):
    SIMPLE = 10,
    CALCULATE = 11,
    REVIEW = 12,
    REFERENCE = 13


class SimpleRule(RuleIFC):
    rule_type = RuleType.SIMPLE


class CalculateRule(RuleIFC):
    rule_type = RuleType.CALCULATE


class ReviewRule(RuleIFC):
    rule_type = RuleType.REVIEW


class RefRule(RuleIFC):
    rule_type = RuleType.REFERENCE
