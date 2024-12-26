import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010201_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.2.1 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '전단력'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.1 일반
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 전단력];
    B["KDS 24 14 21 4.1.2.1 (1)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 계수하중에 의한 단면 전단력/];
		VarIn2[/입력변수: 검증단면의 설계전단강도/];

		VarIn1 & VarIn2

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.2.1 (1)"])
		C --> Variable_def

		Variable_def--->D
		D--->E
		D{"<img src='https://latex.codecogs.com/svg.image?V_{u}\leq&space;V_{d}'>---------------------------------"}

		E(["Pass or Fail"])
    """

    @rule_method
    def shear_force(fIVu,fIVd) -> RuleUnitResult:
        """전단력

        Args:
            fIVu (float): 계수하중에 의한 단면 전단력
            fIVd (float): 검증단면의 설계전단강도

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.1 일반 (1)의 판단 결과 1
            sOVuVd (string): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.1 일반 (1)의 판단 결과 2
        """

        assert isinstance(fIVu, float)
        assert isinstance(fIVd, float)

        if fIVu <= fIVd:
          return RuleUnitResult(
              result_variables = {
                  "sOVuVd": "4.1.5에 규정한 스트럿-타이 모델에 따라 설계된 부재 제외",
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "sOVuVd": "4.1.5에 규정한 스트럿-타이 모델에 따라 설계된 부재 제외",
                  "pass_fail": False,
              }
          )