import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS142054_040301_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 14 20 54 4.3.1 (2)' # 건설기준문서
    ref_date = '2021-02-18'  # 디지털 건설문서 작성일
    doc_date = '2023-09-21'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '앵커의 공칭강도'    # 건설기준명

    #
    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.3 인장하중에 대한 설계 조건
    4.3.1 인장력을 받는 앵커의 강재강도
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
    A[인장을 받는 앵커의 공칭강도];
    B["KDS 14 20 54 4.3.1 (2)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 앵커의 공칭강도/];
    VarIn1[/입력변수 : 인장에 대한 달일 앵커의 유효단면적/];
    VarIn2[/입력변수 : 앵커 강재의 설계기준인장강도/];
    VarIn3[/입력변수 : 앵커 강재의 설계기준항복강도/];
    VarOut ~~~ VarIn1
    VarOut ~~~ VarIn2
    VarOut ~~~ VarIn3
    end
    Python_Class~~~Variable_def
    D{"<img src='https://latex.codecogs.com/svg.image?f_{uta}=min(1.9f_{ya},860MPa)'>-----------------------------------------"};
    F["<img src='https://latex.codecogs.com/svg.image?&space;N_{sa}=A_{se,N}f_{uta}'>------------------------"];
    ariable_def--->D--->F
    F--->G(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def nominal_strength_of_anchor(fINsa,fIAseN,fIfuta,fIfya) -> bool:
        """앵커의 공칭강도

        Args:
            fINsa (float): 앵커의 공칭강도
            fIAseN (float): 인장에 대한 단일 앵커의 유효단면적
            fIfuta (float): 앵커 강재의 설계기준인장강도
            fIfya (float): 앵커 강재의 설계기준항복강도

        Returns:
            bool: 콘크리트용 앵커 설계기준  4.3.1 인장력을 받는 앵커의 강재강도 (2)의 통과여부
        """

        if fIfuta <= min(1.9*fIfya, 860):
          if fINsa <= fIAseN * fIfuta:
            return "Pass"

        return "Fail"


# 

