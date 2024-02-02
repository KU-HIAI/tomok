import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040303020201_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.3.3.2.2.1 (2)' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-12'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '수평보강재가 없는 웨브의 단면비'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.2 박스거더
    4.3.3.2.2 단면비 요구조건
    4.3.3.2.2.1 웨브 단면비
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
		A[Title: 웨브 단면비] ;
		B["KDS 14 31 10 4.3.3.2.2.1 (2)"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarIn1[/입력변수: 수평보강재가 없는 웨브의 단면비/] ;
      VarIn2[/입력변수: 수평보강재 안의 최대 웨브 높이/] ;
      VarIn3[/입력변수: 웨브 두께/] ;
			end
			Python_Class ~~~ Variable_def

			C["<img src=https://latex.codecogs.com/svg.image?\frac{D}{t_{w}}\leq&space;150>------------------------"]
			Variable_def --> C --> D(["PASS or Fail"])

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Section_ratio_of_web_without_horizontal_stiffeners(fIsrwwhs,fID,fItw) -> bool:
        """수평보강재가 없는 웨브의 단면비
        Args:
            fIsrwwhs (float): 수평보강재가 없는 웨브의 단면비
            fID (float): 수평보강재 안의 최대 웨브 높이
            fItw (float): 웨브두께


        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.3.3.2.2.1 웨브 단면비 (2)의 통과여부
        """

        if fID / fItw <= 150:
          fIsrwwhs = fID / fItw
          return "Pass"
        else:
          return "Fail"


# 

