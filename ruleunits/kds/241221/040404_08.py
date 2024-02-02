import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241221_040404_08 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 12 21 4.4.4 (8)' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-11-21'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '충격계수'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.4 충격하중 : IM
    4.4.4 표준열차하중에 대한 동적 효과(충격계수)
    (8)
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
        A[구조물의 충격계수];
        B["KDS 24 12 21 4.4.4 (8)"];
        A ~~~ B
        end
      subgraph Variable_def
    VarOut[/출력변수 : 구조물의 충격계수/];
    VarIn1[/입력변수 : 구조물에 복토가 없다고 보았을 때의 충격계수/];
    VarIn2[/입력변수 : 구조물 상면에서 침목상단까지의 복토 높이/];
    VarOut ~~~ VarIn1
    VarOut ~~~ VarIn2
    end
    Python_Class~~~Variable_def

    D["<img src='https://latex.codecogs.com/svg.image?i=i_{0}(H_{c}-1.0)(\geq&space;0)'>------------------------------"];
    E{"구조물의 상면이 흙 1m 이상 덮어져 있는 경우"};
    F(["표준연차하중"]);
    Variable_def--->E--Yes--->D--->F
        """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Impact_coefficient(fOi,fIio,fIHc) -> float:
        """충격계수

        Args:
            fOi (float): 구조물의 충격계수
            fIio (float): 구조물에 복토가 없다고 보았을 때의 충격계수
            fIHc (float): 구조물 상면에서 침목상단까지의 복토 높이


        Returns:
            float: 강교 설계기준(한계상태설계법)  4.4.4 표준열차하중에 대한 동적 효과(충격계수) (8) 의 값
        """

        fOi = max(fIio-0.1*(fIHc-1.0),0)
        return(fOi)


# 

