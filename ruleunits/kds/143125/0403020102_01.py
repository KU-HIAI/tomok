import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_0403020102_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 31 25 4.3.2.1.2 (1)' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-12-05'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = 'T-및 Y-형 접합에서 주강관의 소성화의 한계상태'  # 건설기준명


    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.2 강관 간의 트러스접합
    4.3.2.1 원형강관
    4.3.2.1.2 T, Y, X형 접합의 압축력을 받는 지강관
    (1)
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
		A[T, Y, X형 접합의 압축력을 받는 지강관] ;
		B["KDS 14 31 25 4.3.2.1.2"] ;
		A ~~~ B
		end

		subgraph Variable_def
	 	VarOut1[/출력변수: 인장 지강관의 설계강도/] ;
	  VarOut2[/출력변수: T-및 Y-형 접합에서 주강관의 소성화의 한계상태/] ;
	  VarOut3[/출력변수: 전단항복'뚫림'의 한계상태/] ;
    VarIn1[/입력변수: 주강관의 소성화/]
	  VarIn2[/입력변수: 전단항복'뚫림'/]
	  VarIn3[/입력변수: 주강관의 항복강도/]
	  VarIn4[/입력변수: 주강관의 두께/]
	  VarIn5[/입력변수: 폭비/]
	  VarIn6[/입력변수: 주강관 세장비/]
	  VarIn7[/입력변수: 주강관 응력상관계수/]
	  VarIn8[/입력변수: 원형 지강관의 외경/]
	  VarIn9[/입력변수: 저항계수/]
		end
 VarOut1 &	VarOut2 &	VarOut3 ~~~ VarIn1 & VarIn2 & VarIn3
 VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
 VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9

		Python_Class ~~~ Variable_def -->F & G

    C["<img src='https://latex.codecogs.com/svg.image?P_{n}sin\theta=F_{y}t^{2}(3.1&plus;15.6\beta^{2})\gamma^{0.2}Q_{f}'>---------------------------------------------------------------------------------------------------"] ;
    D["<img src='https://latex.codecogs.com/svg.image?P_{n}=0.6F_{y}t\pi&space;D_{b}[(1&plus;sin\theta)/2sin^{2}\theta]'>---------------------------------------------------------------------------------------------------"] ;
    E["<img src='https://latex.codecogs.com/svg.image?&space;P_{n}sin\theta=F_{y}t^{2}[5.7/(1-0.81\beta)]Q_{f}'>---------------------------------------------------------------------------------------------------"] ;
    F["T- 및 Y-형 접합"] ;
    G["X형 이음"] ;
    H["<img src='https://latex.codecogs.com/svg.image?\phi&space;P_{n}'>-----------"] ;
    I["<img src='https://latex.codecogs.com/svg.image?\phi=0.90'>--------------------------"]

    K["<img src='https://latex.codecogs.com/svg.image?\phi=0.95'>--------------------------"]
    L["<img src='https://latex.codecogs.com/svg.image?\phi=0.90'>--------------------------"]
    M(["<img src='https://latex.codecogs.com/svg.image?\phi&space;P_{n}'>-----------"]) ;

F--"소성화의 한계상태"-->C
F--"전단항복의 한계상태"-->D
C-->I-->H
D-->K-->H
H --"Minimun"-->Q(["<img src='https://latex.codecogs.com/svg.image?\phi&space;P_{n}'>-----------"]) ;
G-->E-->L-->M
        """

      # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Limit_state_of_chord_plastification_i_T_and_Y_shaped_joints(fOPnsintheta,fIFy,fIt,fIbeta,fIgamma,fIQf) -> float:
        """T-및 Y-형 접합에서 주강관의 소성화의 한계상태

        Args:
            fOPnsintheta (float): T-및 Y-형 접합에서 주강관의 소성화의 한계상태
            fIFy (float): 주강관의 항복강도
            fIt (float): 주강관의 두께
            fIbeta (float): 폭비
            fIgamma (float): 주강관 세장비
            fIQf (float): 주강관 응력상관계수

        Returns:
            float: 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.1.2 T, Y, X형 접합의 압축력을 받는 지강관 (1) 의 값
        """

        fOPnsintheta = fIFy * (fIt**2) * (3.1 + 15.6 * (fIbeta**2)) * (fIgamma**0.2) * fIQf
        return fOPnsintheta


# 

