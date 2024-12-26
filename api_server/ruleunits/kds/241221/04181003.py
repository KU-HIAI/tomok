import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241221_04181003(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 21 4.18.10.3'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '선박의 돛대 충격력'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.18 선박충돌하중: CV
    4.18.10 상부구조물에 작용하는 선박의 충격력
    4.18.10.3 돛대와의 충돌
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 선박의 돛대 충격력];
    B["KDS 24 12 21 4.18.10.3"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 선박의 돛대 충격력/];
    VarIn1[/입력변수 : 갑판실의 충격력/];
    end

    Python_Class ~~~ C(["KDS 24 12 21 4.18.10.3"])
		C --> Variable_def

    D["<img src='https://latex.codecogs.com/svg.image?P_{MT}=0.10P_{DH}'>--------------------"];
    E(["선박의 돛대 충격력"]);
    Variable_def--->D--->E
    """

    @rule_method
    def the_impact_force_of_a_ship_mast(fIPdh) -> RuleUnitResult:
        """선박의 돛대 충격력

        Args:
            fIPdh (float): 갑판실의 충격력

        Returns:
            fOPmt (float): 강교 설계기준(한계상태설계법)  4.18.10.3 돛대와의 충돌의 값
        """

        assert isinstance(fIPdh, float)

        fOPmt = 0.1*fIPdh

        return RuleUnitResult(
            result_variables = {
                "fOPmt": fOPmt,
            }
        )