import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_0405040302(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.5.4.3.2'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '구조물의 최소토피고'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5. 기타 부재
    4.5.4 파형강판 구조물
    4.5.4.3 박스형 파형강판 구조물
    4.5.4.3.2 최소토피고
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 구조물의 최소토피고] ;
		B["KDS 14 31 10 4.5.4.3.2"] ;
		A ~~~ B
		end

    subgraph Variable_def
    VarIn1[/입력변수: 구조물의 최소토피고/] ;
		end

    Python_Class ~~~ C(["KDS 14 31 10 4.5.4.3.2"])
		C --> Variable_def

		Q{"구조물의 최소토피고 &ge; 0.3m"}

		Variable_def --> Q --> X(["PASS or Fail"])
    """


    @rule_method
    def minimum_cover_of_the_structure(fIHmin) -> RuleUnitResult:
        """구조물의 최소토피고

        Args:
            fIHmin (float): 구조물의 최소토피고

        Returns:
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법)  4.5.4.3.2 최소토피고의 판단 결과
        """

        assert isinstance(fIHmin, float)

        if fIHmin >= 0.3:
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