import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241221_041811_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 12 21 4.18.11 (2)' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-11-28'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '표준호퍼바지선의 충격력'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.18 선박충돌하중: CV
    4.18.11 교각에 작용하는 바지선의 충격력
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
        A[교각에 작용되는 표준호퍼바지선의 충격력];
        B["KDS 24 12 21 4.18.11 (2)"];
        A ~~~ B
        end
    subgraph Variable_def
    VarOut[/출력변수 : 표준호퍼바지선의 충격력/];
    VarIn1[/입력변수 : 식 4.18-25에 규정도니 바지선의 이물 손상길이/];
    end
    Python_Class~~~Variable_def
    D{"<img src='https://latex.codecogs.com/svg.image?a_{B}<100mm&space;'>-----------------"};
    E["<img src='https://latex.codecogs.com/svg.image?P_{B}=6.0\times10^{4}a_{B}&space;'>-----------------"];
    F["<img src='https://latex.codecogs.com/svg.image?P_{B}=6.0\times10^{6}+1,600a_{B}&space;'>-------------------------"];
    G(["표준호퍼바지선의 충격력"]);
    Variable_def--->D--Yes--->E--->G
    D--No--->F--->G
        """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def impact_force_of_standard_hopper_barge(fOPb,fIaB) -> bool:
        """표준호퍼바지선

        Args:
            fOPb (float): 표준호퍼바지선의 충격력
            fIaB (float): 식 (4.18-25)에 규정된 바지선의 이물 손상길이

        Returns:
            float: 강교 설계기준(한계상태설계법) 4.18.11 교각에 작용하는 바지선의 충격력 (2) 의 통과여부
        """

        if fIaB < 100:
          fOPb = 6.0*10**4*fIaB
        elif fIaB > 100:
          fOPb = 6.0*10**6+1600*fIaB

        return(fOPb)


# 

