import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241221_04030102(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 21 4.3.1.2'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '다차로 재하계수'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.3 활하중
    4.3.1 차량활하중 : LL
    4.3.1.2 활하중의 동시재하
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 다차로 재하계수];
    B["KDS 24 12 21 4.3.1.2"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 다차로 재하계수/];
    VarIn1[/입력변수 : 재하차로의 수/];
    end

    Python_Class ~~~ C(["KDS 24 12 21 4.3.1.2"])
		C --> Variable_def

    D{"재하차로의 수"};
    E["다차로 재하계수=1.0"];
    F["다차로 재하계수=0.9"];
    G["다차로 재하계수=0.8"];
    H["다차로 재하계수=0.7"];
    I["다차로 재하계수=0.65"];
    J(["다차로 재하계수"]);
    Variable_def--->D--1--->E--->J
    D--2--->F--->J
    D--3--->G--->J
    D--4--->H--->J
    D--5이상--->I--->J
    """

    @rule_method
    def multiple_lane_loading_coefficient(iIN) -> RuleUnitResult:
        """다차로 재하계수

        Args:
            iIN (int): 재하차로의 수

        Returns:
            fOm (float): 강교 설계기준(한계상태설계법)  4.3.1.2 활하중의 동시재하의 값
        """

        assert isinstance(iIN, int)

        if iIN == 1:
          fOm = 1.0
        elif iIN == 2:
          fOm = 0.9
        elif iIN == 3:
          fOm = 0.8
        elif iIN == 4:
          fOm = 0.7
        else:
          fOm = 0.65

        return RuleUnitResult(
            result_variables = {
                "fOm": fOm,
            }
        )