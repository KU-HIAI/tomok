import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241711_04060304_02(RuleUnit): # KDS241711_04060304_02

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 17 11 4.6.3.4 (2)' # 건설기준문서
    ref_date = '2022-02-25'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-10-13'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '원형기둥의 나선철근비'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.3 기둥
    4.6.3.4 소성힌지구역에서의 심부구속 횡방향철근량
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
	A[원형기둥의 나선철근비]
	B["KDS 24 17 11 4.6.3.4(2)"]
	A ~~~ B
	end

	subgraph Variable_def
	VarOut1[/출력변수: 원형기둥의 나선철근비/]

  VarIn1[/입력변수: 나선철근의 단면적/]
	VarIn2[/입력변수: 나선철근 외측표면을 기준으로 한 콘크리트 심부의 단면 치수/]
	VarIn3[/입력변수: 나선철근의 수직간격/]
	VarIn4[/입력변수: 나선철근 외측표면을 기준으로 한 기둥 심부의 면적/]
	VarIn5[/입력변수: 기둥의 총단면적/]
	VarIn6[/입력변수: 콘크리트의 설계기준 압축강도/]
	VarIn7[/입력변수: 횡방향철근의 설계기준 항복강도/]
	end
  VarOut1 ~~~ VarIn1 & 	VarIn2 & 	VarIn3
	VarIn2 ~~~ 	VarIn4 & 	VarIn5 & 	VarIn6 	& 	VarIn7

	Python_Class ~~~ Variable_def -->D
		D["<img src='https://latex.codecogs.com/svg.image?\rho&space;_{s}=\frac{4A_{sp}}{d_{s}s}'>--------------------"]
    G["원형기둥의 나선철근비 =\n max (<img src='https://latex.codecogs.com/svg.image?\rho&space;_{s}=0.45(\frac{A_{g}}{A_{c}}-1)\frac{f_{ck}}{f_{yh}}'>-----------------------------------------,<img src='https://latex.codecogs.com/svg.image?\rho&space;_{s}=0.12\frac{f_{ck}}{f_{yh}}'>))"];
		H(["원형기둥의 나선철근비"])
		D-->G-->H
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def spiral_rebar_ratio_of_circular_column(fOrhos,fIAsp,fIds,fIs,fIAc,fIAg,fIfck,fIfyh) -> float:
        """원형기둥의 나선철근비

        Args:
            fOrhos (float): 원형기둥의 나선철근비
            fIAsp (float): 나선철근의 단면적
            fIds (float): 나선철근 외측표면을 기준으로 한 콘크리트 심부의 단면 치수
            fIs (float): 나선철근의 수직 간격
            fIAc (float): 나선철근 외측표면을 기준으로 한 기둥 심부의 면적
            fIAg (float): 기둥의 총단면적
            fIfck (float): 콘크리트의 설계기준 압축강도
            fIfyh (float): 횡방향철근의 설계기준 항복강도

        Returns:
            float: fOrhos, 원형기둥의 나선철근비
        """

        fOrhos = 4 * fIAsp / (fIds * fIs)
        fOrhos = max(0.45 * ((fIAg / fIAc) - 1) * (fIfck / fIfyh), 0.12 * fIfck / fIfyh)
        return fOrhos