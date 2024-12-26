import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403010102(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.1.1.2'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '강관에 대한 연성'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.1 강관구조의 집중하중
    4.3.1.1 적용한계
    4.3.1.1.2 연성
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 강관에 대한 연성]
	  B["KDS 14 31 25 4.3.1.1.2"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn1[/입력변수: 강재의 항복강도/]
	  VarIn2[/입력변수: 강재의 최소인장강도/]
	  end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.1.1.2"])
		C --> Variable_def

	  Variable_def --> E --> D(["PASS or Fail"])
	  E{"<img src='https://latex.codecogs.com/svg.image?F_y/F_u\leq&space;0.8'>-------------------------"}
    """

    @rule_method
    def Ductile_strength_of_steel(fIFy,fIFu) -> RuleUnitResult:
        """강관에 대한 연성

        Args:
            fIFy (float): 강재의 항복강도
            fIFu (float): 강재의 최소인장강도

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.1.1.2 연성의 판단 결과
        """

        assert isinstance(fIFy, float)
        assert isinstance(fIFu, float)
        assert fIFu != 0

        if fIFy / fIFu <= 0.8:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )