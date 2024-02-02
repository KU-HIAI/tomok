import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS115015_04010101_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 11 50 15 4.1.1.1 (2)' # 건설기준문서
    ref_date = '2021-05-12'  # 디지털 건설문서 작성일
    doc_date = '2023-09-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '말뚝기초의 축방향 허용변위'    # 건설기준명

    #
    description = """
    깊은기초 설계기준(일반설계법)
    4. 설계
    4.1 말뚝기초
    4.1.1 말뚝의 축방향 지지력과 변위
    4.1.1.1 말뚝기초의 축방향 허용지지력과 허용변위
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
    A[말뚝기초의 축방향 허용변위];
    B["KDS 11 50 15 4.1.1.1 (2)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarIn1[/입력변수: 말뚝기초의 축방향 허용변위/];
    VarIn2[/입력변수: 상부 구조물의 허용변위량/] ;
    VarIn1 ~~~ VarIn2
    end

    Python_Class ~~~ Variable_def
    D["말뚝기초의 축방향 허용변위 < 상부 구조물의 허용변위량"];

    Variable_def --> D
    D --> E([PASS or Fail]);
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def longitudinal_allowable_displacement_of_pilefoundation(fIladisp,fIaldiss) -> bool:
        """말뚝기초의 축방향 허용변위

        Args:
            fIladisp (float): 말뚝기초의 축방향 허용변위
            fIaldiss (float): 상부구조물의 허용변위량

        Returns:
            bool: 깊은기초 설계기준(일반설계법)  4.1.1.1 말뚝기초의 축방향 허용지지력과 허용변위 (2)의 통과 여부
        """

        if fIladisp <= fIaldiss:
          return "Pass"

        else:
          return "Fail"


# 

