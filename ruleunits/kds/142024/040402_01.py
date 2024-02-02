import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS142024_040402_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 14 20 24 4.4.2 (1)' # 건설기준문서
    ref_date = '2021-02-18'  # 고시일
    doc_date = '2023-11-22'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '절점영역의 공칭강도'    # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    콘크리트구조 스트럿-타이모델 기준
    4. 설계
    4.4 절점영역의 강도
    4.4.2 축강도 산정
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
    A[절점영역의 공칭강도];
    B["KDS 14 20 24 4.4.2 (1)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 절점영역의 공칭강도/];
    VarIn1[/입력변수 : 절점영역의 유효압축강도/];
    VarIn2[/입력변수 : 절점영역 경계면의 면적/];
    VarOut~~~ VarIn1
    VarOut~~~VarIn2
    end
    Python_Class~~~Variable_def
    D["<img src='https://latex.codecogs.com/svg.image?&space;F_{nn}=f_{ce}A_{n}'>--------------------------------------------"];
    E(["절점영역의 공칭강도"]);
    Variable_def--->D--->E
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Nominal_strength_of_nodalzone(fOFnn,fIfce,fIAn) -> float:
        """절점영역의 공칭강도

        Args:
            fOFnn (float): 절점영역의 공칭강도
            fIfce (float): 스트럿 또는 절점영역의 콘크리트 유효압축강도
            fIAn (float): 절점영역 경계면의 면적

        Returns:
            float: 콘크리트 스트럿-타이모델 기준  4.4.2 축강도 산정 (1)의 절점영역의 공칭강도 값
        """
        fOFnn=fIfce*fIAn
        return fOFnn


# 

