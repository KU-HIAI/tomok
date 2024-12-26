import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_040501_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.5.1 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-21'
    title = '경량콘크리트의 최소피복두께'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.5 철근 상세
    4.5.1 일반
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 경량콘크리트의 최소피복두께];
    B["KDS 24 14 21 4.5.1 (2)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarOut1["경량콘크리트의 최소피복두께"]
		VarIn1["콘크리트 최소피복두께"]
		VarOut1~~~VarIn1

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.5.1 (2)"])
		C --> Variable_def

		Variable_def--->D--->F
		D["경량콘크리트의 최소피복두께=콘크리트 최소피복두께+5mm"]

		F(["경량콘크리트의 최소피복두께"])
    """

    @rule_method
    def Minimum_cover_thickness_of_lightweight_concrete(fImincoc) -> RuleUnitResult:
        """경량콘크리트의 최소피복두께

        Args:
            fImincoc (float): 콘크리트 최소피복두께

        Returns:
            fOmictlc (float): 콘크리트교 설계기준 (한계상태설계법)  4.5.1 일반 (2)의 값
        """

        fOmictlc = fImincoc + 5

        return RuleUnitResult(
            result_variables = {
                "fOmictlc": fOmictlc,
            }
        )