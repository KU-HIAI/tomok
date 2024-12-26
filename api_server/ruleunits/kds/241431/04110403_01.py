import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241431_04110403_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 31 4.11.4.3 (1)'
    ref_date = '2018-08-30'
    doc_date = '2024-02-21'
    title = '플랜지의 폭-두께비'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.11 구조형식
    4.11.4 충복아치
    4.11.4.3 플랜지 좌굴
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 플랜지의 폭-두께비];
    B["KDS 24 14 31 4.11.4.3 (1)"];
    A ~~~ B
    end

    subgraph Variable_def;
    VarIn1[/입력변수: 플랜지의 폭-두께비/] ;
    VarIn2[/입력변수: 모멘트 확대계수를 고려한 설계하중에 의한 최대응력/];
    VarIn3[/입력변수: 설계하중에 의한 축방향응력/];
    VarIn4[/입력변수: 탄성계수/];
		VarIn5[/입력변수: 플랜지의 폭/];
    VarIn6[/입력변수: 플랜지의 두께/];

		VarIn1 ~~~ VarIn4
		VarIn2 ~~~ VarIn5
		VarIn3 ~~~ VarIn6
		end

		Python_Class ~~~ C(["KDS 24 14 31 4.11.4.3 (1)"])
		C --> Variable_def

		D{"<img src='https://latex.codecogs.com/svg.image?\frac{b}{t}\leq&space;1.06\sqrt{\frac{E}{f_{a}&plus;f_{b}}}'>----------------------------------------"}

		Variable_def --> D
		D --> E([Pass or Fail])
    """

    @rule_method
    def width_thickness_ratio_of_flange(fIfb,fIfa,fIE,fIb,fIt) -> RuleUnitResult:
        """플랜지의 폭-두께비

        Args:
            fIfb (float): 모멘트 확대계수를 고려한 설계하중에 의한 최대응력
            fIfa (float): 설계하중에 의한 축방향응력
            fIE (float): 탄성계수
            fIb (float): 보강재의 폭
            fIt (float): 보강재의 두께

        Returns:
            pass_fail (bool): 강교 설계기준(한계상태설계법)  4.11.4.3 플랜지 좌굴 (1)의 판단 결과
        """

        assert isinstance(fIfb, float)
        assert fIfb > 0
        assert isinstance(fIfa, float)
        assert fIfa > 0
        assert isinstance(fIE, float)
        assert fIE > 0
        assert isinstance(fIb, float)
        assert isinstance(fIt, float)
        assert fIt != 0

        if fIb / fIt <= 1.06 * (fIE / (fIfa + fIfb))**(1/2) :
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