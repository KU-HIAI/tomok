import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04060302_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.6.3.2 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '전단철근을 사용하는 경우 슬래브의 최소두께'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.3 슬래브
    4.6.3.2 전단철근
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 전단철근을 사용하는 경우 슬래브의 최소두께];
    B["KDS 24 14 21 4.6.3.2 (1)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수:슬래브의 최소두께/];

		VarIn1
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.6.3.2 (1)"])
		C --> Variable_def

		Variable_def--->F

		F{"슬래브의 최소두께≥200mm"}
		F --->G(["Pass or Fail"])
    """

    @rule_method
    def minimum_slab_thickness_When_using_shear_reinforcement(fIminslt) -> RuleUnitResult:
        """전단철근을 사용하는 경우 슬래브의 최소두께

        Args:
            fIminslt (float): 슬래브의 최소두께


        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.6.3.2 전단철근 (1)의 판단 결과
        """

        assert isinstance(fIminslt, float)

        if fIminslt>=200:
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