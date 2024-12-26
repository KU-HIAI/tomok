import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403020102_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.2.1.2 (3)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-25'
    title = 'X형 이음에서 주강관 소성화의 한계상태'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.2 강관 간의 트러스접합
    4.3.2.1 원형강관
    4.3.2.1.2 T, Y, X형 접합의 압축력을 받는 지강관
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: X형 이음에서 주강관 소성화의 한계상태]
	  B["KDS 14 31 25 4.3.2.1.2 (3)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut1[/출력변수: 전단항복'뚫림'의 한계상태/] ;

	  VarIn1[/입력변수: 주강관의 항복강도/]
	  VarIn2[/입력변수: 주강관의 두께/]
	  VarIn3[/입력변수: 폭비/]
	  VarIn4[/입력변수: 주강관 응력상관계수/]

	  end

    VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4

    Python_Class ~~~ C(["KDS 14 31 25 4.3.2.1.2 (3)"])
		C --> Variable_def

    Variable_def -->G

    E["<img src='https://latex.codecogs.com/svg.image?&space;P_{n}sin\theta=F_{y}t^{2}[5.7/(1-0.81\beta)]Q_{f}'>---------------------------------------------------------------------------------------------------"] ;
    G["X형 이음"] ;
    L["<img src='https://latex.codecogs.com/svg.image?\phi=0.90'>--------------------------"]
    M(["<img src='https://latex.codecogs.com/svg.image?\phi&space;P_{n}'>-----------"]) ;

    G-->E-->L-->M
    """

    @rule_method
    def Limit_state_of_chord_plastification_in_X_shaped_joints(fIFy,fIt,fIbeta,fIQf) -> RuleUnitResult:
        """X형 이음에서 주강관 소성화의 한계상태

        Args:
            fIFy (float): 주강관의 항복강도
            fIt (float): 주강관의 두께
            fIbeta (float): 폭비
            fIQf (float): 주강관 응력상관계수

        Returns:
            fOPnsint (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.1.2 T, Y, X형 접합의 압축력을 받는 지강관 (3)의 값 1
            fOphi (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.1.2 T, Y, X형 접합의 압축력을 받는 지강관 (3)의 값 2
        """

        assert isinstance(fIFy, float)
        assert isinstance(fIt, float)
        assert isinstance(fIbeta, float)
        assert fIbeta != 0
        assert isinstance(fIQf, float)

        fOPnsint = fIFy * (fIt**2) * (5.7/(1-0.81*fIbeta)) * fIQf
        fOphi = 0.9

        return RuleUnitResult(
            result_variables = {
                "fOPnsint": fOPnsint,
                "fOphi": fOphi,
            }
        )