import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040302010113_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.3.2.1.1.13 (3)' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-11'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '연장길이'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.2 형강 및 강관
    4.3.2.1 단일부재
    4.3.2.1.1 휨강도
    4.3.2.1.1.13 휨부재의 단면산정
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
	  A[휨부재의 단면산정]
	  B["KDS 14 31 10 4.3.2.1.1.13(3)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: 연장길이/]
	  VarIn1[/입력변수: 커버플레이트 단부면의 전체폭에 걸친 용접치수/]
	  VarIn2[/입력변수: 커버플레이트 두께/]
	  VarIn3[/입력변수: 커버플레이트 폭/]

	  VarOut ~~~ VarIn1 & VarIn2 & VarIn3
  	end
	  Python_Class ~~~ Variable_def --> D & E
	  D --> F
	  E --> G
	  F & G --> H
	  D["커버플레이트 단부면의 전체폭에 걸쳐 용접치수 ≥커버플레이트x3/4인 연속용접"]
	  E["커버플레이트 단부면의 전체폭에 걸쳐 용접치수 <커버플레이트x3/4인 연속용접"]
	  F["연장길이=커버플레이트 폭"]
	  G["연장길이=(커버플레이트 폭)x1.5"]
	  H(["연장길이"])
    ```
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def extension_length(fIWeldim,fIcovplathi,fIextlen,fIcovplawid,fOextlen) -> bool:
        """연장길이
        Args:
            fIWeldim (float): 커버플레이트 단부면의 전체폭에 걸친 용접치수
            fIcovplathi (float): 커버플레이트 두께
            fIextlen (float): 연장길이
            fIcovplawid (float): 커버플레이트 폭
            fOextlen (float): 연장길이


        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.3.2.1.1.13 휨부재의 단면산정 (3)의 값
        """

        if fIWeldim >= fIcovplathi * 3 / 4:
            fIextlen = fIcovplawid
            return fIextlen
        else:
            fOextlen = fIcovplawid * 1.5
            return fOextlen


# 

