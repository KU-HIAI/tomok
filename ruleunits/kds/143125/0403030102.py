import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_0403030102 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 14 31 25 4.3.3.1.2' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-12-05'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '설계강도'  # 건설기준명


    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.3 강관 간의 모멘트접합
    4.3.3.1 원형강관
    4.3.3.1.2 T, Y, X형 접합에서 지강관의 면내휨모멘트
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
        A[Title: T, Y, X형 접합에서 지강관의 면내휨모멘트] ;
        B["KDS 14 31 25 4.3.3.1.2"] ;
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

        Python_Class ~~~ Variable_def
        C["<img src='https://latex.codecogs.com/svg.image?M_{n}sin\theta=5.39F_{y}t^{2}\gamma^{0.5}\beta&space;D_{b}Q_{f}'>---------------------------------------------------------------------------------------------------"] ;
        D["<img src='https://latex.codecogs.com/svg.image?M_{n}=0.6F_{y}tD_{b}^{2}[(1&plus;3sin\theta)/4sin^{2}\theta]'>---------------------------------------------------------------------------------------------------"] ;
        H["<img src='https://latex.codecogs.com/svg.image?\phi&space;M_{n}'>-----------"] ;
        I["<img src='https://latex.codecogs.com/svg.image?\phi=0.90'>--------------------------"]
        J["검토"]
        K["<img src='https://latex.codecogs.com/svg.image?\phi=0.95'>--------------------------"]
        E["<img src='https://latex.codecogs.com/svg.image?\beta>(1-1/\gamma)'>--------------------------"]
        F(["검토안함"]) ;
        Variable_def-->E--No-->J-->C & D
        C-->I-->H
        D-->K-->H
        E--yes-->F
        H --"Minimum"--> Q(["<img src='https://latex.codecogs.com/svg.image?\phi&space;M_{n}'>-----------"])
        """

      # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def design_strength(fOphiMn,fIplstpi,fIMn,fOMnsintheta,fIFy,fIt,fIgamma,fIbeta,fIDb,fIQf,fItheta) -> float:
        """설계강도

        Args:
            fOphiMn (float): 설계강도
            fIplstpi (float): 주강관의 소성화
            fIMn (float): 전단항복(뚫림)의 한계상태
            fOMnsintheta (float): 주강관 소성화의 한계상태
            fIFy (float): 주강관의 항복강도
            fIt (float): 주강관의 두께
            fIgamma (float): 주강관 세장비
            fIbeta (float): 폭비
            fIDb (float): 원형 지강관의 외경
            fIQf (float): 응력상관계수
            fItheta (float): 각도

        Returns:
            float : 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.1.2 T, Y, X형 접합에서 지강관의 면내휨모멘트 의 값
        """

        # Pass --> 이 한계상태는 검토할 필요가 없다.

        if fIbeta > 1-1/fIgamma:
          return("Pass")
        else:
          fOMnsintheta = 5.39*fIFy*fIt**2*fIgamma**0.5*fIbeta*fIDb*fIQf
          fIMn = 0.6*fIFy*fIt*fIDb**2*((1+3*math.sin(fItheta*math.pi/180))/(4*math.sin(fItheta*math.pi/180)**2))
          fOphiMn = min(fOMnsintheta*0.9/math.sin(fItheta*math.pi/180),fIMn*0.95)
          return(fOphiMn)


# 

