import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241221_041809 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 12 21 4.18.9' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-11-28'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '선박의 이물손상길이'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.18 선박충돌하중: CV
    4.18.9 선박의 이물손상길이
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
        A[견고한 물체에 부딪쳐 부서진 이물의 수평길이];
        B["KDS 24 12 21 4.18.9"];
        A ~~~ B
        end
    subgraph Variable_def
    VarOut[/출력변수 : 손상을 입은 이물의 길이/];
    VarIn1[/입력변수 : 선박의 충돌에너지/];
    VarIn2[/입력변수 : 선박의 충격력/];
    end
    Python_Class~~~Variable_def

    D["<img src='https://latex.codecogs.com/svg.image?&space;a_{s}=1.54\times&space;10^{3}\left(\frac{KE}{P_{s}}\right)'>-------------------------------"];
    E(["손상을 입은 이물의 길이"]);
    Variable_def--->D--->E
        """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def the_length_of_the_damaged_foreign_body(fOas,fIKE,fIPs) -> float:
        """선박의 이물손상길이

        Args:
            fOas (float): 손상을 입은 이물의 길이
            fIKE (float): 선박의 충돌에너지
            fIPs (float): 식 (4.18-17)에서 규정된 선박의 충격력

        Returns:
            float: 강교 설계기준(한계상태설계법) 4.18.9 선박의 이물손상길이 의 값
        """

        fOPs=1.54*10**3*fIKE/fIPs
        return(fOPs)


# 

