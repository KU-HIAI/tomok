import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS142054_0401_07 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 20 54 4.1 (7)' # 건설기준문서
    ref_date = '2021-02-18'  # 디지털 건설문서 작성일
    doc_date = '2023-12-11'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '콘크리트 설계기준압축강도'    # 건설기준명

    #
    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.1 설계 일반
    (7)
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
    A[콘크리트 설계기준압축강도];
    B["KDS 14 20 54 4.1 (7)"];
    A ~~~ B
    end
	  subgraph Variable_def
    VarIn1[/입력변수 : 콘크리트 설계기준압축강도/];
    VarIn1
    end
    Python_Class~~~Variable_def

    D{"앵커설치 방법"};
    E["<img src='https://latex.codecogs.com/svg.image?&space;f_{ck}\leq70MPa'>--------------------"];
    F{"<img src='https://latex.codecogs.com/svg.image?&space;f_{ck}\leq55MPa'>--------------------"};
    G([PASS or Fail]);
    Variable_def--->D
    D--선설치--->E
    D--후설치--->F
    E & F--->G
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Design_standard_compressive_strength_of_concrete(fIfck,fIuserdefined) -> bool:
        """콘크리트 설계기준압축강도

        Args:
            fIfck (float): 콘크리트 설계기준압축강도
            fIuserdefined (float): 사용자 선택

        Returns:
            float: 콘크리트용 앵커 설계기준  4.1 설계 일반 (7)의 통과 여부

        """

        #선설치앵커: fIuserdefined = 1
        #후설치앵커: fIuserdefined = 2

        if fIuserdefined == 1:
          if fIfck <= 70 :
            return "Pass"
          else:
            return "Fail"

        elif fIuserdefined == 2:
          if fIfck <= 55 :
            return "Pass"
          else:
            return "Fail"


# 

