import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040203_02_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.2.3 (2) ①'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '좌굴응력'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.2 압축부재
    4.2.3 비세장판 단면을 가진 부재의 휨좌굴에 대한 압축강도
    (2)
    ①
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 비세장판 단면을 가진 부재의 휨좌굴에 대한 압축강도] ;
		B["KDS 14 31 10 4.2.3 (2) ①"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarOut1[/출력변수: 공칭압축강도/]
    VarIn1[/입력변수: 횡좌굴에 대한 비지지길이/]
    VarIn2[/입력변수: 단면2차반경/]
    VarIn3[/입력변수: 유효좌굴길이계수/]
    VarIn4[/입력변수: 좌굴 응력/]
    VarIn5[/입력변수: 부재의 총단면적/]
    VarIn6[/입력변수: 탄성좌굴해석을 통하여 구하는 탄성좌굴응력/]
    VarIn7[/입력변수: 강재의 항복강도/]
    VarIn8[/입력변수: 강재의 탄성계수/]
    VarIn9[/입력변수: 부재의 횡좌굴에 대한 비지지길이/]
    VarIn10[/입력변수: 좌굴축에 대한 단면2차반경/]
    VarIn1~~~ VarIn6
    VarIn2~~~ VarIn7
    VarOut1~~~ VarIn3~~~ VarIn8
    VarIn4~~~ VarIn9
    VarIn5~~~ VarIn10

		end

		Python_Class ~~~ C(["KDS 14 31 10 4.2.3 (2) ①"])
		C --> Variable_def

	  I(["<img src='https://latex.codecogs.com/svg.image?P_{n}=F_{cr}A_{q}'>-----------------------------------"]) ;
    D{"<img src='https://latex.codecogs.com/svg.image?\frac{KL}{r}\leq&space;4.71\sqrt{\frac{E}{F_{y}}}or\frac{F_{y}}{F_{e}}\leq&space;2.25'>--------------------------------------------------------"} ;
    E{"<img src='https://latex.codecogs.com/svg.image?\frac{KL}{r}>4.71\sqrt{\frac{E}{F_{y}}}or\frac{F_{y}}{F_{e}}>2.25'>--------------------------------------------------------"} ;
    F["<img src='https://latex.codecogs.com/svg.image?F_{cr}=\left[0.658^{\frac{F_{y}}{F_{e}}}\right]F_{y}'>-----------------------------------"] ;
    G["<img src='https://latex.codecogs.com/svg.image?F_{cr}=0.877F_{e}'>-----------------------------------"] ;
    H["<img src='https://latex.codecogs.com/svg.image?F_{e}=\frac{\pi^{2}E}{\left(\frac{KL}{r}\right)^{2}}(MPa)'>----------------------------------------------"] ;
	  Variable_def-->H
    H-->D-->F
    H-->E-->G
    F & G --> I
    """

    @rule_method
    def buckling_stress(fIFy,fIE,fIK,fIL,fIr) -> RuleUnitResult:
        """좌굴응력

        Args:
            fIFy (float): 강재의 항복강도
            fIE (float): 강재의 탄성계수
            fIK (float): 유효좌굴길이계수
            fIL (float): 부재의 횡좌굴에 대한 비지지길이
            fIr (float): 좌굴축에 대한 단면2차반경

        Returns:
            fOFcr (float): 강구조부재설계기준(하중저항계수설계법)  4.2.3 비세장판 단면을 가진 부재의 휨좌굴에 대한 압축강도 (2) ①의 값 1
            fOFe (float): 강구조부재설계기준(하중저항계수설계법)  4.2.3 비세장판 단면을 가진 부재의 휨좌굴에 대한 압축강도 (2) ①의 값 2
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법)  4.2.3 비세장판 단면을 가진 부재의 휨좌굴에 대한 압축강도 (2) ①의 판단 결과
        """

        assert isinstance(fIFy, float)
        assert fIFy > 0
        assert isinstance(fIE, float)
        assert fIE > 0
        assert isinstance(fIK, float)
        assert fIK > 0
        assert isinstance(fIL, float)
        assert fIL > 0
        assert isinstance(fIr, float)
        assert fIr > 0

        import math

        fOFe = ((math.pi)**2)*fIE/((fIK*fIL/fIr)**2)

        if fIK*fIL/fIr <= 4.71*(fIE/fIFy)**(0.5) or fIFy/fOFe <= 2.25:
          fOFcr = 0.658**(fIFy/fOFe) * fIFy
          return RuleUnitResult(
              result_variables = {
                  "fOFcr": fOFcr,
              }
          )

        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )