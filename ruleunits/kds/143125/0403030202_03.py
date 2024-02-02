import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_0403030202_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 14 31 25 4.3.3.2.2 (3)' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-12-04'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '국부항복의 한계상태'  # 건설기준명


    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.3 강관 간의 모멘트접합
    4.3.3.2 각형강관
    4.3.3.2.2 T, X형 접합에서 지강관의 면내 휨모멘트
    (3)
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
        B["KDS 14 31 25 4.3.3.2.2(3)"] ;
        A ~~~ B
        end

        subgraph Variable_def
          VarOut1[/출력변수: 국부항복의 한계상태/] ;
          VarIn1[/입력변수: 지강관의 항복강도/] ;
          VarIn2[/입력변수: 휨축에 대한 지강관의 소성단면계수/] ;
          VarIn3[/입력변수: 주강관에 용접된 지강관 면의 유효폭/] ;
          VarIn4[/입력변수: 접합평면과 90를 이루는 각형 지강관의 폭/] ;
          VarIn5[/입력변수: 접합평면에서 측정한 각형 지강관의 높이/] ;
          VarIn6[/입력변수: 지강관의 두께/] ;
          VarIn7[/입력변수: 접합평면과 90º를 이루는 각형 강관폭/] ;
          VarIn8[/입력변수: 주강관의 두께/] ;
          VarIn9[/입력변수: 주강관의 항복강도/] ;
          VarIn10[/입력변수: 폭비/] ;
        end
        VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
        VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
        VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9 & VarIn10

        Python_Class ~~~ Variable_def
        C["<img src='https://latex.codecogs.com/svg.image?M_{n}=F_{yb}[Z_{b}-(1-b_{eoi}/B_{b})B_{b}H_{b}t_{b}]'>--------------------------------------------------------------------------"] ;
        D["<img src='https://latex.codecogs.com/svg.image?b_{eoi}=[10/(B/t)][F_{y}t/(F_{yb}t_{b})]B_{b}\leq&space;B_{b}'>------------------------------------------------------------------------"] ;
        H(["<img src='https://latex.codecogs.com/svg.image?\space M_{n}'>-----------"]) ;
        J["비균일 하중분포로 인한 국부항복의 한계상태 검토"]
        E["<img src='https://latex.codecogs.com/svg.image?\beta<0.85'>--------------------"]
        F(["검토안함"]) ;
    Variable_def-->E--No--->J-->D-->C
    C-->H
    E--yes-->F
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def limit_state_of_local_surrender(fOMn,fIFyb,fIZb,fIbeoi,fIBb,fIHb,fItb,fIB,fIt,fIFy,fIbeta) -> float:
        """국부항복의 한계상태

        Args:
            fOMn (float): 국부항복의 한계상태
            fIFyb (float): 지강관의 항복강도
            fIZb (float): 휨축에 대한 지강관의 소성단면계수
            fIbeoi (float): 주강관에 용접된 지강관 면의 유효폭
            fIBb (float): 접합평면과 90를 이루는 각형 지강관의 폭
            fIHb (float): 접합평면에서 측정한 각형 지강관의 높이
            fItb (float): 지강관의 두께
            fIB (float): 접합평면과 90°를 이루는 각형 강관폭
            fIt (float): 주강관의 두께
            fIFy (float): 주강관의 항복강도
            fIbeta (float): 폭비


        Returns:
            float: 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.2.2 T, X형 접합에서 지강관의 면내 휨모멘트 (3) 의 값
        """
        #Pass --> 국부항복의 한계상태는 검토할 필요 없음


        if fIbeta >=0.85:
          fIbeoi = (10/(fIB/fIt))*(fIFy*fIt)/(fIFyb*fItb)*fIBb
          fOMn = fIFyb*(fIZb-(1-fIbeoi/fIBb)*fIBb*fIHb*fItb)
          return(fOMn)
        if fIbeta < 0.85:
          return("Pass")


# 

