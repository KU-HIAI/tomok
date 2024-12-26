import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241221_040404_08(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 21 4.4.4 (8)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '충격계수'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.4 충격하중 : IM
    4.4.4 표준열차하중에 대한 동적 효과(충격계수)
    (8)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 충격계수];
    B["KDS 24 12 21 4.4.4 (8)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 구조물의 충격계수/];
    VarIn1[/입력변수 : 구조물에 복토가 없다고 보았을 때의 충격계수/];
    VarIn2[/입력변수 : 구조물 상면에서 침목상단까지의 복토 높이/];
    VarOut ~~~ VarIn1
    VarOut ~~~ VarIn2
    end

    Python_Class ~~~ C(["KDS 24 12 21 4.4.4 (8)"])
		C --> Variable_def

    D["<img src='https://latex.codecogs.com/svg.image?i=i_{0}(H_{c}-1.0)(\geq&space;0)'>------------------------------"];
    E{"구조물의 상면이 흙 1m 이상 덮어져 있는 경우"};
    F(["표준연차하중"]);
    Variable_def--->E--Yes--->D--->F
    """

    @rule_method
    def Impact_coefficient(fIio,fIHc) -> RuleUnitResult:
        """충격계수

        Args:
            fIio (float): 구조물에 복토가 없다고 보았을 때의 충격계수
            fIHc (float): 구조물 상면에서 침목상단까지의 복토 높이

        Returns:
            fOi (float): 강교 설계기준(한계상태설계법)  4.4.4 표준열차하중에 대한 동적 효과(충격계수) (8)의 값
            pass_fail (bool): 강교 설계기준(한계상태설계법)  4.4.4 표준열차하중에 대한 동적 효과(충격계수) (8)의 판단 결과
        """

        assert isinstance(fIio, float)
        assert isinstance(fIHc, float)

        fOi = fIio - 0.1 * (fIHc - 1.0)

        if 0 <= fOi :
          return RuleUnitResult(
              result_variables = {
                  "fOi": fOi,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "fOi": fOi,
                  "pass_fail": False,
              }
          )