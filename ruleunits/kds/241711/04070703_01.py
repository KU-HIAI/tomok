import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241711_04070703_01(RuleUnit): # KDS241711_04070703_01

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 17 11 4.7.7.3 (1)' # 건설기준문서
    ref_date = '2022-02-25'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-11-16'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '등가정적 지진하중의 단위길이 당 하중강도'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.7 지진격리교량의 설계
    4.7.7 해석방법
    4.7.7.3 단일모드스펙트럼해석법
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
	A[등가정적 지진하중의 단위길이 당 하중강도];
	B["KDS 24 17 11 4.7.7.3(1)"];
	A ~~~ B
	end

	subgraph Variable_def
	VarOut[/출력변수: 등가정적 지진하중의 단위길이당 하중강도/];
	VarIn1[/입력변수: 상부구조의 단위길이당 고정하중/];
	VarIn2[/입력변수: 탄성지진응답계수/];
	VarOut ~~~ VarIn1 & VarIn2
	end
	Python_Class ~~~ Variable_def

	D["<img src='https://latex.codecogs.com/svg.image?p_e(x)=w(x)C_s'>-----------------------------------------"];

	E(["<img src='https://latex.codecogs.com/svg.image?p_e(x)'>"]);

	Variable_def --> D --> E
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def Load_intensity_per_unit_length_of_equivlent_static_seismic_load(fOpex,fIwx,fICs) -> float:
        """등가정적 지진하중의 단위길이 당 하중강도

        Args:
            fOpex (float): 등가정적 지진하중의 단위길이 당 하중강도
            fIwx (float): 상부구조의 단위길이 당 고정하중
            fICs (float): 탄성지진응답계수

        Returns:
            float: 교량내진설계기준(한계상태설계법) 4.7.7.3 단일모드스펙트럼해석법 (1)의 값
        """

        fOpex = fIwx * fICs
        return fOpex