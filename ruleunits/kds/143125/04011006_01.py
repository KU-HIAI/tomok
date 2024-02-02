import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_04011006_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 31 25 4.1.10.6' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-11-24'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '전단력과 압축력을 받는 패널존의 공칭강도'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.10 집중하중을 받는 플랜지와 웨브
    4.1.10.6 웨브 패널존 전단강도
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
	A([패널존의 설계강도])
	B["KDS 14 31 25 4.1.10.6(1)"]
	A ~~~ B
	end

	subgraph Variable_def
  VarOut[/출력변수: 전단력과 압축력을 받는 패널존의 설계강도/]
	VarIn1[/입력변수: 웨브 패널존 공칭강도/]
	VarIn2[/입력변수: 소요강도/]
	VarIn3[/입력변수: 기둥의 축방향 항복강도/]
	VarIn4[/입력변수: 기둥웨브의 명시된 최소항복강도/]
	VarIn5[/입력변수: 기둥의 높이/]
	VarIn6[/입력변수: 기둥웨브의 두께/]

	VarOut ~~~ VarIn1 & VarIn2 & VarIn3
	VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
	end

	Python_Class ~~~ Variable_def --> C --> D --> E
	E --Pass--> F
	E --Fail--> G
	F & G --> H
	C["골조 안정성에 대한 패널존 변형의 효과가 해석에서 고려되지않을때"]
	D["<img src='https://latex.codecogs.com/svg.image?P_r\leq&space;0.4P_c'>----------------------"]
	E["Pass or Fail"]
	F["<img src='https://latex.codecogs.com/svg.image?R_n=0.60F_yd_ct_w'>---------------------------------------------"]
	G["<img src='https://latex.codecogs.com/svg.image?R_n=0.60F_yd_ct_w(1.4-\frac{P_r}{P_c})'>----------------------------------------------------"]
	H(["<img src='https://latex.codecogs.com/svg.image?R_n'>"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Nominal_strength_of_panel_zones_subjected_to_shear_and_compressive_forces(fOphiRn,fIRn,fIPr,fIPc,fIFy,fIdc,fItw) -> bool:
        """전단력과 압축력을 받는 패널존의 공칭강도
        Args:
            fOphiRn (float): 전단력과 압축력을 받는 패널존의 설계강도
            fIRn (float): 웨브 패널존 공칭강도
            fIPr (float): 소요강도
            fIPc (float): 기둥의 축방향 항복강도
            fIFy (float): 기둥 웨브의 명시된 최소 항복강도
            fIdc (float): 기둥의 높이
            fItw (float): 기둥 웨브의 두께

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법)  4.1.10.6 웨브 패널존 전단강도 (1)의 값
        """
        if fIPr <= (0.4)*fIPc:
          fORn = 0.6 * fIFy * fIdc * fItw
        else:
          fORn = 0.6 * fIFy * fIdc * fItw * (1.4-fIPr/fIPc)

        return fORn


# 

