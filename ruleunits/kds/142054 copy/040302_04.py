import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS142054_040302_04 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 14 20 54 4.3.2 (4)' # 건설기준문서
    ref_date = '2021-02-18'  # 디지털 건설문서 작성일
    doc_date = '2023-11-26'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '인장력의 편심이 작용하는 앵커 그룹에 대한 수정계수'    # 건설기준명

    #
    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.3 인장하중에 대한 설계 조건
    4.3.2 인장력을 받는 앵커의 콘크리트 브레이크아웃강도
    (4)
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
    A[인장력의 편심이 작용하는 앵커 그룹에 대한 수정계수];
    B["KDS 14 20 54 4.3.2 (4)"];
    A ~~~ B
    end
  	subgraph Variable_def
    VarOut[/출력변수 : 인장력의 편심이 작용하는 앵커 그룹에 대한 수정계수/];
    VarIn1[/입력변수 : 인장하중을 받는 앵커 그룹에 작용하는 인장력의 합력과 앵커 그룹 도심사이의 거리/];
    VarIn2[/입력변수 : 앵커의 유효묻힘깊이/];
    end
    Python_Class~~~Variable_def
    D{"두 축에 대하여 편심하중이 존재하는 경우"};
    E["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{ec,N}=\frac{1}{\left(1&plus;\frac{2e_{N}^{,}}{3h_{ef}}\right)}(\leq&space;1)'>---------------------------------------"];
    F["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{ec,N}=\frac{1}{\left(1&plus;\frac{2e_{N}^{,}}{3h_{ef}}\right)}(\leq&space;1)'>각 축에 대해 독립적으로 계산후 곱합"];
    G(["인장력의 편심이 작용하는 앵커 그룹에 대한 수정계수"]);
    Variable_def--->D--Yes--->F--->G
    D--No --->E--->G
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Modification_factor_for_anchor_group_under_eccentric_tensile(fOpsiecN,fIeprimN,fIhef) -> float:
        """인장력의 편심이 작용하는 앵커 그룹에 대한 수정계수

        Args:
            fOpsiecN (float): 인장력의 편심이 작용하는 앵커 그룹에 대한 수정계수
            fIeprimN (float): 인장하중을 받는 앵커 그룹에 작용하는 인장력의 합력과 앵커 그룹 도심 사이의 거리
            fIhef (float): 앵커의 유효묻힘깊이

        Returns:
            float: 콘크리트용 앵커 설계기준  4.3.2 인장력을 받는 앵커의 콘크리트 브레이크아웃강도 (4)의 값
        """

        fOpsiecN = min(1 / (1+2*fIeprimN/3/fIhef) , 1)
        return fOpsiecN


# 

