import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040303011103_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.3.3.1.11.3 (3)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '수평보강재의 단면2차모멘트와 회전반경'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.1 플레이트거더
    4.3.3.1.11 보강재
    4.3.3.1.11.3 수평보강재
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 수평보강재의 단면2차모멘트와 회전반경] ;
		B["KDS 14 31 10 4.3.3.1.11.3 (3)"] ;
		A ~~~ B
		end

    subgraph Variable_def
    VarIn1[/출력변수: 수평보강재의 단면2차모멘트/] ;
    VarIn2[/입력변수: 수평보강재 안의 최대 웨브 높이/] ;
    VarIn3[/입력변수: 웨브두께/] ;
    VarIn4[/입력변수: 수직보강재 간격/] ;
    VarIn5[/출력변수: 수평보강재 휨강성을 위한 곡률보정계수/] ;
    VarIn6[/입력변수: 조합단면의 중립축에 대한 회전반경/] ;
    VarIn7[/입력변수: 보강재의 최소항복강도/] ;
    VarIn8[/입력변수: 압축플랜지의 최소항복강도/] ;
    VarIn9[/입력변수: 강재의 탄성계수/] ;
    VarIn10[/입력변수: 하이브리드 단면의 응력감소계수/] ;
    VarIn11[/입력변수: 곡률인자/] ;
    VarIn12[/입력변수: 해당 패널의 최소거더반경/] ;
    VarIn13[/입력변수: 수직보강재 간격/] ;
    VarIn14[/입력변수: 웨브두께/] ;
    end
    VarIn1 & VarIn2 & VarIn3 ~~~ VarIn4 & VarIn5 & VarIn6
    VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9
    VarIn8 ~~~ VarIn10 & VarIn11 & VarIn12
    VarIn11 ~~~ VarIn13 & VarIn14

    D["<img src=https://latex.codecogs.com/svg.image?Z=\frac{0.95d_{0}^{2}}{Rt_{w}}\leq&space;10>------------------------------"]
    E["<img src=https://latex.codecogs.com/svg.image?I_{l}=Dt_{w}^{3}[2.4(\frac{d_{0}}{D})^{2}-0.13]\beta&space;>--------------------------------------------------"]
    F{"<img src=https://latex.codecogs.com/svg.image?r\geq\frac{0.16d_{0}\sqrt{\frac{F_{ys}}{E}}}{\sqrt{1-0.6\frac{F_{yc}}{R_{h}F_{ys}}}}>------------------------------------------------------------------------"}
    G{"수평보강재가 곡률중심 쪽 웨브면에 설치된 경우"}

		Python_Class ~~~ C(["KDS 14 31 10 4.3.3.1.11.3 (3)"])
		C --> Variable_def

		Variable_def --> D --> G --"yes"--> H["<img src=https://latex.codecogs.com/svg.image?\beta=\frac{Z}{12}&plus;1>-----------------------"]
    G --"No"--> I["<img src=https://latex.codecogs.com/svg.image?\beta=\frac{Z}{6}&plus;1>-----------------------"]

    H & I --> E --> F --> Q(["PASS or Fail"])
    """

    @rule_method
    def moment_of_inertia_and_turning_radius_of_horizontal_stiffener(fIIlA,fIIlB,fID,fItw,fIdo,fIsr,fIFys,fIFyc,fIE,fIRh,fIZ,fILR) -> RuleUnitResult:
        """수평보강재의 단면2차모멘트와 회전반경

        Args:
            fIIlA (float): 수평보강재의 단면2차모멘트 (수평보강재가 곡률중심의 반대편 웨브면에 설치된 경우)
            fIIlB (float): 수평보강재의 단면2차모멘트 (수평보강재가 곡률중심 쪽 웨브면에 설치된 경우)
            fID (float): 수평보강재 안의 최대 웨브 높이
            fItw (float): 웨브두께
            fIdo (float): 수직보강재 간격
            fIsr (float): 조합단면의 중립축에 대한 회전반경
            fIFys (float): 보강재의 최소항복강도
            fIFyc (float): 압축플랜지의 최소항복강도
            fIE (float): 강재의 탄성계수
            fIRh (float): 하이브리드 단면의 응력감소계수
            fIZ (float): 곡률인자
            fILR (float): 해당 패널의 최소 거더반경

        Returns:
            fOIl (float): 강구조부재설계기준(하중저항계수설계법)  4.3.3.1.11.3 수평보강재 (3)의 값 1
            fObeta (float): 강구조부재설계기준(하중저항계수설계법)  4.3.3.1.11.3 수평보강재 (3)의 값 2
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법)  4.3.3.1.11.3 수평보강재 (3)의 판단 결과
        """

        assert isinstance(fID, float)
        assert fID > 0
        assert isinstance(fItw, float)
        assert fItw > 0
        assert isinstance(fIdo, float)
        assert isinstance(fIsr, float)
        assert isinstance(fIFys, float)
        assert fIFys > 0
        assert isinstance(fIFyc, float)
        assert isinstance(fIE, float)
        assert fIE > 0
        assert isinstance(fIRh, float)
        assert fIRh > 0
        assert isinstance(fIZ, float)
        assert isinstance(fILR, float)
        assert fILR > 0

        fIZ = min(0.95 * (fIdo**2) / (fILR * fItw) , 10)

        if fIIlA != 0 and fIIlB == 0 :
          fObeta = fIZ / 6 + 1
          fOIl = fID * fItw ** 3 * (2.4 * (fIdo / fID) ** 2 - 0.13) * fObeta

          if fIsr >= (0.16 * fIdo * (fIFys / fIE) ** 0.5) / (1 - 0.6 * (fIFyc / (fIRh * fIFys))) ** 0.5:
            return RuleUnitResult(
                result_variables = {
                    "fOIl": fOIl,
                    "pass_fail": True,
                }
            )
          else:
            return RuleUnitResult(
                result_variables = {
                    "fOIl": fOIl,
                    "pass_fail": False,
                }
            )

        elif fIIlA == 0 and fIIlB != 0 :
          fObeta = fIZ / 12 + 1
          fOIl = fID * fItw ** 3 * (2.4 * (fIdo / fID) ** 2 - 0.13) * fObeta
          if fIsr >= (0.16 * fIdo * (fIFys / fIE) ** 0.5) / (1 - 0.6 * (fIFyc / (fIRh * fIFys))) ** 0.5:
            return RuleUnitResult(
                result_variables = {
                    "fOIl": fOIl,
                    "pass_fail": True,
                }
            )
          else:
            return RuleUnitResult(
                result_variables = {
                    "fOIl": fOIl,
                    "pass_fail": False,
                }
            )

        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )