import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241011_010302_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 10 11 1.4 (2)' # 건설기준문서
    ref_date = '2021-04-15'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-09-21'  # 건설기준문서 -> 디지털 건설기준 변환 기준일 (작성 년월)
    title = '최소하중계수가 적용되는 하중의 경우 하중수정계수'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량 설계 일반사항(한계상태설계법)
    1. 일반사항
    1.3 설계원칙
    1.3.2 한계상태
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
     A[저항계수];
     B["KDS 24 10 11 1.3.2 (1)"];
     A ~~~ B
     end
    subgraph Variable_def
    VarIn1[/입력변수 : 계수저항/];
    VarIn2[/입력변수 : 하중효과/];
    VarIn3[/입력변수 : 하중계수/];
    VarIn4[/입력변수 : 1.3.3에 규정된 연성에 관련된 계수/];
    VarIn5[/입력변수 : 1.3.4에 규정된 여용성에 관련된 계수/];
    VarIn6[/입력변수 : 1.3.5에 규정된 구조물 중요도에 관련된 계수/];
    VarIn1~~~VarIn4
    VarIn2~~~VarIn5
    VarIn3~~~VarIn6
    end
    Python_Class~~~Variable_def
    D{"최대하중계수 OR 최소하중계수가 적용되는 하중의 경우"};
    E["<img src='https://latex.codecogs.com/svg.image?\eta_{i}=\eta_{D}\eta_{R}\eta_{I}(\geq&space;0.95)'>------------------------------------------"];
    F["<img src='https://latex.codecogs.com/svg.image?\eta_{i}=\frac{1}{\eta_{D}\eta_{R}\eta_{I}}(\leq&space;1.0)'>------------------------------------------"];
    G["<img src='https://latex.codecogs.com/svg.image?\sum \eta_{i}\gamma_{i}Q_{i}\leq R_{r}'>------------------------------------------"];
    H(["Pass or Fail"]);
    Variable_def--->D--최대하중계수--->E--->G
    D--최소하중계수--->F--->G--->H
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def coefficient_resistance_of_bridge(fIRr,fIQi,fIgammai,fIetaD,fIetaR,fIetaI) -> bool:
        """최소하중계수가 적용되는 하중의 경우 하중수정계수

        Args:
            fIRr (float): 계수저항.
            fIQi (float): 하중효과.
            fIgammai (float): 하중계수.
            fIetaD (float): 1.3.3에 규정된 연성에 관련된 계수.
            fIetaR (float): 1.3.4에 규정된 여용성에 관련된 계수.
            fIetaI (float): 1.3.5에 규정된 구조물중요도에 관련된 계수.

        Returns:
            bool: 교량 설계 일반사항(한계상태설계법) 계수저항이 1.3.2(1)의 기준을 만족하는지 여부
        """
        A=fIetaD*fIetaR*fIetaI
        B=1/fIetaD*fIetaR*fIetaI

        if A>= 0.95:
            if A*fIQi*fIgammai<=fIRr:
              return 'Pass'
            else:
              return 'Fail'

        elif B<= 1.0:
          if B*fIQi*fIgammai<=fIRr:
            return 'Pass'
          else:
            return 'Fail'
        else:
          return 'Fail'


