import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0401020202_06(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.2.2.2 (6)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '단속 필릿용접의 한 세그멘트 길이'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.2 용접
    4.1.2.2 필릿용접
    4.1.2.2.2 제한사항
    (6)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
    A[Title: 단속 필릿용접의 한 세그멘트 길이]
    B["KDS 14 31 25 4.1.2.2.2 (6)"]
  	A ~~~ B
  	end

	  subgraph Variable_def
	  VarIn1[/입력변수: 단속 필릿용접의 한 세그멘트의 길이/]
	  VarIn2[/입력변수: 용접치수/]
	  end

		Python_Class ~~~ C(["KDS 14 31 25 4.1.2.2.2 (6)"])
		C --> Variable_def

	  Variable_def --> D  --> F

    D{"단속필릿용접의 한 세그멘트의 길이≥ 용접치수x4 and 40mm"}
	  F(["Pass or Fail"])
    """

    @rule_method
    def Length_of_one_segment_of_an_interrupted_fillet_weld(fIlosifw,fIweldim) -> RuleUnitResult:
        """단속 필릿용접의 한 세그멘트 길이

        Args:
            fIlosifw (float): 단속 필릿용접의 한 세그멘트 길이
            fIweldim (float): 용접치수

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)   4.1.2.2.2 제한사항 (6)의 판단 결과
        """

        assert isinstance(fIlosifw, float)
        assert isinstance(fIweldim, float)

        if fIlosifw >= fIweldim*4 and fIlosifw >= 40 :
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )