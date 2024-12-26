import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403020102_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.2.1.2 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-25'
    title = '전단항복(뚫림)의 한계상태'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.2 강관 간의 트러스접합
    4.3.2.1 원형강관
    4.3.2.1.2 T, Y, X형 접합의 압축력을 받는 지강관
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A["Title: 전단항복(뚫림)의 한계상태"]
	  B["KDS 14 31 25 4.3.2.1.2 (2)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut3[/출력변수: 전단항복'뚫림'의 한계상태/] ;

    VarIn1[/입력변수: 주강관의 소성화/]

	  VarIn3[/입력변수: 주강관의 항복강도/]
	  VarIn4[/입력변수: 주강관의 두께/]

	  VarIn8[/입력변수: 원형 지강관의 외경/]
	  VarIn9[/지강관과 주강관 사이의 실제 각도/]
		end

    VarOut3 ~~~ VarIn1 & VarIn3
    VarIn3 ~~~ VarIn4 & VarIn8 & VarIn9

    Python_Class ~~~ C(["KDS 14 31 25 4.3.2.1.2 (2)"])
		C --> Variable_def

    Variable_def -->F

    D["<img src='https://latex.codecogs.com/svg.image?P_{n}=0.6F_{y}t\pi&space;D_{b}[(1&plus;sin\theta)/2sin^{2}\theta]'>---------------------------------------------------------------------------------------------------"] ;
    F["T- 및 Y-형 접합"] ;
    H["<img src='https://latex.codecogs.com/svg.image?\phi&space;P_{n}'>-----------"] ;
    K["<img src='https://latex.codecogs.com/svg.image?\phi=0.95'>--------------------------"]

    F--"전단항복의 한계상태"-->D

    D-->K-->H
    """

    @rule_method
    def Limit_state_of_shea_yielding_punching(fIFy,fIt,fIDb,fItheta) -> RuleUnitResult:
        """전단항복(뚫림)의 한계상태

        Args:
            fIFy (float): 주강관의 항복강도
            fIt (float): 주강관의 두께
            fIDb (float): 원형 지강관의 외경
            fItheta (float): 지강관과 주강관 사이의 실제 각도

        Returns:
            fOPn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.1.2 T, Y, X형 접합의 압축력을 받는 지강관 (2)의 값 1
            fOphi (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.1.2 T, Y, X형 접합의 압축력을 받는 지강관 (2)의 값 2
        """

        assert isinstance(fIFy, float)
        assert isinstance(fIt, float)
        assert isinstance(fIDb, float)
        assert isinstance(fItheta, float)
        assert 0 < fItheta <180

        import math

        fOPn = 0.6*fIFy*fIt*(math.pi)*fIDb*((1+math.sin(math.radians(fItheta)))/(2*(math.sin(math.radians(fItheta)))**2))
        fOphi = 0.95

        return RuleUnitResult(
            result_variables = {
                "fOPn": fOPn,
                "fOphi": fOphi,
            }
        )