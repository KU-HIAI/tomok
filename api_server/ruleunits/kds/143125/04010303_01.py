import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_04010303_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.3.3 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-14'
    title = '볼트의 인장 및 전단강도'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.3 볼트
    4.1.3.3 볼트의 인장 및 전단강도
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A([Title: 볼트의 인장 및 전단강도])
  	B["KDS 14 31 25 4.1.3.3(1)"]
	  A ~~~ B
	  end

  	subgraph Variable_def
  	VarOut1[/출력변수: 설계인장강도/]
  	VarOut2[/출력변수: 설계전단강도/]
  	VarIn1[/입력변수: 저항계수/]
  	VarIn2[/입력변수: 공칭인장강도/]
  	VarIn3[/입력변수: Fnv/]
  	VarIn4[/입력변수: 볼트, 또는 나사강봉의 나사가 없는 부분의 공칭단면적/]
  	VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2 & VarIn3
  	VarIn2 ~~~ VarIn4
  	end

	  Python_Class ~~~ C(["KDS 14 31 25 4.1.3.3(1)"])
		C --> Variable_def

    Variable_def --> D --> E


	  D["<img src='https://latex.codecogs.com/svg.image?R_n=F_nA_b'>-----------------------------------------------"]
	  E(["<img src='https://latex.codecogs.com/svg.image?\phi&space;R_n'>----------------"])
    """

    @rule_method
    def Tensile_and_shear_strength_of_bolt(fIphi,fIFn,fIAb) -> RuleUnitResult:
        """볼트의 인장 및 전단강도

        Args:
            fIphi (float): 저항계수
            fIFn (float): 공칭인장강도
            fIAb (float): 볼트, 또는 나사 강봉의 나사가 없는 부분의 공칭단면적

        Returns:
            fOphiRn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.1.3.3 볼트의 인장 및 전단강도 (1)의 값
        """

        assert isinstance(fIphi, float)
        assert isinstance(fIFn, float)
        assert isinstance(fIAb, float)

        fOphiRn = fIphi * fIFn * fIAb

        return RuleUnitResult(
            result_variables = {
                "fOphiRn": fOphiRn,
            }
        )