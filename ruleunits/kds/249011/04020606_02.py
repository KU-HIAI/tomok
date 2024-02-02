import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS249011_04020606_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 90 11 4.2.6.6 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-10-04'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = 'PTFE 최소두께'    # 건설기준명

    #
    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.6 받침 마찰요소의 설계
    4.2.6.6 미끄럼요소 설계
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
    A[PTFE 최소두께];
    B["KDS 24 90 11 4.2.6.6 (2)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarIn1[/입력변수: 두께/];
		VarIn2[/입력변수: 돌출높이/];
		VarIn3[/입력변수: PTFE의 직경/];

    VarIn1 & VarIn2 & VarIn3


    end

    Python_Class ~~~ Variable_def;
		Variable_def--->K & L


    K["<img src='https://latex.codecogs.com/svg.image?h=1.75&plus;\frac{L}{1200}\geq&space;2.2mm'>--------------------------------------------------------"];
		L["<img src='https://latex.codecogs.com/svg.image?2.2h\leq&space;t_{p}\leq&space;8.0mm'>--------------------------------------------------------"];
		K & L--->M
		M(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Thickness(fItp,fIh,fIL) -> bool:
        """PTFE 최소두께

        Args:
            fItp (float): 두께
            fIh (float): 돌출높이
            fIL (float): PTFE의 직경

        Returns:
            bool: 교량 기타시설설계기준 (한계상태설계법)  4.2.6.6 미끄럼요소 설계 (2)의 통과 여부
        """

        if 1.75 + fIL / 1200 >= 2.2:
          fIh = 1.75 + fIL / 1200
          2.2 * fIh <= fItp <= 8.0
          return "Pass"
        else:
           return "Fail"


# 

