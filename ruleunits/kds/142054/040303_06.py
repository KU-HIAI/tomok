import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS142054_040303_06 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 14 20 54 4.3.3 (6)' # 건설기준문서
    ref_date = '2021-02-18'  # 디지털 건설문서 작성일
    doc_date = '2023-11-07'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '균열 유무에 따른 앵커뽑힘강도에 대한 수정계수'    # 건설기준명

    #
    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.3 인장하중에 대한 설계 조건
    4.3.3 인장력을 받는 선설치앵커, 후설치 확장앵커 및 언더컷앵커의 뽑힘강도
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
    A[균열 유무에 따른 앵커뽑힘강도에 대한 수정계수];
    B["KDS 14 20 54 4.3.3 (6)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 균열 유무에 따른 앵커뽑힘강도에 대한 수정계수/];
    end
    Python_Class~~~Variable_def
    D{"부재가 사용하중을 받을 때 균열이 발생될 경우"};
    E["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{c,P}=1.0'>"];
    F["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{c,P}=1.4'>"];
    G(["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{c,P}'>"]);
    Variable_def--->D
    D--Yes-->E--->G
    D—No--->F--->G
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def correction_factor_for_anchor_pullout_strength_with_and_without_cracks(fOpsicP,fIuserdefined) -> float:
        """균열 유무에 따른 앵커뽑힘강도에 대한 수정계수

        Args:
            fOpsicP (float): 균열 유무에 따른 앵커뽑힘 강도에 대한 수정계수
            fIuserdefined (float): 사용자 선택

        Returns:
            float: 콘크리트용 앵커 설계기준  4.3.3 인장력을 받는 선설치앵커, 후설치 확장앵커 및 언더컷앵커의 뽑힘강도 (6)의 값
        """

        #균열이 없는 경우 : fIuserdefined = 1
        #균열이 발생한 경우 : fIuserdefined = 2

        if fIuserdefined == 1:
          fOpsicP = 1.4
        elif fIuserdefined == 2:
          fOpsicP = 1.0

        return fOpsicP


