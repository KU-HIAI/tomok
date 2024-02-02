import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04010202_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 14 21 4.1.2.2 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '전단강도'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.2 전단보강철근이 없는 부재
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
    A["설계전단강도"];
    B["KDS 24 14 21 4.1.2.2 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut1[/출력변수: 설계전단강도/];
		VarIn1[/입력변수: 단면2차모멘트/];
		VarIn2[/입력변수: 도심축 위쪽 단면의 도심축에 대한 단면1차모멘트/];
		VarIn3[/입력변수: 전달길이의 시작점부터 검토하는 단면까지의거리/];
		VarIn4[/입력변수: 전단길이의 시작점부터 검토하는 단면까지의 거리와 프리스트레싱 긴장재의 전달길이의 비/];
		VarIn5[/입력변수: 프리스트레싱 긴장재의 전달길이/];
		VarIn6[/입력변수: 축응력/];
		VarIn7[/입력변수: 축력/];
		VarIn8[/입력변수: 주인장 철근량/];
		VarIn9[/입력변수: 철근의 재료계수/];
		VarIn10[/입력변수: 철근의 기준항복강도/];
		VarIn11[/입력변수: 단면적/];

		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
    VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9
		VarIn8 ~~~ VarIn10 & VarIn11


		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C
			Variable_def--->D

		C & D---->E--->F
		C["<img src='https://latex.codecogs.com/svg.image?&space;f_{n}=(N_{u}-A_{s}\phi&space;_{s}f_{y})/A_{c}'>---------------------------------"]

		D["<img src='https://latex.codecogs.com/svg.image?\alpha&space;_{l}=l_{x}/l_{tp2}'>---------------------------------"]

		E["<img src='https://latex.codecogs.com/svg.image?V_{cd}=\frac{Ib_{w}}{Q}\sqrt{(\phi&space;_{c}f_{ctk})^{2}&plus;\alpha&space;_{l}f_{n}\phi&space;_{c}f_{ctk}}'>---------------------------------"]
		F(["설계전단강도"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def shear_strength(fOVcd,fII,fIQ,fIalphai,fIIx,fIlpt2,fIfn,fINu,fIAs,fIphis,fIfy,fIAc,flbw,fIphic,fIfctk) -> float:
        """전단강도

        Args:
             fOVcd (float): 전단강도
             fII (float): 단면2차모멘트
             fIQ (float): 도심축 위쪽 단면의 도심축에 대한 단면1차모멘트
             fIalphai (float): 전단길이의 시작점부터 검토하는 단면까지의 거리와 프리스트레싱 긴장재의 전달길이의 비
             fIIx (float): 전달길이의 시작점부터 검토하는 단면까지의거리
             fIlpt2 (float): 프리스트레싱 긴장재의 전달길이
             fIfn (float): 축응력
             fINu (float): 축력
             fIAs (float): 주인장 철근량
             fIphis (float): 철근의 재료계수
             fIfy (float): 철근의 기준항복강도
             fIAc (float): 단면적
             flbw (float): 단면의 복부 폭
             fIphic (float): 콘크리트 재료계수
             fIfctk (float): 콘크리트 인장강도

        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.1.2.2 전단보강철근이 없는 부재 (2)의 값
        """
        fIalphai = fIIx/fIlpt2
        fIfn = (fINu-fIAs*fIphis*fIfy)/fIAc
        fOVcd = fII*flbw/fIQ*(((fIphic*fIfctk)**2+fIalphai*fIfn*fIphic*fIfctk)**0.5)/1000
        return(fOVcd)


# 

