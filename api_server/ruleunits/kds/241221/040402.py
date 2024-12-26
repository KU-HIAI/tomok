import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241221_040402(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 21 4.4.2'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '암거나 매설된 구조물에 대한 충격하중'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.4 충격하중 : IM
    4.4.2 매설된 부재
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 암거나 매설된 구조물에 대한 충격하중];
    B["KDS 24 12 21 4.4.2"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 충격하중계수/];
    VarIn1[/입력변수 : 구조물을 덮고 있는 최소깊이/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ C(["KDS 24 12 21 4.4.2"])
		C --> Variable_def

    D["<img src='https://latex.codecogs.com/svg.image? IM = 40 (1.0-4.1 \times 10^{-4} D_{E}) \geq&space; 0%'>-------------------------------------------------------"]
		E(["충격하중계수"])
    Variable_def--->D--->E
    """

    @rule_method
    def Impact_load_on_hidden_or_buried_structures(fIDE) -> RuleUnitResult:
        """암거나 매설된 구조물에 대한 충격하중

        Args:
            fIDE (float): 구조물을 덮고 있는 최소깊이

        Returns:
            fOIM (float): 강교 설계기준(한계상태설계법)  4.4.2 매설된 부재의 값
            pass_fail (bool): 강교 설계기준(한계상태설계법)  4.4.2 매설된 부재의 판단 결과
        """

        assert isinstance(fIDE, float)

        fOIM = 40*(1.0-4.1*10**(-4)*fIDE)

        if fOIM >= 0 :
          return RuleUnitResult(
              result_variables = {
                  "fOIM": fOIM,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "fOIM": fOIM,
                  "pass_fail": False,
              }
          )