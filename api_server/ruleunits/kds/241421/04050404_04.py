import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04050404_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.5.4.4 (4)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-21'
    title = '섬유구조인 경우 지름'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.5 철근 상세
    4.5.4 철근의 정착
    4.5.4.4 기본정착길이
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 섬유구조인 경우 지름];
    B["KDS 24 14 21 4.5.4.4 (4)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수: 철근의 지름/];

		VarOut1[/출력변수: 등가의 지름/];

		VarOut1~~~VarIn1
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.5.4.4 (4)"])
		C --> Variable_def

		Variable_def--->D

		D["<img src='https://latex.codecogs.com/svg.image?d_{b,n}=d_b\sqrt{2}'>---------------------------------"]

		D--->F
		F(["등가의지름"])
    """

    @rule_method
    def Diameter_in_case_of_fibrous_structure(fIdb) -> RuleUnitResult:
        """섬유구조인 경우 지름

        Args:
            fIdb (float): 철근의 지름

        Returns:
            fOdbn (float): 콘크리트교 설계기준 (한계상태설계법)  4.5.4.4 기본정착길이 (4)의 값
        """

        assert isinstance(fIdb, float)

        fOdbn = fIdb*(2**0.5)

        return RuleUnitResult(
            result_variables = {
                "fOdbn": fOdbn,
            }
        )