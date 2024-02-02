import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_0401020202_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 31 25 4.1.2.2.2 (2)' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-09-11'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '겹침이음의 필릿용접 최대치수'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.2 용접
    4.1.2.2 필릿용접
    4.1.2.2.2 제한사항
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
	  A([겹침이음의 필릿용접 최대치수])
  	B["KDS 14 31 25 4.1.2.2.2(2)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: 겹침이음의 필릿용접 최대치수/]
	  VarIn[/입력변수: 용접되는 판의 두께/]
	  VarOut ~~~ VarIn
	  end

	  Python_Class ~~~ Variable_def --> C
	  C--yes-->E
	  C--no-->F
	  E & F --> G
	  C{"<img src='https://latex.codecogs.com/svg.image?t<6(mm)'>-------------"}
	  E["<img src='https://latex.codecogs.com/svg.image?s=t'>---------"]
	  F["<img src='https://latex.codecogs.com/svg.image?s=t-2(mm)'>-----------------"]
	  G([겹침이음의 필릿용접 최대치수 s])

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def maximum_fillet_welding_dimensions_of_overlapping_joints(fOs,fIt) -> bool:
        """겹침이음의 필릿용접 최대치수

        Args:
            fOs (float): 겹침이음의 필릿용접 최대치수
            fIt (float): 용접되는 판의 두께

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법)  4.1.2.2.2 제한사항 (2)의 값
        """
        if fIt < 6 :
          fOs = fIt
          return fOs
        else:
          fOs = fIt - 2
          return fOs


# 

