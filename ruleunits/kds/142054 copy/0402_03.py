import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS142054_0402_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 20 54 4.2 (3)' # 건설기준문서
    ref_date = '2021-02-18'  # 디지털 건설문서 작성일
    doc_date = '2023-12-11'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '인장을 받는 단일부착식 앵커의 기본부착강도'    # 건설기준명

    #
    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.2 앵커 상도에 관한 일반 규정
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
    A[지속 인장하중을 받는 부착식 앵커];
    B["KDS 14 20 54 4.2 (3)"];
    A ~~~ B
    end
	  subgraph Variable_def
    VarIn1[/입력변수 : 인장을 받는 단일 부착식 앵커의 기본 부착강도/];
		VarIn2[/입력변수 : 계수 지속 인장하중/];
		VarIn3[/입력변수 : 강도감소계수/];
    VarIn1
		VarIn1 ~~~ VarIn2 & VarIn3
    end
    Python_Class~~~Variable_def

    D["<img src='https://latex.codecogs.com/svg.image?&space;0.55\phi N_{ba}\geq N_{ua,s}'>--------------------"];
    E([PASS or Fail]);
    Variable_def--->D
    D--->E
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Attached_anchor_with_continuous_tensile_load(fINba,fINuas,fIphi) -> bool:
        """지속 인장하중을 받는 부착식 앵커

        Args:
            fINba (float): 인장을 받는 단일 부착식 앵커의 기본 부착강도
            fINuas (float): 계수 지속 인장하중
            fIphi (float): 강도감소계수

        Returns:
            float: 콘크리트용 앵커 설계기준  4.2 앵커 상도에 관한 일반 규정 (3)의 통과 여부

        """

        if 0.55 * fIphi * fINba >= fINuas :
          return "Pass"
        else:
          return "Fail"


# 

