import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04010402_04 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 4.1.4.2 (4)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-07'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '받침점 반력이 편심으로 작용하는 경우 계수하중에 의한 최대전단응력에 곱하는 계수'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.4 뚫림
    4.1.4.2 뚫림전단 설계
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
    A["β"];
    B["KDS 24 14 21 4.1.4.2 (4)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 기본 위험단면 둘레길이/];
		VarIn2[/입력변수: 기둥 치수  c1과 c2의 비에 따른 계수/];
		VarIn3[/입력변수: 하중 편심방향과 평행한 방향의 기둥 치수/];
		VarIn4[/입력변수: 하중 편심방향과 직각인 방향의 기둥 치수/];
		VarIn5[/입력변수: 위험단면둘레 1차모멘트/];
		VarIn6[/입력변수: 편심 거리/];
		VarIn7[/입력변수: 계수하중에 의한 단면의 휨모멘트 값/];
		VarIn8[/입력변수: 원형 단면 기둥의 지름/];
    VarIn9[/입력변수: 계수하중에 의한 전단력/];
    VarIn10[/입력변수: 슬래브의 평균 유효깊이/];
		VarOut1[/출력변수: β/];
		VarOut1~~~VarIn1 & VarIn2 & VarIn3
		VarIn2~~~VarIn4 & VarIn5 & VarIn6
    VarIn5~~~VarIn7 & VarIn8 & VarIn9 & VarIn10
		end
		Python_Class ~~~ Variable_def;
		Variable_def---> C--사각형기둥인경우--->D--->E
		C{"기둥의 형상에 따라"}
		D["<img src='https://latex.codecogs.com/svg.image?\beta=1&plus;k\frac{M_u}{V_u}\cdot\frac{u_1}{W_1}'>---------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?W_1=\frac{c_1^2}{2}&plus;c_1c_2&plus;4c_2d&plus;16d^2&plus;2\pi&space;dc_1'>---------------------------------"]
		C--내부 원형 기둥인경우--->F--->G
		F["<img src='https://latex.codecogs.com/svg.image?e=\frac{M_u}{D}'>---------------------------------"]
		G["<img src='https://latex.codecogs.com/svg.image?\beta=1&plus;0.6\pi\frac{e}{D&plus;4d}'>---------------------------------"]
		E & G--->H
		H(["β"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def facor_of_eccentric_reaction_force_at_the_bearing(fObeta,fIVu,fIu1,fIk,fIc1,fIc2,fIw1,fId,fIe,fIMu,fID,fIuserdefined) -> float:
        """받침점 반력이 편심으로 작용하는 경우 계수하중에 의한 최대전단응력에 곱하는 계수

        Args:
             fObeta (float): 받침점 반력이 편심으로 작용하는 경우 계수하중에 의한 최대전단응력에 곱하는 계수
             fIVu (float): 계수하중에 의한 전단력
             fIu1 (float): 기본 위험단면 둘레길이
             fIk (float): 기둥 치수  c1과 c2의 비에 따른 계수
             fIc1 (float): 하중 편심방향과 평행한 방향의 기둥 치수
             fIc2 (float): 하중 편심방향과 직각인 방향의 기둥 치수
             fIw1 (float): 위험단면둘레 1차모멘트
             fId (float): 슬래브의 평균 유효깊이
             fIe (float): 편심 거리
             fIMu (float): 계수하중에 의한 단면의 휨모멘트 값
             fID (float): 원형 단면 기둥의 지름
             fIuserdefined (float): 사용자 선택



        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.1.4.2 뚫림전단 설계 (4)의 값
        """

        # 사각형 기둥의 경우 : fIuserdefined = 1
        # 내부 원형기둥인 경우 : fIuserdefined = 2
        if fIuserdefined == 1:
          if fIc1/fIc2 <=0.5:
            fIk = 0.45
          elif 0.5 < fIc1/fIc2 <= 1.0:
            fIk = 0.45 + 0.15/0.5*(fIc1/fIc2-0.5)
          elif 1.0 < fIc1/fIc2 <= 2.0:
            fIk = 0.6 + 0.10/1.0*(fIc1/fIc2-1.0)
          elif 2.0 < fIc1/fIc2 < 3.0:
            fIk = 0.70 + 0.10/1.0*(fIc1/fIc2-2.0)
          else:
            fIk = 0.80
          fIw1 = (fIc1**2)/2 + fIc1*fIc2 + 4*fIc2*fId + 16*fId**2 + 2*math.pi*fId*fIc1
          fObeta = 1+fIk*(fIMu/fIVu)*(fIu1/fIw1)
        elif fIuserdefined == 2:
          fIe = fIMu/fID
          fObeta = 1 + 0.6*math.pi*fIe/(fID+4*fId)
        return fObeta


# 

