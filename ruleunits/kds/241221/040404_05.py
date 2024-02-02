import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241221_040404_05 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 12 21 4.4.4 (5)' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-11-21'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '충격계수'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.4 충격하중 : IM
    4.4.4 표준열차하중에 대한 동적 효과(충격계수)
    (5)
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
        A[충격계수];
        B["KDS 24 12 21 4.4.4 (5)"];
        A ~~~ B
        end
      subgraph Variable_def
    VarOut[/출력변수 : 비균열 콘크리트에 사용되는 후설치 앵커의 수정계수/];
    VarIn1[/입력변수 : 앵커 샤프트 중심부터 콘크리트 단부까지 최소연단거리/];
    VarIn2[/입력변수 : 위험 연단거리/];
    VarOut ~~~ VarIn1
    VarOut ~~~ VarIn2
    end
    Python_Class~~~Variable_def
    D["<img src='https://latex.codecogs.com/svg.image?I_{m}=\frac{1.44}{\sqrt{L_{e}}-0.2}-0.18'>--------------------------"];
    E["0 < Im ≤ 0.67"];
    F(["충격계수 or Fail"])
    Variable_def--->D--->E--->F
        """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Impact_coefficient(fOIm,fILe) -> float:
        """충격계수

        Args:
            fOIm (float): 충격계수
            fILe (float): 구조물의 길이 특성치


        Returns:
            float: 강교 설계기준(한계상태설계법)  4.4.4 표준열차하중에 대한 동적 효과(충격계수) (5) 의 값
        """

        fOIm = 1.44/(fILe**0.5-0.2)-0.18
        return(fOIm)


# 

