import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241011_010303_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 10 11 1.3.3 (3)' # 건설기준문서
    ref_date = '2021-04-15'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-09-21'  # 건설기준문서 -> 디지털 건설기준 변환 기준일 (작성 년월)
    title = '극한한계상태의 연성'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량 설계 일반사항(한계상태설계법)
    1. 일반사항
    1.3 설계원칙
    1.3.3 연성
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
     A[연성에 관련된 계수];
     B["KDS 24 10 11 1.3.3 (3)"];
     A ~~~ B
     end
    subgraph Variable_def
    VarIn1[/입력변수 : 연성에 관련된 계수/];
    end
    Python_Class~~~Variable_def
    D{"극한한계상태의 경우"};
    E{"연성 분류"};
    F["<img src='https://latex.codecogs.com/svg.image?\eta_{D}\geq&space;1.05'>"];
    G["<img src='https://latex.codecogs.com/svg.image?\eta_{D}=&space;1.00'>"];
    H["<img src='https://latex.codecogs.com/svg.image?\eta_{D}\geq&space;0.95'>"];
    I["<img src='https://latex.codecogs.com/svg.image?\eta_{D}=&space;1.00'>"];
    J(["pass or Fail"]);
    Variable_def--->D--Yes--->E--비연성 구성요소 및 연결부--->F--->J
    D--No--->I--->J
    E--이 코드에 부합하는 통상적인 설계 및 상세--->G--->J
    E--이 코드가 요구하는 것 이외의 추가 연성보강장치가 규정되어 있는 구성요소 및 연결부--->H--->J
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def Factors_related_to_ductility(fIetaD,fIuserdefined) -> bool:
        """극한한계상태의 연성

        Args:
            fIetaD (float): 1.3.3에 규정된 연성에 관련된 계수
            fIuserdefined (float): 사용자 선택

        Returns:
            bool: 교량 설계 일반사항(한계상태설계법) 1.3.3(3) 연성계수가 조건을 만족하는지 여부
        """
        if fIuserdefined == 1: #극한한계상태,비연성구성요소및연결부
           if fIetaD >= 1.05 :
            return "Pass"
           else:
            return "Fail"
        if fIuserdefined == 2: #극한한계상태,이코드에부합하는통상적인설계및상세
           if fIetaD == 1.00 :
            return "Pass"
           else:
            return "Fail"
        if fIuserdefined == 3: #극한한계상태,이코드가요구하는것이외의추가연성보강장치가규정되어있는구성요소및연결부
           if fIetaD >= 0.95 :
            return "Pass"
           else:
            return "Fail"
        if fIuserdefined == 4: #기타한계상태
           if fIetaD == 1.00 :
            return "Pass"
           else:
            return "Fail"


