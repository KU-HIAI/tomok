import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_04020702_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.2.7.2 (3)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-19'
    title = '단면의 설계강도'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.2 해석 및 설계
    4.2.7 설계지진력
    4.2.7.2 기초의 설계지진력
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 기초의 설계지진력]
	  B["KDS 24 17 11 4.2.7.2 (3)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: 단면의 설계강도/]
	  VarIn[/입력변수: 최대하중에 대한 소요강도/]
	  VarOut ~~~ VarIn
	  end

	  Python_Class ~~~ C(["KDS 24 17 11 4.2.7.2 (3)"])
		C --> Variable_def--> D --> F


	  D{"단면의 설계강도 ≥ 최대하중에 대한 소요강도"}

  	F([Pass or Fail])
    """

    @rule_method
    def cross_section_design_strength(fIdestse,fIrestml) -> RuleUnitResult:
        """단면의 설계강도


        Args:
            fIdestse (float): 단면의 설계강도
            fIrestml (float): 최대하중에 대한 소요강도

        Returns:
            pass_fail (bool): 교량내진설계기준(한계상태설계법) 4.2.7.2 지진위험도 및 유효수평지반가속도 (3)의 판단 결과
        """

        assert isinstance(fIdestse, float)
        assert isinstance(fIrestml, float)


        if fIdestse >= fIrestml :
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