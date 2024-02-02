import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04060206_08 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 4.6.2.6 (8)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-19'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '전단철근의 최대 폭방향 간격'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.2 보
    4.6.2.6 전단철근
    (8)
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
    A["전단철근의 최대 폭방향 간격"];
    B["KDS 24 14 21 4.6.2.6 (8)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 단면의 유효깊이/];
		VarOut1[/출력변수: 전단철근의 최대 간격/]
		VarOut1~~~VarIn1
		end

		Python_Class ~~~ Variable_def--->F--->G

		F["<img src='https://latex.codecogs.com/svg.image?s_{max}=0.75d\leq&space;600mm'>---------------------------------"]


		G(["전단철근의 최대 폭방향 간격"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Maximum_spacing_of_shear_bars(fOsmax,fId) -> float:
        """전단철근의 최대 폭방향 간격
        Args:
             fOsmax (float): 전단철근의 최대 폭방향 간격
             fId (float): 단면의 유효깊이

        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.6.2.6 전단철근의 최대 간격(7)의 값
        """

        fOsmax = min(0.75*fId,600)
        return fOsmax


# 

