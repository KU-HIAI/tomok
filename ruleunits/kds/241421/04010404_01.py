import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04010404_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 4.1.4.4 (1)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-12'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '소요 전단철근량'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.4 뚫림
    4.1.4.4 전단철근이 있는 슬래브 또는 기초판의 뚫림전단강도
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
    A["소요 전단철근량"];
    B["KDS 24 14 21 4.1.4.4 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 전단철근과 슬래브 평면 사이의 각/];
		VarIn2[/입력변수: 콘크리트가 기여하는 설계전단강도/];
		VarIn3[/입력변수: 슬래브의 평균 유효깊이/];
		VarIn4[/입력변수: 전단철근의 반경 방향 간격/];
		VarIn5[/입력변수: 기둥 주변의 각 위험단면의 전단철근의 면적/];
		VarIn6[/입력변수: 철근의 재료계수/];
		VarIn7[/입력변수: 전단 보강 철근의 유효항복강도/];
		VarIn8[/입력변수: 기본 위험단면 둘레길이/];
		VarIn9[/입력변수: 전단 보강 철근의 기준항복강도/];
		VarOut1[/출력변수: 소요 전단철근량/];
		VarOut1~~~VarIn1 & VarIn2 & VarIn3
		VarIn2~~~VarIn4 & VarIn5 & VarIn6
		VarIn5~~~VarIn7 & VarIn8 & VarIn9
		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C--->D--->E
		C["<img src='https://latex.codecogs.com/svg.image?\phi&space;_sf_{vy,ef}=250&plus;0.25d\leq\phi&space;_sf_{vy}'>---------------------------------"]
    D["<img src='https://latex.codecogs.com/svg.image?v_{csd}=0.75v_{cd}+(\frac{1.5d}{s_{r}})A_{v}\phi_{s}f_{vy,ef}(\frac{1}{u_{1}d})sin\alpha'>---------------------------------"]
		E(["소요 전단철근량"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Required_amount_of_shear_reinforcement(fOreqasr,fIVcd,fId,fISr,fIAv,fIphis,fIfvyef,fIu1,fIfvy,fIalpha) -> float:
        """소요 전단철근량

        Args:
             fOreqasr (float): 소요 전단철근량
             fIVcd (float): 콘크리트가 기여하는 설계전단강도
             fId (float): 슬래브의 평균 유효깊이
             fISr (float): 전단철근의 반경 방향 간격
             fIAv (float): 기둥 주변의 각 위험단면의 전단철근의 면적
             fIphis (float): 철근의 재료계수
             fIfvyef (float): 전단 보강 철근의 유효항복강도
             fIu1 (float): 기본 위험단면 둘레길이
             fIfvy (float): 전단 보강 철근의 기준항복강도
             fIalpha (float): 전단철근과 슬래브 평면 사이의 각




        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.1.4.4 전단철근이 있는 슬래브 또는 기초판의 뚫림전단강도 (1)의 값
        """

        if 250 + 0.25*fId <= fIphis * fIfvy:
          var1 = 250 + 0.25*fId
        else:
          var1 = fIphis * fIfvy

        fOreqasr = 0.75* fIVcd + (1.5*fId/fISr)*fIAv*var1*(1/fIu1/fId)*math.sin(math.radians(fIalpha))
        return fOreqasr


# 

