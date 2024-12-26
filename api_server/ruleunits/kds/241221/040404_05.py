import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241221_040404_05(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 21 4.4.4 (5)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '충격계수'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.4 충격하중 : IM
    4.4.4 표준열차하중에 대한 동적 효과(충격계수)
    (5)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 충격계수];
    B["KDS 24 12 21 4.4.4 (5)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 동적 효과: 충격계수/];
    VarIn1[/입력변수 : 구조물의 길이 특성치/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ C(["KDS 24 12 21 4.4.4 (5)"])
		C --> Variable_def

    D["<img src='https://latex.codecogs.com/svg.image?I_{m}=\frac{1.44}{\sqrt{L_{e}}-0.2}-0.18'>--------------------------"];
    E{"0 < Im ≤ 0.67"};
    F(["충격계수"])
    G(["Pass or Fail"])
    Variable_def--->D--->E--->F--->G
    """

    @rule_method
    def Impact_coefficient(fILe) -> RuleUnitResult:
        """충격계수

        Args:
            fILe (float): 구조물의 길이 특성치

        Returns:
            fOIm (float): 강교 설계기준(한계상태설계법)  4.4.4 표준열차하중에 대한 동적 효과(충격계수) (5)의 값
            pass_fail (bool): 강교 설계기준(한계상태설계법)  4.4.4 표준열차하중에 대한 동적 효과(충격계수) (5)의 판단 결과
        """

        assert isinstance(fILe, float)
        assert fILe > 0

        fOIm = 1.44/(fILe**0.5-0.2)-0.18

        if 0 < fOIm <= 0.67  :
          return RuleUnitResult(
              result_variables = {
                  "fOIm": fOIm,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "fOIm": fOIm,
                  "pass_fail": False,
              }
          )