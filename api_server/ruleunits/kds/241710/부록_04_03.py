import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241710_부록_04_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 10 부록 4 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-20'
    title = '단부구역의 공칭전단강도'

    description = """
    교량 내진설계기준(일반설계법)
    부록. 철근콘크리트 기둥의 연성도 내진설계
		4. 전단 설계
		(3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 단부구역의 공칭전단강도]
	  B["KDS 24 17 10 부록 4 (3)"]
	  A ~~~ B
	  end

	  subgraph Variable_def;
		VarIn1[/입력변수:축력 작용에 의한 공칭전단강도/];
		VarIn2[/입력변수:콘크리트에 의한 공칭전단강도/];
		VarIn3[/입력변수:전단철근에 의한 공칭전단강도/];

		VarOut1[/출력변수:단부구역을 제외한 구역의 공칭전단강도/];
		VarOut1~~~VarIn1 & VarIn2  & VarIn3

		end

	  Python_Class ~~~ C(["KDS 24 17 10 부록 4 (3)"])
		C --> Variable_def

	  Variable_def--->E--->F

		E["<img src='https://latex.codecogs.com/svg.image?\inline&space;V_n=V_c&plus;V_s&plus;V_p'>---------------------------------"]

		F(["단부구역을 제외한 구역의 공칭전단강도"])
    """

    @rule_method
    def Nominal_shear_strength_in_end_region(fIVc,fIVs,fIVp) -> RuleUnitResult:
        """단부구역의 공칭전단강도

        Args:
            fIVc (float): 콘크리트에 의한 공칭전단강도
            fIVs (float): 전단철근에 의한 공칭전단강도
            fIVp (float): 축력 작용에 의한 공칭전단강도

        Returns:
            fOVn (float): 교량 내진설계기준(일반설계법) 부록 4. 전단 설계 (3)의 값
        """

        assert isinstance(fIVc, float)
        assert isinstance(fIVs, float)
        assert isinstance(fIVp, float)

        fOVn = fIVc + fIVs + fIVp

        return RuleUnitResult(
            result_variables = {
                "fOVn": fOVn,
            }
        )