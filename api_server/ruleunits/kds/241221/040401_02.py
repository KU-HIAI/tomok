import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241221_040401_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 21 4.4.1 (2)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '정적하중에 적용시켜야 할 충격하중계수'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.4 충격하중 : IM
    4.4.1 일반사항
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 정적하중에 적용시켜야 할 충격하중계수];
    B["KDS 24 12 21 4.4.1 (2)"];
    A ~~~ B
    end
	  subgraph Variable_def
    VarOut[/출력변수 : 충격하중계수/];
    VarIn1[/입력변수 : 충격하중/];
    end

    Python_Class ~~~ C(["KDS 24 12 21 4.4.1 (2)"])
		C --> Variable_def

    D["충격하중계수=1+IM/100"];
    E(["충격하중계수"]);
    Variable_def--->D--->E
    """

    @rule_method
    def static_load(fIIM) -> RuleUnitResult:
        """정적하중

        Args:
            fIIM (float): IM

        Returns:
            fOfacimp (float): 강교 설계기준(한계상태설계법)  4.4.1 일반사항 (2)의 값
        """

        assert isinstance(fIIM, float)

        fOfacimp = (1 + fIIM) / 100

        return RuleUnitResult(
            result_variables = {
                "fOfacimp": fOfacimp,
            }
        )