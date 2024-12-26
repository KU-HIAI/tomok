import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_04050203(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.5.2.3'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '아이바 핀의 직경'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5. 기타 부재
    4.5.2 핀
    4.5.2.3 아이바 핀의 최소치수
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 아이바 핀의 직경] ;
		B["KDS 14 31 10 4.5.3.4 (2)"] ;
		A ~~~ B
		end

    subgraph Variable_def
    VarIn1[/입력변수: 핀의 직경/] ;
    VarIn2[/입력변수: 핀의 최소항복강도/] ;
    VarIn3[/입력변수: 아이바 몸체의 폭/] ;

		end

    Python_Class ~~~ C(["KDS 14 31 10 4.5.3.4 (2)"])
		C --> Variable_def

		E{"<img src=https://latex.codecogs.com/svg.image?D\geq\left(\frac{3}{4}&plus;\frac{F_{y}}{2760}\right)b>------------------------------------------"}

		Variable_def --> E --> D(["PASS or Fail"])
    """

    @rule_method
    def diameter_of_eyebar_pin(fID,fIFy,fIb) -> RuleUnitResult:
        """아이바 핀의 직경

        Args:
            fID (float): 핀의 직경
            fIFy (float): 핀의 최소항복강도
            fIb (float): 아이바 몸체의 폭

        Returns:
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법) 4.5.2.3 아이바 핀의 최소치수의 통과여부
        """

        assert isinstance(fID, float)
        assert isinstance(fIFy, float)
        assert isinstance(fIb, float)

        if fID >= (3 / 4 + fIFy / 2760) * fIb:
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