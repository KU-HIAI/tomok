import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_040108_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Hyunjong Shin'  # 작성자명
    ref_code = 'KDS 14 31 25 4.1.8' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-11-17'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '콘크리트 단면의 일부분이 지압을 받는 경우 콘크리트의 설계지압강도'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.8 주각부 및 콘크리트의 지압
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
	A([Title: 주각부 및 콘크리트의 지압])
	B["KDS 14 31 25 4.1.8(2)"]
	A ~~~ B
	end

	subgraph Variable_def
  VarOut[/출력변수: 설계지압강도/]
	VarIn1[/입력변수: 콘크리트의 공칭지압강도/]
	VarIn2[/입력변수: 콘크리트의 설계기준 압축강도/]
	VarIn3[/입력변수: 베이스플레이트의 면적/]
	VarIn4[/입력변수: 베이스플레이트와 닮은꼴의 콘크리트 지지부분의 최대면적/]
	VarOut ~~~  VarIn1 & VarIn2
	VarIn1 & VarIn2 ~~~~ VarIn3 & VarIn4
	end

	Python_Class ~~~ Variable_def --> C --> D --> E
	C["콘크리트의 단면의 일부분이 지압을 받는 경우"]
	D["<img src='https://latex.codecogs.com/svg.image?P_p=0.85f_{ck}A_1\sqrt{{A_2}/{A_1}}\leq&space;1.7f_{ck}A_1'>------------------------------------------------------"]
	E(["<img src='https://latex.codecogs.com/svg.image?P_p'>--------"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Design_Pressure_Strength_of_Concrete_when_Part_of_the_Cross_Section_of_Concrete_is_Under_Acupressure(fOphicPp,fIPp,fIfck,fIA1,fIA2) -> bool:
        """콘크리트 단면의 일부분이 지압을 받는 경우 콘크리트의 설계지압강도
        Args:
            fOphicPp (float): 설계지압강도
            fIPp (float): 콘크리트의 공칭지압강도
            fIfck (float): 콘크리트의 설계기준 압축강도
            fIA1 (float): 베이스플레이트의 면적
            fIA2 (float): 베이스플레이트와 닮은꼴의 콘크리트 지지부분의 최대면적

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법)  4.1.8 콘크리트압괴의 한계상태에 대해 단면의 일부분이 지압을 받는 경우 콘크리트의 설계지압강도 (2)의 값
        """
        fIPp = min((0.85)*fIfck*fIA1*((fIA2/fIA1)**0.5), (1.7)*fIfck*fIA1)
        fOphicPp = 0.65 * fIPp
        return fOphicPp


# 

