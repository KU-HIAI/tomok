import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403030201_06(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.3.2.1 (6)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '형상비'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.3 강관 간의 모멘트접합
    4.3.3.2 각형강관
    4.3.3.2.1 적용한계
    (6)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 형상비]
	  B["KDS 14 31 25 4.3.3.2.1 (6)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
    VarOut1[/출력변수: 형상비/] ;
    VarIn1[/입력변수: 높이와 폭의 비/] ;
    VarOut1 ~~~ VarIn1
    end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.3.2.1 (6)"])
		C --> Variable_def

	  D{"0.5≤높이와 폭의 비≤2.0"}
    Variable_def-->D-->Q(["PASS or Fail"])
    """

    @rule_method
    def aspect_ratio(fIasprat) -> RuleUnitResult:
        """형상비

        Args:
            fIasprat (float): 형상비

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.2.1 적용한계 (6)의 판단 결과
        """

        assert isinstance(fIasprat, float)

        if 0.5<= fIasprat <=2.0:
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