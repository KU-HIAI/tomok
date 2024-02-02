import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_0401020102_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 31 25 4.1.2.1.2 (1)' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-09-08'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '부분용입 그루브용접의 유효목두께'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.2 용접
    4.1.2.1 그루브용접
    4.1.2.1.2 부분용입 그루브용접
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
  	A([부분용입 그루브용접])
  	B["KDS 14 31 25 4.1.2.1.2(1)"]
  	A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn1[/입력변수: 부분용입 그루브용접의 유효목두께/]
	  VarIn2[/입력변수: 접합부의 두꺼운쪽 판의 두께/]
  	VarIn3[/입력변수: 얇은 쪽 판의 두께/]
	  end

	  Python_Class ~~~ Variable_def --> D --> E

	  D["얇은 쪽 판의두께≥부분용입 그루브용접의 유효목두께 ≥ <img src='https://latex.codecogs.com/svg.image?\sqrt{2t}(mm)'>"]
	  E([Pass or Fail])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Effective_throat_thickness_of_partial_joint_penetration_groove_weld(fIettPJP,fIt,fItsplth) -> bool:
        """고장력볼트의 구멍중심에서 볼트머리 또는 너트가 접하는 부재의 연단까지의 최대거리

        Args:
            fIettPJP (float): 부분용입 그루브용접의 유효목두께
            fIt (float): 접합부의 두꺼운 쪽 판의 두께
            fItsplth (float): 얇은 쪽 판의 두께

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법)  4.1.2.1.2 부분용입 그루브용접 (1)의 통과 여부
        """

        if (fIt*2)**(1/2) <= fIettPJP <= fItsplth :
          return "Pass"
        else:
          return "Fail"


# 

