import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04060206_05 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Hyunjong Shin'  # 작성자명
    ref_code = 'KDS 24 14 21 4.6.2.6 (5)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-13'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '전단철근비'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.2 보
    4.6.2.6 전단철근
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
    A["전단철근비"];
    B["KDS 24 14 21 4.6.2.6 (5)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:길이 s내의 전단철근 단면적/];
		VarIn2[/입력변수:부재의 종방향 축을 따른 전단철근의 간격/];
		VarIn3[/입력변수: 부재의 복부 폭/]
		VarIn4[/입력변수: 전단철근과 부재축과의 각/]
			VarIn5[/입력변수: 전단철근비/]
			VarIn6[/입력변수: 28일 콘크리트 공시체의 기준 압축강도/]
		VarIn7[/입력변수: 철근의 기준항복강도/]
		VarOut1[/출력변수: 전단철근비/]
			VarOut1~~~VarIn1 & VarIn2 & VarIn3
			VarIn2~~~VarIn4 & VarIn5 & VarIn6 & VarIn7
		end

		Python_Class ~~~ Variable_def--->F--->E--->H-->I

		E["<img src='https://latex.codecogs.com/svg.image?\rho&space;_{v}=A_v/(sb_wsin\alpha)'>---------------------------------"]
		F["<img src='https://latex.codecogs.com/svg.image?\rho&space;_{v,min}=(0.08\sqrt{f_{ck}})/f_y'>---------------------------------"]

		H["<img src='https://latex.codecogs.com/svg.image?\rho&space;_{v}\geq\rho&space;_{v,min}'>---------------------------------"]

			I(["전단철근비"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Shear_reinforcement_ratio(fOrhov,fIAv,fIs,fIbw,fIalpha,fIrhovmin,fIfck,fIfy) ->float:
        """전단철근비
        Args:
             fOrhov (float): 전단철근비
             fIAv (float): 길이 s내의 전단철근 단면적
             fIs (float): 부재의 종방향 축을 따른 전단철근의 간격
             fIbw (float): 부재의 복부 폭
             fIalpha (float): 전단철근과 부재축과의 각
             fIrhovmin (float): 최소 전단철근비
             fIfck (float): 28일 콘크리트 공시체의 기준 압축강도
             fIfy (float): 철근의 기준항복강도

        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.6.2.6 전단철근에서 전단철근비(5)의 값
        """
        import math
        fIrhovmin = (0.08*fIfck)/fIfy
        fOrhov = max(fIAv/(fIs*fIbw*math.sin(math.radians(fIalpha))) , fIrhovmin)

        return fOrhov


# 

