import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403030201_05(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.3.2.1 (5)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '폭 비'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.3 강관 간의 모멘트접합
    4.3.3.2 각형강관
    4.3.3.2.1 적용한계
    (5)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 폭 비]
	  B["KDS 14 31 25 4.3.3.2.1 (5)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
    VarOut1[/출력변수: 폭비/] ;
    VarIn1[/입력변수: 지강관의 폭비/] ;
    VarOut1 ~~~ VarIn1
    end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.3.2.1 (5)"])
		C --> Variable_def

	  D{"폭비 ≥ 0.25"}
    Variable_def-->D-->Q(["PASS or Fail"])
    """

    @rule_method
    def width_ratio(fIbeta) -> RuleUnitResult:
        """폭 비

        Args:
            fIbeta (float): 폭비

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.2.1 적용한계 (5)의 판단 결과
        """

        assert isinstance(fIbeta, float)

        if fIbeta >= 0.25 :
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