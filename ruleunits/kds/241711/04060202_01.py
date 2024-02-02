import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241711_04060202_01(RuleUnit): # KDS241711_04060202_01

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 17 11 4.6.2.2 (1)' # 건설기준문서
    ref_date = '2022-02-25'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-09-26'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '축방향력을 고려한 교각의 항복강성'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.2 교각의 해석 및 설계 강도
    4.6.2.2 교각의 휨강성
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
	A([교각의 휨강성])
	B["KDS 24 17 11 4.6.2.2 (1)"]
	A ~~~ B
	end

	subgraph Variable_def
	VarOut[/출력변수: 축방향력을 고려한 교각의 항복강성/]
	VarIn1[/입력변수: 축방향력을 고려한 교각의 항복모멘트/]
	VarIn2[/입력변수: 축방향력을 고려한 교각의 항복곡률/]
	VarOut ~~~ VarIn1 & VarIn2
	end
	Python_Class ~~~ Variable_def --> D
 	D["<img src='https://latex.codecogs.com/svg.image?EI_y=\frac{M_u}{\psi&space;_u}'------------------------------------>"]
	E(["<img src='https://latex.codecogs.com/svg.image?EI_{y}'>--------"])

	D --> E
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def yield_stiffness_of_pier_axial_direction(fOEIy,fIMy,fIpsi) -> float:
        """축방향력을 고려한 교각의 항복강성

        Args:
            fOEIy (float): 축방향을 고려한 교각의 항복강성
            fIMy (float): 축방향을 고려한 교각의 항복모멘트
            fIpsi (float): 축방향력을 고려한 교각의 항복곡률

        Returns:
            float: fOEIy, 축방향을 고려한 교각의 항복강성
        """
        fOEIy = fIMy / fIpsi
        return fOEIy