import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS171000_04020104_04 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 17 10 00 4.2.1.4 (4)' # 건설기준문서
    ref_date = '2018-12-06'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-09-15'  # 건설기준문서 -> 디지털 건설기준 변환 기준일 (작성 년월)
    title = '유효수평지반가속도'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    내진설계 일반
    4. 설계
    4.2 지진재해
    4.2.1 지반운동
    4.2.1.4 설계지반운동의 특성 표현
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
     A[유효수평지반가속도];
     B["KDS 17 10 00 4.2.1.4 (4)"];
     A ~~~ B
     end
   subgraph Variable_def
   VarOut1[/출력변수 : 유효수평지반가속도/];
   VarIn1[/입력변수 : 행정구역에 따라 결정한 값/];
   end
   Python_Class~~~Variable_def

   D{"국가지진 위험지도 이용"};
   E["S"]
   F["S &ge; 행정구역에 따라 결정한 값x0.8"];
   G(["유표수평지반가속도"]);
   Variable_def--->D--Yes--->E--->G
   D--No--->F--->G
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def effective_lateral_ground_acceleration(fIS,fldivis) -> bool:
        """유효수평지반가속도
        Args:
            fIS (float): 유효수평지반가속도.
            fIdivis (float): 행정구역에 따라 결정한 값.
        Returns:
            bool: 내진설계 일반  4.2.1.4 설계지반운동의 특성 표현 (4)의 통과 여부
        """
        A = fIS
        B = fIdivis * 0.8

        if A >= B:
            return 'Pass'
        else:
            return 'Fail'


