import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_0403020205_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 14 31 25 4.3.2.2.5 (2)' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-12-07'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '총 유효용접길이'  # 건설기준명


    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.2 강관 간의 트러스접합
    4.3.2.2 각형강관
    4.3.2.2.5 지강관의 용접
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
        A[Title: 지강관의 용접] ;
        B["KDS 14 31 25 4.3.2.2.5(2)"] ;
        A ~~~ B
        end

        subgraph Variable_def
        VarOut1[/출력변수: 총 유효용접길이/] ;
        VarIn1[/입력변수: 접합평면에서 측정한 각형 지강관의 높이/] ;
        VarIn2[/입력변수: 지강관의 두께/] ;
        VarIn3[/입력변수: 접합평면과 90를 이루는 각형 지강관의 폭/] ;

        VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
        end

        Python_Class ~~~ Variable_def

        C["각 지강관 주위의 간격 K형 접합에서 θ≤50º 인 경우"] ;
        D(["<img src='https://latex.codecogs.com/svg.image?L_{e}=\frac{2(H_{b}-1.2t_{b})}{sin\theta}&plus;2(B_{b}-1.2t_{b})'>------------------------------------------------------------------------"]) ;
        E["각 지강관 주위의 간격 K형 접합에서 50º≤θ≤60º 인 경우"] ;
        F(["직선보간법"]) ;
        G["각 지강관 주위의 간격 K형 접합에서 60º≤θ 인 경우"] ;
        H(["<img src='https://latex.codecogs.com/svg.image?L_{e}=\frac{2(H_{b}-1.2t_{b})}{sin\theta}&plus;(B_{b}-1.2t_{b})'>------------------------------------------------------------------------"]) ;
        Variable_def --> C-->D
        Variable_def --> E-->F
        Variable_def --> G-->H
        """

      # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def total_effective_weld_length(fOLe,fIHb,fItb,fIBb,fItheta) -> float:
        """총 유효용접길이
        Args:
            fOLe (float): 총 유효용접길이
            fIHb (float): 접합평면에서 측정한 각형 지강관의 높이
            fItb (float): 지강관의 두께
            fIBb (float): 접합평면과 90를 이루는 각형 지강관의 폭
            fItheta (float): 각도
        Returns:
            float : 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.2.5 지강관의 용접 (2) 의 값
        """

        if fItheta <= 50:
          fOLe = 2*(fIHb-1.2*fItb)/math.sin(fItheta*math.pi/180)+2*(fIBb-1.2*fItb)
        elif fItheta >= 60:
          fOLe = 2*(fIHb-1.2*fItb)/math.sin(fItheta*math.pi/180)+(fIBb-1.2*fItb)
        elif 50 < fItheta < 60:
          theta50 = 2*(fIHb-1.2*fItb)/math.sin(50*math.pi/180)+2*(fIBb-1.2*fItb)
          theta60 = 2*(fIHb-1.2*fItb)/math.sin(60*math.pi/180)+(fIBb-1.2*fItb)
          fOLe = theta50 + (theta60-theta50)/10*(60-fItheta)
        return(fOLe)


# 

