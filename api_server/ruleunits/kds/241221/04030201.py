import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241221_04030201(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 21 4.3.2.1'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '피로의 영향을 검토하는 경우의 활하중'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.3 활하중
    4.3.2 피로하중
    4.3.2.1 크기와 형태
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 피로의 영향을 검토하는 경우의 활하중];
    B["KDS 24 12 21 4.3.2.1"];
    A ~~~ B
    end
	  subgraph Variable_def
    VarOut[/출력변수 : 활하중/];
    VarIn1[/입력변수 : 표준트럭하중/];
    end

    Python_Class ~~~ C(["KDS 24 12 21 4.3.2.1"])
		C --> Variable_def

    D["활하중=KDS 24 12 21 4.3.1.3.1 에 규정된 표준트럭하중 X 0.8"];
    E(["활하중"]);
    Variable_def--->D--->E
    """

    @rule_method
    def Live_load(fILsttr) -> RuleUnitResult:
        """활하중

        Args:
            fILsttr (float): 4.3.1.3.1에서 규정된 표준트럭하중

        Returns:
            fOLlive (float): 강교 설계기준(한계상태설계법)  4.3.2.1 크기와 형태의 값
        """

        assert isinstance(fILsttr, float)

        fOLlive = fILsttr * 0.8

        return RuleUnitResult(
            result_variables = {
                "fOLlive": fOLlive,
            }
        )