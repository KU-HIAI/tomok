import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403030101_06(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.3.1.1 (6)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-25'
    title = '강도'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.3 강관 간의 모멘트접합
    4.3.3.1 원형강관
    4.3.3.1.1 적용한계
    (6)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 강도]
	  B["KDS 14 31 25 4.3.3.1.1 (6)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
    VarOut1[/출력변수: 강도/] ;
    VarIn1[/입력변수: 주강관과 지강관에 대한 항복강도/] ;
    VarOut1 ~~~ VarIn1
    end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.3.1.1 (6)"])
		C --> Variable_def

	  E(["강도"]) ;
    D["<img src='https://latex.codecogs.com/svg.image?F_{y}\leq&space;360MPa'>------------------------"] ;
    Variable_def -->D-->E
    """

    @rule_method
    def strength(fIFy) -> RuleUnitResult:
        """강도

        Args:
            fIFy (float): 주강관과 지강관에 대한 항복강도

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)   4.3.3.1.1 적용한계 (6)의 판단 결과
        """

        assert isinstance(fIFy, float)

        if fIFy <= 360:
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