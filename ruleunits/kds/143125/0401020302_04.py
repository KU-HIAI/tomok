import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_0401020302_04 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 31 25 4.1.2.3.2 (4)' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-09-12'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '슬롯용접의 제한사항'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.2 용접
    4.1.2.3 플러그 및 슬롯용접
    4.1.2.3.2 제한사항
    (4)
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
  	A([슬롯용접의 슬롯길이 및 슬롯의 폭])
  	B["KDS 14 31 25 4.1.2.3.2(4)"]
  	A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn1[/입력변수: 슬롯용접의 슬롯길이/]
	  VarIn2[/입력변수: 용접두께/]
	  VarIn3[/입력변수: 슬롯의 폭/]
	  VarIn4[/입력변수: 판의두께/]
	  end

	  Python_Class ~~~ Variable_def --> D & E
	  D --> F
	  E --> F

	  D["슬롯용접의 슬롯길이 ≤ 용접두께+8mm "]
	  E["판의두께+8mm ≤ 슬롯의 폭 ≤ 용접두께x2.25"]
	  F([PASS or Fail])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Restricton_for_solt_welding(fIsllesw,fIwelthi,fIslowid,fIthipla) -> bool:
        """슬롯용접의 제한사항

        Args:
            fIsllesw (float): 슬롯용접의 슬롯길이
            fIwelthi (float): 용접두께
            fIslowid (float): 슬롯의 폭
            fIthipla (float): 판의 두께

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법)  4.1.2.3.2 제한사항 (4)의 통과 여부
        """
        if fIsllesw <= 10*fIwelthi and (fIthipla+8) <= fIslowid <= (2.25*fIwelthi) :
          return "Pass"
        else:
          return "Fail"


# 

