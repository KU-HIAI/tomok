import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040104_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 14 31 10 4.1.4 (2)' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-11-23'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '조립인장재'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.1 인장부재
    4.1.4 조립 인장부재
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
		A[조립 인장부재] ;
		B["KDS 14 31 10 4.1.4(2)"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarIn1[/입력변수: 조립인장재/]
    VarIn2[/입력변수: 세장비/]

		end

		Python_Class ~~~ Variable_def
  	C["끼움재를 사용한 2개 이상의 형강으로 구성된 조립인장재"]
    E["세장비 ≤ 300"]
	  Variable_def --> C
    C-->E --> Q(["PASS or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def assembly_tension_member(fIasteme,fILr) -> bool:
        """조립인장재

        Args:
            fIasteme (float): 조립인장재
            fILr (float): 세장비

        Returns:
            float: 강구조부재설계기준(하중저항계수설계법)  4.1.4 조립 인장부재 (2)의 통과여부
        """

        if fILr <= 300:
          return 'Pass'
        else:
          return 'Fail'


# 

