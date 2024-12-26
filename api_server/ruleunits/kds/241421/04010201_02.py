import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010201_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.2.1 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '전단보강철근이 없는 부재의 설계전단강도'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.1 일반
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 전단보강철근이 없는 부재의 설계전단강도];
    B["KDS 24 14 21 4.1.2.1 (2)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarOut1[/출력변수: 전단보강철근이 없는 부재의 설계전단강도/];
		VarIn1[/입력변수: 콘크리트 설계전단강도/];

		VarOut1~~~VarIn1

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.2.1 (2)"])
		C --> Variable_def

		Variable_def--->D

		D(["<img src='https://latex.codecogs.com/svg.image?V_{d}=V_{cd}'>---------------------------------"])
    """

    @rule_method
    def Design_shear_strength_of_members_without_shear_rebar(fIVcd) -> RuleUnitResult:
        """전단보강철근이 없는 부재의 설계전단강도

        Args:
            fIVcd (float): 콘크리트 설계전단강도

        Returns:
            fOVd (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.1 일반 (2)의 값
        """

        assert isinstance(fIVcd, float)

        fOVd = fIVcd

        return RuleUnitResult(
            result_variables = {
                "fOVd": fOVd,
            }
        )