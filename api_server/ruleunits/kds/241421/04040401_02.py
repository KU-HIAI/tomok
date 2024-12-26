import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04040401_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.4.4.1 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '공칭피복두께'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.4 내구성 및 피복두께
    4.4.4 콘크리트 피복두께
    4.4.4.1 일반 사항
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 공칭피복두께];
    B["KDS 24 14 21 4.4.4.1 (2)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수: 최소피복두께/];
		VarIn2[/입력변수: 설계 편차 허용량/];
		VarOut1[/출력변수: 공칭피복두께/];
		VarOut1~~~VarIn1 & VarIn2

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.4.4.1 (2)"])
		C --> Variable_def

		Variable_def--->D--->F
		D["<img src='https://latex.codecogs.com/svg.image?t_{c,nom}=t_{c,min}&plus;\Delta&space;t_{c,dev}'>---------------------------------"]

		F(["공칭피복두께"])
    """

    @rule_method
    def Nominal_clear_cover(fItcmin,fIdtcdev) -> RuleUnitResult:
        """공칭피복두께

        Args:
            fItcmin (float): 최소피복두께
            fIdtcdev (float): 설계 편차 허용량

        Returns:
            fOtcnom (float): 콘크리트교 설계기준 (한계상태설계법) 4.4.4.1 일반 사항 (2)의 값
        """

        assert isinstance(fItcmin, float)
        assert isinstance(fIdtcdev, float)

        fOtcnom = fItcmin + fIdtcdev

        return RuleUnitResult(
            result_variables = {
                "fOtcnom": fOtcnom,
            }
        )