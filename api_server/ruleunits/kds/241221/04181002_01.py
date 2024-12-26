import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241221_04181002_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 21 4.18.10.2 (1)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '선박 갑판실의 충격력'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.18 선박충돌하중: CV
    4.18.10 상부구조물에 작용하는 선박의 충격력
    4.18.10.2 갑판실과의 충돌
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 선박 갑판실의 충격력];
    B["KDS 24 12 21 4.18.10.2 (1)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 선박 갑판실의 충격력/];
    VarIn1[/입력변수 : 감소계수/];
    VarIn2[/입력변수 : 식4.18-17에 규정된 선박의 충격력/];
    end

    Python_Class ~~~ C(["KDS 24 12 21 4.18.10.2 (1)"])
		C --> Variable_def

    D["<img src='https://latex.codecogs.com/svg.image?P_{DH}=(R_{DH})(P_{s})'>-----------------------"];
    E(["선박 갑판선의 충격력"]);
    Variable_def--->D--->E
    """

    @rule_method
    def impact_force_of_the_ship_deck_compartment(fIRDH,fIPs) -> RuleUnitResult:
        """선박 갑판실의 충격력

        Args:
            fIRDH (float): 감소계수
            fIPs (float): 식 (4.18-17)에서 규정된 선박의 충격력

        Returns:
            fOPDH (float): 강교 설계기준(한계상태설계법)  4.18.10.2 갑판실과의 충돌 (1)의 값
        """

        assert isinstance(fIRDH, float)
        assert isinstance(fIPs, float)

        fOPDH = fIRDH*fIPs

        return RuleUnitResult(
            result_variables = {
                "fOPDH": fOPDH,
            }
        )