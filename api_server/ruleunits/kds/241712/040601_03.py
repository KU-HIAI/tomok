import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241712_040601_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 12 4.6.1 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-16'
    title = '하중계수'

    description = """
    교량내진 설계기준(케이블교량)
    4. 설계
    4.6 붕괴방지수준의 내진성능 검증
    4.6.1 일반사항
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 하중계수];
    B["KDS 24 17 12 4.6.1 (3)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 지속하중/];
		VarIn2[/입력변수: 지진하중/];
		VarIn3[/입력변수: 하중계수/];

	  VarIn1 & VarIn2 & VarIn3

		end

		Python_Class ~~~ C(["KDS 24 17 12 4.6.1 (3)"])
		C --> Variable_def--->E

		E["지속하중 하중계수=1.0, 지진하중 하중계수=1.0"]
    """

    @rule_method
    def laod_factor(fOsusloa,fOloafac) -> RuleUnitResult:
        """하중계수

        Args:
            fOsusloa (float): 지속하중 하중계수
            fOloafac (float): 지진하중 하중계수

        Returns:
            fOsusloa (float): 교량내진 설계기준(케이블교량)  4.6.1 일반사항 (3)의 값 1
            fOloafac (float): 교량내진 설계기준(케이블교량)  4.6.1 일반사항 (3)의 값 2
        """

        fOsusloa = 1.0
        fOloafac = 1.0

        return RuleUnitResult(
            result_variables = {
                "fOsusloa": fOsusloa,
                "fOloafac": fOloafac,
            }
        )