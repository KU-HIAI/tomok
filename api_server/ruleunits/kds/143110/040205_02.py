import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040205_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.2.5 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '유효세장비'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.2 압축부재
    4.2.5 단일ㄱ형강 압축부재
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[세장판단면을 갖는 압축부재] ;
		B["KDS 14 31 10 4.2.7 (2)"] ;
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

		Python_Class ~~~ C1(["KDS 14 31 10 4.2.7 (2)"]) --> Variable_def
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
    def effective_slender_ratio(fIKLrA,fIKLrB,fIL,fIrx,fIlelera,fIbI,fIbs,fIrz) -> RuleUnitResult:
        """유효세장비

        Args:
            fIKLrA (float): 유효세장비
            fIKLrB (float): 유효세장비 (ㄱ형강의 짧은 다리가 접합되는 경우)
            fIL (float): 부재길이
            fIrx (float): 접합된 다리와 평행한 축에 대한 단면2차반경
            fIlelera (float): 다리길이의 비
            fIbI (float): ㄱ형강의 긴 쪽 다리의 길이
            fIbs (float): ㄱ형강의 짧은 쪽 다리의 길이
            fIrz (float): 약축에 대한 단면2차반경

        Returns:
            fOKLr (float): 강구조부재설계기준(하중저항계수설계법)  4.2.5 단일ㄱ형강 압축부재 (2)의 값
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법)  4.2.5 단일ㄱ형강 압축부재 (2)의 판단 결과 1
            sOnone (string): 강구조부재설계기준(하중저항계수설계법)  4.2.5 단일ㄱ형강 압축부재 (2)의 판단 결과 2
        """

        assert isinstance(fIL, float)
        assert isinstance(fIrx, float)
        assert fIrx > 0
        assert isinstance(fIlelera, float)
        assert isinstance(fIbI, float)
        assert fIbI > 0
        assert isinstance(fIbs, float)
        assert fIbs > 0
        assert isinstance(fIrz, float)
        assert fIrz > 0

        if fIKLrA != 0 and fIKLrB == 0 :
          if 0 <= fIL/fIrx <= 75 :
            fOKLr = 60 + 0.8 * fIL/fIrx
          elif fIL/fIrx > 75:
            fOKLr = min(45 + fIL / fIrx, 200)
          return RuleUnitResult(
              result_variables = {
                  "fOKLr": fOKLr,
              }
          )

        elif fIlelera <= 1.7 and fIKLrA == 0 and fIKLrB != 0 :
          if 0 <= fIL/fIrx <= 75 :
            fOKLr = max(60 + 0.8 * fIL / fIrx + 6 * ((fIbI / fIbs)**2 - 1), 0.82 * fIL / fIrz)
          elif fIL/fIrx > 75 :
            fOKLr = max(min(45 + fIL / fIrx, 200) + 6 * ((fIbI/fIbs)**2 - 1), 0.82 * fIL / fIrz)
          return RuleUnitResult(
              result_variables = {
                  "fOKLr": fOKLr,
              }
          )

        else :
          return RuleUnitResult(
              result_variables = {
                  "sOnone": "해당없음",
              }
          )