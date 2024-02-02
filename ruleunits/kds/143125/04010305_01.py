import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_04010305_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Hyunjong Shin'  # 작성자명
    ref_code = 'KDS 14 31 25 4.1.3.5 (1)' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-10-06'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '지압강도 한계상태에 대한 볼트구멍에서 설계강도'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.3 볼트
    4.1.3.5 볼트구멍의 지압강도
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
	  A([볼트구멍의 지압강도])
	  B["KDS 14 31 25 4.1.3.5(1)"]
	  A ~~~ B
	  end

  	subgraph Variable_def
  	VarOut[/출력변수: 볼트구멍에서 설계강도/]
    VarIn1[/입력변수: 구멍의 끝과 피접합체의 끝 또는 인접구멍의 끝까지의 거리/]
    VarIn2[/입력변수: 피접합체의 두께/]
    VarIn3[/입력변수: 피접합체의 공칭인장강도/]
    VarIn4[/입력변수: 볼트 공칭직경/]
    VarOut ~~~ VarIn1 & VarIn2 ~~~ VarIn3 & VarIn4
  	end

	  Python_Class ~~~ Variable_def  --> C & H
    C --> D & E
    D --> F
    E --> G
    H --> I
    F & G & I --> J


	  C["표준구멍,과대구멍,단슬롯의 모든방향에 대한 지압력 또는 장슬롯의 길이방향에 평행으로 작용하는 지압력의 경우"]
	  D["사용하중상태에서 볼트구멍의 변형을 설계에 고려할 필요가 있는 경우"]
    F([조합응력효과 무시])
    E["사용하중상태에서 볼트구멍의 변형을 설계에 고려할 필요가 없는 경우"]
    F["<img src='https://latex.codecogs.com/svg.image?R_n=1.2L_ctF_u\leq&space;2.4dtF_u'>---------------------------------------------------"]
    G["<img src='https://latex.codecogs.com/svg.image?R_n=1.5L_ctF_u\leq&space;3.0dtF_u'>-----------------------------------------------------"]
    H["장슬롯의 길이방향에 직각으로 작용하는 지압력의 경우"]
    I["<img src='https://latex.codecogs.com/svg.image?R_n=1.0L_ctF_u\leq&space;2.0dtF_u'>----------------------------------------------------"]
    J(["<img src='https://latex.codecogs.com/svg.image?R_n'>-----------------"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def design_strength_per_unit_length_of_fillet_weld(fOphiRn,fILc,fIt,fIFu,fId,fIuserdefined) -> bool:
        """지압강도 한계상태에 대한 볼트구멍에서 설계강도

        Args:
            fOphiRn (float): 볼트구멍에서 설계강도
            fILc (float): 구멍의 끝과 피접합재의 끝 또는 인접구멍의 끝까지의 거리
            fIt (float): 피접합재의 두께
            fIFu (float): 피접합재의 공칭인장강도
            fId (float): 볼트 공칭직경
            fIuserdefined (float): 사용자 선택

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법)  4.1.3.5 볼트구멍의 지압강도 (1)의 값
        """

        #표준구멍, 과대구멍, 단슬롯의 모든 방향에 대한 지압력 또는 장슬롯의 길이방향에 평행으로 작용하는 지압력의 경우 (사용하중상태에서 볼트구멍의 변형을 설계에 고려할 필요가 있는  경우) : fIuserdefined == 1
        #표준구멍, 과대구멍, 단슬롯의 모든 방향에 대한 지압력 또는 장슬롯의 길이방향에 평행으로 작용하는 지압력의 경우 (사용하중상태에서 볼트구멍의 변형을 설계에 고려할 필요가 없는  경우) : fIuserdefined == 2
        #장슬롯의 길이방향에 직각으로 작용하는 지압력의 경우 : fIuserdefined == 3

        if fIuserdefined == 1:
          fOphiRn = min((1.2)*fILc*fIt*fIFu, (2.4)*fId*fIt*fIFu)

        if fIuserdefined == 2:
          fOphiRn = min((1.5)*fILc*fIt*fIFu, (3.0)*fId*fIt*fIFu)

        if fIuserdefined == 3:
          fOphiRn = min((1.0)*fILc*fIt*fIFu, (2.0)*fId*fIt*fIFu)

        return fOphiRn


# 

