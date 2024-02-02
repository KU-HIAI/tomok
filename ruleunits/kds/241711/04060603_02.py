import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241711_04060603_02(RuleUnit): # KDS241711_04060603_02

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 17 11 4.6.6.3 (2)' # 건설기준문서
    ref_date = '2022-02-25'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-10-17'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '원형기둥의 나선철근비'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.6 철근콘크리트 기둥의 연성도 내진설계
    4.6.6.3 심부구속 횡방향철근량
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
	B["KDS 24 17 11 4.6.6.3(2)"]
	A ~~~ B
	end

	subgraph Variable_def
	VarOut[/출력변수: 원형기둥의 나선철근비/]
	VarIn1[/입력변수: 나선철근의 단면적/]
	VarIn2[/입력변수: 나선철근 외측표면을 기준으로 한 콘크리트 심부의 단면 치수/]
	VarIn3[/입력변수: 나선철근의 수직간격/]
	VarIn4[/입력변수: 콘크리트의 설계기준 압축강도/]
	VarIn5[/입력변수: 횡방향철근의 설계기준 항복강도/]
	VarIn6[/입력변수: 축방향철근의 설계기준 항복강도/]
	VarIn7[/입력변수: 기둥의 총단면적/]
	VarIn8[/입력변수: 기둥의 계수축력/]
	VarIn9[/입력변수: 소요 곡률 연성도/]
	VarIn10[/입력변수: 기둥의 축방향철근비/]
	VarOut ~~~ VarIn1 & VarIn2 & VarIn3
	VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
	VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9
  VarIn8 ~~~ VarIn10
	end
	Python_Class ~~~ Variable_def --> D & G & H & I
	D --> E
	G & H & I --> F --> E
	D["원형기둥의 나선철근비 =<img src='https://latex.codecogs.com/svg.image?\rho&space;_s=\frac{4A_{sp}}{d_ss}'>"]
	E(["<img src='https://latex.codecogs.com/svg.image?\rho&space;_s'>"])
	F["쇼요나선 철근비= <img src='https://latex.codecogs.com/svg.image?\rho&space;_s=0.08\alpha\beta\frac{f_{ck}}{f_{yh}}&plus;\gamma&space;'>---------------------------------------------------------------------------"]
	G["<img src='https://latex.codecogs.com/svg.image?\alpha=3\left(\mu&space;_\phi&plus;1\right)\frac{P_u}{f_{ck}A_g}&plus;0.8\mu&space;_\phi-3.5'>------------------------------"]
	H["<img src='https://latex.codecogs.com/svg.image?\beta=\frac{f_y}{350}-0.12&space;'>-------------------------------"]
	I["<img src='https://latex.codecogs.com/svg.image?\gamma=0.1(\rho&space;_l-0.01)'>--------------------"]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def spiral_rebar_ratio_of_circular_column(fOrhos,fIAsp,fIds,fIs,fIfck,fIfyh,fIfy,fIAg,fIPu,fImuphi,fIrhol) -> float:
        """원형기둥의 나선철근비

        Args:
            fOrhos (float): 원형기둥의 나선철근비
            fIAsp (float): 나선철근의 단면적
            fIds (float): 나선철근 외측표면을 기준으로 한 콘크리트 심부의 단면 치수
            fIs (float): 나선철근의 수직간격
            fIfck (float): 콘크리트의 설계기준 압축강도
            fIfyh (float): 횡방향철근의 설계기준 항복강도
            fIfy (float): 축방향철근의 설계기준 항복강도
            fIAg (float): 기둥의 총단면적
            fIPu (float): 기둥의 계수축력
            fImuphpi (float): 소요 곡률 연성도
            fIrhol (float): 기둥의 축방향철근비

        Returns:
            float: fOrhos, 원형기둥의 나선철근비
        """

        fOrhos = 4 * fIAsp / (fIds * fIs)
        fIalpha = 3 * (fImuphi + 1) * fIPu / (fIfck * fIAg) + 0.8 * fImuphi - 3.5
        fIbeta = fIfy / 350 - 0.12
        fIgamma = 0.1 * (fIrhol - 0.01)
        fOrhos = 0.008 * fIalpha * fIbeta * fIfck / fIfyh + fIgamma
        return fOrhos