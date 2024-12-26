import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040303020701_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.3.3.2.7.1 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '정모멘트 구간 플랜지와 웨브의 최소항복강도'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.2 박스거더
    4.3.3.2.7 휨강도-정모멘트부
    4.3.3.2.7.1 조밀단면
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 정모멘트 구간 플랜지와 웨브의 최소항복강도] ;
		B["KDS 14 31 10 4.3.3.2.7.1 (1)"] ;
		A ~~~ B
		end

    subgraph Variable_def
    VarIn1[/입력변수: 계수하중에 의한 단면의 주축에 대한 휨모멘트/] ;
    VarIn2[/입력변수: 휨에 대한 강도저항계수/] ;
    VarIn3[/입력변수: 단면의 공칭휨강도/] ;
		end
		Python_Class ~~~ C1(["KDS 14 31 10 4.3.3.2.7.1 (1)"]) -->Variable_def

		C["<img src=https://latex.codecogs.com/svg.image?M_{u}\leq\phi&space;_{f}M_{n}>--------------------------"]

		Variable_def --> C --> F(["PASS or Fail"])
    """

    @rule_method
    def Minimum_yield_strength_of_flange(fIMu,fIphif,fIMn) -> RuleUnitResult:
        """정모멘트 구간 플랜지와 웨브의 최소항복강도

        Args:
            fIMu (float): 계수하중에 의한 단면의 주축에 대한 휨모멘트
            fIphif (float): 휨에 대한 강도저항계수
            fIMn (float): 단면의 공칭휨강도

        Returns:
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법)  4.3.3.2.7.1 조밀단면 (1)의 통과여부
        """

        assert isinstance(fIMu, float)
        assert isinstance(fIphif, float)
        assert isinstance(fIMn, float)

        if fIMu <= fIphif * fIMn:
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