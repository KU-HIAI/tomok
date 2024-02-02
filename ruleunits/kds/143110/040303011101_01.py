import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040303011101_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.3.3.1.11.1 (1)' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-15'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '웨브-플랜지 용접부'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.1 플레이트거더
    4.3.3.1.11 보강재
    4.3.3.1.11.1 중간수직보강재
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
		A[Title: 중간수직보강재] ;
		B["KDS 14 31 10 4.3.3.1.11.1 (1)"] ;
		A ~~~ B
		end

    subgraph Variable_def
      VarIn1[/입력변수: 웨브-플랜지 용접부/] ;
      VarIn2[/입력변수: 수평보강재-웨브 용접단까지의 거리/] ;
      VarIn3[/입력변수: 웨브두께/] ;
			end

			Python_Class ~~~ Variable_def

    C["<img src=https://latex.codecogs.com/svg.image?4t_{w}\leq&space;A&space;or&space;B\leq&space;6t_{w}and&space;100mm>------------------------------------------------"]
    D["웨브-플랜지 용접부 = A"]
    E["수평보강재-웨브 용접단까지의 거리 = B"]

    Variable_def --> D & E -->C -->F(["PASS or Fail"])

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Web_flange_welds(fIweflwe,fIhswdwe,fItw) -> bool:
        """웨브-플랜지 용접부
        Args:
            fIweflwe (float): 웨브-플랜지 용접부
            fIhswdwe (float): 수평보강재-웨브 용접단까지의 거리
            fItw (float): 웨브두께

        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.3.3.1.11.1 중간수직보강재 (1)의 통과여부
        """


        if 4 * fItw <= fIweflwe <= 6 * fItw and fIweflwe <= 100 or 4 * fItw <= fIhswdwe <= 6 * fItw and fIhswdwe <= 100:
          return "Pass"
        else:
          return "Fail"


# 

