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

    @classmethod
    def retrieve_entities(
            cls,
            reader: IFCReader
    ) -> List[Product]:
        raise NotImplementedError

    @classmethod
    def pre_process(
            cls,
            entity: Product
    ):
        pass

    @classmethod
    def process(
            cls,
            entity: Product
    ):
        raise NotImplementedError

    @classmethod
    def post_process(
            cls,
            entity: Product
    ):
        pass

    @classmethod
    def make_result(
            cls,
            entity: Product
    ) -> Union[str, OKNGResult]:
        raise NotImplementedError

    @classmethod
    def save_result(
            cls,
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
