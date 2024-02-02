import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241011_04060102_04 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 10 11 4.6.1.2 (4)' # 건설기준문서
    ref_date = '2021-04-15'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-09-27'  # 건설기준문서 -> 디지털 건설기준 변환 기준일 (작성 년월)
    title = '곡선교 다중 강거더교'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량 설계 일반사항(한계상태설계법)
    4. 구조해석
    4.6 정적 해석
    4.6.1 평면 형상의 영향
    4.6.1.2 곡선교
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
     A[한 부재의 실제 편심량];
     B["KDS 24 10 11 4.6.1.2 (4)"];
     A ~~~ B
     end
    subgraph Variable_def
    VarIn1[/입력변수 : 실제 편심량/];
    VarIn2[/입력변수 : 절점 간격/];
    end
    Python_Class~~~Variable_def
    D["0.025X절점간격 &ge; 한부재의 실지 편심량"];
    E(["Pass or Fail"]);
    Variable_def--->D--->E
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def actual_eccentricity(fIeact,fIsnod) -> bool:
        """실제 편심량 KDS 24 10 11 4.6.1.2 (4)의 기준을 만족하는지 여부

        Args:
            fIeact (float): 실제 편심량.
            fIsnod (float): 절점 간격.

        Returns:
            bool: 교량 설계 일반사항(한계상태설계법) 실제 편심량 KDS 24 10 11 4.6.1.2 (4)의 기준을 만족하는지 여부
        """

        if fIsnod*0.25>=fIeact:
              return 'Pass'
        else:
              return 'Fail'


