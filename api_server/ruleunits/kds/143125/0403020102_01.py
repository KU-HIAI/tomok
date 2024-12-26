import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403020102_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.2.1.2 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-25'
    title = 'T- 및 Y-형 접합에 주강관 소성화의 한계상태'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.2 강관 간의 트러스접합
    4.3.2.1 원형강관
    4.3.2.1.2 T, Y, X형 접합의 압축력을 받는 지강관
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: T- 및 Y-형 접합에 주강관 소성화의 한계상태]
	  B["KDS 14 31 25 4.3.2.1.2 (1)"]
	  A ~~~ B
	  end

	  subgraph Variable_def

	  VarOut2[/출력변수: T-및 Y-형 접합에서 주강관의 소성화의 한계상태/] ;

	  VarIn3[/입력변수: 주강관의 항복강도/]
	  VarIn4[/입력변수: 주강관의 두께/]
	  VarIn5[/입력변수: 폭비/]
	  VarIn6[/입력변수: 주강관 세장비/]
	  VarIn7[/입력변수: 주강관 응력상관계수/]

		end

    VarOut2 ~~~ VarIn3
    VarIn3 ~~~ VarIn4 & VarIn5 & VarIn6
    VarIn5 ~~~ VarIn7

    Python_Class ~~~ C(["KDS 14 31 25 4.3.2.1.2 (1)"])
		C --> Variable_def

    Variable_def -->F

    E["<img src='https://latex.codecogs.com/svg.image?P_{n}sin\theta=F_{y}t^{2}(3.1&plus;15.6\beta^{2})\gamma^{0.2}Q_{f}'>---------------------------------------------------------------------------------------------------"] ;
    F["T- 및 Y-형 접합"] ;
    H["<img src='https://latex.codecogs.com/svg.image?\phi&space;P_{n}'>-----------"] ;
    I["<img src='https://latex.codecogs.com/svg.image?\phi=0.90'>--------------------------"]


    F--"소성화의 한계상태"-->E
    E-->I-->H
    H --"Minimun"-->Q(["<img src='https://latex.codecogs.com/svg.image?\phi&space;P_{n}'>-----------"]) ;
    """

    @rule_method
    def Limit_state_of_chord_plastification_of_T_and_Y_type_joints(fIFy,fIt,fIbeta,fIgamma,fIQf) -> RuleUnitResult:
        """T- 및 Y-형 접합에 주강관 소성화의 한계상태

        Args:
            fIFy (float): 주강관의 항복강도
            fIt (float): 주강관의 두께
            fIbeta (float): 폭비
            fIgamma (float): 주강관 세장비
            fIQf (float): 주강관 응력상관계수

        Returns:
            fOPnsint (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.1.2 T, Y, X형 접합의 압축력을 받는 지강관 (1)의 값 1
            fOphi (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.1.2 T, Y, X형 접합의 압축력을 받는 지강관 (1)의 값 2
        """

        assert isinstance(fIFy, float)
        assert isinstance(fIt, float)
        assert isinstance(fIbeta, float)
        assert isinstance(fIgamma, float)
        assert isinstance(fIQf, float)

        fOPnsint = fIFy * (fIt**2) * (3.1 + 15.6 * (fIbeta**2)) * (fIgamma**0.2) * fIQf
        fOphi = 0.9

        return RuleUnitResult(
            result_variables = {
                "fOPnsint": fOPnsint,
                "fOphi": fOphi,
            }
        )