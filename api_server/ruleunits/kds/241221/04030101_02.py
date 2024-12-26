import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241221_04030101_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 21 4.3.1.1 (2)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '재하차로의 폭'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.3 활하중
    4.3.1 차량활하중 : LL
    4.3.1.1 재하차로의 수
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 재하차로의 폭];
    B["KDS 24 12 21 4.3.1.1 (2)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 재하차로의 수/];
    VarIn1[/입력변수 : 연석, 방호울타리간의 교폭/];
    VarIn2[/입력변수 : 재하차로의 수/];
    VarOut ~~~ VarIn1
    VarOut ~~~ VarIn2
    end

    Python_Class ~~~ C(["KDS 24 12 21 4.3.1.1 (2)"])
		C --> Variable_def

    D["<img src='https://latex.codecogs.com/svg.image?W=\frac{W_{c}}{N}(\leq&space;3.6m)'>--------------------"];
    Variable_def--->D--->F(["재하차로의 폭"])
    """

    @rule_method
    def width_of_a_loading_lane(fIWc,iIN) -> RuleUnitResult:
        """재하차로의 수

        Args:
            fIWc (float): 연석,방호 울타리간의 교폭
            iIN (int): 재하차로의 수

        Returns:
            fOW (float): 강교 설계기준(한계상태설계법)  4.3.1.1 재하차로의 수 (2)의 값
            pass_fail (bool): 강교 설계기준(한계상태설계법)  4.3.1.1 재하차로의 수 (2)의 판단 결과
        """

        assert isinstance(fIWc, float)
        assert isinstance(iIN, int)
        assert iIN != 0

        fOW = fIWc / float(iIN)

        if fOW <= 3.6 :
          return RuleUnitResult(
              result_variables = {
                  "fOW": fOW,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "fOW": fOW,
                  "pass_fail": False,
              }
          )