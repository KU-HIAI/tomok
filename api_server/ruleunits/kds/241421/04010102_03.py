import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010102_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.1.2 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '극한한계변형률'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.1 휨과 축력
    4.1.1.2 휨 및 축력이 작용하는 부재의 극한한계상태 검증
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 극한한계변형률];
    B["KDS 24 14 21 4.1.1.2 (3)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 극한한계변형률/];
		VarIn2[/입력변수: 콘크리트 정점변형률/];

		VarIn1 & VarIn2
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.1.2 (3)"])
		C --> Variable_def

		Variable_def--->E--->D

		E{"극한한계변형률≤ 콘크리트 정점변형률"}
		D(["Pass or Fail"])
    """

    @rule_method
    def Ultimate_limit_strain(fIultlis,fIepsco) -> RuleUnitResult:
        """극한한계변형률

        Args:
            fIultlis (float): 극한한계변형률
            fIepsco (float): 콘크리트 정점변형률

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.1.1.2 휨 및 축력이 작용하는 부재의 극한한계상태 검증 (3)의 판단 결과
        """

        assert isinstance(fIultlis, float)
        assert isinstance(fIepsco, float)

        if fIultlis <= fIepsco :
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