import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040302010113_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.3.2.1.1.13 (3)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '세장한 자유돌출판의 저감계수'

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
    content = """
    """
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
	  Python_Class ~~~ C1(["KDS 14 31 10 4.3.2.1.1.13(3)"]) -->Variable_def --> D & E
	  D --> F
	  E --> G
	  F & G --> H
	  D["커버플레이트 단부면의 전체폭에 걸쳐 용접치수 ≥커버플레이트x3/4인 연속용접"]
	  E["커버플레이트 단부면의 전체폭에 걸쳐 용접치수 <커버플레이트x3/4인 연속용접"]
	  F["연장길이=커버플레이트 폭"]
	  G["연장길이=(커버플레이트 폭)x1.5"]
	  H(["연장길이"])
    """

    @rule_method
    def extension_length(fIWeldim,fIcovplathi,fIextlen,fIcovplawid,fOextlen) -> RuleUnitResult:
        """연장길이

        Args:
            fIWeldim (float): 커버플레이트 단부면의 전체폭에 걸친 용접치수
            fIcovplathi (float): 커버플레이트 두께
            fIextlen (float): 연장길이
            fIcovplawid (float): 커버플레이트 폭
            fOextlen (float): 연장길이

        Returns:
            fOextlen (float): 연장길이
        """

        assert isinstance(fIWeldim, float)
        assert isinstance(fIcovplathi, float)
        assert isinstance(fIextlen, float)
        assert isinstance(fIcovplawid, float)
        assert isinstance(fOextlen, float)

        if fIWeldim >= fIcovplathi * 3 / 4:
            fIextlen = fIcovplawid
            return RuleUnitResult(
            result_variables = {
              "fOextlen": fOextlen,
               }
            )
        else:
            fOextlen = fIcovplawid * 1.5
            return RuleUnitResult(
            result_variables = {
              "fOextlen": fOextlen,
               }
            )