import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241221_040402 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 12 21 4.4.2' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-11-21'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '암거나 매설된 구조물에 대한 충격하중'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.4 충격하중 : IM
    4.4.2 매설된 부재
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
        A[암거나 매설된 구조물에 대한 충격하중계수];
        B["KDS 24 12 21 4.4.2"];
        A ~~~ B
        end
      subgraph Variable_def
    VarOut[/출력변수 : 충격하중계수/];
    VarIn1[/입력변수 : 구조물을 덮고 있는 최소깊이/];
    VarOut ~~~ VarIn1
    end
    Python_Class~~~Variable_def
    D["<img src='https://latex.codecogs.com/svg.image?IM=40(1.0-4.1 \times 10^{-4}D_{E}\geq&space;0%'>-------------------------------------------------------"]
    E(["충격하중계수"])
    Variable_def--->D--->E
        """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Impact_load_on_hidden_or_buried_structures(fOIM,fIDE) -> float:
        """암거나 매설된 구조물에 대한 충격하중

        Args:
            fOIM (float): 충격하중계수
            fIDE (float): 구조물을 덮고 있는 최소깊이


        Returns:
            float: 강교 설계기준(한계상태설계법)  4.4.2 매설된 부재 의 값
        """


        fOIM = max(40*(1.0-4.1*10**(-4)*fIDE),0)
        return(fOIM)


# 

