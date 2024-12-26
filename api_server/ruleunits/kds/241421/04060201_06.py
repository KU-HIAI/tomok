import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04060201_06(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.6.2.1 (6)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '최대 휨모멘트'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.2 보
    4.6.2.1 주철근
    (6)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 최대 휨모멘트];
    B["KDS 24 14 21 4.6.2.1 (6)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수:최대 휨모멘트/];
		VarIn2[/입력변수:지점부 단면이 저항할 수 있는 휨모멘트/];
		VarIn1 & VarIn2
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.6.2.1 (6)"])
		C --> Variable_def

		Variable_def--->F--->G

		F{"휨모멘트≥ 최대 휨모멘트X0.15"}
		G(["Pass or fail"])
    """

    @rule_method
    def maximum_bending_moment(fIbemmax,fIbemrcs) -> RuleUnitResult:
        """최대 휨모멘트

        Args:
            fIbemmax (float): 최대 휨모멘트
            fIbemrcs (float): 지점부 단면이 저항할 수 있는 휨모멘트


        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.6.2.1 주철근 (6)의 판단 결과
        """

        assert isinstance(fIbemmax, float)
        assert isinstance(fIbemrcs, float)

        if fIbemrcs >= 0.15 * fIbemmax :
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