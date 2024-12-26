import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_030203_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 3.2.3 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '철근의 평균 단위 질량'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.2 철근
    3.2.3 설계 가정
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 철근의 평균 단위 질량];
    B["KDS 24 14 21 3.2.3 (3)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarOut1[/출력변수: 탄성계수의 설계값/];
		VarOut1

		end

	  Python_Class ~~~ C(["KDS 24 14 21 3.2.3 (3)"])
		C --> Variable_def

		Variable_def--->D--->G

		D["탄성계수의 설계값=200GPa"]

		G(["탄성계수의 설계값"])
    """

    @rule_method
    def Average_unit_mass_of_reinforcing_bars(fOavgumr) -> RuleUnitResult:
        """철근의 평균 단위 질량

        Args:
            fOavgumr (float): 철근의 평균 단위 질량

        Returns:
            fOavgumr (float): 콘크리트교 설계기준(한계상태설계법)  3.2.3 설계 가정 (3)의 값
        """

        fOavgumr = 7850

        return RuleUnitResult(
            result_variables = {
                "fOavgumr": fOavgumr,
            }
        )