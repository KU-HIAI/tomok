import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS142024_040204_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 14 20 24 4.2.4 (2)' # 건설기준문서
    ref_date = '2021-02-18'  # 고시일
    doc_date = '2023-11-21'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '종방향으로 보강된 스트럿의 강도'    # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    콘크리트구조 스트럿-타이모델 기준
    4. 설계
    4.2 스트럿의 축강도
    4.2.4 철근 효과
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
    A[종방향으로 보강된 스트럿의 강도];
    B["KDS 14 20 24 4.2.4 (2)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarOut[/출력변수 : 종방향으로 보강된 스트럿의 강도/];
		VarIn1[/입력변수 : 절점영역의 콘크리트 유효압축강도/];
		VarIn2[/입력변수 : 스트럿의 유효단면적/];
		VarIn3[/입력변수 : 철근스트럿의 단면적/];
		VarIn4[/입력변수 : 압축철근의 응력/];
		VarOut ~~~VarIn1~~~VarIn3
		VarOut ~~~VarIn2~~~VarIn4
    end

		Python_Class ~~~ Variable_def

		D["<img src='https://latex.codecogs.com/svg.image?f^{,}_{s}'>"];
		E{"설계기준항복강도 ≤500MPa"}--->G["<img src='https://latex.codecogs.com/svg.image?f^{,}_{s}'>=설계기준항복강도"];
		F{"압축철근의 응력으로 스트럿이 압축파괴 될 경우"}--->H["스트럿 변형률로부터 계산"];

		Variable_def--->D
		D--->E
		D--->F

		I["<img src='https://latex.codecogs.com/svg.image?F_{ns}=f_{ce}A_{c}&plus;1.13A^{,}_{s}f^{,}_{s}'>-----------------------------------"];
		G--->I
		H--->I
		I--->J(["종방향으로 보강된 스트럿의 강도"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Strength_of_longitudinally_reinforcedstruts(fOFns,fIfprims,fIAprims,fIAc,fIfce) -> float:
        """종방향으로 보강된 스트럿의 강도

        Args:
            fOFns (float): 종방향으로 보강된 스트럿의 강도
            fIfprims (float): 압축철근의 응력
            fIAprims (float): 철근스트럿의 단면적
            fIAc (float): 스트럿의 유효단면적
            fIfce (float): 스트럿 또는 절점영역의 콘크리트 유효압축강도

        Returns:
            float: 콘크리트 스트럿-타이모델 기준  4.2.4 철근 효과 (2)의 값
        """
        fOFns=fIfce*fIAc+1.13*fIAprims*fIfprims
        return fOFns


# 

