import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241011_010305_02(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 10 11 1.3.5(2)' # 건설기준문서
    ref_date = '2021-04-15'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-09-22'  # 건설기준문서 -> 디지털 건설기준 변환 기준일 (작성 년월)
    title = '기타 한계상태의 구조물의 중요도'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량 설계 일반사항(한계상태설계법)
    1. 일반사항
    1.3 설계원칙
    1.3.5 구조물의 중요도
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
     A[구조물중요도에 관련된 계수];
     B["KDS 24 10 11 1.3.5 (2)"];
     A ~~~ B
     end
    subgraph Variable_def
    VarIn1[/입력변수 : 구조물중요도에 관련된 계수/];
    end
    Python_Class~~~Variable_def
    D{"극한한계상태의 경우"};
    E{"구조물 중요도"};
    F["<img src='https://latex.codecogs.com/svg.image?\eta_{D}\geq&space;1.05'>"];
    G["<img src='https://latex.codecogs.com/svg.image?\eta_{D}=&space;1.00'>"];
    H["<img src='https://latex.codecogs.com/svg.image?\eta_{D}\geq&space;0.95'>"];
    I["<img src='https://latex.codecogs.com/svg.image?\eta_{D}=&space;1.00'>"];
    J(["pass or Fail"]);
    Variable_def--->D--Yes--->E--중요교량--->F--->J
    D--No--->I--->J
    E--일반교량--->G--->J
    E--상대적으로 중요도가 낮은 교량--->H--->J
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def Coefficients_related_to_structure_criticality(fIetaI,fIuserdefined) -> bool:
        """기타 한계상태의 구조물의 중요도

        Args:
            fIetaI (float) : 1.3.5에 규정된 구조물중요도에 관련된 계수
            fIuserdefined (float) : 사용자 선택

        Returns:
            bool: 교량 설계 일반사항(한계상태설계법) 1.3.5에 규정된 구조물중요도에 관련된 계수가 조건을 만족하는지 여부
        """

        if fIuserdefined == 1: #극한한계상태,중요 교량
           if fIetaI >= 1.05 :
            return "Pass"
           else:
            return "Fail"
        if fIuserdefined == 2: #극한한계상태,일반교량
           if fIetaI == 1.00 :
            return "Pass"
           else:
            return "Fail"
        if fIuserdefined == 3: #극한한계상태,상대적으로 중요도가 낮은 교량
           if fIetaI >= 0.95 :
            return "Pass"
           else:
            return "Fail"
        if fIuserdefined == 4: #기타한계상태
           if fIetaI == 1.00 :
            return "Pass"
           else:
            return "Fail"


