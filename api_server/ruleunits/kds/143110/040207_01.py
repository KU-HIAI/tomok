import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040207_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.2.7 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '좌굴응력'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.2 압축부재
    4.2.7 세장판단면을 갖는 압축부재
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[좌굴응력] ;
		B["KDS 14 31 10 4.2.7 (1)"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarOut1[/출력변수: 공칭압축강도/]
    VarIn1[/입력변수: 좌굴응력/]
    VarIn2[/입력변수: 세장비/]
    VarIn3[/입력변수: root E/QFy/]
    VarIn4[/입력변수: QFy/Fe/]
    VarIn5[/입력변수: 모든 세장 압축요소를 고려하는 순 감도계수/]
    VarIn6[/입력변수: 탄성좌굴응력/]
    VarIn7[/입력변수: 강재의 항복강도/]
    VarOut1~~~ VarIn4
    VarIn1~~~ VarIn5
    VarIn2~~~ VarIn6
    VarIn3~~~ VarIn7
		end

		Python_Class ~~~ C1(["KDS 14 31 10 4.2.7 (1)"]) --> Variable_def
    C["<img src='https://latex.codecogs.com/svg.image?P_{n}=F_{cr}A_{g}'>------------------------------"] ;
    D["<img src='https://latex.codecogs.com/svg.image?\frac{KL}{r}\leq&space;4.71\sqrt{\frac{E}{QF_{y}}}or\frac{QF_{y}}{F_{e}}\leq&space;2.25'>------------------------------------------------------"] ;
    E(["<img src='https://latex.codecogs.com/svg.image?F_{cr}=Q\left[0.658^{\frac{QF_{y}}{F_{e}}}\right]F_{y}'>---------------------------------------------------"]) ;
    F["<img src='https://latex.codecogs.com/svg.image?\frac{KL}{r}>4.71\sqrt{\frac{E}{QF_{y}}}or\frac{QF_{y}}{F_{e}}>2.25'>--------------------------------------------------------------"] ;
    G(["<img src='https://latex.codecogs.com/svg.image?F_{cr}=0.877F_{e}'>-----------------------------------"]) ;

    Variable_def-->C-->D & F
    D-->E
    F-->G
    """

    @rule_method
    def Nominal_Compressive_Strength(fIE,fIQ,fIFe,fIFy,fIKLr) -> RuleUnitResult:
        """좌굴응력

        Args:
            fIE (float): 세장비
            fIQ (float): 모든 세장 압축요소를 고려하는 순감소계수
            fIFe (float): 탄성좌굴응력
            fIFy (float): 모든 세장 압축요소를 고려하는 순감소계수
            fIKLr (float): 모든 세장 압축요소를 고려하는 순감소계수

        Returns:
            fOFcr (float): 강구조부재설계기준(하중저항계수설계법)  4.2.7 세장판단면을 갖는 압축부재의 값 (1)의 값
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법)  4.2.7 세장판단면을 갖는 압축부재의 값 (1)의 통과여부 1
            sOnone (string): 강구조부재설계기준(하중저항계수설계법)  4.2.7 세장판단면을 갖는 압축부재의 값 (1)의 통과여부 2
        """

        assert isinstance(fIE, float)
        assert fIE > 0
        assert isinstance(fIQ, float)
        assert fIQ > 0
        assert isinstance(fIFe, float)
        assert fIFe > 0
        assert isinstance(fIFy, float)
        assert fIFy > 0
        assert isinstance(fIKLr, float)


        if fIKLr <= 4.71*(fIE/(fIQ*fIFy))**0.5 or fIQ*fIFy/fIFe <= 2.25:
          fOFcr = fIQ*(0.658)**(fIQ*fIFy/fIFe) * fIFy

          return RuleUnitResult(
            result_variables = {
             "fOFcr": fOFcr,
              }
          )

        else :
          return RuleUnitResult(
              result_variables = {
                  "sOnone": "해당없음",
              }
          )