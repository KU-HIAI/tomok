import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241711_04060202_02(RuleUnit): # KDS241711_04060202_02

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 17 11 4.6.2.2 (2)' # 건설기준문서
    ref_date = '2022-02-25'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-10-05'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '항복유효 단면2차모멘트'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.2 교각의 해석 및 설계 강도
    4.6.2.2 교각의 휨강성
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
	A([교각의 휨강성])
	B["KDS 24 17 11 4.6.2.2(2)"]
	A ~~~ B
	end
	subgraph Variable_def
	VarOut[/출력변수: 항복유효 단면2차모멘트/]
	VarIn1[/입력변수: 교각의 총단면적/]
	VarIn2[/입력변수: 콘크리트의 설계기준압축강도/]
	VarIn3[/입력변수: 철근을 무시한 교각 전체 단면의 중심축에 대한 단면2차모멘트/]
	VarIn4[/입력변수: 계수 축력/]
	VarIn5[/입력변수: 교각의 축방향철근비/]
	VarOut ~~~ VarIn1 & VarIn3
	VarIn1 & VarIn3 ~~~ VarIn2 & VarIn4 & VarIn5
	end
	Python_Class ~~~ Variable_def --> D & F
	F--> E --> H
	D --> G
	D["<img src='https://latex.codecogs.com/svg.image?I_{y,eff}=(0.16&plus;12\rho&space;_l&plus;0.3\sqrt{\frac{P_u}{f_{ck}A_g}})I_g';width='30'/>--------------------------------------------------"]
	E["<img src='https://latex.codecogs.com/svg.image?EI_y=\frac{M_u}{\psi&space;_u}'------------------------------------>"]
	F["교각의 축방향철근이 항복할것으로 예상되는 경우"]
	G(["<img src='https://latex.codecogs.com/svg.image?I_{y,eff}'--------------->"])
	H(["<img src='https://latex.codecogs.com/svg.image?EI_y'>"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def yield_effective_area_moment_of_inertia(fOIyeff,fOEIy,fIAg,fIfck,fIIg,fIPu,fIrhol,fIMy,fIpsi) -> float:
        """항복유효 단면2차모멘트

        Args:
            fOIyeff (float): 항복유효 단면2차모멘트
            fOEIy (float): 축방향을 고려한 교각의 항복강성
            fIAg (float): 교각의 총단면적
            fIfck (float): 콘크리트의 설계기준압축강도
            fIIg (float): 철근을 무시한 교각 전체 단면의 중심축에 대한 단면2차모멘트
            fIPu (float): 계수 축력
            fIrhol (float): 교각의 축방향철근비
            fIMy (float): 축방향력을 고려한 교각의 항복 모멘트
            fIpsi (float): 축방향력을 고려한 교각의 항복곡률

        Returns:
            float: fOIyeff, 항복유효 단면2차모멘트, fOEIy, 축방향을 고려한 교각의 항복강성
        """
        fOIyeff = (0.16 + 12 * fIrhol + 0.3 * ((fIPu / (fIfck * fIAg)) ** 0.5)) * fIIg
        fOEIy = fIMy / fIpsi
        return (fOIyeff,fOEIy)