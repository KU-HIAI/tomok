import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403030201_08(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.3.2.1 (8)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '연성'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.3 강관 간의 모멘트접합
    4.3.3.2 각형강관
    4.3.3.2.1 적용한계
    (8)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 연성]
	  B["KDS 14 31 25 4.3.3.2.1 (8)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
    VarOut1[/출력변수: 연성/] ;
    VarIn1[/입력변수: 주강관의 항복강도/] ;
    VarIn2[/입력변수: 강재의 최소인장강도/] ;
    VarOut1 ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.3.2.1 (8)"])
		C --> Variable_def

	  D{"<img src='https://latex.codecogs.com/svg.image?F_{y}/F_{u}\leq&space;0.8'>------------------"}
    Variable_def-->D-->Q(["PASS or Fail"])
    """

    @rule_method
    def ductility(fIFy,fIFu) -> RuleUnitResult:
        """연성

        Args:
            fIFy (float) : 주강관의 항복강도
            fIFu (float): 강재의 최소인장강도

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.2.1 적용한계 (8)의 판단 결과
        """

        assert isinstance(fIFy, float)
        assert isinstance(fIFu, float)
        assert fIFu != 0

        if fIFy/fIFu <= 0.8:
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