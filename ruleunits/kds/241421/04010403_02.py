import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04010403_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 4.1.4.3 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-12'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '기둥 기초판의 설계뚫림전단강도'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.4 뚫림
    4.1.4.3 전단철근이 없는 슬래브 또는 기둥 기초판의 뚫림전단강도
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
    A["기둥 기초판의 설계뚫림전단강도"];
    B["KDS 24 14 21 4.1.4.3 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 콘크리트 재료계수/];
		VarIn2[/입력변수: k/];
		VarIn3[/입력변수: 인장철근비/];
		VarIn4[/입력변수: 콘크리트 기준압축강도/];
		VarIn5[/입력변수: 단면의 유효깊이/];
		VarIn6[/입력변수: 기둥면에서부터 검토하는 위험단면까지의 거리/];
		VarIn7[/입력변수: 콘크리트 인장강도/];
		VarOut1[/출력변수: 기둥 기초판의 설계뚫림전단강도/];
		VarOut1~~~VarIn1 & VarIn2 & VarIn3
		VarIn2~~~VarIn4 & VarIn5 & VarIn6 & VarIn7
		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C--->E
		C["<img src='https://latex.codecogs.com/svg.image?v&space;_{d}=0.85\phi&space;_c\kappa(100\rho&space;_lf_ck)^{1/3}\frac{2d}{\alpha}\geq&space;0.4\phi&space;_cf_{ctk}\frac{2d}{a};'>---------------------------------"]
		E(["기둥 기초판의 설계뚫림전단강도"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Design_penetration_shear_strength_of_column_base_plate(fOVd,fIphic,fIk,fIrhol,fIfck,fId,fIa,fIfctk) -> float:
        """기둥 기초판의 설계뚫림전단강도

        Args:
             fOVd (float): 기둥 기초판의 설계뚫림전단강도
             fIphic (float): 콘크리트 재료계수
             fIk (float): 단면 유효깊이에 의해 결정되는 계수
             fIrhol (float): 인장철근비
             fIfck (float): 콘크리트 기준압축강도
             fId (float): 단면의 유효깊이
             fIa (float): 기둥면에서부터 검토하는 위험단면까지의 거리
             fIfctk (float): 콘크리트 인장강도




        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.1.4.3 전단철근이 없는 슬래브 또는 기둥 기초판의 뚫림전단강도 (2)의 값
        """

        if 0.85*fIphic*fIk*(100*fIrhol*fIfck)**(1/3)*2*fId/fIa >= 0.4*fIphic*fIfctk*2*fId/fIa:
          fOVd = 0.85*fIphic*fIk*(100*fIrhol*fIfck)**(1/3)*2*fId/fIa
        else:
          fOVd = 0.4*fIphic*fIfctk*2*fId/fIa
        return fOVd


# 

