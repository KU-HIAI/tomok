import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS249011_04020609_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 90 11 4.2.6.9 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-10-05'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '압축응력'    # 건설기준명

    #
    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.6 받침 마찰요소의 설계
    4.2.6.9 설계검증
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
    A[압축응력 검토];
    B["KDS 24 90 11 4.2.6.9 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 극한한계상태에서의 작용 축력/];
		VarIn2[/입력변수: 압축강도/];
		VarIn3[/입력변수: 미끄럼면의 유효 접촉면적/];

		VarIn1 & VarIn2 & VarIn3


		end

		Python_Class ~~~ Variable_def;
		Variable_def--->K


		K["<img src='https://latex.codecogs.com/svg.image?N_{Sd}\leq\frac{f_{k}}{1.4}\times&space;A_{r}'>--------------------------------------------------------"];
		K --->M
		M(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Actuated_Axial_Force_At_Extreme_Limits(fINsd,fIfk,fIAr) -> bool:
        """압축응력

        Args:
            fINsd (float): 극한한계상태에서의 작용 축력
            fIfk (float): 압축강도
            fIAr (float): 미끄럼면의 유효 접촉면적

        Returns:
            bool: 교량 기타시설설계기준 (한계상태설계법) 4.2.6.9 설계검증 (2)의 통과 여부
        """

        if fINsd <= (fIfk/1.4)*fIAr :
           return 'Pass'
        else:
           return 'Fail'


# 
