import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_04010301(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.1.3.1'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '총단면의 항복한계상태'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.1 인장부재
    4.1.3 인장강도
    4.1.3.1 총단면의 항복한계상태
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 총단면의 항복한계상태] ;
		B["KDS 14 31 10 4.1.3.1"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarOut1[/출력변수: 공칭인장강도/]
    VarIn1[/입력변수: 부재의 총단면적/]
    VarIn2[/입력변수: 항복강도/]

		end

		Python_Class ~~~ C(["KDS 14 31 10 4.1.3.1"])
		C --> Variable_def

  	D(["<img src='https://latex.codecogs.com/svg.image?P_{n}=F_{y}A_{g}'>----------------------"])
    Variable_def --> D
    """

    @rule_method
    def yield_limit_state_of_total_cross_section(fIAg,fIFy) -> RuleUnitResult:
        """총단면의 항복한계상태

        Args:
            fIAg (float): 부재의 총단면적
            fIFy (float): 항복강도

        Returns:
            fOPn (float): 깊은기초 설계기준(일반설계법)  4.1.3.1 총단면의 항복한계상태의 값
        """

        assert isinstance(fIAg, float)
        assert isinstance(fIFy, float)

        fOPn = fIFy * fIAg

        return RuleUnitResult(
            result_variables = {
                "fOPn": fOPn,
            }
        )