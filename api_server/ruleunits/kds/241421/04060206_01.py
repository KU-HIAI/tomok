import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04060206_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.6.2.6 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-21'
    title = '부재 종방향 축과의 각도'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.2 보
    4.6.2.6 전단철근
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 부재 종방향 축과의 각도];
    B["KDS 24 14 21 4.6.2.6 (1)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수:종방향 축과의 각도/];

		VarIn1
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.6.2.6 (1)"])
		C --> Variable_def

		Variable_def--->F--->G

		F{"45°<종방향 축과의 각도<90°"}
		G(["Pass or fail"])
    """

    @rule_method
    def angle_with_the_longitudinal_axis(fIalpha) -> RuleUnitResult:
        """부재 종방향 축과의 각도

        Args:
            fIalpha (float): 전단철근비

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.6.2.6 전단철근 (1)의 판단 결과
        """

        assert isinstance(fIalpha, float)

        if 45 <= fIalpha <= 90:
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