import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_04010110_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.1.10 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-14'
    title = '필릿용접의 최소유효길이'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.1 일반사항
    4.1.1.10 이음부 설계세칙
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
    A[Title: 필릿용접의 최소유효길이]
    B["KDS 14 31 25 4.1.1.10(1)"]
  	A ~~~ B
  	end

	  subgraph Variable_def
  	VarIn1[/입력변수: 필릿용접의 최소유효길이/]
	  VarIn2[/입력변수: 공칭용접치수/]
	  end

		Python_Class ~~~ C(["KDS 14 31 25 4.1.1.10(1)"])
		C --> Variable_def

	  Variable_def --> D --> E
  	D{"필릿용접의 최소유효길이 ≥ 공칭용접치수x10 and 30mm"}
	  E([Pass or Fail])
    """

    @rule_method
    def minimum_effective_length_of_fillet_weld(fImielfw,fInowedi) -> RuleUnitResult:
        """필릿용접의 최소유효길이

        Args:
            fImielfw (float): 필릿용접의 최소유효길이
            fInowedi (float): 공칭용접치수

        Returns:
            pass_fail (bool):  강구조 연결 설계기준(하중저항계수설계법)   4.1.1.10 이음부 설계세칙 (1)의 판단 결과
        """

        assert isinstance(fImielfw, float)
        assert isinstance(fInowedi, float)

        if fImielfw >= (fInowedi*10 or 30) :
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