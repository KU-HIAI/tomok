import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04020302_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 4.2.3.2 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-12'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '콘크리트 인장 영역 내의 소요 최소 철근량'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.2 사용한계상태
    4.2.3 균열
    4.2.3.2 최소철근량
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
    A["콘크리트 인장 영역 내의 소요 최소 철근량"];
    B["KDS 24 14 21 4.2.3.2 (2)"];
    A ~~~ B
    end
		subgraph Variable_def;
		VarIn1[/입력변수: 첫 균열 발생 직전 상태에서 계산된 콘크리트의인장영역단면적/];
		VarIn2[/입력변수: 첫 균열 발생 직후에 허용하는 철근의 인장응력/];
		VarIn3[/입력변수: 첫 균열이 발생할 때 유효한 콘크리트 인장강도/];
		VarIn4[/입력변수: 균열 발생 직전의 단면 내 응력 분포 상태를 반영하는계수/];
		VarIn5[/입력변수: 단면에 작용하는 평균 법선응력/];
		VarIn6[/입력변수: 단면에 작용하는 축력/];
		VarIn7[/입력변수: 단면 기준 깊이/];
		VarIn8[/입력변수: 단면 깊이/];
		VarIn9[/입력변수: 축력이 응력 분포에 미치는 영향을 반영하는 계수/];
		VarIn10[/입력변수: 플랜지에 균열이 처음 발생하기 직전에 부재전단면에작용하는휨모멘트와축력으로계산한플랜지의인장력/];
		VarIn11[/입력변수: 간접하중영향에 의해 부등 분포하는 응력의영향을반영하는계수/];
		VarIn12[/입력변수: 복부폭을 포함한 플랜지 너비/];
		VarOut1[/출력변수: 콘크리트 인장 영역 내의 소요 최소 철근량/]
		VarOut1~~~VarIn1 & VarIn2 & VarIn3 & VarIn4
		VarIn2~~~ VarIn5 & VarIn6 & VarIn7 & VarIn8
		VarIn5~~~ VarIn9 & VarIn10 & VarIn11 & VarIn12
		end
		Python_Class ~~~ Variable_def;
		Variable_def--->F
		C{"축력이 응력 분포에 미치는 영향을 반영하는 계수"}
		C--축력Nu가 압축력일때--->D
		D["철근의 인장응력≤<img src='https://latex.codecogs.com/svg.image?k_1=1.5'>---------------------------------"]
		C--축력Nu가 인장력일때--->E
		E["프리스트레스 강재의 응력≤<img src='https://latex.codecogs.com/svg.image?2h^*/3h'>---------------------------------"]
		F{단면 기준 깊이}
		G["<img src='https://latex.codecogs.com/svg.image?h^*=h'>---------------------------------"]
		H["<img src='https://latex.codecogs.com/svg.image?h^*=1.0m'>---------------------------------"]
		F--h<1.0일때--->G
		F--h≥1.0일때--->H
		G & H--->C
		I{"Kc=균열 발생 직전의 단면 내 응력 분포 상태를 반영하는 계수"}
		D -->I
		J["<img src='https://latex.codecogs.com/svg.image?K_c=1.0'>---------------------------------"]
		K["<img src='https://latex.codecogs.com/svg.image?0.4[1-\frac{f_n}{k(h/h^*)f_{ct}}]\leq&space;1'>---------------------------------"]
		L["<img src='https://latex.codecogs.com/svg.image?0.9\frac{N_{cr}}{A_{ct}f_{ct}}\geq&space;0.5'>---------------------------------"]
		I--순수인장을 받는 경우--->J
		I--휨과 축력을 받는 부재 복부--->K
		I--박스형이나 T형 단면 부재 플랜지--->L

		P{"k= 간접하중영향에 의해 부등 분포하는 응력의 영향을 반영하는 계수"}
		M["1.0"]
		N["0.65"]
		O["사이 값 보간"]
		Variable_def--->P
		P--면 깊이 또는 복부 폭을 포함한 플랜지 너비가 300mm 이하일 경우--->M
		P--단편 깊이 또는 복부 폭을 포함한 플랜지 너비가 800mm 이상일 경우--->N
		P--단편 깊이 또는 복부 폭을 포함한 플랜지 너비가 800mm 이상일 경우--->O
		E["<img src='https://latex.codecogs.com/svg.image?A_{s,min}=k_ckA_{ct}\frac{f_{ct}}{f_s}'>---------------------------------"]
		M & N & O & J & K & L--->E
		E--->Z
		Z(["콘크리트 인장 영역 내의 소요 최소 철근량"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Minimum_amount_of_rebar_required_within_concrete_tensile_area(fOAsmin,fIAct,fIfs,fIfct,fIkc,fIfn,fINu,fIhstar,fIk1,fINcr,fIk,fIh,fIflawid,fIuserdefined) -> float:
        """콘크리트 인장 영역 내의 소요 최소 철근량

        Args:
             fOAsmin (float): 콘크리트 인장 영역 내의 소요 최소 철근량
             fIAct (float): 첫 균열 발생 직전 상태에서 계산된 콘크리트의 인장 영역 단면적
             fIfs (float): 첫 균열 발생 직후에 허용하는 철근의 인장응력
             fIfct (float): 첫 균열이 발생할 때 유효한 콘크리트 인장강도
             fIkc (float): 균열 발생 직전의 단면 내 응력 분포 상태를 반영하는 계수
             fIfn (float): 단면에 작용하는 평균 법선응력
             fINu (float): 단면에 작용하는 축력
             fIhstar (float): 단면 기준 깊이
             fIk1 (float): 축력이 응력 분포에 미치는 영향을 반영하는 계수
             fINcr (float): 플랜지에 균열이 처음 발생하기 직전에 부재 전단면에 작용하는 휨모멘트와 축력으로 계산한 플랜지의 인장력
             fIk (float): 간접하중영향에 의해 부등 분포하는 응력의 영향을 반영하는 계수
             fIh (float): 단면 깊이
             fIflawid (float): 복부폭을 포함한 플랜지 너비
             fIuserdefined (float): 사용자 선택



        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.2.3.2 최소철근량 (2)의 값
        """

        if fIh < 1000:
          fIhstar = fIh
        else:
          fIhstar = 1000

        if fINu >= 0:
          fIk1 = 1.5
        else:
          fIk1 = 2 * fIhstar / ( 3 * fIh)

        if min(fIh, fIflawid) <= 300:
          fIk = 1.0
        elif max(fIh, fIflawid) >= 800:
          fIk = 0.65
        else:
          fIk = ((1.0-0.65)/(300-800)) * (min(fIh*1000, fIflawid) - 300) + 1.0

        # 순수인장을 받는 경우: fIuserdefined =1
        # 휨과 축력을 받는 부재 복부: fIuserdefined = 2
        # 박스형이나 T형 단면 부재 플랜지: fIuserdefined = 3
        if fIuserdefined == 1:
          fIkc = 1.0
        elif fIuserdefined == 2:
          fIkc = min(0.4 * ( 1 - fIfn/(fIk1 * fIh / fIhstar * fIfct)), 1)
        elif fIuserdefined == 3:
          fIkc = max(0.9 * fINcr / ( fIAct * fIfct ), 0.5)

        fOAsmin = fIkc * fIk * fIAct * fIfct / fIfs

        return fOAsmin


# 

