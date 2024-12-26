import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_04060604_06(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.6.6.4 (6)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-14'
    title = '축력 작용에 의한 공칭전단강도'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.6 철근콘크리트 기둥의 연성도 내진설계
    4.6.6.4 전단 설계
    (6)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 축력 작용에 의한 공칭전단강도]
	  B["KDS 24 17 11 4.6.6.4(6)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: 축력 작용에 의한 공칭전단강도/]
	  VarIn1[/입력변수: 교각의 최소 계수축력/]
	  VarIn2[/입력변수: 고려하는 방향으로의 단면 최대 두께/]
	  VarIn3[/입력변수: 기둥 형상비의 기준이 되는 기둥 길이/]
  	VarOut ~~~ VarIn1 & VarIn2 & VarIn3
  	end

  	Python_Class ~~~ C(["KDS 24 17 11 4.6.6.4(6)"])
		C --> Variable_def--> D --> E

  	D["<img src='https://latex.codecogs.com/svg.image?&space;V_p=0.15\frac{P_yh}{L_s}'>-------------------------"]
	  E(["<img src='https://latex.codecogs.com/svg.image?&space;V_p'>"])
    """

    @rule_method
    def nominal_shear_strength_by_axial_force(fIPu,fIh,fILs) -> RuleUnitResult:
        """축력 작용에 의한 공칭전단강도

        Args:
            fIPu (float): 교각의 최소 계수축력
            fIh (float): 고려하는 방향으로의 단면 최대 두께
            fILs (float): 기둥 형상비의 기준이 되는 기둥 길이

        Returns:
            fOVp (float): 교량내진설계기준(한계상태설계법) 4.6.6.4 전단 설계 (6)의 값
        """

        assert isinstance(fIPu, float)
        assert isinstance(fIh, float)
        assert isinstance(fILs, float)
        assert fILs > 0

        fOVp = 0.15 * fIPu * fIh / fILs

        return RuleUnitResult(
            result_variables = {
                "fOVp": fOVp,
                }
            )