import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241221_041102_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 12 21 4.11.2 (1)' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-11-23'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = 'A의 제원'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.11 온도변화
    4.11.2 온도경사(TG)
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
        A[4.11-1에서 A의 제원];
        B["KDS 24 12 21 4.11.2 (2)"];
        A ~~~ B
        end
    subgraph Variable_def
    VarOut[/출력변수 : A/];
    VarIn1[/입력변수 : 두께/];
    end
    Python_Class~~~Variable_def
    D{"두께 &ge; 400mm 인 콘크리트 상부구조물의 경우"};
    E{"강재로 된 상부구조물인 경우"};
    F["A=300mm"];
    G["A = 실제 두께 - 100mm"];
    H["A=300mm"]
    I(["A"]);
    Variable_def--->D--Yes--->F--->I
    D--No--->G--->I
    Variable_def--->E--->H--->I
        """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def specifications_of_A(fOA,fIthick,fIuserdefine) -> float:
        """A의 제원

        Args:
            fOA (float): A
            fIthick (float): 두께
            fIuserdefine (float): 사용자가 정의한 값

        Returns:
            float: 강교 설계기준(한계상태설계법) 4.11.2 온도경사(TG) 의 값
        """

        #두께가 400mm 이상인 콘크리트 상부구조물의 경우 : fIuserdefine = 1
        #400mm 이하의 콘크리트단면의 경우 : fIuserdefine = 2
        #강재로 된 상부구조물인 경우 : fIuserdefine = 3

        if fIuserdefine == 1:
          fOA = 300
        elif fIuserdefine == 2:
          fOA = fIthick-100
        elif fIuserdefine == 3:
          fOA = 300

        return(fOA)


# 

