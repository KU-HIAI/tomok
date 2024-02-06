import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241221_04030105_04 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 12 21 4.3.1.5 (4)' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-11-21'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '횡방향 재하위치'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.3 활하중
    4.3.1 차량활하중 : LL
    4.3.1.5 주거더를 설계하는 경우의 설계차량활하중
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
        A[표준트럭하중 최외측 차륜중심의 횡방향 재하위치];
        B["KDS 24 12 21 4.3.1.5 (4)"];
        A ~~~ B
        end
      subgraph Variable_def
    VarOut[/출력변수 : 횡방향 재하위치/];
    end
    Python_Class~~~Variable_def
    D["횡방향 재하위치 = 차도부분의 단부로부터 600mm"]
    E(["Pass or Fail"])
    Variable_def--->D--->E
        """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def the_width_of_a_loading_lane(fIlatpos) -> bool:
        """횡방향 재하위치

        Args:
            fIlatpos (float): 횡방향 재하위치

        Returns:
            float: 강교 설계기준(한계상태설계법)  4.3.1.1 재하차로의 수 (2) 의 통과여부
        """


        if fIlatpos == 600:
          return("Pass")
        else:
          return("Fail")


# 
