import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241221_0420_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 12 21 4.20.3' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-11-28'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '장대레일 종하중'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.20 장대레일 종하중 : LR
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
        A[한쪽 끝단에 고정 받침을 가지는 자갈도상이 있는 상부구조인 경우의 장대레일 종하중];
        B["KDS 24 12 21 4.20 (3)"];
        A ~~~ B
        end
    subgraph Variable_def
    VarOut[/출력변수 : 장대레일 종하중/];
    VarIn1[/입력변수 : 슬래브의 팽창이 고려될 수 있는 길이/];
    end
    Python_Class~~~Variable_def
    D{"레일 신축이음장치가 없을 경우"};
    E["<img src='https://latex.codecogs.com/svg.image?f_{v0}=\pm&space;3L'>"];
    F["<img src='https://latex.codecogs.com/svg.image?f_{v0}=\pm&space;500'>"];
    G(["장대레일 종하중"]);
    Variable_def--->D--Yes--->E--->G
    D--No--->F--->G
        """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def longitudinal_load_of_longitudinal_rail(fOfvo,fIL,fIuserdefine) -> float:
        """장대레일 종하중

        Args:
            fOfvo (float): 장대레일 종하중
            fIL (float): 슬래브의 팽창이 고려될 수 있는 길이
            fIuserdefine (float): 사용자가 정의한 값

        Returns:
            float: 강교 설계기준(한계상태설계법) 4.20 장대레일 종하중 : LR (3) 의 값
        """
        #레일신축이음장치가 없을 경우 : fIuserdefine = 1
        #구조물의 가동끝단에서 레일 신축이음이 있는 경우 : fIuserdefine = 2

        if fIuserdefine == 1:
          fOfvo = 3*fIL
        elif fIuserdefine == 2:
          fOfvo = 500
        return(fOfvo)


# 

