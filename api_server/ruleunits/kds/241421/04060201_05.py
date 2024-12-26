import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04060201_05(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.6.2.1 (5)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '휨강도'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.2 보
    4.6.2.1 주철근
    (5)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 휨강도];
    B["KDS 24 14 21 4.6.2.1 (5)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수:휨강도/];
		VarIn2[/입력변수: 균열휨모멘트/];
		VarIn1 & VarIn2
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.6.2.1 (5)"])
		C --> Variable_def

		Variable_def--->F

		F{"휨강도≥ 균열휨모멘트X1.15"}
		F---->J
		J(["Pass or Fail"])
    """

    @rule_method
    def flexural_strength(fIflestr,fIcrabem) -> RuleUnitResult:
        """휨강도

        Args:
            fIflestr (float): 휨강도
            fIcrabem (float): 균열휨모멘트


        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.6.2.1 주철근 (5)의 판단 결과
        """

        assert isinstance(fIflestr, float)
        assert isinstance(fIcrabem, float)

        if fIflestr >= 1.15 * fIcrabem :
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