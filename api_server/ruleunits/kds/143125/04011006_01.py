import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_04011006_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.10.6 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '웨브 패널존 공칭강도'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.10 집중하중을 받는 플랜지와 웨브
    4.1.10.6 웨브 패널존 전단강도
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 웨브 패널존 공칭강도]
	  B["KDS 14 31 25 4.1.10.6 (1)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
    VarOut[/출력변수: 전단력과 압축력을 받는 패널존의 설계강도/]
  	VarIn1[/입력변수: 웨브 패널존 공칭강도/]
  	VarIn2[/입력변수: 소요강도/]
  	VarIn3[/입력변수: 기둥의 축방향 항복강도/]
  	VarIn4[/입력변수: 기둥웨브의 명시된 최소항복강도/]
  	VarIn5[/입력변수: 기둥의 높이/]
  	VarIn6[/입력변수: 기둥웨브의 두께/]

  	VarOut ~~~ VarIn1 & VarIn2 & VarIn3
  	VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
  	end


    Python_Class ~~~ C(["KDS 14 31 25 4.1.10.6 (1)"])
		C --> Variable_def

	  Variable_def --> I --> D --> E
  	E --Pass--> F
  	E --Fail--> G
  	F & G --> H
  	I["골조 안정성에 대한 패널존 변형의 효과가 해석에서 고려되지않을때"]
  	D{"<img src='https://latex.codecogs.com/svg.image?P_r\leq&space;0.4P_c'>----------------------"}
  	E["Pass or Fail"]
  	F["<img src='https://latex.codecogs.com/svg.image?R_n=0.60F_yd_ct_w'>---------------------------------------------"]
  	G["<img src='https://latex.codecogs.com/svg.image?R_n=0.60F_yd_ct_w(1.4-\frac{P_r}{P_c})'>----------------------------------------------------"]
  	H(["<img src='https://latex.codecogs.com/svg.image?R_n'>"])
    """

    @rule_method
    def Nominal_strength_of_panel_zone(fIPr,fIPc,fIFy,fIdc,fItw) -> RuleUnitResult:
        """웨브 패널존 공칭강도

        Args:
            fIPr (float): 소요강도
            fIPc (float): 기둥의 축방향 항복강도
            fIFy (float): 기둥 웨브의 명시된 최소 항복강도
            fIdc (float): 기둥의 높이
            fItw (float): 기둥 웨브의 두께

        Returns:
            fORn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.1.10.6 웨브 패널존 전단강도 (1)의 값
        """

        assert isinstance(fIPr, float)
        assert isinstance(fIPc, float)
        assert fIPc != 0
        assert isinstance(fIFy, float)
        assert isinstance(fIdc, float)
        assert isinstance(fItw, float)

        if fIPr <= (0.4)*fIPc:
          fORn = 0.6 * fIFy * fIdc * fItw
        else:
          fORn = 0.6 * fIFy * fIdc * fItw * (1.4-fIPr/fIPc)

        return RuleUnitResult(
            result_variables = {
                "fORn": fORn,
            }
        )