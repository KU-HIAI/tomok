import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_04030302_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 14 31 25 4.3.3.2 (1)' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-12-05'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '응력상관계수'  # 건설기준명


    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.3 강관 간의 모멘트접합
    4.3.3.2 각형강관
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
        A[Title: 각형강관] ;
        B["KDS 14 31 25 4.3.3.2(1)"] ;
        A ~~~ B
        end

        subgraph Variable_def
          VarOut1[/출력변수: 응력상관계수/] ;
        end

        Python_Class ~~~ Variable_def
        C["주강관이 인장인 경우"] ;
        D(["<img src='https://latex.codecogs.com/svg.image?Q_{f}=1.0'>---------------------"]) ;


    Variable_def-->C-->D
        """

      # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def stress_correlation_coefficient(fOQf) -> float:
        """응력상관계수

        Args:
            fOQf (float): 응력상관계수
        Returns:
            float: 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.2 각형강관 (1) 의 값
        """
        fOQf = 1.0
        return(fOQf)


# 
