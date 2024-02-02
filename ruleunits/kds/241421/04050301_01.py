import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04050301_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 21 4.5.3.1 (1)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '현장타설 콘크리트에서 철근의 수평 순간격'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.5 철근 상세
    4.5.3 철근의 간격
    4.5.3.1 철근의 최소간격
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
    A["철근의 최소간격"];
    B["KDS 24 14 21 4.5.3.1 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;

		VarIn1["철근의 수평 순간격"]
		VarIn2["철근 공칭지름"]
		VarIn3["굵은 골재의 최대치수"]

		end
		Python_Class ~~~ Variable_def--->C & D & E--->F
		C["철근의 수평 순각격≥철근 공칭지름X1.5"]
		D["철근의 수평 순각격≥굵은 골재 최대치수X1.5"]
		E["철근의 수평 순각격≥40mm"]
		F(["Pass or fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Horizontal_moment_spacing_of_rebar_in_cast_in_place_concrete(fIhorins,fIrebnod,fImaxsco) -> float:
        """현장타설 콘크리트에서 철근의 수평 순간격

        Args:
             fIhorins (float): 철근의 수평 순간격
             fIrebnod (float): 철근 공칭지름
             fImaxsco (float): 굵은 골재의 최대치수

        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.5.3.1 철근의 최소간격 (1)의 값
        """

        if fIhorins >= max(fIrebnod*1.5, fImaxsco*1.5, 40):
          return "Pass"
        else:
          return "Fail"


# 

