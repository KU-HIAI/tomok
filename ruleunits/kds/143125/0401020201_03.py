import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_0401020201_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 31 25 4.1.2.2.1 (3)' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-09-11'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '필릿용접의 유효목두께'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.2 용접
    4.1.2.2 필릿용접
    4.1.2.2.1 필릿용접의 유효면적
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
	  A([필릿용접의 유효목두께])
	  B["KDS 14 31 25 4.1.2.2.1(3)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: 필릿용접의 유효목두께/]
	  VarIn1[/입력변수: 용접치수/]
	  VarIn2[/입력변수: 두 부재사이의 각도/]
	  VarIn3[/입력변수: 내접 삼각형의 높이/]
	  VarOut ~~~ VarIn1 & VarIn2 & VarIn3
	  end

  	Python_Class ~~~ Variable_def --> C --yes--> D --> F
  	C --no--> E --> F
  	C --"no(용접 다리의 크기가 서로 다른 경우)" --> H --> F
  	C{"두부재사이의 각도 90°"}
  	D["필릿용접의 유효목두께=용접치수x0.7"]
  	E["필릿용접의 유효목두께=용접루트를 꼭지점으로 하는 내접삼각형의 높이"]
	  F([필릿용접의 유효목두께])
	  H["필릿용접의 유효목두께=용접외측면을 밑변으로 하는 내접삼각형의 높이"]

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Effective_throat_thickness_of_fillet_weld(fOetthfw,fIweldim,fIanbtme,fIheintr) -> bool:
        """필릿용접의 유효목두께

        Args:
            fOetthfw (float): 필릿용접의 유효목두께
            fIweldim (float): 용접치수
            fIanbtme (float): 두 부재사이의 각도
            fIheintr (float): 내접 삼각형의 높이

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법)  4.1.2.2.1 필릿용접의 유효면적 (3)의 값
        """
        if fIanbtme == 90 :
          fOetthfw = fIweldim*0.7
          return fOetthfw
        else:
          fOetthfw = fIheintr
          return fOetthfw


# 

