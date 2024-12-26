import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04060803_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.6.8.3 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-22'
    title = '수평 철근'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.8 벽체
    4.6.8.3 수평 철근
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 수평 철근];
    B["KDS 24 14 21 4.6.8.3 (1)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수:수평 철근량/];
		VarIn2[/입력변수:수직철근량/];
		VarIn3[/입력변수:콘크리트 단면적/];
		VarIn1 & VarIn2 & VarIn3
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.6.8.3 (1)"])
		C --> Variable_def

		Variable_def--->D
		D{"수평 철근량≥max(수평 철근량x25%,0.001Ac)"}
    H(["Pass or Fail"])
    """

    @rule_method
    def horizontal_reinforcement(fIhorent, fIverent, fIAc) -> RuleUnitResult:
        """수평 철근

        Args:
            fIhorent (float): 수평 철근량
            fIverent (float): 수직철근량
            fIAc (float): 콘크리트 단면적

        Returns:
            pass_fail (bool):  콘크리트교 설계기준 (한계상태설계법)  4.6.8.3 수평 철근 (1)의 판단 결과
        """

        assert isinstance(fIhorent, float)
        assert isinstance(fIverent, float)
        assert isinstance(fIAc, float)

        if fIhorent >= max(fIverent/4, 0.001*fIAc):
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