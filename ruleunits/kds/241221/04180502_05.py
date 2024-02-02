import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241221_04180502_05 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 12 21 4.18.5.2 (5)' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-11-27'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '통과경로에 평행한 유속에 대한 보정계수'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.18 선박충돌하중: CV
    4.18.5 연간파괴빈도
    4.18.5.2 항로이탈확률
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
        A[선박의 통과경로에 평행한 유속에 대한 보정계수];
        B["KDS 24 12 21 4.18.5.2 (5)"];
        A ~~~ B
        end
    subgraph Variable_def
    VarOut[/출력변수 : 통과경로에 평행한 유속에 대한 보정계수/];
    VarIn1[/입력변수 : 선박의 통과경로에 평행한 유속성분/];
    end
    Python_Class~~~Variable_def
    D["<img src='https://latex.codecogs.com/svg.image?R_{C}=1.0&plus;\frac{V_{C}}{19}'>--------------------------"];
    E(["통과경로에 직각방향 유속에 대한 보정계수"]);
    Variable_def--->D--->E
        """
    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def correction_factor_for_flow_rate_parallel_to_the_passage_path(fORc,fIVc) -> float:
        """통과경로에 평행한 유속에 대한 보정계수

        Args:
            fORc (float): 통과경로에 평행한 유속에 대한 보정계수
            fIVc (float): 선박의 통과경로에 평행한 유속성분
        Returns:
            float: 강교 설계기준(한계상태설계법) 4.18.5.2 항로이탈확률 (5) 의 값
        """

        fORc = 1+fIVc/19

        return(fORc)


# 

