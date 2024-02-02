import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_04050203 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.5.2.3' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-15'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '아이바 핀의 직경'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5. 기타 부재
    4.5.2 핀
    4.5.2.3 아이바 핀의 최소치수
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
		A[Title: 아이바 핀의 최소치수] ;
		B["KDS 14 31 10 4.5.2.3"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarIn1[/입력변수: 핀의 직경/] ;
      VarIn2[/입력변수: 핀의 최소항복강도/] ;
      VarIn3[/입력변수: 아이바 몸체의 폭/] ;

			end

		Python_Class ~~~ Variable_def

		E["<img src=https://latex.codecogs.com/svg.image?D\geq\left(\frac{3}{4}&plus;\frac{F_{y}}{2760}\right)b>------------------------------------------"]

		Variable_def --> E --> D(["PASS or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def diameter_of_pin(fID,fIFy,fIb) -> bool:
        """아이바 핀의 직경
        Args:
            fID (float): 핀의 직경
            fIFy (float): 핀의 최소항복강도
            fIb (float): 아이바 몸체의 폭



        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.5.2.3 아이바 핀의 최소치수의 통과여부
        """

        if fID >= (3 / 4 + fIFy / 2760) * fIb:
          return "Pass"
        else:
          return "Fail"


# 

