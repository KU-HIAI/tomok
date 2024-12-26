import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_040108_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.8 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '설계지압강도'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.8 주각부 및 콘크리트의 지압
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 설계지압강도]
	  B["KDS 14 31 25 4.1.8 (1)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
    VarOut[/출력변수: 설계지압강도/]
  	VarIn1[/입력변수: 콘크리트의 공칭지압강도/]
	  VarIn2[/입력변수: 콘크리트의 설계기준 압축강도/]
  	VarIn3[/입력변수: 베이스플레이트의 면적/]
  	VarOut ~~~ VarIn1 & VarIn2 & VarIn3
  	end

    Python_Class ~~~ C(["KDS 14 31 25 4.1.8 (1)"])
		C --> Variable_def

	  Variable_def --> F --> D --> E
  	F["콘크리트의 총단면이 지압을 받는 경우"]
  	D["<img src='https://latex.codecogs.com/svg.image?P_p=0.85f_{ck}A_1'>------------------------------"]
  	E(["<img src='https://latex.codecogs.com/svg.image?P_p'>----------"])
    """

    @rule_method
    def nominal_bearing_strength(fIfck,fIA1) -> RuleUnitResult:
        """설계지압강도

        Args:
            fIfck (float): 콘크리트의 설계기준 압축강도
            fIA1 (float): 베이스플레이트의 면적

        Returns:
            fOPp (float): 강구조 연결 설계기준(하중저항계수설계법)  4.1.8 주각부 및 콘크리트의 지압 (1)의 값
        """

        assert isinstance(fIfck, float)
        assert isinstance(fIA1, float)

        fOPp = (0.85)*fIfck*fIA1

        return RuleUnitResult(
            result_variables = {
                "fOPp": fOPp,
            }
        )