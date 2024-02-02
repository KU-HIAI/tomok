import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040303020203_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.3.3.2.2.3 (3)' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-12'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '웨브의 경사도'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.2 박스거더
    4.3.3.2.2 단면비 요구조건
    4.3.3.2.2.3 다중 박스단면의 활하중 분배계수 적용 특별제한
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
		A[Title: 다중 박스단면의 활하중 분배계수 적용 특별제한] ;
		B["KDS 14 31 10 4.3.3.2.2.3 (3)"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarIn1[/입력변수: 웨브의 경사도/] ;
			end
			Python_Class ~~~ Variable_def

			D["1/4 &ge; 웨브의 경사도"]

			Variable_def --> D --> F(["PASS or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def slope_of_the_web(fIsloweb) -> bool:
        """웨브의 경사도
        Args:
            fIsloweb (float): 웨브의 경사도



        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.3.3.2.2.3 다중 박스단면의 활하중 분배계수 적용 특별제한 (3)의 통과여부
        """


        if fIsloweb <= 1 / 4:
            return "Pass"
        else:
            return "Fail"


# 

