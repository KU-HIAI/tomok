import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241221_04030101_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 12 21 4.3.1.1 (2)' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-11-21'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '재하차로의 폭'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.3 활하중
    4.3.1 차량활하중 : LL
    4.3.1.1 재하차로의 수
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
        A[재하차로의 수];
        B["KDS 24 12 21 4.3.1.1 (2)"];
        A ~~~ B
        end
      subgraph Variable_def
    VarOut[/출력변수 : 재하차로의 수/];
    VarIn1[/입력변수 : 연석, 방호울타리간의 교폭/];
    VarIn2[/입력변수 : 재하차로의 수/];
    VarOut ~~~ VarIn1
    VarOut ~~~ VarIn2
    end
    Python_Class~~~Variable_def

    D["<img src='https://latex.codecogs.com/svg.image?W=\frac{W_{c}}{N}(\leq&space;3.6m)'>--------------------"];
    Variable_def--->D--->F(["재하차로의 폭"])
        """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def the_width_of_a_loading_lane(fOW,fIWc,fIN) -> float:
        """재하차로의 폭


        Args:
            fOW (float): 재하차로의 폭
            fIWc (float): 연석,방호 울타리간의 교폭
            fIN (float): 재하차로의 수

        Returns:
            float: 강교 설계기준(한계상태설계법)  4.3.1.1 재하차로의 수 (2) 의 값
        """


        fOW = min(fIWc/fIN,3.6)
        return(fOW)


# 

