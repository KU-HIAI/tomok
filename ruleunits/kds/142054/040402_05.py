import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS142054_040402_05 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 14 20 54 4.4.2 (5)' # 건설기준문서
    ref_date = '2021-02-18'  # 디지털 건설문서 작성일
    doc_date = '2023-11-07'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '편심을 받는 앵커 그룹에 대한 수정계수'    # 건설기준명

    #
    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.4 전단하중에 대한 설계 조건
    4.4.2 전단력을 받는 앵커의 콘크리트 브레이크아웃강도
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
    A[전단력에 대한 편심을 받는 앵커 그룹에 대한 수정계수];
    B["KDS 14 20 54 4.4.2 (5)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 편심을 받는 앵커 그룹에 대한 수정계수/];
    VarIn1[/입력변수 : 앵커 그룹에 작용하는 전단력의 편심/];
    VarIn2[/입력변수 : 앵커 샤프드 중심부터 콘크리트 단부까지의 거리/];
    VarOut ~~~ VarIn1
    VarOut ~~~ VarIn2
    end
    Python_Class~~~Variable_def
    D{"앵커 그룹에서 일부 앵커만이 같은 방향으로 전단력을 받는 경우"};
    E["e'와 Vcbg를 계산할 때 같은 방향으로 전단력을 받는 앵커만을 고려"];
    F["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{ec,V}=\frac{1}{1&plus;\frac{2e^{,}_{V}}{3c_{a1}}}(\leq&space;1)'>-----------------------------"];
    G(["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{ec,V}'>"]);
    Variable_def--->D
    D--Yes--->E---->F
    D—No--->F--->G
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def correction_factor_for_anchor_groups_subject_to_eccentricity(fOpsiecV,fIeprimV,fIcaone) -> float:
        """편심을 받는 앵커 그룹에 대한 수정계수

        Args:
            fOpsiecV (float): 편심을 받는 앵커그룹에 대한 수정계수
            fIeprimV (float): 앵커 그룹에 작용하는 전단력의 편심
            fIcaone (float): 앵커 샤프트 중심부터 콘크리트 단부까지의 거리

        Returns:
            float: 콘크리트용 앵커 설계기준  4.4.2 전단력을 받는 앵커의 콘크리트 브레이크아웃강도 (5)의 값
        """

        fOpsiecV = min(1/(1+2*fIeprimV / (3*fIcaone)), 1.0)
        return fOpsiecV


