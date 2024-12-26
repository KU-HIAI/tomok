import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403030203_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.3.2.3 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '측벽 국부항복의 한계상태'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.3 강관 간의 모멘트접합
    4.3.3.2 각형강관
    4.3.3.2.3 T, X형 접합에서 지강관의 면외 휨모멘트
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 측벽 국부항복의 한계상태]
	  B["KDS 14 31 25 4.3.3.2.3 (2)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
    VarOut1[/출력변수: 설계강도/] ;
    VarOut2[/출력변수: 측벽 국부항복의 한계상태/] ;
    VarIn1[/입력변수: 접합평면에서 측정한 각형 지강관의 높이/] ;
    VarIn2[/입력변수: 접합평면과 90º를 이루는 각형 강관폭/] ;
    VarIn3[/입력변수: 주강관의 두께/] ;
    VarIn4[/입력변수: 폭비/] ;
    VarIn5[/입력변수: T형,X형 접합에 대한 항복강도/] ;
    end
    VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5

    Python_Class ~~~ C(["KDS 14 31 25 4.3.3.2.3 (2)"])
		C --> Variable_def

    D["<img src='https://latex.codecogs.com/svg.image?\phi=1.00'>-----------------------"] ;
    G["측벽 국부항복의 한계상태"]
    K(["검토안함"]) ;
    L["<img src='https://latex.codecogs.com/svg.image?\beta<0.85'>--------------------"]
    M["<img src='https://latex.codecogs.com/svg.image?M_{n}=F_{y}^{*}t(B-t)(H_{b}&plus;5t)'>-----------------------------------------------------------------------------------"]
    N["<img src='https://latex.codecogs.com/svg.image?\phi&space;M_{n}'>--------------"] ;

    Variable_def-->L--No--->G-->M
    M-->D-->N
    L--yes-->K
    """

    @rule_method
    def limit_state_of_pontoon_side_wall_local_yielding(fIFystar,fIt,fIHb,fIbeta,fIB) -> RuleUnitResult:
        """측벽 국부항복의 한계상태

        Args:
            fIFystar (float): T형,X형 접합에 대한 항복강도
            fIt (float): 주강관의 두께
            fIHb (float): 접합평면에서 측정한 각형 지강관의 높이
            fIbeta (float): 폭 비
            fIB (float): 접합평면과 90°를 이루는 각형 강관폭

        Returns:
            fOMn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.2.3 T, X형 접합에서 지강관의 면외 휨모멘트 (2)의 값 1
            fOphi (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.2.3 T, X형 접합에서 지강관의 면외 휨모멘트 (2)의 값 2
        """

        assert isinstance(fIFystar, float)
        assert isinstance(fIt, float)
        assert isinstance(fIHb, float)
        assert isinstance(fIbeta, float)
        assert fIbeta >= 0.85
        assert isinstance(fIB, float)

        fOphi = 1.0

        if fIbeta >= 0.85 :
          fOMn = fIFystar*fIt*(fIB-fIt)*(fIHb+5*fIt)

        return RuleUnitResult(
            result_variables = {
                "fOMn": fOMn,
                "fOphi": fOphi,
            }
        )