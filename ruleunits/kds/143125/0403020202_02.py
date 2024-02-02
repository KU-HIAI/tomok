import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_0403020202_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 31 25 4.3.2.2.2 (2) ' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-12-05'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '전단항복(뚫림)의 한계상태'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.2 강관 간의 트러스접합
    4.3.2.2 각형강관
    4.3.2.2.2 T, Y, X형 접합의 압축력을 받는 지강관
    (2)
    """
    # https://dillinger.io/ 표와 이미지 랜더링 확인 사이트
    # 이미지 링크 변환 사이트 https://www.somanet.xyz/2017/06/blog-post_21.html
    # 건설기준문서내용(text)
    content = """
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: T, Y, X형 접합의 압축력을 받는 지강관] ;
		B["KDS 14 31 25 4.3.2.2.2"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarOut1[/출력변수: 지강관의 설계강도/] ;
    VarOut2[/출력변수: 주강관벽 소성화의 한계상태/] ;
    VarOut3[/출력변수: 비균일 하중분포로 인한 국부항복의 한계상태/] ;
	  VarIn1[/입력변수: 주강관 소성화/]
	  VarIn2[/입력변수: 전단항복'뚫림'/]
	  VarIn3[/입력변수: 측벽강도/]
	  VarIn4[/입력변수: 비균일 하중분포/]
	  VarIn5[/입력변수: 국부항복의 한계상태/]
	  VarIn6[/입력변수: 주강관의 항복강도/]
	  VarIn7[/입력변수: 주강관의 두께/]
	  VarIn8[/입력변수: 각형강관에서만 적용할 수 있는 하중길이 변수/]
	  VarIn9[/입력변수: 폭비/]
	  VarIn10[/입력변수: 주강관 응력상관계수/]
	  VarIn11[/입력변수: 접합평면과 90º를 이루는 각형 강관폭/]
	  VarIn12[/입력변수: 강관 모서리의 외부반경/]
	  VarIn13[/입력변수: 주강관축에 평행한 하중지지길이/]
	  VarIn14[/입력변수: 주강관의 높이/]
	  VarIn15[/입력변수: 강재의 탄성계수/]
	  VarIn16[/입력변수: 지강관의 항복강도/]
	  VarIn17[/입력변수: 지강관의 두께/]
	  VarIn18[/입력변수: 접합평면에서 측정한 각형 지강관의 높이/]
	  VarIn19[/입력변수: 주강관에 용접된 지강관 면의 유효폭/]

	  VarOut1 & VarOut2 & VarOut3 ~~~ VarIn1 &  VarIn2 & VarIn3
	  VarIn2 ~~~ VarIn4 &  VarIn5 & VarIn6
	  VarIn5 ~~~ VarIn7 &  VarIn8 & VarIn9
	  VarIn8 ~~~ VarIn10 &  VarIn11 & VarIn12
	  VarIn11 ~~~ VarIn13 &  VarIn14 & VarIn15
	  VarIn14 ~~~ VarIn16 &  VarIn17 & VarIn18 & VarIn19
		end
		Python_Class ~~~ Variable_def -->D & F & H & J & L & N
D-->C
F-->E
H-->I
J-->K
L-->Q
N-->R-->M
C & E & I & K & Q & M -->U(["<img src='https://latex.codecogs.com/svg.image?\phi&space;P_{n}'>--------------------"])
U --"Minimum"-->W(["<img src='https://latex.codecogs.com/svg.image?\phi&space;P_{n}'>--------------------"])

    C(["<img src='https://latex.codecogs.com/svg.image?P_{n}sin\theta=F_{y}t^{2}[2\eta/(1-\beta)&plus;4/(1-\beta)^{0.5}]Q_{f}'>---------------------------------------------------------------------------------------------------"]);
    D["<img src='https://latex.codecogs.com/svg.image?\phi=1.00'>--------------------------------------------"] ;
    E(["<img src='https://latex.codecogs.com/svg.image?P_{n}sin\theta=0.6F_{y}tB[2\eta&plus;2\beta&space;_{eop}]'>----------------------------------------------------------------------------------------------------------------"]);
    F["<img src='https://latex.codecogs.com/svg.image?\phi=0.95'>--------------------------------------------"] ;
    H["<img src='https://latex.codecogs.com/svg.image?\phi=1.00'>--------------------------------------------"] ;
    I(["<img src='https://latex.codecogs.com/svg.image?P_{n}sin\theta=2F_{y}t[5k&plus;N]'>----------------------------------------------------------------------------------------------------------------------------------------"])
    J["<img src='https://latex.codecogs.com/svg.image?\phi=0.75'>--------------------------------------------"] ;
    K(["<img src='https://latex.codecogs.com/svg.image?P_{n}sin\theta=1.6t^2[1&plus;3N/(H-3t)](EF_{y}^{0.5}Q_{f})'>---------------------------------------------------------------------------------------------------------------"])
    L["<img src='https://latex.codecogs.com/svg.image?\phi=0.90'>--------------------------------------------"] ;
    M(["<img src='https://latex.codecogs.com/svg.image?P_{n}=F_{yb}t_{b}[2H_{b}&plus;2b_{eoi}-4t_{b}]'>-----------------------------------------------------------------------------------------------------------"])
	  N["<img src='https://latex.codecogs.com/svg.image?\phi=0.95'>--------------------------------------------"] ;
    Q(["<img src='https://latex.codecogs.com/svg.image?P_{n}sin\theta=[48t^{3}/(H-3t)](EF_{y})^{0.5}Q_{f}'>------------------------------------------------------------------------------------------------------------------------"])
    R["<img src='https://latex.codecogs.com/svg.image?b_{eoi}=F_{yb}t_{b}[2H_{b}&plus;2b_{eoi}-4t_{b}]'>--------------------------------------------------------------------------------------------------------------------------"]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Limit_State_of_Shear_Yield_Breaking(fOPnsintheta,fIFy,fIt,fIeta,fIbeta,fIbetaeop,fIB,fIgamma) -> bool:
        """전단항복(뚫림)의 한계상태
        Args:
            fOPnsintheta (float): 주강관벽 소성화의 한계상태
            fIFy (float): 강재의 최소인장강도
            fIt (float): 주강관의 두께
            fIeta (float): 각형강관에서만 적용할 수 있는 하중길이 변수
            fIbeta (float): 폭비
            fIbetaeop (float): 유효외부뚫림변수
            fIB (float): 접합평면과 90°를 이루는 각형 강관폭
            fIgamma (float): 주강관 세장비


        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법) 4.3.2.2.2 T, Y, X형 접합의 압축력을 받는 지강관 (2)의 통과여부
        """

        fIbetaeop=min(5*fIbeta/fIgamma, fIbeta)
        fOPnsintheta = 0.6*fIFy*fIt*fIB*(2*fIeta+2*fIbetaeop)
        return fOPnsintheta


# 

