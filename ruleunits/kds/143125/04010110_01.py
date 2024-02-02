import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_04010110_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 31 25 4.1.1.10 (1)' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-09-08'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '필릿용접의 최소유효길이'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.1 일반사항
    4.1.1.10 이음부 설계세칙
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
    A([이음부 설계세칙])
    B["KDS 14 31 25 4.1.1.10(1)"]
  	A ~~~ B
  	end

	  subgraph Variable_def
  	VarIn1[/입력변수: 필릿용접의 최소유효길이/]
	  VarIn2[/입력변수: 공칭용접치수/]
	  end

	  Python_Class ~~~ Variable_def --> D --> E
  	D["필릿용접의 최소유효길이 ≥ 공칭용접치수x10 and 30mm"]
	  E([Pass or Fail])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def minimum_effective_length_of_fillet_weld(fImielfw,fInowedi) -> bool:
        """필릿용접의 최소유효길이

        Args:
            fImielfw (float): 필릿용접의 최소유효길이
            fInowedi (float): 공칭용접치수

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법)  4.1.1.10 이음부 설계세칙 (1)의 통과 여부
        """

        if fImielfw >= (fInowedi*10 or 30) :
          return "Pass"
        else:
          return "Fail"


# 

