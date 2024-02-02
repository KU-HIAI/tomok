import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_0403030201_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 14 31 25 4.3.3.2.1 (1)' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-12-04'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '지강관 각도'  # 건설기준명


    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.3 강관 간의 모멘트접합
    4.3.3.2 각형강관
    4.3.3.2.1 적용한계
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
        A[Title: 적용한계] ;
        B["KDS 14 31 25 4.3.3.2.1(1)"] ;
        A ~~~ B
        end

        subgraph Variable_def
          VarOut1[/출력변수: 지강관 각도/] ;
        end

        Python_Class ~~~ Variable_def
        E["θ≈90º"] ;

        Variable_def-->E-->Q(["θ"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def cast_steel_pipe_wall_thinning_equipment(fOphi) -> float:
        """주강관 벽세장비

        Args:
            fOphi (float): 지강관 각도

        Returns:
            float: 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.2.1 적용한계 (1) 의 값
        """
        fOphi = 90
        return(fOphi)


# 

