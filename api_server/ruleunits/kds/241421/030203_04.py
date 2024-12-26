import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_030203_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 3.2.3 (4)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '철근의 평균 탄성계수'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.2 철근
    3.2.3 설계 가정
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 철근의 평균 탄성계수];
    B["KDS 24 14 21 3.2.3 (4)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarOut1[/출력변수: 평균밀도/];
		VarOut1

		end

	  Python_Class ~~~ C(["KDS 24 14 21 3.2.3 (4)"])
		C --> Variable_def

		Variable_def--->E--->D

		E["평균밀도=7850kg/m³"]

		D(["평균밀도"])
    """

    @rule_method
    def Average_modulus_of_elasticity_of_reinforcing_bars(fOEs) -> RuleUnitResult:
        """철근의 평균 탄성계수

        Args:
            fOEs (float): 철근의 평균 탄성계수

        Returns:
            fOEs (float): 콘크리트교 설계기준(한계상태설계법)  3.2.3 설계 가정 (4)의 값
        """

        fOEs = 200

        return RuleUnitResult(
            result_variables = {
                "fOEs": fOEs,
            }
        )