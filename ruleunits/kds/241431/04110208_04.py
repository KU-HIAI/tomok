import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241431_0411208_04 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 31 4.11.2.8 (4)' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-09-04'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '트러스교의 연결판'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.11 구조형식
    4.11.2 트러스교
    4.11.2.8 연결판
    (4)
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
    A(["Title : 연결판"]);
    B["KDS 24 14 31 4.11.2.8(4)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarIn1[/입력변수: 가장자리의 길이/];
    VarIn2[/입력변수: 판두께/];
    VarIn3[/입력변수: 강재의 탄성계수/];
    VarIn4[/입력변수: 강재의 설계기준항복강도/];

    VarIn1 & VarIn2 ~~~ VarIn3 & VarIn4
    end

    Python_Class ~~~ Variable_def

    Variable_def -->C
    C["가장자리의 길이 > 판두께 <img src='https://latex.codecogs.com/svg.image?\times&space;2.06(E/F_{y})^{0.5}'>---------------------"];
    D([가장자리보강])
    E([가장자리보강X])

    C--Yes--> D
    C--No--> E

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Connecting_plate_of_truss_bridge(fIlenedg,fIplathi,fIE,fIFy) -> bool:
        """트러스교의 연결판

        Args:
            fIlenedg (float): 가장자리의 길이
            fIplathi (float): 판두께
            fIE (float): 강재의 탄성계수
            fIFy (float): 강재의 설계기준항복강도

        Returns:
            bool: 강교 설계기준(한계상태설계법)  4.11.2.8 연결판 (4)의 통과 여부
        """

        if fIlenedg > fIplathi*2.06*((fIE/fIFy)**0.5) :
          print("가장자리 보강 필요함")


# 

