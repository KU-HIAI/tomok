import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS142054_040305_05 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 14 20 54 4.3.5 (5)' # 건설기준문서
    ref_date = '2021-02-18'  # 디지털 건설문서 작성일
    doc_date = '2023-10-11'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '비균열 콘크리트에 사용되는 부착식 앵커의 수정계수'    # 건설기준명

    #
    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.3 인장하중에 대한 설계 조건
    4.3.5 인장력을 받는 부착식 앵커의 부착강도
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
    A[비균열 콘크리트에 사용되는 부착식 앵커의 수정계수];
    B["KDS 14 20 54 4.3.5 (5)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 비균열 콘크리트에 사용되는 부착식 앵커의 수정계수/];
    VarIn1[/입력변수 : 앵커 샤프트 중심부터 콘크리트 단부까지 최소연단거리/];
    VarIn2[/입력변수 : 위험연단거리/];
    VarOut ~~~ VarIn1
    VarOut ~~~ VarIn2
    end
    Python_Class~~~Variable_def

    D{"<img src='https://latex.codecogs.com/svg.image?c_{a,min}\geq&space;c_{ac}'>"};
    E["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{cp,Na}=1.0'>"];
    F["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{cp,Na}=\frac{c_{a,min}}{c_{ac}}'>"];
    G(["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{cp,Na}'>"])
    Variable_def--->D
    D--Yes--->E--->G
    D--No--->F--->G
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def modification_factors_for_bonded_anchors_used_in_uncracked_concrete(fOpscpNa,fIcamin,fIcac) -> float:
        """비균열 콘크리트에 사용되는 부착식 앵커의 수정계수

        Args:
            fOpscpNa (float): 비균열 콘크리트에 사용되는 부착식앵커의 수정계수
            fIcamin (float): 앵커 샤프트 중심부터 콘크리트 단부까지 최소연단거리
            fIcac (float): 위험 연단거리

        Returns:
            float: 콘크리트용 앵커 설계기준  4.3.5 인장력을 받는 부착식 앵커의 부착강도 (5)의 값
        """

        if fIcamin >= fIcac:
          fOpscpNa = 1.0
        else:
          fOpscpNa = fIcamin / fIcac

        return fOpscpNa


