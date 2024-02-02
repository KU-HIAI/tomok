import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241221_041805_06 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 12 21 4.18.5 (6)' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-11-27'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '연간파괴빈도'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.18 선박충돌하중: CV
    4.18.5 연간파괴빈도
    (6)
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
        A[각 기둥과 경간구조부재의 연간파괴빈도에 대한 허용기준];
        B["KDS 24 12 21 4.18.5 (6)"];
        A ~~~ B
        end
    subgraph Variable_def
    VarIn1[/입력변수 : 폭/];
    VarIn2[/입력변수 : LOA/];
    end
    Python_Class~~~Variable_def
    D{"폭>6 X LOA 인 수로"};
    E["각 기둥과 경간구조부재의 연간파괴빈도에 대한 허용기준은
    전체교량에 대한 허용기준을 입출항 항로의 두 중심선에서 좌우로
    LOA의 3배 거리 내에 위치한 기둥과 상부구조재들에 분포시켜 결정"];
    F(["Pass or Fail"]);

    Variable_def--->D--->E--->F
        """
    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def destruction_frequency(fIW,fILOA) -> bool:
        """연간파괴빈도

        Args:
            fIW (float): 폭
            fILOA (float): 설계선박의 전체길이

        Returns:
            float: 강교 설계기준(한계상태설계법) 4.18.5 연간파괴빈도 (6) 의 통과여부
        """

        #Pass =  각 기둥과 경간구조부재의 연간파괴빈도에 대한 허용기준은 전체 교량에 대한 허용기준을 입출항 항로의 두 중심선에서 좌우로 의 3배 거리 내에 위치한 기둥과 상부 구조재들에 분포시켜 결정하여야 한다.
        #Fail = 건설기준 4.18.5 (5) 참고

        if fIW >= fILOA*6:
          return("Pass")
        else:
          return("Fail")


# 

