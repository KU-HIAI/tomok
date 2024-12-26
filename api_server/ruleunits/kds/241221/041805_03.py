import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241221_041805_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 21 4.18.5 (3)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '중요 교량에 대하여 전 교량에 대한 최대 연간파괴빈도'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.18 선박충돌하중: CV
    4.18.5 연간파괴빈도
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 중요 교량에 대하여 전 교량에 대한 최대 연간파괴빈도];
    B["KDS 24 12 21 4.18.5 (3)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 중요 교량에 대하여 전 교량에 대한 최대 연간파괴빈도/];
    end

    Python_Class ~~~ C(["KDS 24 12 21 4.18.5 (3)"])
		C --> Variable_def

    D["AF=0.0001"];
    Variable_def--->D--->E(["중요 교량에 대하여 전 교량에 대한 최대 연간파괴빈도"])
    """

    @rule_method
    def maximum_annual_destruction_frequency_of_important_bridge(fOmaxAFA) -> RuleUnitResult:
        """중요 교량에 대하여 전 교량에 대한 최대 연간파괴빈도

        Args:
            fOmaxAFA (float): 중요 교량에 대하여 전 교량에 대한 최대 연간파괴빈도

        Returns:
            fOmaxAFA (float): 강교 설계기준(한계상태설계법)  4.18.5 연간파괴빈도 (3)의 값
        """

        fOmaxAFA = 0.0001

        return RuleUnitResult(
            result_variables = {
                "fOmaxAFA": fOmaxAFA,
            }
        )