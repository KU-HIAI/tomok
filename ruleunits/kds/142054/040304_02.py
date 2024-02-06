import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS142054_040304_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 20 54 4.3.4 (2)' # 건설기준문서
    ref_date = '2021-02-18'  # 디지털 건설문서 작성일
    doc_date = '2023-12-11'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '공칭측면파열강도'    # 건설기준명

    #
    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.3 인장하중에 대한 설계 조건
    4.3.4 인장력을 받는 앵커의 콘크리트측면파열강도
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
    A[인장력을 받는 앵커 그룹의 콘크리트측면파열강도];
    B["KDS 14 20 54 4.3.4 (2)"];
    A ~~~ B
    end
	  subgraph Variable_def
    VarIn1[/입력변수 : 앵커 그룹의 공칭측면파열강도/];
    VarIn2[/입력변수 : 앵커의 유효묻힘깊이/];
    VarIn3[/입력변수 : 앵커 샤프트 중심부터 콘크리트 단부까지의 거리/];
    VarIn4[/입력변수 : 양 끝에 있는 앵커들 사이의 간격/];
    VarIn5[/입력변수 : 단일 헤드 앵커의 공칭측면파열강도/];
    VarIn1~~~VarIn4
    VarIn2~~~VarIn5
    VarIn3
    end
    Python_Class~~~Variable_def
    D{"<img src='https://latex.codecogs.com/svg.image?h_{ef}\geq&space;2.5c_{a1}'>이며 앵커간격<6ca1인 앵커그룹인 경우"};
    E["<img src='https://latex.codecogs.com/svg.image?N_{sbg}\leq\left(1+\frac{s}{6c_{a1}}\right)N_{sb}'>--------------------------------------------"];
    F(["Pass or Fail"]);
    Variable_def--->D--->E--->F
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Nominal_lateral_tear_strength(fIhef,fIcaone,fINsbg,fINsb,fIs) -> float:
        """공칭측면파열강도

        Args:
            fIhef (float): 앵커의 유효묻힘깊이
            fIcaone (float): 앵커 샤프트 중심부터 콘크리트 단부까지의 거리
            fINsbg (float): 앵커 그룹의 공칭측면파열강도
            fINsb (float): 공칭측면파열강도
            fIs (float): 양 끝에 있는 앵커들 사이의 간격


        Returns:
            float: 4.3.4 인장력을 받는 앵커의 콘크리트측면파열강도 (2)의 통과여부
        """

        if fIhef >= 2.5 * fIcaone :
          if fINsbg <= (1 + fIs/6/fIcaone) * fINsb :
            return "Pass"
          else:
            return "Fail"


