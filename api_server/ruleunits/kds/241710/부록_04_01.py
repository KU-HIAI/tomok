import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241710_부록_04_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 10 부록 4 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-20'
    title = '설계전단강도'

    description = """
    교량 내진설계기준(일반설계법)
    부록. 철근콘크리트 기둥의 연성도 내진설계
		4. 전단 설계
		(1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 설계전단강도]
	  B["KDS 24 17 10 부록 4 (1)"]
	  A ~~~ B
	  end

	  subgraph Variable_def;
		VarIn1[/입력변수:공칭전단강도/];
		VarIn2[/입력변수:강도감소계수/];

		VarOut1[/출력변수: 설계전단강도/];
		VarOut1~~~VarIn1 & VarIn2

		end

	  Python_Class ~~~ C(["KDS 24 17 10 부록 4 (1)"])
		C --> Variable_def

	  Variable_def--->D--->E--->F
		D["강도감소계수=1.0"]

		E["설계전단강도=공칭전단강도 x 강도감소계수"]

		F(["설계전단강도"])
    """

    @rule_method
    def Design_shear_strength(fInoshst) -> RuleUnitResult:
        """설계전단강도

        Args:
            fInoshst (float): 공칭전단강도

        Returns:
            fOshstr (float): 교량 내진설계기준(일반설계법) 부록 4. 전단 설계 (1)의 값 1
            fOphi (float): 교량 내진설계기준(일반설계법) 부록 4. 전단 설계 (1)의 값 2
        """

        assert isinstance(fInoshst, float)

        fOphi = 1
        fOshstr = fInoshst * fOphi

        return RuleUnitResult(
            result_variables = {
                "fOshstr": fOshstr,
            }
        )