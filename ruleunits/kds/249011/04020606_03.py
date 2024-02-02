import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS249011_04020606_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 90 11 4.2.6.6 (3)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-10-04'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '유도궤도'    # 건설기준명

    #
    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.6 받침 마찰요소의 설계
    4.2.6.6 미끄럼요소 설계
    (3)
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
    A[유도궤도];
    B["KDS 24 90 11 4.2.6.6 (3)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarIn1[/입력변수: 미끄럼요소간의 틈/];
		VarIn2[/입력변수: PTFE의 직경/];

    VarIn1 & VarIn2


    end

    Python_Class ~~~ Variable_def;
		Variable_def--->K--->M


    K["<img src='https://latex.codecogs.com/svg.image?c\leq&space;1.0mm&plus;\frac{L}{1000}mm'>--------------------------------------------------------"];

    M(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Gaps_Between_Sliding_Elements(fIc,fIL) -> bool:
        """유도궤도

        Args:
            fIc (float): 미끄럼요소간의 틈
            fIL (float): PTFE의 직경

        Returns:
            bool: 교량 기타시설설계기준 (한계상태설계법)  4.2.6.6 미끄럼요소 설계 (3)의 통과 여부
        """

        if fIc <= 1.0+fIL/1000 :
           return 'Pass'
        else:
           return 'Fail'


# 

