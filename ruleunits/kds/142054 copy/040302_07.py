import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS142054_040302_07 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 14 20 54 4.3.2 (7)' # 건설기준문서
    ref_date = '2021-02-18'  # 디지털 건설문서 작성일
    doc_date = '2023-09-26'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '비균열 콘크리트에 사용되는 후설치앵커의 수정계수'    # 건설기준명

    #
    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.3 인장하중에 대한 설계 조건
    4.3.2 인장력을 받는 앵커의 콘크리트 브레이크아웃강도
    (7)
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
    A[비균열 콘크리트에 사용되는 후설치 앵커의 수정계수];
    B["KDS 14 20 54 4.3.2 (7)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 비균열 콘크리트에 사용되는 후설치 앵커의 수정계수/];
    VarIn1[/입력변수 : 앵커 샤프트 중심부터 콘크리트 단부까지 최소연단거리/];
    VarIn2[/입력변수 : 위험 연단거리/];
    VarIn3[/입력변수 : 앵커의 유효묻힘깊이/];
    VarOut ~~~ VarIn1
    VarOut ~~~ VarIn2 & VarIn3
    end
    Python_Class~~~Variable_def
    C{"쪼개짐을 제어하기 위한 보조철근을 사용한 경우"};
    D{"<img src='https://latex.codecogs.com/svg.image?c_{a,min}\geq&space;c_{ac}'>--------------------"};
    E["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{cp,N}=1'>"];
    F["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{cp,N}=\frac{c_{a,min}}{c_{ac}}(\geq&space;1.5\frac{h_{ef}}{c_{ac}}))'>-------------------------------------"];
    G(["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{cp,N}'>"]);
    Variable_def--->C--No--->D
    D--Yes--->E--->G
    D--No--->F--->G
    C--Yes--->H["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{cp,N}=1'>"]--->G
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def modification_factor_of_post_installation_anchor_used_for_uncracked_concrete(fOpsicpN,fIcamin,fIcac,fIhef) -> float:
        """비균열 콘크리트에 사용되는 후설치앵커의 수정계수

        Args:
            fOpsicpN (float): 비균열 콘크리트에 사용되는 후설치앵커의 수정계수
            fIcamin (float): 앵커 샤프트 중심부터 콘크리트 단부까지 최소연단거리
            fIcac (float): 위험 연단거리
            fIhef (float): 앵커의 유효묻힘깊이

        Returns:
            float: 콘크리트용 앵커 설계기준  4.3.2 인장력을 받는 앵커의 콘크리트 브레이크아웃강도 (7)의 값
        """

        if fIcamin >= fIcac:
          fOpsicpN = 1.0
          return fOpsicpN

        else:
          fOpsicpN = fIcamin / fIcac
          if fOpsicpN >= 1.5 * fIhef / fIcac :
            return fOpsicpN, "Pass"
          else:
            return fOpsicpN, "Fail"


# 

