import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS142054_040305_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 20 54 4.3.5 (2)' # 건설기준문서
    ref_date = '2021-02-18'  # 디지털 건설문서 작성일
    doc_date = '2023-12-11'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '균열 콘크리트에서 인장력을 받는 단일 부착식 앵커의 기본 부착강도'    # 건설기준명

    #
    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.3 인장하중에 대한 설계 조건
    4.3.5 인장력을 받는 부착식 앵커의 부착강도
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
    A[균열 콘크리트에서 인장력을 받는 단일 부착식 앵커의 기본 부착강도];
    B["KDS 14 20 54 4.3.5 (2)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarIn1[/입력변수 : 인장을 받는 단일 부착식 앵커의 기본부착강도/];
    VarIn2[/입력변수 : 앵커 강도 설계에서 경량콘크리트의 저감된 물성을 고려한 수정계수/];
    VarIn3[/입력변수 : 특성부착강도/];
    VarIn4[/입력변수 : 앵커의 외경, 혹은 헤드스터드, 헤드볼트, 갈고리형볼트의샤프트지름/];
    VarIn5[/입력변수 : 앵커의 유효묻힘깊이/];
    VarIn1 & VarIn2 ~~~ VarIn3 & VarIn4 & VarIn5

    end
    Python_Class~~~Variable_def

    D["<img src='https://latex.codecogs.com/svg.image?N_{ba} \leq \lambda _{a}\tau _{cr}\pi d_{a}h_{ef}'>----------------------------"];
    E(["Pass or Fail"]);

    Variable_def--->D--->E
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Basic_bond_strength_of_single_attached_anchors_in_tension_in_cracked_concrete(fINba,fIlamda,fItaucr,fIda,fIhef) -> bool:
        """균열 콘크리트에서 인장력을 받는 단일 부착식 앵커의 기본 부착강도

        Args:
            fINba (float): 인장을 받는 단일 부착식 앵커의 기본부착강도
            fIlamda (float): 앵커 강도 설계에서 경량콘크리트의 저감된 물성을 고려한 수정계수
            fItaucr (float): 특성부착강도
            fIda (float): 앵커의 외경, 혹은 헤드스터드, 헤드볼트, 갈고리형볼트의 샤프트지름
            fIhef (float): 앵커의 유효묻힘깊이

        Returns:
            bool: 콘크리트용 앵커 설계기준  4.3.5 인장력을 받는 부착식 앵커의 부착강도 (2)의 통과여부
        """

        if fINba <= fIlamda * fItaucr * math.pi * fIda * fIhef :
          return "Pass"
        else:
          return "Fail"


