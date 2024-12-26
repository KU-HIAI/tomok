import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040303020702_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.3.3.2.7.2 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '비조밀단면의 공칭휨강도'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.2 박스거더
    4.3.3.2.7 휨강도-정모멘트부
    4.3.3.2.7.2 비조밀단면
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 비조밀단면의 공칭휨강도] ;
		B["KDS 14 31 10 4.3.3.2.7.2 (2)"] ;
		A ~~~ B
		end

    subgraph Variable_def
		VarOut1[/출력변수: 압축플랜지 공칭휨강도/] ;
    VarOut2[/출력변수: 인장플랜지 공칭휨강도/] ;
    VarIn1[/입력변수: 웨브 응력감소계수/] ;
    VarIn2[/입력변수: 하이브리드 단면의 응력감소계수/] ;
    VarIn3[/입력변수: 압축플랜지의 최소항복강도/] ;
    VarIn4[/입력변수: 하중조합으로 구해진 1차 층간변위/] ;
    VarIn5[/입력변수: 계수하중에 의한 플랜지의 순수비틀림 전단응력/] ;
    VarIn6[/입력변수: 박스거더 단면의 폐합단면적/] ;
    VarIn7[/입력변수: 계수하중에 의한 내부 비틀림모멘트/] ;
    VarIn8[/입력변수: 인장플랜지의 최소항복강도/] ;
    VarIn9[/입력변수: 계수하중에 의한 플랜지의 순수비틀림 전단응력/] ;
		end

		VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2 & VarIn3
		VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
		VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9

		Python_Class ~~~ C(["KDS 14 31 10 4.3.3.2.7.2 (2)"])
		C --> Variable_def

		D["<img src=https://latex.codecogs.com/svg.image?F_{nc}=R_{b}R_{h}F_{yc}>--------------------------"]
		E["<img src=https://latex.codecogs.com/svg.image?F_{nc}=R_{b}R_{h}F_{yc}\Delta&space;>--------------------------"]
		F["<img src=https://latex.codecogs.com/svg.image?\Delta=\sqrt{1-3(\frac{f_{v}}{F_{yc}})^{2}}>--------------------------"]
		I["<img src=https://latex.codecogs.com/svg.image?F_{nt}=R_{h}F_{yt}\Delta&space;>--------------------------"]
		J["<img src=https://latex.codecogs.com/svg.image?\Delta=\sqrt{1-3(\frac{f_{v}}{F_{yt}})^{2}}>--------------------------"]

		Variable_def --"U형단면 박스의 압축플랜지"--> D --> G(["<img src=https://latex.codecogs.com/svg.image?F_{nc}>---------"])
		Variable_def --"폐단면 박스의 압축플랜지"--> F --> E --> G
		Variable_def --"인장플랜지"--> J --> I --> G
    """

    @rule_method
    def nominal_flexural_strength_of_noncompact_section(fIFncA,fIFncB,fIFnt,fIRb,fIRh,fIFyc,fIAo,fIT,fIFyt,fItfc,fItft) -> RuleUnitResult:
        """비조밀단면의 공칭휨강도

        Args:
            fIFncA (float): U형단면 박스의 압축플랜지 공칭휨강도
            fIFncB (float): 폐단면 박스의 압축플랜지 공칭휨강도
            fIFnt (float): 인장플랜지 공칭휨강도
            fIRb (float): 웨브응력감소계수
            fIRh (float): 하이브리드 단면의 응력감소계수
            fIFyc (float): 압축플랜지의 최소항복강도
            fIAo (float): 박스거더 단면의 폐합단면적
            fIT (float): 계수하중에 의한 내부 비틀림모멘트
            fIFyt (float): 인장플랜지의 최소항복강도
            fItfc (float): 압축플랜지의 두께
            fItft (float): 인장플랜지의 두께

        Returns:
            fOFnc (float): 강구조부재설계기준(하중저항계수설계법)  4.3.3.2.7.2 비조밀단면 (2)의 값 1
            fOFnt (float): 강구조부재설계기준(하중저항계수설계법)  4.3.3.2.7.2 비조밀단면 (2)의 값 2
            fOdelta (float): 강구조부재설계기준(하중저항계수설계법)  4.3.3.2.7.2 비조밀단면 (2)의 값 3
            fOFv (float): 강구조부재설계기준(하중저항계수설계법)  4.3.3.2.7.2 비조밀단면 (2)의 값 4
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법)  4.3.3.2.7.2 비조밀단면 (2)의 판단 결과
        """

        assert isinstance(fIRb, float)
        assert isinstance(fIRh, float)
        assert isinstance(fIFyc, float)
        assert fIFyc > 0
        assert isinstance(fIAo, float)
        assert fIAo > 0
        assert isinstance(fIT, float)
        assert isinstance(fIFyt, float)
        assert isinstance(fItfc, float)
        assert fItfc > 0
        assert isinstance(fItft, float)

        if fIFncA != 0 and fIFncB == 0 and fIFnt == 0 :
          fOFnc = fIRb * fIRh * fIFyc
          return RuleUnitResult(
              result_variables = {
                  "fOFnc": fOFnc,
              }
          )

        elif fIFncA == 0 and fIFncB != 0 and fIFnt == 0 :
          fOFv = fIT / (2 * fIAo * fItfc)
          fOdelta = (1 - 3 * (fOFv / fIFyc) ** 2) ** 0.5
          fOFnc = fIRb * fIRh * fIFyc * fOdelta
          return RuleUnitResult(
              result_variables = {
                  "fOFnc": fOFnc,
              }
          )

        elif fIFncA == 0 and fIFncB == 0 and fIFnt != 0 :
          fOFv = fIT / (2 * fIAo * fItft)
          fOdelta = (1 - 3 * (fOFv / fIFyc) ** 2) ** 0.5
          fOFnt = fIRh * fIFyt * fOdelta
          return RuleUnitResult(
              result_variables = {
                  "fOFnt": fOFnt,
              }
          )

        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )