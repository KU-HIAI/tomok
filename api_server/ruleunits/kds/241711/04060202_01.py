import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_04060202_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.6.2.2 (1)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-19'
    title = '축방향력을 고려한 교각의 항복강성'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.2 교각의 해석 및 설계 강도
    4.6.2.2 교각의 휨강성
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 축방향력을 고려한 교각의 항복강성]
	  B["KDS 24 17 11 4.6.2.2(1)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
  	VarOut[/출력변수: 축방향력을 고려한 교각의 항복강성/]
  	VarIn1[/입력변수: 축방향력을 고려한 교각의 항복모멘트/]
  	VarIn2[/입력변수: 축방향력을 고려한 교각의 항복곡률/]
  	VarOut ~~~ VarIn1 & VarIn2
  	end

	  Python_Class ~~~ C(["KDS 24 17 11 4.6.2.2(1)"])
		C --> Variable_def

	  Variable_def --> D --> E
   	D["<img src='https://latex.codecogs.com/svg.image?EI_y=\frac{M_u}{\psi&space;_u}'------------------------------------>"]
  	E(["<img src='https://latex.codecogs.com/svg.image?EI_{y}'>--------"])
    """

    @rule_method
    def yield_stiffness_of_pier_axial_direction(fIMy,fIpsi) -> RuleUnitResult:
        """축방향력을 고려한 교각의 항복강성

        Args:
            fIMy (float): 축방향을 고려한 교각의 항복모멘트
            fIpsi (float): 축방향력을 고려한 교각의 항복곡률

        Returns:
            fOEIy (float): 교량내진설계기준(한계상태설계법) 4.6.2.2 교각의 휨강성 (1)의 값
        """

        assert isinstance(fIMy, float)
        assert isinstance(fIpsi, float)
        assert fIpsi != 0

        fOEIy = fIMy / fIpsi

        return RuleUnitResult(
            result_variables = {
                "fOEIy": fOEIy,
            }
        )