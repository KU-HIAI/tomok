import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04040403_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 21 4.4.4.3 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '설계 편차 허용량'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.4 내구성 및 피복두께
    4.4.4 콘크리트 피복두께
    4.4.4.3 설계 편차 허용량
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
    A["최소피복두께"];
    B["KDS 24 14 21 4.4.4.2 (3)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 최소피복두께/];
		VarIn2[/입력변수: 부착에 대한 요구사항을 만족하는 최소피복두께/];

		VarIn1 & VarIn2

		end
		Python_Class ~~~ Variable_def--->C--->F
		C["최소피복두께><img src='https://latex.codecogs.com/svg.image?t_{c,min,b}'>---------------------------------"]
		C~~~|KDS 24 14 21 table 4.4-3|C
		F(["Pass or fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Design_Deviation_Tolerance(fOdtcdev) -> float:
        """설계 편차 허용량

        Args:
             fOdtcdev (float): 설계 편차 허용량

        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.4.4.3 설계 편차 허용량 (2)의 값
        """

        fOdtcdev = 10
        return fOdtcdev


# 

