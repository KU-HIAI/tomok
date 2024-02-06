import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS142054_040303_04 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 14 20 54 4.3.3 (4)' # 건설기준문서
    ref_date = '2021-02-18'  # 디지털 건설문서 작성일
    doc_date = '2023-09-27'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '단일 헤드스터드 또는 헤드볼트의 뽑힘강도'    # 건설기준명

    #
    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.3 인장하중에 대한 설계 조건
    4.3.3 인장력을 받는 선설치앵커, 후설치 확장앵커 및 언더컷앵커의 뽑힘강도
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
    A[뽑힘강도];
    B["KDS 14 20 54 4.3.3 (4)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarIn1[/입력변수 : 인장을 받는 단일 헤드스터드 또는 헤드볼트의 뽑힘강도/];
    VarIn2[/입력변수 : 스터드 또는 앵커볼트의 헤드 지압면적/];
    VarIn3[/입력변수 : 콘크리트의 설계기준압축강도/];
    VarIn1
    VarIn1 ~~~ VarIn2 & VarIn3
    end
    Python_Class~~~Variable_def
    D{"인장을 받는 단일 헤드스터드 또는 헤드볼트의 경우"};
    E["<img src='https://latex.codecogs.com/svg.image?N_{p}\leq&space;8A_{brg}f_{ck}'>-------------------------------"];
    F(["Pass of Fail"]);
    Variable_def--->D--->E--->F
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def pullout_strength_of_a_single_head_stud_or_head_bolt(fINp,fIAbrg,fIfck) -> bool:
        """단일 헤드스터드 또는 헤드볼트의 뽑힘강도

        Args:
            fINp (float): 단일 헤드스터드 또는 헤드볼트의 뽑힘강도
            fIAbrg (float): 스터드 또는 앵커볼트의 헤드 지압 면적
            fIfck (float): 콘크리트의 설계기준압축강도

        Returns:
            bool: 콘크리트용 앵커 설계기준  4.3.3 인장력을 받는 선설치앵커, 후설치 확장앵커 및 언더컷앵커의 뽑힘강도 (4)의 통과여부
        """

        if fINp <= 8 * fIAbrg * fIfck:
          return "Pass"
        else:
          return "Fail"


