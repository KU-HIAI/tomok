import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04060203_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.6.2.3 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-21'
    title = '받침부의 경간 내에 배치된 철근량'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.2 보
    4.6.2.3 단부 하부 철근의 정착
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 받침부의 경간 내에 배치된 철근량];
    B["KDS 24 14 21 4.6.2.3 (1)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수:경간 내에 배치된 철근량/];
		VarIn2[/입력변수: 철근량/];
		VarIn1 & VarIn2
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.6.2.3 (1)"])
		C --> Variable_def

		Variable_def--->F--->G

		F{"철근량≥경간 내에 배치된 철근량X1/3"}
		G(["Pass or fail"])
    """

    @rule_method
    def Amount_of_reinforcement_placed_within_the_span(fIreipsp,fIrebamo) -> RuleUnitResult:
        """받침부의 경간 내에 배치된 철근량

        Args:
            fIreipsp (float): 경간 내에 배치된 철근량
            fIrebamo (float): 철근량

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.6.2.3 단부 하부 철근의 정착 (1)의 판단 결과
        """

        assert isinstance(fIreipsp, float)
        assert isinstance(fIrebamo, float)

        if fIrebamo >= fIreipsp / 3:
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