import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04040403_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.4.4.3 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-21'
    title = '설계 편차 허용량'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.4 내구성 및 피복두께
    4.4.4 콘크리트 피복두께
    4.4.4.3 설계 편차 허용량
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 설계 편차 허용량];
    B["KDS 24 14 21 4.4.4.3 (2)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarOut1[/입력변수: 설계 편차 허용량/]

		VarOut1

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.4.4.3 (2)"])
		C --> Variable_def

		Variable_def--->D--->E
		D["<img src='https://latex.codecogs.com/svg.image?\Delta t_{c,dev} = 10mm'>---------------------------------"]
		E(["설계 편차 허용량"])
    """

    @rule_method
    def Design_Deviation_Tolerance(fOdtcdev) -> RuleUnitResult:
        """설계 편차 허용량

        Args:
            fOdtcdev (float): 설계 편차 허용량

        Returns:
            fOdtcdev (float): 콘크리트교 설계기준 (한계상태설계법)  4.4.4.3 설계 편차 허용량 (2)의 값
        """

        fOdtcdev = 10

        return RuleUnitResult(
            result_variables = {
                "fOdtcdev": fOdtcdev,
            }
        )