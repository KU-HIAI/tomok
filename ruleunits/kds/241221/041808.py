import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241221_041808 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 12 21 4.18.8' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-11-28'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '등가 정적선박충격하중'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.18 선박충돌하중: CV
    4.18.8 교각에 작용되는 선박 충격력
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
        A[등가 정적선박충격하중];
        B["KDS 24 12 21 4.18.8"];
        A ~~~ B
        end
    subgraph Variable_def
    VarOut[/출력변수 : 등가 정적선박충격하중/];
    VarIn1[/입력변수 : 선박충돌속도/];
    VarIn2[/입력변수 : 선박의 적재중량톤수/];
    end
    Python_Class~~~Variable_def
    C{"선박과 교각이 정면 충돌하는 경우"}
    D["<img src='https://latex.codecogs.com/svg.image?P_{s}=1.2\times&space;10^{5}V\sqrt{DWT}'>-------------------------------"];
    E(["등가 정적선박충격하중"]);
    Variable_def--->C--->D--->E
        """
    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def equivalent_static_ship_impact_load(fOPs,fIDWT,fIV) -> float:
        """수리동적질량계수

        Args:
            fOPs (float): 용골과 수로바닥과의 간격
            fIDWT (float): 선박의 흘수
            fIV (float): 수리동적질량계수

        Returns:
            float: 강교 설계기준(한계상태설계법) 4.18.8 교각에 작용되는 선박 충격력 의 값
        """

        fOPs=1.2*10**5*fIV*(fIDWT)**0.5
        return(fOPs)


# 

