import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403020202_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.2.2.2 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-25'
    title = '전단항복(뚫림)의 한계상태'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.2 강관 간의 트러스접합
    4.3.2.2 각형강관
    4.3.2.2.2 T, Y, X형 접합의 압축력을 받는 지강관
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A["Title: 전단항복(뚫림)의 한계상태"]
	  B["KDS 14 31 25 4.3.2.2.2 (2)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
    VarOut1[/출력변수: 전단항복뚫림의 한계상태/] ;

	  VarIn1[/입력변수: 주강관의 항복강도/]
	  VarIn2[/입력변수: 주강관의 두께/]
	  VarIn3[/입력변수: 접합평면과 90°를 이루는 각형 강관폭/]
	  VarIn4[/입력변수: 각형강관에서만 적용할 수 있는 하중길이 변수/]
    VarIn5[/입력변수: 폭비/]
	  VarIn6[/입력변수: 주강관 세장비/]

	  VarOut1  ~~~ VarIn1 & VarIn2 & VarIn3
	  VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6

		end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.2.2.2 (2)"])
		C --> Variable_def

	  Variable_def -->F

    G1["<img src='https://latex.codecogs.com/svg.image?\\beta_{eop} = 5\beta/\gamma (\beta_{eop}< \beta)'>--------------------------------------------"] ;
    G2["<img src='https://latex.codecogs.com/svg.image?\\\beta_{eop} = \beta         (\beta_{eop}\geq \beta)'>--------------------------------------------"] ;

    F-->G1-->E -->U(["<img src='https://latex.codecogs.com/svg.image?\phi&space;P_{n}'>--------------------"])
    F-->G2-->E

    E(["<img src='https://latex.codecogs.com/svg.image?P_{n}sin\theta=0.6F_{y}tB[2\eta&plus;2\beta&space;_{eop}]'>----------------------------------------------------------------------------------------------------------------"]);
    F["<img src='https://latex.codecogs.com/svg.image?\phi=0.95'>--------------------------------------------"] ;
    """

    @rule_method
    def Limit_state_of_shear_yield_breaking(fIFy,fIt,fIeta,fIbeta,fIB,fIgamma)  -> RuleUnitResult:
        """전단항복(뚫림)의 한계상태

        Args:
            fIFy (float): 주강관의 항복강도
            fIt (float): 주강관의 두께
            fIeta (float): 각형강관에서만 적용할 수 있는 하중길이 변수
            fIbeta (float): 폭비
            fIB (float): 접합평면과 90°를 이루는 각형 강관폭
            fIgamma (float): 주강관 세장비

        Returns:
            fOPnsint (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.2.2 T, Y, X형 접합의 압축력을 받는 지강관 (2)의 값 1
            fOphi (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.2.2 T, Y, X형 접합의 압축력을 받는 지강관 (2)의 값 2
            fObetaeo (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.2.2 T, Y, X형 접합의 압축력을 받는 지강관 (2)의 값 3
            sOnone (string): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.2.2 T, Y, X형 접합의 압축력을 받는 지강관 (2)의 판단 결과
        """

        assert isinstance(fIFy, float)
        assert isinstance(fIt, float)
        assert isinstance(fIeta, float)
        assert isinstance(fIbeta, float)
        assert isinstance(fIB, float)
        assert isinstance(fIgamma, float)
        assert fIgamma != 0

        if fIbeta <= (1 - 1 / fIgamma) and fIbeta >= 0.85 and fIB / fIt < 10 :

          fOphi = 0.95
          fObetaeo=min(5*fIbeta/fIgamma, fIbeta)
          fOPnsint = 0.6*fIFy*fIt*fIB*(2*fIeta+2*fObetaeo)

          return RuleUnitResult(
              result_variables = {
                  "fOPnsint": fOPnsint,
                  "fOphi": fOphi,
             }
          )
        else :
          return RuleUnitResult(
              result_variables = {
                  "sOnone": "해당없음",
              }
          )