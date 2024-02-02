import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04010202_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 14 21 4.1.2.2 (3)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '설계전단강도'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.2 전단보강철근이 없는 부재
    (3)
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
    A["설계전단강도"];
    B["KDS 24 14 21 4.1.2.2 (3)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut1[/출력변수: 설계전단강도/];
		VarIn1[/입력변수: 최대설계전단강도/];
		VarIn2[/입력변수: 도콘크리트의 재료계수/];
		VarIn3[/입력변수: 유효깊이 변화에 따른 전단강도 보정계수/];
		VarIn4[/입력변수: 주인장 철근비/];
		VarIn5[/입력변수: 28일 콘크리트 공시체의 기준압축강도/];
		VarIn6[/입력변수: 단면의 유효깊이/];
		VarIn7[/입력변수: 받침점 내면으로부터의 거리/];
		VarIn8[/입력변수: 축응력/];
		VarIn9[/입력변수: 단면의 복부폭/];
		VarIn10[/입력변수: 콘크리트 압축강도 유효계수/];

		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
    VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9 & VarIn10


		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C--->D
		Variable_def--->E
		C["<img src='https://quicklatex.com/cache3/dd/ql_9256bf477cbe1ab06960b620370873dd_l3.png'>---------------------------------"]

		D["<img src='https://quicklatex.com/cache3/b2/ql_9e3b4879440b166609e2dbdd66992fb2_l3.png'>---------------------------------"]

		E["<img src='https://latex.codecogs.com/svg.image?V_{cd}=[0.85\phi&space;_{c}\kappa(\rho&space;f_{ck})^{1/3}(\frac{2d}{x})&plus;0.15f_{n}]b_{w}d'>---------------------------------"]
		F["<img src='https://latex.codecogs.com/svg.image?V_{cd}\leq&space;V_{cd,max}'>---------------------------------"]

		E & D--->F--->G
		G(["설계전단강도"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def designed_shear_strength(fOshestr,fIVcdmax,fIphic,fIk,fIfck,fIrho,fId,fIx,fIfn,fIbw,fInu) -> float:
        """설계전단강도

        Args:
             fOshestr (float): 설계전단강도
             fIVcdmax (float): 최대설계전단강도
             fIphic (float): 콘크리트의 재료계수
             fIk (float): 유효깊이 변화에 따른 전단강도 보정계수
             fIfck (float): 주인장 철근비
             fIrho (float): 28일 콘크리트 공시체의 기준압축강도
             fId (float): 단면의 유효깊이
             fIx (float): 받침점 내면으로부터의 거리
             fIfn (float): 축응력
             fIbw (float): 단면의 복부폭
             fInu (float): 콘크리트 압축강도 유효계수

        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.1.2.2 전단보강철근이 없는 부재 (3)의 값
        """

        fInu = 0.6*(1-fIfck/250)
        fOshestr = ((0.85*fIphic*fIk*(fIrho*fIfck)**(1/3))*(2*fId/fIx)+0.15*fIfn)*fIbw*fId
        fIVcdmax = 0.5*fIphic*fInu*fIfck*fIbw*fId

        if fOshestr >= fIVcdmax :
          return fOshestr
        else:
          fOshestr = fIVcdmax
          return fOshestr

        return(fOshestr)


# 

