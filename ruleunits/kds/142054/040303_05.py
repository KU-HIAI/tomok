import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS142054_040303_05 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 14 20 54 4.3.3 (5)' # 건설기준문서
    ref_date = '2021-02-18'  # 디지털 건설문서 작성일
    doc_date = '2023-09-27'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '단일 갈고리볼트가 인장력을 받는 경우 뽑힘강도'    # 건설기준명

    #
    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.3 인장하중에 대한 설계 조건
    4.3.3 인장력을 받는 선설치앵커, 후설치 확장앵커 및 언더컷앵커의 뽑힘강도
    (5)
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
    B["KDS 14 20 54 4.3.3 (5)"];
    A ~~~ B
    end
	  subgraph Variable_def
	  VarIn1[/입력변수 : 단일 갈고리볼트가 인장력을 받는 경우 뽑힘강도/];
	  VarIn2[/입력변수 : 콘크리트의 설계기준압축강도/];
	  VarIn3[/입력변수 : J 또는 L볼트 샤프트의 안쪽면부터 J또는 L볼트의 바깥쪽 끝까지거리/];
	  VarIn4[/입력변수 : 앵커의 외경, 혹은 헤드스터드, 헤드볼트, 갈고리형볼트의 샤프트지름/];
	  VarIn1 ~~~ VarIn3
	  VarIn2 ~~~ VarIn4

	  end
	  Python_Class~~~Variable_def
	  E{"단일 갈고리볼트가 인장력을 받는 경우"};
	  G["<img src='https://latex.codecogs.com/svg.image?N_{p}\leq&space;0.9f_{ck}e_{h}d_{a}'>--------------------------------"];
	  H(["Pass of Fail"]);
	  I{"<img src='https://latex.codecogs.com/svg.image?3d_{a}\leq&space;e_{h}\leq&space;4.5d_{a}'>----------------------------"};
	  Variable_def--->E--->I--->G--->H
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def pullout_strength_with_single_hookbolt_under_tensile_force(fINp,fIfck,fIeh,fIda) -> bool:
        """단일 갈고리볼트가 인장력을 받는 경우 뽑힘강도

        Args:
            fINp (float): 단일 갈고리볼트가 인장력을 받는 경우 뽑힘강도
            fIfck (float): 콘크리트의 설계기준압축강도
            fIeh (float): J 또는 L볼트 샤프트의 안쪽면부터 J또는 L볼트의 바깥쪽끝까지 거리
            fIda (float): 앵커의 외경, 혹은 헤드스터드, 헤드볼트, 갈고리형볼트의 샤프트지름

        Returns:
            bool: 콘크리트용 앵커 설계기준  4.3.3 인장력을 받는 선설치앵커, 후설치 확장앵커 및 언더컷앵커의 뽑힘강도 (5)의 통과여부
        """

        if 3*fIda <= fIeh <= 4.5*fIda :
          if fINp <= 0.9 * fIfck * fIeh * fIda:
            return "Pass"
          else:
            return "Fail"

        else:
          return "Fail"


