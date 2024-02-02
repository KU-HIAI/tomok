import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241711_04060602_06(RuleUnit): # KDS241711_04060602_06

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 17 11 4.6.6.2 (6)' # 건설기준문서
    ref_date = '2022-02-25'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-10-17'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '소요 곡률연성도'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.6 철근콘크리트 기둥의 연성도 내진설계
    4.6.6.2 소요연성도
    (6)
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
	A[소요 곡률연성도]
	B["KDS 24 17 11 4.6.6.2(6)"]
	A ~~~ B
	end

	subgraph Variable_def
	VarOut[/출력변수: 소요 곡률연성도/]
	VarIn1[/입력변수: 고려하는 방향으로의 단면 최대두께/]
	VarIn2[/입력변수: 기둥 형상비의 기준이 되는 기둥길이/]
	VarOut ~~~ VarIn1 & VarIn2
	end
	Python_Class ~~~ Variable_def --> D --> E
	D["<img src='https://latex.codecogs.com/svg.image?\mu_\phi=\frac{u_\Delta-0.5\left\{0.7&plus;0.75\left(\frac{h}{L_s}\right)\right\}}{0.13\left(1.1&plus;\frac{h}{L_s}\right)}'>------------------------------------------"]
	E(["<img src='https://latex.codecogs.com/svg.image?\mu_\phi'>"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def required_curvature_ductility(fOmuphi,fImudelta,fIh,fILs) -> float:
        """소요 곡률연성도

        Args:
            fOmuphi (float): 소요 곡률연성도
            fImudelta (float): 소요 변위연성도
            fIh (float): 고려하는 방향으로의 단면 최대 두께
            fILs (float): 기둥 형상비의 기준이 되는 기둥길이

        Returns:
            float: fOmuphi, 소요 곡률연성도
        """

        fOmuphi = (fImudelta - 0.5 * (0.7 + 0.75 * fIh / fILs))/(0.13 * (1.1 + fIh / fILs))
        return fOmuphi