import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403030102_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.3.1.2 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-25'
    title = '주강관 소성화의 한계상태'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.3 강관 간의 모멘트접합
    4.3.3.1 원형강관
    4.3.3.1.2 T, Y, X형 접합에서 지강관의 면내휨모멘트
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 주강관 소성화의 한계상태]
	  B["KDS 14 31 25 4.3.3.1.2 (1)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
    VarOut1[/출력변수: 설계강도/] ;
    VarOut2[/출력변수: 주강관 소성화의 한계상태/] ;
    VarIn1[/입력변수: 주강관의 소성화/] ;
    VarIn2[/입력변수: 전단항복'뚫림'의 한계상태/] ;
    VarIn3[/입력변수: 주강관의 항복강도/] ;
    VarIn4[/입력변수: 주강관의 두께/] ;
    VarIn5[/입력변수: 주강관의 세장비/] ;
    VarIn6[/입력변수: 폭비/] ;
    VarIn7[/입력변수: 원형 지강관의 외경/] ;
    VarIn8[/입력변수: 응력상관계수/] ;
    end
    VarOut1 & VarOut2 ~~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~  VarIn5 & VarIn6 & VarIn7 & VarIn8

    Python_Class ~~~ C(["KDS 14 31 25 4.3.3.1.2 (1)"])
		C --> Variable_def

    L["<img src='https://latex.codecogs.com/svg.image?M_{n}sin\theta=5.39F_{y}t^{2}\gamma^{0.5}\beta&space;D_{b}Q_{f}'>---------------------------------------------------------------------------------------------------"] ;
    D["<img src='https://latex.codecogs.com/svg.image?M_{n}=0.6F_{y}tD_{b}^{2}[(1&plus;3sin\theta)/4sin^{2}\theta]'>---------------------------------------------------------------------------------------------------"] ;
    H["<img src='https://latex.codecogs.com/svg.image?\phi&space;M_{n}'>-----------"] ;
    I["<img src='https://latex.codecogs.com/svg.image?\phi=0.90'>--------------------------"]
    J["검토"]
    K["<img src='https://latex.codecogs.com/svg.image?\phi=0.95'>--------------------------"]
    E["<img src='https://latex.codecogs.com/svg.image?\beta>(1-1/\gamma)'>--------------------------"]
    F(["검토안함"]) ;
    Variable_def-->E--No-->J-->L & D
    L-->I-->H
    D-->K-->H
    E--yes-->F
    H --"Minimum"--> Q(["<img src='https://latex.codecogs.com/svg.image?\phi&space;M_{n}'>-----------"])
    """

    @rule_method
    def Limit_state_of_chord_plastification(fIFy,fIt,fIbeta,fIgamma,fIDb,fIQf) -> RuleUnitResult:
        """주강관 소성화의 한계상태

        Args:
            fIFy (float): 주강관의 항복강도
            fIt (float): 주강관의 두께
            fIbeta (float): 폭비
            fIgamma (float): 주강관 세장비
            fIDb (float): 원형 지강관의 외경
            fIQf (float): 주강관 응력상관계수

        Returns:
            fOMnsint (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.1.2 T, Y, X형 접합에서 지강관의 면내휨모멘트 (1)의 값 1
            fOphi (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.1.2 T, Y, X형 접합에서 지강관의 면내휨모멘트 (1)의 값 2
        """

        assert isinstance(fIFy, float)
        assert isinstance(fIt, float)
        assert isinstance(fIbeta, float)
        assert isinstance(fIgamma, float)
        assert fIgamma > 0
        assert isinstance(fIDb, float)
        assert isinstance(fIQf, float)

        fOMnsint = 5.39*fIFy*fIt**2*fIgamma**0.5*fIbeta*fIDb*fIQf
        fOphi = 0.9

        return RuleUnitResult(
            result_variables = {
                "fOMnsint": fOMnsint,
                "fOphi": fOphi,
            }
        )