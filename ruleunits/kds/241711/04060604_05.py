import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241711_04060604_05(RuleUnit): # KDS241711_04060604_05

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 17 11 4.6.6.4 (5)' # 건설기준문서
    ref_date = '2022-02-25'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-10-19'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '전단철근에 의한 공칭전단강도'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.6 철근콘크리트 기둥의 연성도 내진설계
    4.6.6.4 전단 설계
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
	A[전단철근에 의한 공칭전단강도]
	B["KDS 24 17 11 4.6.6.4(5)"]
	A ~~~ B
	end

	subgraph Variable_def
	VarOut[/출력변수: 전단철근에 의한 공칭전단강도/]
	VarIn1[/입력변수: 전단철근으로 작용하는 띠철근의 단면적/]
	VarIn2[/입력변수: 나선철근 또는 원형 후프띠철근의 단면적/]
	VarIn3[/입력변수: 원형단면에 배근되는 보강띠철근의 단면적/]
	VarIn4[/입력변수: 심부 콘크리트 치수/]
	VarIn5[/입력변수: 띠철근 또는 나선철근의 항복강도/]
	VarIn6[/입력변수: 원형단면에 배근되는 보강디철근에서 갈고리 부분과 연장길이를 제외한 길이/]
	VarIn7[/입력변수: 띠철근 또는 나선철근의 수직간격/]
	VarOut ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4
  VarIn2  ~~~ VarIn5 & VarIn6 & VarIn7




	end
	Python_Class ~~~ Variable_def --> H & I & J
	H --> D
	I --> E
	J --> F
	D & E & F --> G
	D["<img src='https://latex.codecogs.com/svg.image?V_s=\frac{A_vf_{yh}D_c}{s}'>----------------------------------"]
	E["<img src='https://latex.codecogs.com/svg.image?V_s=\frac{\pi}{2}\frac{A_{sp}f_{yh}D_c}{s}'>---------------------------------------"]
	F["<img src='https://latex.codecogs.com/svg.image?&space;V_s=\frac{\sum&space;A_{ct}f_{yh}l_{ct}}{s}'>------------------------------------------"]
	G(["<img src='https://latex.codecogs.com/svg.image?&space;V_s'>------"])
	H["사각형 띠철근 단면"]
	I["원형단면의 나선철근 또는 원형 후프띠철근"]
	J["원형후프띠철근에 보강띠철근이 추가된 경우"]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def nominal_shear_strength_by_shear_rebar(fOVs,fIAv,fIAsp,fIAct,fIDc,fIfyh,fIlct,fIs,fIuserdefined) -> float:
        """전단철근에 의한 공칭전단강도

        Args:
            fOVs (float): 전단철근에 의한 공칭전단강도
            fIAv (float): 전단철근으로 작용하는 띠철근의 단면적
            fIAsp (float): 나선철근 또는 원형 후프띠철근의 단면적
            fIAct (float): 원형단면에 배근되는 보강띠철근의 단면적
            fIDc (float): 심부 콘크리트 치수
            fIfyh (float): 띠철근 또는 나선철근의 항복강도
            fIlct (float): 원형단면에 배근되는 보강디철근에서 갈고리 부분과 연장길이를 제외한 길이
            fIs (float): 띠철근 또는 나선철근의 수직간격
            fIuserdefined (float): 사용자 선택

        Returns:
            float: fOVs, 전단철근에 의한 공칭전단강도
        """

        import math
        if fIuserdefined == 1: #사각형 띠철근 단면
          fOVs = fIAv * fIfyh * fIDc / fIs
          return fOVs
        elif fIuserdefined == 2: #원형단면의 나선철근 또는 원형 후프띠철근
          fOVs = math.pi / 2 * fIAsp * fIfyh * fIDc / fIs
          return fOVs
        elif fIuserdefined == 3: #원형후프띠철근에 보강띠철근이 추가된 경우
          fOVs = fIAct * fIfyh * fIlct / fIs
          return fOVs