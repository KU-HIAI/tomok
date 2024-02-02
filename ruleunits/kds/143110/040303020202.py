import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040303020202 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.3.3.2.2.2' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-12'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '압축 또는 인장을 받는 U형 단면의 상부플랜지 단면비'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.2 박스거더
    4.3.3.2.2 단면비 요구조건
    4.3.3.2.2.2 플랜지 단면비
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
		A[Title: 플랜지 단면비] ;
		B["KDS 14 31 10 4.3.3.2.2.2"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarIn1[/입력변수: 압축 또는 인장을 받는 U형 단면의 상부플랜지 단면비/] ;
      VarIn2[/입력변수: 플랜지의 폭/] ;
      VarIn3[/입력변수: 플랜지의 두께/] ;
			VarIn4[/입력변수: 웨브 두께/] ;
			end
			Python_Class ~~~ Variable_def
			VarIn1 & VarIn2 ~~~ VarIn3 & VarIn4

			C["<img src=https://latex.codecogs.com/svg.image?\frac{b_{f}}{2t_{f}}\leq&space;12.0>------------------------"]
			D["<img src=https://latex.codecogs.com/svg.image?b_{f}\geq&space;D/6>------------------------"]
			E["<img src=https://latex.codecogs.com/svg.image?t_{f}\geq&space;1.1t_{w}>------------------------"]

			Variable_def --> C --> D --> E --> F(["PASS or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Upper_flange_section_ratio_of_U_shaped_section_under_compression_or_tension(fIbf,fItf,fItw,fId) -> bool:
        """압축 또는 인장을 받는 U형 단면의 상부플랜지 단면비
        Args:
            fIbf (float): 플랜지의 폭
            fItf (float): 플랜지의 두께
            fItw (float): 웨브두께
            fId (float):


        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법)  4.3.3.2.2.2 플랜지 단면비의 통과여부
        """

        if fIbf / (2 * fItf) <= 12.0 and fIbf >= fId / 6 and fItf >= 1.1 * fItw:
          return "Pass"
        else:
          return "Fail"






# 

