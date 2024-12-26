import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403010202_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.1.2.2 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '각형강관 제한조건'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.1 강관구조의 집중하중
    4.3.1.2 축직각방향 집중하중
    4.3.1.2.2 각형강관
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 각형강관 제한조건]
	  B["KDS 14 31 25 4.3.1.2.2 (1)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn1[/입력변수: 접합평면과 90°를 이루는 판폭/]
	  VarIn2[/입력변수: 접합평면과 90°를 이루는 각형 강관폭/]
	  VarIn1 ~~~ VarIn2
	  end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.1.2.2 (1)"])
		C --> Variable_def

	  Variable_def --> E --> K
	  E{"<img src='https://latex.codecogs.com/svg.image?0.2<B_p/B\leq&space;1.0'>--------------------------------------------"}
		K(["Pass or Fail"])
    """

    @rule_method
    def Restriction_conditions_of_square_pipe(fIBp,fIB) -> RuleUnitResult:
        """각형강관 제한조건

        Args:
            fIBp (float): 접합평면과 90°를 이루는 판폭
            fIB (float): 접합평면과 90°를 이루는 각형 강관폭

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.1.2.2 각형강관 (1)의 판단 결과
        """

        assert isinstance(fIBp, float)
        assert isinstance(fIB, float)
        assert fIB != 0

        if 0.25 < fIBp / fIB <= 1.0:
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