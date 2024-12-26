import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010205_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.2.5 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-17'
    title = '시공이음 계면의 전단'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.5 서로 다른 시기에 타설한 콘크리트의 계면 전단
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 시공이음 계면의 전단];
    B["KDS 24 14 21 4.1.2.5 (1)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 계수하중에 의한 계면에서 전단응력/];
		VarIn2[/입력변수: 계면의 설계전단강도/];

		VarIn1 & VarIn2

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.2.5 (1)"])
		C --> Variable_def

		Variable_def--->E--->D
		E{"<img src='https://latex.codecogs.com/svg.image?v_{u}&space;\leq&space;v_{d}'>---------------------------------"}
		D(["Pass or Fail"])
    """

    @rule_method
    def Shear_stress_at_the_interface_due_to_modulus_load(fIVu,fIVd) -> RuleUnitResult:
        """시공이음 계면의 전단

        Args:
            fIVu (float): 계수하중에 의한 계면에서 전단응력
            fIVd (float): 계면의 설계전단강도

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.5 서로 다른 시기에 타설한 콘크리트의 계면 전단 (1)의 판단 결과
        """

        assert isinstance(fIVu, float)
        assert isinstance(fIVd, float)

        if fIVu <= fIVd:
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