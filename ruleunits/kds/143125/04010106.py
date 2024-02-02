import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_04010106 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 31 25 4.1.1.6' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-09-08'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '접합부의 설계강도'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.1 일반사항
    4.1.1.6 접합부의 최소강도
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
	  A([접합부의 최소강도])
	  B["KDS 14 31 25 4.1.1.6"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn[/입력변수: 접합부의 설계강도/]
	  end
	  Python_Class ~~~ Variable_def --> D --> E

	  D["접합부의 설계강도 ≥ 45KN"]
	  E([Pass or Fail])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Design_strength_of_connection(fIdestco) -> bool:
        """접합부의 설계강도

        Args:
            fIdestco (float): 접합부의 설계강도

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법)  4.1.1.6 접합부의 최소강도의 통과 여부
        """

        if fIdestco >= 45 :
          return "Pass"
        else:
          return "Fail"


# 

# 

