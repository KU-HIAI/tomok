import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_04010110_06 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 31 25 4.1.1.10 (6)' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-09-08'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '고장력볼트의 구멍중심에서 볼트머리 또는 너트가 접하는 부재의 연단까지의 최대거리'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.1 일반사항
    4.1.1.10 이음부 설계세칙
    (6)
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
  	A[Title: 이음부 설계세칙]
	  B["KDS 14 31 25 4.1.1.10(6)"]
  	A ~~~ B
  	end

	  subgraph Variable_def
	  VarOut[/출력변수: 부재의 연단까지의 최대거리/]
	  VarIn[/입력변수: 판 두께/]
	  VarOut ~~~ VarIn
	  end

	  Python_Class ~~~ Variable_def --> D --> E
	  D["부재의 연단까지의 최대거리 ≤ 판두께x12 and 150mm"]
	  E([Pass or Fail])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Maximum_distance_from_the_center_of_the_hole_in_the_high_strength_bolt_to_the_edge_of_the_member_in_contact_with_the_bolt_head_or_nut(fOdiplme,fIplathi) -> bool:
        """고장력볼트의 구멍중심에서 볼트머리 또는 너트가 접하는 부재의 연단까지의 최대거리

        Args:
            fOdiplme (float): 부재의 연단까지의 거리
            fIplathi (float): 판 두께

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법)  4.1.1.10 이음부 설계세칙 (6)의 통과 여부
        """

        if fOdiplme <= (fIplathi*12 or 150) :
          return "Pass"
        else:
          return "Fail"


# 

