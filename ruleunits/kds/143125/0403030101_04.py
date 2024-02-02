import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_0403030101_04 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 14 31 25 4.3.3.1.1 (4)' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-12-05'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '압축 지강관벽의 세장비'  # 건설기준명


    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.3 강관 간의 모멘트접합
    4.3.3.1 원형강관
    4.3.3.1.1 적용한계
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
        A[Title: 적용한계] ;
        B["KDS 14 31 25 4.3.3.1.1(4)"] ;
        A ~~~ B
        end

        subgraph Variable_def
        VarOut1[/출력변수: 압축 지강관벽의 세장비/] ;
        VarIn1[/입력변수: 벽지름 두께비/] ;
        VarIn2[/입력변수: 강재의 탄성계수/] ;
        VarIn3[/입력변수: 주강관의 항복강도/] ;
        VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
        end

        Python_Class ~~~ Variable_def
        D["벽지름 두께비 ≤ <img src='https://latex.codecogs.com/svg.image?0.05E/F_{y}'>-----------"] ;

        Variable_def -->D-->F["압축 지강관벽의 세장비 = 벽지름 두께비"] --> Q(["압축 지강관벽의 세장비"])
        """

      # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def slenderness_ratio_of_compressed_branch_steel_pipe_wall(fOsrcbsp,fIwathra,fIE,fIFy) -> bool:
        """압축 지강관벽의 세장비

        Args:
            fOsrcbsp (float): 압축 지강관벽의 세장비
            fIwathra (float): 벽지름 두께비
            fIE (float): 강재의 탄성계수
            fIFy (float): 주강관의 항복강도

        Returns:
            bool : 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.1.1 적용한계 (4) 의 통과여부
        """
        fOsrcbsp = fIwathra
        if fOsrcbsp <= 0.05*fIE/fIFy:
          return("Pass")
        else:
          return("Fail")


# 

