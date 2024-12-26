import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040104_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.1.4 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '조립인장재'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.1 인장부재
    4.1.4 조립 인장부재
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[조립 인장부재] ;
		B["KDS 14 31 10 4.1.4(2)"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarIn1[/입력변수: 조립인장재/]
    VarIn2[/입력변수: 세장비/]

		end

		Python_Class ~~~ Variable_def
  	C["끼움재를 사용한 2개 이상의 형강으로 구성된 조립인장재"]
    E["세장비 ≤ 300"]
	  Variable_def --> C
    C-->E --> Q(["PASS or Fail"])
    """

    @rule_method
    def assembly_tension_member(fILr) -> RuleUnitResult:
        """조립인장재

        Args:
            fILr (float): 세장비

        Returns:
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법)  4.1.4 조립 인장부재 (2)의 통과여부
        """

        assert isinstance(fILr, float)

        if fILr <= 300:
          return RuleUnitResult(
              result_variables = {
                "pass_fail": True,
              }
          )

        else :
          return RuleUnitResult(
              result_variables = {
                "pass_fail": False,
              }
          )