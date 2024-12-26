import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241221_041809(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 21 4.18.9'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '선박의 이물손상길이'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.18 선박충돌하중: CV
    4.18.9 선박의 이물손상길이
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 선박의 이물손상길이];
    B["KDS 24 12 21 4.18.9"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 손상을 입은 이물의 길이/];
    VarIn1[/입력변수 : 선박의 충돌에너지/];
    VarIn2[/입력변수 : 선박의 충격력/];
    end

    Python_Class ~~~ C(["KDS 24 12 21 4.18.9"])
		C --> Variable_def

    D["<img src='https://latex.codecogs.com/svg.image?&space;a_{s}=1.54\times&space;10^{3}\left(\frac{KE}{P_{s}}\right)'>-------------------------------"];
    E(["손상을 입은 이물의 길이"]);
    Variable_def--->D--->E
    """

    @rule_method
    def the_length_of_the_damaged_foreign_body(fIKE,fIPs) -> RuleUnitResult:
        """선박의 이물손상길이

        Args:
            fIKE (float): 선박의 충돌에너지
            fIPs (float): 식 (4.18-17)에서 규정된 선박의 충격력

        Returns:
            fOas (float): 강교 설계기준(한계상태설계법)  4.18.9 선박의 이물손상길이의 값
        """

        assert isinstance(fIKE, float)
        assert isinstance(fIPs, float)

        fOas = 1.54 * (10**3) * fIKE / fIPs

        return RuleUnitResult(
            result_variables = {
                "fOas": fOas,
            }
        )