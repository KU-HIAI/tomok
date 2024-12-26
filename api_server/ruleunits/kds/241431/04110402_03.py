import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241431_04110402_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 31 4.11.4.2 (3)'
    ref_date = '2018-08-30'
    doc_date = '2024-02-20'
    title = '아치리브 복부판의 세장비'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.11 구조형식
    4.11.4 충복아치
    4.11.4.2 복부판의 세장비
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 아치리브 복부판의 세장비];
    B["KDS 24 14 31 4.11.4.2 (3)"];
    A ~~~ B
    end

    subgraph Variable_def;
    VarIn1[/입력변수: 보강재의 폭-두께비/] ;
    VarIn2[/입력변수: 모멘트 확대계수를 고려한 설계하중에 의한 최대응력/];
    VarIn3[/입력변수: 설계하중에 의한 축방향응력/];
    VarIn4[/입력변수: 탄성계수/];
		VarIn5[/입력변수: 보강재의 폭/];
    VarIn6[/입력변수: 보강재의 두께/];

		VarIn1 ~~~ VarIn4
		VarIn2 ~~~ VarIn5
		VarIn3 ~~~ VarIn6
		end

		Python_Class ~~~ C(["KDS 24 14 31 4.11.4.2 (3)"])
		C --> Variable_def

		D{"<img src='https://latex.codecogs.com/svg.image?\frac{b}{t_{s}}\leq&space;0.408\sqrt{\frac{E}{f_{a}&plus;\frac{f_{b}}{3}}}\leq&space;12'>-----------------------------------------------"}

		Variable_def --> D --> E([Pass or Fail])
    """

    @rule_method
    def stiffener_width_thickness_ratio(fIfb,fIfa,fIE,fIb,fIts) -> RuleUnitResult:
        """아치리브 복부판의 세장비

        Args:
            fIfb (float): 모멘트 확대계수를 고려한 설계하중에 의한 최대응력
            fIfa (float): 설계하중에 의한 축방향응력
            fIE (float): 탄성계수
            fIb (float): 보강재의 폭
            fIts (float): 보강재의 두께

        Returns:
            pass_fail (bool): 강교 설계기준(한계상태설계법)  4.11.4.2 복부판의 세장비 (3)의 판단 결과
        """

        assert isinstance(fIfb, float)
        assert fIfb > 0
        assert isinstance(fIfa, float)
        assert fIfa > 0
        assert isinstance(fIE, float)
        assert fIE > 0
        assert isinstance(fIb, float)
        assert isinstance(fIts, float)
        assert fIts != 0

        if fIb / fIts <= 0.408 * (fIE / (fIfa + fIfb / 3))**0.5 <= 12 :
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