import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241221_041812(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 21 4.18.12'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '바지선의 이물 손상길이'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.18 선박충돌하중: CV
    4.18.10 상부구조물에 작용하는 선박의 충격력
    4.18.12 바지선의 이물 손상길이
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 바지선의 이물 손상길이];
    B["KDS 24 12 21 4.18.12"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 바지선의 이물 손상길이/];
    VarIn1[/입력변수 : 선박의 충돌에너지/];
    end

    Python_Class ~~~ C(["KDS 24 12 21 4.18.12"])
		C --> Variable_def

    D["<img src='https://latex.codecogs.com/svg.image?a_{B}=3100(\sqrt{1&plus;1.3\times&space;10^{-7}KE}-1)'>---------------------------------------"];
    E(["바지선의 이물 손상길이"]);
    Variable_def--->D--->E
    """

    @rule_method
    def foreign_body_damage_length_of_barge(fIKE) -> RuleUnitResult:
        """바지선의 이물 손상길이

        Args:
            fIKE (float): 선박의 충돌에너지

        Returns:
            fOaB (float): 강교 설계기준(한계상태설계법)  4.18.12 바지선의 이물 손상길이의 값
        """

        assert isinstance(fIKE, float)

        fOaB = 3100 * ((1 + 1.3 * 10**(-7) * fIKE)**0.5 - 1)

        return RuleUnitResult(
            result_variables = {
                "fOaB": fOaB,
            }
        )