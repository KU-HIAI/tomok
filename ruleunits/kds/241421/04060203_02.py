import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04060203_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 14 21 4.6.2.3 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-19'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '정착 영역에 작용하는 힘'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.2 보
    4.6.2.3 단부 하부 철근의 정착
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
    A["인장력"];
    B["KDS 24 14 21 4.6.2.3 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:작용하는 계수하중에 의한 단면 전단력/];
		VarIn2[/입력변수: 철근의 인장력 분포의 이동거리/];
		VarIn3[/입력변수: 단면의 내부 모멘트 팔길이/]
		VarIn4[/입력변수: 축력/]
		VarOut1[/출력변수: 인장력/]
			VarOut1~~~VarIn1 & VarIn2 & VarIn3 & VarIn4
		end

		Python_Class ~~~ Variable_def--->F--->G

		F["<img src='https://latex.codecogs.com/svg.image?T=\frac{V_ua_l}{z}&plus;N_u'>---------------------------------"]


		G(["인장력"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def tensile_force(fOT,fIVu,fIai,fIz,fINu) ->float:
        """정착 영역에 작용하는 힘
        Args:
             fOT (float): 인장력
             fIVu (float): 작용하는 계수하중에 의한 단면 전단력
             fIai (float): 철근의 인장력 분포의 이동거리
             fIz (float): 단면의 내부 모멘트 팔길이
             fINu (float): 축력

        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.6.2.3(2)의 인장력의 값
        """
        fOT=fIVu*fIai/fIz+fINu
        return fOT


# 

