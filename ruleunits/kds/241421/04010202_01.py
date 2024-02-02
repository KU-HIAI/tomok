import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04010202_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 14 21 4.1.2.2 (1)' # 건설기준문서
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
    A["설계전단강도"];
    B["KDS 24 14 21 4.1.2.2 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut1[/출력변수: 설계전단강도/];
		VarIn1[/입력변수: 최소설계전단강도/];
		VarIn2[/입력변수: 콘크리트 재료계수/];
		VarIn3[/입력변수: 콘크리트 기준압축강도/];
		VarIn4[/입력변수: 콘크리트 인장강도/];
		VarIn5[/입력변수: 유효깊이 변화에 따른 전단강도 보정계수/];
		VarIn6[/입력변수: 단면유효깊이/];
		VarIn7[/입력변수: 철근비/];
		VarIn8[/입력변수: 단면의 복부폭/];
		VarIn9[/입력변수: 주인장 철근량/];
		VarIn10[/입력변수: 축응력/];
		VarIn11[/입력변수: 축력/];
		VarIn12[/입력변수: 철근비/];
		VarIn13[/입력변수: 단면적/];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
    VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9
		VarIn8 ~~~ VarIn10 & VarIn11 & VarIn12
		VarIn11 ~~~ VarIn13

		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C--->D

		C["<img src='https://latex.codecogs.com/svg.image?V_{cd}=[0.85\phi&space;_{c}\kappa(\rho&space;f_{ck})^{1/3}&plus;0.15f_{n}]b_{w}d'>---------------------------------"]
		D(["설계전단강도"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def designed_shear_strength(fOVcd,fIVcdmin,fIphic,fIfck,fIfctk,fIk,fId,fIrho,fIAs,fIbw,fIfn,fINu,fIAc) -> float:
        """설계전단강도

        Args:
             fOVcd (float): 설계전단강도
             fIVcdmin (float): 최소설계전단강도
             fIphic (float): 콘크리트 재료계수
             fIfck (float): 콘크리트 기준압축강도
             fIfctk (float): 콘크리트 인장강도
             fIk (float): 유효깊이 변화에 따른 전단강도 보정계수
             fId (float): 단면유효깊이
             fIrho (float): 철근비
             fIAs (float): 주인장 철근량
             fIbw (float): 단면의 복부폭
             fIfn (float): 축응력
             fINu (float): 축력
             fIAc (float): 단면적


        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.1.2.2 전단보강철근이 없는 부재 (1)의 값
        """
        fIk = min(1+(200/fId)**0.5, 2)
        fIrho = min(fIAs/fIbw/fId, 0.02)
        fIfn = min(fINu/fIAc, 0.2*fIphic*fIfck)
        fOVcd = (0.85*fIphic*fIk*(fIrho*fIfck)**(1/3)+0.15*fIfn)*fIbw*fId/1000
        fIVcdmin = (0.4*fIphic*fIfctk+0.15*fIfn)*fIbw*fId/1000

        if fOVcd >= fIVcdmin :
          return fOVcd
        else:
          fOVcd = fIVcdmin
          return fOVcd


# 

