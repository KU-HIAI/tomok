import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040303011101_01_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.3.3.1.11.1 (1) ③'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '중간수직보강재의 거리 제한 사항'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.1 플레이트거더
    4.3.3.1.11 보강재
    4.3.3.1.11.1 중간수직보강재
    (1)
    ③
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 중간수직보강재의 거리 제한 사항] ;
		B["KDS 14 31 10 4.3.3.1.11.1 (1) ③"] ;
		A ~~~ B
		end

    subgraph Variable_def
      VarIn1[/입력변수: 웨브-플랜지 용접부/] ;
      VarIn2[/입력변수: 수평보강재-웨브 용접단까지의 거리/] ;
      VarIn3[/입력변수: 웨브두께/] ;
			end

			Python_Class ~~~ C1(["KDS 14 31 10 4.3.3.1.11.1 (1) ③"]) --> Variable_def

    C["<img src=https://latex.codecogs.com/svg.image?4t_{w}\leq&space;A&space;or&space;B\leq&space;6t_{w}and&space;100mm>------------------------------------------------"]
    D["웨브-플랜지 용접부 = A"]
    E["수평보강재-웨브 용접단까지의 거리 = B"]

    Variable_def --> D & E -->C -->F(["PASS or Fail"])
    """

    @rule_method
    def Distance_restrictions_for_intermediate_vertical_stiffener(fIweflwe,fIhswdwe,fItw) -> RuleUnitResult:
        """중간수직보강재의 거리 제한 사항

        Args:
            fIweflwe (float): 웨브-플랜지 용접부
            fIhswdwe (float): 수평보강재-웨브 용접단까지의 거리
            fItw (float): 웨브두께

        Returns:
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법)  4.3.3.1.11.1 중간수직보강재 (1) ③의 판단 결과
        """

        assert isinstance(fIweflwe, float)
        assert isinstance(fIhswdwe, float)
        assert isinstance(fItw, float)


        if 4 * fItw <= fIweflwe <= 6 * fItw and fIweflwe <= 100 or 4 * fItw <= fIhswdwe <= 6 * fItw and fIhswdwe <= 100:
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