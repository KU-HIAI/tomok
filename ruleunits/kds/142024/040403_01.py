import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS142024_040403_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 14 20 24 4.4.3 (1)' # 건설기준문서
    ref_date = '2021-02-18'  # 고시일
    doc_date = '2023-11-22'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '유효압축강도'    # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    콘크리트구조 스트럿-타이모델 기준
    4. 설계
    4.4 절점영역의 강도
    4.4.3 유효압축강도
    (1)
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
    A[단면력에 의한 절점영역 경계면의 유효압축강도];
    B["KDS 14 20 24 4.4.3 (1)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarOut[/출력변수 : 유효묻힘깊이/];
    VarIn1[/입력변수 : 앵커 샤프트 중심부터 콘크리트 단부까지 최대 연단거리/];
    VarIn2[/입력변수 : 최대 앵커 간격/];
    end
    Python_Class~~~Variable_def
    D{"앵커가 세개 또는 네개의 가장자리부터 1.5hef보다 짧은 거리에 위치한 경우"};
    E{"앵커 그룹인 경우"};
    F["<img src='https://latex.codecogs.com/svg.image?h_{ef}=\frac{c_{a,max}}{1.5}'>와 최대앵커간격/3 중 큰 값"];
    G["<img src='https://latex.codecogs.com/svg.image?h_{ef}=\frac{c_{a,max}}{1.5}'>"];
    H(["<img src='https://latex.codecogs.com/svg.image?A_{Nc}'>와 식(4.3-2)~식(2.3-9)까지 적용"]);

    Variable_def--->D--->E--Yes--->F--->H
    E--No--->G--->H

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Effective_compressive_strength(fIfce,fIbetan,fIfck) -> bool:
        """유효압축강도

        Args:
            fIfce (float): 유효압축강도
            fIbetan (float): 타이의 정착영향을 고려하기 위한 계수
            fIfck (float): 콘크리트의 설계기준압축강도

        Returns:
            bool: 콘크리트 스트럿-타이모델 기준  4.4.3 유효압축강도 (1)의 유효압축강도 값
        """
        if fIfce <= 0.85*fIbetan*fIfck:
          return "Pass"
        else:
          return "Fail"


# 

