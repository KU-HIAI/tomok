import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_040501_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 21 4.5.1 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '경량콘크리트의 최소피복두께'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.5 철근 상세
    4.5.1 일반
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
    A["경량콘크리트의 최소피복두께"];
    B["KDS 24 14 21 4.5.1 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut1["경량콘크리트의 최소피복두께"]
		VarIn1["콘크리트 최소피복두께"]
		VarOut1~~~VarIn1

		end
		Python_Class ~~~ Variable_def--->C--->F
		C["경량콘크리트의 최소피복두께=콘크리트 최소피복두께+5mm"]

		F(["경량콘크리트의 최소피복두께"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Minimum_cover_thickness_of_lightweight_concrete(fOmictlc,fImincoc) -> float:
        """경량콘크리트의 최소피복두께

        Args:
             fOmictlc (float): 경량콘크리트의 최소피복두께
             fImincoc (float): 콘크리트 최소피복두께

        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.5.1 일반 (2)의 값
        """

        fOdtcdev = 10
        return fOdtcdev


# 

