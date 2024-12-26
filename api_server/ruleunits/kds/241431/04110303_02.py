import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241431_04110303_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 31 4.11.3.3 (2)'
    ref_date = '2018-08-30'
    doc_date = '2024-02-20'
    title = '전체인장을 받는 바닥판 검토'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.11 구조형식
    4.11.3 강바닥판
    4.11.3.3 전체 및 국부적 영향의 중첩
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 전체인장을 받는 바닥판 검토];
    B["KDS 24 14 31 4.11.3.3 (2)"];
    A ~~~ B
    end

    subgraph Variable_def;
    VarIn1[/입력변수: 바닥판의 전체 축방향 응력/] ;
    VarIn2[/입력변수: 바닥판의 전체전단응력/];
    VarIn3[/입력변수: 종방향리브를 포함한 바닥판의 유효단면적/];
    VarIn4[/입력변수: 바닥판의 유효폭을 고려한 바닥강판의 설계인장강도/];
		VarIn5[/입력변수: 설계하중에 의한 종방향리브의 국부 휨모멘트/];
    VarIn6[/입력변수: 연단의 항복 도달을 기준으로 한 종방향 리브의 휨강도/];

		VarIn1 & VarIn2 & VarIn3 ~~~ VarIn4 & VarIn5 & VarIn6
		VarIn1 ~~~ VarIn4
		VarIn2 ~~~ VarIn5
		VarIn3 ~~~ VarIn6
		end

		Python_Class ~~~ C(["KDS 24 14 31 4.11.3.3 (2)"])
		C --> Variable_def

		F{"<img src='https://latex.codecogs.com/svg.image?\frac{P_{u}}{P_{r}}&plus;\frac{M_{ur}}{M_{rr}}\leq&space;1.33'>------------------------------------"}
		D{"<img src='https://latex.codecogs.com/svg.image?P_{u}=A_{d,eff}(f_{g}^{2}&plus;3f_{vg}^{2})^{0.5}'>-----------------------------------------------------------"}
		E([Pass or Fail])

		Variable_def --> D --> F

		F --> E
    """

    @rule_method
    def Examine_the_floor_plate_under_full_tension(fIfg,fIfvg,fIAdeff,fIPr,fIMur,fIMrr) -> RuleUnitResult:
        """전체인장을 받는 바닥판 검토

        Args:
            fIfg (float): 바닥판의 전체 축방향 응력
            fIfvg (float): 바닥판의 전체전단응력
            fIAdeff (float): 종방향리브를 포함한 바닥판의 유효단면적
            fIPr (float): 바닥판의 유효폭을 고려한 바닥강판의 설계인장강도
            fIMur (float): 설계하중에 의한 종방향리브의 국부 휨모멘트
            fIMrr (float): 연단의 항복 도달을 기준으로 한 종방향 리브의 휨강도

        Returns:
            pass_fail (bool): 강교 설계기준(한계상태설계법)  4.11.3.3 전체 및 국부적 영향의 중첩 (2)의 판단 결과
            fOPu (float): 강교 설계기준(한계상태설계법)  4.11.3.3 전체 및 국부적 영향의 중첩 (2)의 값
        """

        assert isinstance(fIfg, float)
        assert isinstance(fIfvg, float)
        assert isinstance(fIAdeff, float)
        assert isinstance(fIPr, float)
        assert fIPr != 0
        assert isinstance(fIMur, float)
        assert isinstance(fIMrr, float)
        assert fIMrr != 0

        fOPu = fIAdeff * (((fIfg**2) + 3 * (fIfvg**2))**0.5)
        if (fOPu / fIPr) + (fIMur / fIMrr) <= 1.33 :
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