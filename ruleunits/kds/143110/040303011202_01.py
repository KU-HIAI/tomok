import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040303011202_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.3.3.1.12.2 (1)' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-12'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '단면변화를 준 덮개판 끝의 폭'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.1 플레이트거더
    4.3.3.1.12 덮개판
    4.3.3.1.12.2 단부 요구조건
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
		A[Title: 단부 요구조건] ;
		B["KDS 14 31 10 4.3.3.1.12.2 (1)"] ;
		A ~~~ B
		end

    subgraph Variable_def
      VarIn1[/입력변수: 단면변화를 준 덮개판 끝의 폭/] ;
    end

    Python_Class ~~~ Variable_def

    C["단면변화를 준 덮개판 끝의 폭 &ge; 75mm"]

    Variable_def --> C --> D(["PASS or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Cover_plate_tip_width_with_cross_section_change(fIcptwcc) -> bool:
        """단면변화를 준 덮개판 끝의 폭
        Args:
            fIcptwcc (float): 단면변화를 준 덮개판 끝의 폭



        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.3.3.1.12.2 단부 요구조건 (1)의 통과여부
        """

        if fIcptwcc >= 75:
          return "Pass"
        else:
          return "Fail"


# 

