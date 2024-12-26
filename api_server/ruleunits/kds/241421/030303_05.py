import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_030303_05(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 3.3.3 (5)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '열팽창계수'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.3 프리스트레싱 강재
    3.3.3 설계 가정
    (5)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 열팽창계수];
    B["KDS 24 14 21 3.3.3 (5)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarOut1[/출력변수: 열팽창계수/];
		VarOut1

		end

	  Python_Class ~~~ C(["KDS 24 14 21 3.3.3 (5)"])
		C --> Variable_def

		Variable_def--->C--->G

		C["열팽창계수=12x10-6/°C"]

		D(["열팽창계수"])
    """

    @rule_method
    def coefficient_of_thermal_expansion(fOcoethe) -> RuleUnitResult:
        """열팽창계수

        Args:
            fOcoethe (float): 열팽창계수

        Returns:
            fOcoethe (float): 콘크리트교 설계기준(한계상태설계법)  3.3.3 설계 가정 (5)의 값
        """

        fOcoethe = 12*10**(-6)

        return RuleUnitResult(
            result_variables = {
                "fOcoethe": fOcoethe,
            }
        )