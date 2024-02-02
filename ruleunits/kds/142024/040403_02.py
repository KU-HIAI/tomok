import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS142024_040403_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 14 20 24 4.4.3 (2)' # 건설기준문서
    ref_date = '2021-02-18'  # 고시일
    doc_date = '2023-11-22'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '절점영역 압축강도를 계산할 때 타이의 정착 영향을 고려하기 위한 계수'    # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    콘크리트구조 스트럿-타이모델 기준
    4. 설계
    4.4 절점영역의 강도
    4.4.3 유효압축강도
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
    A[타이의 정착영향을 고려하기 위한 계수];
    B["KDS 14 20 24 4.4.3 (2)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 타이의 정착영향을 고려하기 위한 계수/];
    VarIn1[/입력변수 : 절점영역에 연결된 타이 개수/];
    end
    Python_Class~~~Variable_def
    D{"절점영역에 연결된 타이 개수"};
    E{"지지판, 스트럿 또는 지지판과 스트럿에 의해 형성된 절점영역"};
    F["<img src='https://latex.codecogs.com/svg.image?\beta_{n}=0.80'>"];
    G["<img src='https://latex.codecogs.com/svg.image?\beta_{n}=0.60'>"];
    H["<img src='https://latex.codecogs.com/svg.image?\beta_{n}=1.0'>"];
    I(["<img src='https://latex.codecogs.com/svg.image?\beta_{n}'>"]);
    Variable_def--->D--1개--->F--->I
    D--2개--->G--->I
    Variable_def--->E--->H--->I
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Coefficients_to_consider_the_settlementeffectsofthetie(fObetan,fIusedefined) -> float:
        """절점영역 압축강도를 계산할 때 타이의 정착 영향을 고려하기 위한 계수

        Args:
            fObetan (float): 타이의 정착 영향을 고려하기 위한 계수
            fIusedefined (float): 사용자 선택

        Returns:
            float: 콘크리트 스트럿-타이모델 기준  4.4.3 유효압축강도 (1)의 타이의 정착 영향을 고려하기 위한 계수값
        """

        #지지판, 스트럿 또는 지지판과 스트럿에 의해 형성된 절점영역: fIuserdefined = 1
        #하나의 타이가 연결된 절점영역: fIuserdefined = 2
        #두 개 이상의 타이가 연결된 절점영역: fIuserdefined = 3

        if fIusedefined==1:
          fObetan=1.0
        elif fIusedefined==2:
          fObetan=0.80
        elif fIusedefined==3:
          fObetan=0.60

        return fObetan


# 

