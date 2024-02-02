import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241711_04060304_04(RuleUnit): # KDS241711_04060304_04

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 17 11 4.6.3.4 (4)' # 건설기준문서
    ref_date = '2022-02-25'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-10-13'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '횡방향철근의 총단면적'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.3 기둥
    4.6.3.4 소성힌지구역에서의 심부구속 횡방향철근량
    (4)
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
	A[사각형기둥에서 심부구속 횡방향철근의 총단면적]
	B["KDS 24 17 11 4.6.3.4(4)"]
	A ~~~ B
	end

	subgraph Variable_def
	VarOut[/출력변수: 횡방향철근의 총단면적/]
	VarIn1[/입력변수: 띠철근의 수직간격/]
	VarIn2[/입력변수: 수직간격이 a이고, 심부의 단면치수가 hc인 단면을 가로지르는 보강디철근을 포함하는 횡방향철근의 총단면적/]
	VarIn3[/입력변수: 띠철근 기둥의 고려하는 방향으로의, 띠철근 외측표면을 기준으로 한 심부의 단면치수/]
	VarOut ~~~ VarIn1 & VarIn3
	VarIn1 & VarIn3 ~~~ VarIn2
	end
	Python_Class ~~~ Variable_def ---> H ---> G
	G(["<img src='https://latex.codecogs.com/svg.image?&space;A_{sh}'>"])
	H["Ash=<img src='https://latex.codecogs.com/svg.image?MAX(0.30ah_c\frac{f_{ck}}{f_{yh}}(\frac{A_h}{A_c}-1),0.12ah_c\frac{f_{ck}}{f_{yh}})'>-----------------------------------------------------------"]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def gross_cross_sectional_area_transverse_rebar(fOAsh,fIa,fIhc,fIAc,fIAg,fIfck,fIfyh) -> float:
        """횡방향철근의 총단면적

        Args:
            fOAsh (float): 횡방향철근의 총단면적
            fIa (float): 띠철근의 수직간격
            fIhc (float): 띠철근 기둥의 고려하는 방향으로의, 띠철근 외측표면을 기준으로 한 신부의 단면 치수
            fIAc (float): 나선철근 외측표면을 기준으로 한 기둥 심부의 면적
            fIAg (float): 기둥의 총단면적
            fIfck (float): 콘크리트의 설계기준 압축강도
            fIfyh (float): 횡방향철근의 설계기준 항복강도

        Returns:
            float: fOAsh, 횡방향철근의 총단면적
        """

        fOAsh = max(0.30 * fIa * fIhc * fIfck / fIfyh * (fIAg / fIAc - 1), 0.12 * fIa * fIhc * fIfck / fIfyh)
        return fOAsh