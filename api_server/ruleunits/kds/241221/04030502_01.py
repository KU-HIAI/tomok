import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241221_04030502_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 21 4.3.5.2 (1)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '연행집중이동하중'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.3 활하중
    4.3.5 열차횡하중 LF
    4.3.5.2 EL 표준열차하중의 열차횡하중
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: EL 표준열차하중의 열차횡하중];
    B["KDS 24 12 21 4.3.5.2 (1)"];
    A ~~~ B
    end
	  subgraph Variable_def
	  VarOut1[/출력변수 : 열차횡하중/];
	  VarIn1[/입력변수 : EL 표준열차하중/];

	  end

	  Python_Class ~~~ C(["KDS 24 12 21 4.3.5.2 (1)"])
		C --> Variable_def

	  D["Q=EL 표준열차하중 x 0.2"];
	  Variable_def --> D --> E([열차횡하중]);
    """

    @rule_method
    def performance_concentrated_moving_load(fILsttr) -> RuleUnitResult:
        """연행집중이동하중

        Args:
            fILsttr (float): 표준열차하중

        Returns:
            fOQ (float): 강교 설계기준(한계상태설계법)  4.3.5.2 EL 표준열차하중의 열차횡하중 (1)의 값
        """

        assert isinstance(fILsttr, float)

        fOQ = 0.2 * fILsttr

        return RuleUnitResult(
            result_variables = {
                "fOQ": fOQ,
            }
        )