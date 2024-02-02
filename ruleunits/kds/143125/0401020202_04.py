import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_0401020202_04 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 31 25 4.1.2.2.2 (4)' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-09-11'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '필릿용접의 길이'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.2 용접
    4.1.2.2 필릿용접
    4.1.2.2.2 제한사항
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
	  A([필릿용접의 길이])
	  B["KDS 14 31 25 4.1.2.2.2(4)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn1[/입력변수: 필릿용접의 길이/]
	  VarIn2[/입력변수: 용접의 직각방향 간격/]
	  VarIn3[/입력변수: 인장재의 유효 순단면적/]
	  VarIn1 ~~~ VarIn2 & VarIn3
	  end

	  Python_Class ~~~ Variable_def --> D & E
	  D --> G
	  E --> F --> H
	  D["필릿용접의 길이> 용접의 직각방향 간격"]
	  E["인장재의 유효 순단면적"]
	  F{"KDS 14 31 25 4.1.2.3"}
	  G(["Pass or Fail"])
	  H([인장재의 유효 순단면적])

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def length_of_fillet_weld(fIlefiwe,fIpespwe) -> bool:
        """필릿용접의 길이

        Args:
            fIlefiwe (float): 필릿용접의 길이
            fIpespwe (float): 용접의 직각방향 간격

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법)  4.1.2.2.2 제한사항 (4)의 통과 여부
        """
        if fIlefiwe > fIpespwe :
          return "Pass"
        else:
          return "Fail"


# 

