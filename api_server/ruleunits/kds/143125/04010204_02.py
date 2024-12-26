import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_04010204_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.2.4 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-14'
    title = '필릿용접의 단위길이당 소요강도'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.2 용접
    4.1.2.4 설계강도
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 필릿용접의 단위길이당 소요강도]
	  B["KDS 14 31 25 4.1.2.4(2)"]
	  A ~~~ B
	  end

  	subgraph Variable_def
  	VarOut[/출력변수: 필릿용접의 단위길이당 소요강도/]
  	VarIn1[/입력변수: 필릿용접의 유효면에 작용하는 수직력/]
  	VarIn2[/입력변수: 필릿용접의 유효면에서 용접축에 직각방향으로 작용하는 전단력/]
  	VarIn3[/입력변수: 필릿용접의 유효면에서 용접축에 평행으로 작용하는 전단력/]
  	VarOut ~~~ VarIn1 & VarIn2 & VarIn3
  	end

    Python_Class ~~~ C(["KDS 14 31 25 4.1.2.4(2)"])
		C --> Variable_def

	  Variable_def --> D --> E


	  D["<img src='https://latex.codecogs.com/svg.image?P_u=\sqrt{P_\perp^2&plus;V_\perp^2&plus;V_\parallel^2}'>-----------------------------------------------"]
	  E(["<img src='https://latex.codecogs.com/svg.image?P_u'>----------------"])
    """

    @rule_method
    def design_strength_per_unit_length_of_fillet_weld(fIPperp,fIVperp,fIVii) -> RuleUnitResult:
        """필릿용접의 단위길이당 소요강도

        Args:
            fIPperp (float): 필릿용접의 유효면에 작용하는 수직력
            fIVperp (float): 필릿용접의 유효면에서 용접축에 직각방향으로 작용하는 전단력
            fIVii (float): 필릿용접의 유효면에서 용접축에 평행으로 작용하는 전단력

        Returns:
            fOPu (float): 강구조 연결 설계기준(하중저항계수설계법)  4.1.2.4 설계강도 (2)의 값
        """

        assert isinstance(fIPperp, float)
        assert isinstance(fIVperp, float)
        assert isinstance(fIVii, float)

        fOPu = ((fIPperp**2)+(fIVperp**2)+(fIVii**2))**(1/2)

        return RuleUnitResult(
            result_variables = {
                "fOPu": fOPu,
            }
        )