import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_0403030202_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 14 31 25 4.3.3.2.2 (1)' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-12-04'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '주강관벽 소성화의 한계상태'  # 건설기준명


    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.3 강관 간의 모멘트접합
    4.3.3.2 각형강관
    4.3.3.2.2 T, X형 접합에서 지강관의 면내 휨모멘트
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
        A[Title: T, X형 접합에서 지강관의 면내 휨모멘트] ;
        B["KDS 14 31 25 4.3.3.2.2(1)"] ;
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

        Python_Class ~~~ Variable_def
        C["<img src='https://latex.codecogs.com/svg.image?M_{n}=F_{y}t^{2}H_{b}[(1/2\eta)&plus;2/(1-\beta)^{0.5}&plus;\eta/(1-\beta)]Q_{f}'>---------------------------------------------------------------------------------------------------"] ;
        H(["<img src='https://latex.codecogs.com/svg.image?\space M_{n}'>-----------"]) ;
        J["주강관벽 소성화의 한계상태 검토"]
        E["<img src='https://latex.codecogs.com/svg.image?\beta>0.85'>--------------------"]
        F(["검토안함"]) ;
    Variable_def-->E--No--->J-->C
    C-->H
    E--yes-->F
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def limit_state_of_plasticization_of_cast_steel_pipe_wall(fOMn,fIFy,fIt,fIHb,fIeta,fIbeta,fIQf) -> float:
        """주강관벽 소성화의 한계상태

        Args:
            fOMn (float): 측벽 국부좌굴의 한계상태
            fIFy (float) : 주강관의 항복강도
            fIt (float): 주강관의 두께
            fIHb (float): 접합평면에서 측정한 각형 지강관의 높이
            fIeta (float): 각형강관에서만 적용할 수 있는 하중길이 변수
            fIbeta (float): 폭비
            fIQf (float): 응력상관계수


        Returns:
            float: 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.2.2 T, X형 접합에서 지강관의 면내 휨모멘트 (1) 의 값
        """

        if fIbeta > 0.85:
          return("Pass")
        else:
          fOMn = fIFy*fIt**2*fIHb*((1/(2*fIeta))+2/(1-fIbeta)**0.5+fIeta/(1-fIbeta))*fIQf
          return(fOMn)


# 

