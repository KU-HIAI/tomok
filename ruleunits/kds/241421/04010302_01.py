import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04010302_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 4.1.3.2 (1)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-05'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '비틀림모멘트에 의해 유발되는 전단력'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.3.2 설계
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
    A["비틀림모멘트에 의해 유발되는 전단력"];
    B["KDS 24 14 21 4.1.3.2 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 작용 계수하중에 의한 비틀림모멘트/];
		VarIn2[/입력변수: 속빈 공간을 포함하는, 벽체의 중심선으로둘러싸인 면적/];
		VarIn3[/입력변수: 벽을 따라 흐르는 전단류/];
		VarIn4[/입력변수: i번 벽체의 전단응력/];
    VarIn5[/입력변수: 인접 벽체와의 교차점 사이의 거리로 정의된i번벽의측면길이/];
    VarIn6[/입력변수: 유효 벽두께/];
    VarIn7[/입력변수: i번 벽체의 전단응력/];
    VarIn8[/입력변수: 단면의 바깥쪽 둘레로 싸인 면적/];
    VarIn9[/입력변수: 단면 바깥쪽 둘레 길이/];
    VarIn10[/입력변수: 횡방향 철근의 피복 두께/];
		VarOut1[/출력변수: 비틀림모멘트에 의해 유발되는 전단력/];
		VarOut1~~~VarIn1 & VarIn2 & VarIn3 & VarIn4
		VarIn3~~~VarIn5 & VarIn6 & VarIn7 & VarIn8
		VarIn6~~~VarIn9 & VarIn10
		end
		Python_Class ~~~ Variable_def;
		Variable_def--->D--->C--->E
		C["<img src='https://latex.codecogs.com/svg.image?V_{u,i}=qy_i'>---------------------------------"]
		D["<img src='https://latex.codecogs.com/svg.image?q=v_it_i=\frac{T}{2A_o}i'>---------------------------------"]
		E(["비틀림모멘트에 의해 유발되는 전단력"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Shear_force_induced_by_torsional_moment(fOVui,fITu,fIAo,fIq,fIvi,fIyi,fIti,fIAcp,fIPcp,fItc) -> float:
        """비틀림모멘트에 의해 유발되는 전단력

        Args:
             fOVui (float): 비틀림모멘트에 의해 유발되는 전단력
             fITu (float): 작용 계수하중에 의한 비틀림모멘트
             fIAo (float): 속빈 공간을 포함하는, 벽체의 중심선으로 둘러싸인 면적
             fIq (float): 벽을 따라 흐르는 전단류
             fIvi (float): i번 벽체의 전단응력
             fIyi (float): 인접 벽체와의 교차점 사이의 거리로 정의된 i번 벽의 측면 길이
             fIti (float): 유효 벽두께
             fIAcp (float): 단면의 바깥쪽 둘레로 싸인 면적
             fIPcp (float): 단면 바깥쪽 둘레 길이
             fItc (float): 횡방향 철근의 피복 두께



        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.1.3.2 설계 (1)의 값
        """

        if fIvi == None or fIti == None:
          fIq = fITu / 2 / fIAo
        elif fITu == None or fIAo == None:
          fIq = fIvi * fIti
        else: fIq = max(fIvi * fIti, fITu / 2 / fIAo)

        fOVui = fIq * fIyi
        return fOVui


# 

