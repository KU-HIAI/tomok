import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS142024_040202_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jaeguk Jang'  # 작성자명
    ref_code = 'KDS 14 20 24 4.2.2 (1)' # 건설기준문서
    ref_date = '2021-02-18'  # 고시일
    doc_date = '2023-08-09'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '콘크리트 스트럿의 유효압축강도 산정'    # 건설기준명

    #
    description = """
    콘크리트구조 스트럿-타이모델 기준
    4. 설계
    4.2 스트럿의 축강도
    4.2.2 유효압축강도
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
    A[콘크리트 스트럿의 유효압축강도];
    B["KDS 14 20 24 4.2.2 (1)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarOut[/출력변수 : 콘크리트 스트럿의 유효압축강도/];
		VarIn1[/입력변수 : 균열의 영향과 구속철근의 영향을 고려하기 위한 계수/];
		VarIn2[/입력변수 : 콘크리트의 설계기준압축강도/];
		VarOut ~~~ VarIn1
		VarOut ~~~ VarIn2
    end

		Python_Class ~~~ Variable_def

		D["<img src='https://latex.codecogs.com/svg.image?f_{ce}=0.85\beta&space;_{s}f_{ck}'>---------------------------------------"];
		E["실험과 적절한 해석을 통해 구한 값"]
		F(["<img src='https://latex.codecogs.com/svg.image?f_{ce}'>"]);
		Variable_def--->D--->F
		Variable_def--->E--->F
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Calculate_the_effective_compressive_strength_of_a_concrete_strut(fOfce, fIbetas, fIfck) -> bool:
        """콘크리트 스트럿의 유효압축강도 산정.

        Args:
            fOfce (float): 콘크리트 스트럿의 유효압축강도
            fIbetas (float): 균열의 영향과 구속철근의 영향을 고려하기 위한 계수
            fIfck (float): 콘크리트의 설계기준압축강도

        Returns:
            bool: 콘크리트 스트럿-타이모델 기준  4.2.1 설계원칙 (1)의 통과 여부
        """
        fOfce = 0.85*fIbetas*fIfck

        return fOfce


# 

