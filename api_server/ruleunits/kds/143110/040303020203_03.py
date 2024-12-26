import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040303020203_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.3.3.2.2.3 (3)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '웨브의 경사도'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.2 박스거더
    4.3.3.2.2 단면비 요구조건
    4.3.3.2.2.3 다중 박스단면의 활하중 분배계수 적용 특별제한
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 웨브의 경사도] ;
		B["KDS 14 31 10 4.3.3.2.2.3 (3)"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarIn1[/입력변수: 웨브의 경사도/] ;
			end
			Python_Class ~~~ C1(["KDS 14 31 10 4.3.3.2.2.3 (3)"]) -->Variable_def

			D["1/4 &ge; 웨브의 경사도"]

			Variable_def --> D --> F(["PASS or Fail"])
    """

    @rule_method
    def slope_of_the_web(fIsloweb) -> RuleUnitResult:
        """웨브의 경사도

        Args:
            fIsloweb (float): 웨브의 경사도

        Returns:
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법) 4.3.3.2.2.3 다중 박스단면의 활하중 분배계수 적용 특별제한 (3)의 통과여부
        """

        assert isinstance(fIsloweb, float)


        if fIsloweb <= 1 / 4:
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