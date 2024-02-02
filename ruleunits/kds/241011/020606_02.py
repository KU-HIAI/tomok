import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241011_020606_02(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 10 11 2.6.6(2)' # 건설기준문서
    ref_date = '2021-04-15'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-09-26'  # 건설기준문서 -> 디지털 건설기준 변환 기준일 (작성 년월)
    title = '설계강우강도'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량 설계 일반사항(한계상태설계법)
    2. 조사 및 계획
    2.6 수문 및 수리
    2.6.6 도로배수
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
     A[교량바닥판 배수에 적용하는 설계강우강도];
     B["KDS 24 10 11 2.6.6 (2)"];
     A ~~~ B
     end
    subgraph Variable_def
    VarIn1[/입력변수 : 설계강우강도/];
    VarIn2[/입력변수 : 인접도로의 포장 배수설계에 적용하는 설계강우강도/];
    end
    Python_Class~~~Variable_def
    C{"발주자가 규정하지 않는 경우"};
    D["설계강우강도 &ge; 인접도로의 포장 배수설계에 적용하는 설계강우강도"];
    E(["Pass or Fail"]);
    Variable_def--->C--->D--->E
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def Design_rainfall_intensity(fIraind,fIrainad) -> bool:
        """설계강우강도가 조건을 만족하는지 여부
        Args:
            fIraind(float): 설계강우강도.
            fIrainad(float): 인접도로의 포장 배수설계에 적용하는 설계강우강도.


        Returns:
            bool: 교량 설계 일반사항(한계상태설계법) 2.6.6(2) 설계강우강도가 조건을 만족하는지 여부
        """

        if fIraind>=fIrainad:
           return 'Pass'
        else:
           return 'Fail'


