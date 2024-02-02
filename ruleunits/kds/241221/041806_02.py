import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241221_041806_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 12 21 4.18.6 (2)' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-11-28'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '설계선박의 전체길이'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.18 선박충돌하중: CV
    4.18.6 설계 충돌 속도
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
        A[설계선박의 전체길이];
        B["KDS 24 12 21 4.18.6 (2)"];
        A ~~~ B
        end
    subgraph Variable_def
    VarOut[/출력변수 : 설계선박의 전체길이/];
    VarIn1[/입력변수 : 선박의 용적톤수/];
    VarIn2[/입력변수 : 수리동적질량계수/];
    VarIn3[/입력변수 : 선박충돌속도/];
    end
    Python_Class~~~Variable_def
    D{"바지선 예의인 경우"};
    E["LOA=바지선 길이 + 예인선 길이 + 예인 로우프의 길이"];
    F(["설계선박의 전체길이(LOA)"]);
    Variable_def--->D--->E--->F
        """
    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def design_ship_total_length(fOLOA,fIlbarge,fIltug,fIltowi) -> float:
        """설계선박의 전체길이

        Args:
            fOLOA (float): 설계선박의 전체길이
            fIlbarge (float): 바지선 길이
            fIltug (float): 예인선 길이
            fIltowi (float): 예인 로우프의 길이
        Returns:
            float: 강교 설계기준(한계상태설계법) 4.18.6 설계 충돌 속도 (2) 의 값
        """

        fOLOA = fIlbarge + fIltug + fIltowi
        return(fOLOA)


# 

