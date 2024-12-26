import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010201_07(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.2.1 (7)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '작용 전단력'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.1 일반
    (7)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 작용 전단력];
    B["KDS 24 14 21 4.1.2.1 (7)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 작용 전단력/];
		VarIn2[/입력변수: 설계최대전단강도/];

		VarIn1 & VarIn2

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.2.1 (7)"])
		C --> Variable_def

		Variable_def--->D--->E

		D{"<img src='https://latex.codecogs.com/svg.image?V_{u}\leq V_{dmax}'>---------------------------------"}
    E(["Pass or Fail"])
    """

    @rule_method
    def acting_shear_force(fIVu,fIVdmax) -> RuleUnitResult:
        """작용 전단력

        Args:
            fIVu (float): 작용 전단력
            fIVdmax (float): 설계최대전단강도

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.1 일반 (7)의 판단 결과
        """

        assert isinstance(fIVu, float)
        assert isinstance(fIVdmax, float)

        if fIVu <= fIVdmax:
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