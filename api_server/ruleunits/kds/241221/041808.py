import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241221_041808(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 21 4.18.8'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '등가 정적선박충격하중'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.18 선박충돌하중: CV
    4.18.8 교각에 작용되는 선박 충격력
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 등가 정적선박충격하중];
    B["KDS 24 12 21 4.18.8"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 등가 정적선박충격하중/];
    VarIn1[/입력변수 : 선박충돌속도/];
    VarIn2[/입력변수 : 선박의 적재중량톤수/];
    end

    Python_Class ~~~ C(["KDS 24 12 21 4.18.8"])
		C --> Variable_def

    F{"선박과 교각이 정면 충돌하는 경우"}
    D["<img src='https://latex.codecogs.com/svg.image?P_{s}=1.2\times&space;10^{5}V\sqrt{DWT}'>-------------------------------"];
    E(["등가 정적선박충격하중"]);
    Variable_def--->F--->D--->E
    """

    @rule_method
    def equivalent_static_ship_impact_load(fIDWT,fIV) -> RuleUnitResult:
        """등가 정적선박충격하중

        Args:
            fIDWT (float): 선박의 흘수
            fIV (float): 수리동적질량계수

        Returns:
            fOPs (float): 강교 설계기준(한계상태설계법)  4.18.8 교각에 작용되는 선박 충격력의 값
        """

        assert isinstance(fIDWT, float)
        assert isinstance(fIV, float)

        fOPs = 1.2 * (10**5) * fIV * (fIDWT**0.5)

        return RuleUnitResult(
            result_variables = {
                "fOPs": fOPs,
            }
        )