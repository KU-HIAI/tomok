import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241011_02050207_01(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 10 11 2.5.2.7(1)' # 건설기준문서
    ref_date = '2021-04-15'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-09-26'  # 건설기준문서 -> 디지털 건설기준 변환 기준일 (작성 년월)
    title = '향후 확폭의 고려'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량 설계 일반사항(한계상태설계법)
    2. 조사 및 계획
    2.5 설게 목적
    2.5.2 사용성
    2.5.2.7 향후 확폭의 고려
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
     A[향후 확폭이 배제되지 않는 경우 외측거더의 내하력];
     B["KDS 24 10 11 2.5.2.7 (1)"];
     A ~~~ B
     end
    subgraph Variable_def
    VarIn1[/입력변수 : 외측거더의 내하력/];
    VarIn2[/입력변수 : 내측거더의 내하력/];
    end
    Python_Class~~~Variable_def
    D["외측거더 내하력&ge; 내측거더 내하력"];
    E(["Pass or Fail"]);
    Variable_def--->D--->E
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def Load_capacity_of_girder(fILoutgd,fILingd) -> bool:
        """설계강우강도가 조건을 만족하는지 여부

        Args:
            fILoutgd(float): 외측거더의 내하력.
            fILingd(float): 내측거더의 내하력.


        Returns:
            bool: 교량 설계 일반사항(한계상태설계법) 2.6.6(2) 설계강우강도가 조건을 만족하는지 여부
        """

        if fILoutgd>=fILingd:
           return 'Pass'
        else:
           return 'Fail'

