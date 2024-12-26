import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_04010308_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.3.8 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '휨모멘트를 받는 핀의 설계전단강도'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.3 볼트
    4.1.3.8 핀접합
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
    A[Title: 휨모멘트를 받는 핀의 설계전단강도]
    B["KDS 14 31 25 4.1.3.8 (2)"]
  	A ~~~ B
  	end

	  subgraph Variable_def
	  VarOut1[/출력변수: 설계전단강도/]
		VarIn1[/입력변수: 핀의 항복강도/]
		VarIn2[/입력변수: 부재의 총단면적/]
	  VarOut1 ~~~ VarIn1 & VarIn2
	  end

		Python_Class ~~~ C(["KDS 14 31 25 4.1.3.8 (2)"])
		C --> Variable_def

	  Variable_def --> D --> E
	  D["<img src='https://latex.codecogs.com/svg.image?V_n=0.6F_yA_\rho&space;'>-------------------------------"]
	  E(["<img src='https://latex.codecogs.com/svg.image?\phi&space;V_n'>-------------"])
    """

    @rule_method
    def Design_shear_strength_of_pins_subjected_to_bending_moments(fIFy,fIAg) -> RuleUnitResult:
        """휨모멘트를 받는 핀의 설계전단강도

        Args:
            fIFy (float): 핀의 항복강도
            fIAg (float): 부재의 총단면적

        Returns:
            fOphiVn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.1.3.8 핀접합 (2)의 값
        """

        assert isinstance(fIFy, float)
        assert isinstance(fIAg, float)

        fOphiVn = 0.9 * 0.6 * fIFy * fIAg

        return RuleUnitResult(
            result_variables = {
                "fOphiVn": fOphiVn,
            }
        )