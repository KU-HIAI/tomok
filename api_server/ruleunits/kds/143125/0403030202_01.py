import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403030202_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.3.2.2 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-25'
    title = '주강관벽 소성화의 한계상태'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.3 강관 간의 모멘트접합
    4.3.3.2 각형강관
    4.3.3.2.2 T, X형 접합에서 지강관의 면내 휨모멘트
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 주강관벽 소성화의 한계상태]
	  B["KDS 14 31 25 4.3.3.2.2 (1)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
    VarOut1[/출력변수: 주강관벽 소성화의 한계상태/] ;
    VarIn1[/입력변수: 주강관의 항복강도/] ;
    VarIn2[/입력변수: 주강관의 두께/] ;
    VarIn3[/입력변수: 접합평면에서 측정한 각형 지강관의 높이/] ;
    VarIn4[/입력변수: 각형강관에서만 적용할 수 있는 하중길이 변수/] ;
    VarIn5[/입력변수: 폭비/] ;
    VarIn6[/입력변수: 응력상관계수/] ;
    end

    VarOut1 ~~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2  ~~~ VarIn4 & VarIn5 & VarIn6


    Python_Class ~~~ C(["KDS 14 31 25 4.3.3.2.2 (1)"])
		C --> Variable_def

	  D["<img src='https://latex.codecogs.com/svg.image?M_{n}=F_{y}t^{2}H_{b}[(1/2\eta)&plus;2/(1-\beta)^{0.5}&plus;\eta/(1-\beta)]Q_{f}'>---------------------------------------------------------------------------------------------------"] ;
    H(["<img src='https://latex.codecogs.com/svg.image?\space M_{n}'>-----------"]) ;
    J["주강관벽 소성화의 한계상태 검토"]
    E["<img src='https://latex.codecogs.com/svg.image?\beta>0.85'>--------------------"]
    F(["검토안함"]) ;
    Variable_def-->E--No--->J-->D
    D-->H
    E--yes-->F
    """

    @rule_method
    def Limit_state_of_plasticization_of_branch_member(fIFy,fIt,fIHb,fIeta,fIbeta,fIQf)  -> RuleUnitResult:
        """주강관벽 소성화의 한계상태

        Args:
            fIFy (float) : 주강관의 항복강도
            fIt (float): 주강관의 두께
            fIHb (float): 접합평면에서 측정한 각형 지강관의 높이
            fIeta (float): 각형강관에서만 적용할 수 있는 하중길이 변수
            fIbeta (float): 폭비
            fIQf (float): 응력상관계수

        Returns:
            fOMn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.2.2 T, X형 접합에서 지강관의 면내 휨모멘트 (1)의 값 1
            fOphi (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.2.2 T, X형 접합에서 지강관의 면내 휨모멘트 (1)의 값 2
        """

        assert isinstance(fIFy, float)
        assert isinstance(fIt, float)
        assert isinstance(fIHb, float)
        assert isinstance(fIeta, float)
        assert fIeta != 0
        assert isinstance(fIbeta, float)
        assert fIbeta <= 0.85
        assert isinstance(fIQf, float)

        if fIbeta <= 0.85 :
          fOphi = 1.0
          fOMn = fIFy*fIt**2*fIHb*((1/(2*fIeta))+2/(1-fIbeta)**0.5+fIeta/(1-fIbeta))*fIQf

        return RuleUnitResult(
            result_variables = {
                "fOMn": fOMn,
                "fOphi": fOphi,
            }
        )