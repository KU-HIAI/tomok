import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04020303_05 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 24 14 21 4.2.3.3 (5)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '2축 응력 상태의 거더 복부의 유효인장강도'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.2 사용한계상태
    4.2.3 균열
    4.2.3.3 간접 균열 제어
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
    A["거더 복부의 유효인장강도"];
    B["KDS 24 14 21 4.2.3.3 (5)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 주압축응력/];
		VarIn2[/입력변수: 콘크리트의 기준압축강도/];
		VarIn3[/입력변수: 콘크리트 하위 0.5 분위 기준인장강도/];
		VarOut1[/출력변수: 거더 복부의 유효인장강도/];
		VarOut1~~~VarIn1 & VarIn2  & VarIn3

		end
		Python_Class ~~~ Variable_def;
		Variable_def--->D--->E--->F
		D["<img src='https://latex.codecogs.com/svg.image?f_{2}\leq&space;0.6f_{ck}'>---------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?f_{cte}=(1-0.8\frac{f_2}{f_{ck}})f_{ctk}'>---------------------------------"]

		F(["거더 복부의 유효인장강도"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Effective_tensile_strength_of_girderweb(fOfcte,fIf2,fIfck,fIfctk) -> float:
        """2축 응력 상태의 거더 복부의 유효인장강도

        Args:
             fOfcte (float): 거더 복부의 유효인장강도
             fIf2 (float): 주압축응력
             fIfck (float): 콘크리트의 기준압축강도
             fIfctk (float): 콘크리트 하위 0.5 분위 기준인장강도


        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.2.3.3 간접 균열 제어 (5)의 값
        """

        fIf2 = min(fIf2, 0.6*fIfck)
        fOfcte = (1-0.8*fIf2/fIfck)*fIfctk

        return fOfcte


# 

