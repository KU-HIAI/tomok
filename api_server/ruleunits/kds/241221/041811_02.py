import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241221_041811_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 21 4.18.11 (2)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '표준호퍼바지선의 충격력'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.18 선박충돌하중: CV
    4.18.10 상부구조물에 작용하는 선박의 충격력
    4.18.11 교각에 작용하는 바지선의 충격력
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 표준호퍼바지선의 충격력];
    B["KDS 24 12 21 4.18.11 (2)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 표준호퍼바지선의 충격력/];
    VarIn1[/입력변수 : 식 4.18-25에 규정도니 바지선의 이물 손상길이/];
    end

    Python_Class ~~~ C(["KDS 24 12 21 4.18.11 (2)"])
		C --> Variable_def

    D{"<img src='https://latex.codecogs.com/svg.image?a_{B}<100mm&space;'>-----------------"};
    E["<img src='https://latex.codecogs.com/svg.image?P_{B}=6.0\times10^{4}a_{B}&space;'>-----------------"];
    F["<img src='https://latex.codecogs.com/svg.image?P_{B}=6.0\times10^{6}+1,600a_{B}&space;'>-------------------------"];
    G(["표준호퍼바지선의 충격력"]);
    Variable_def--->D--Yes--->E--->G
    D--No--->F--->G
    """

    @rule_method
    def impact_force_of_standard_hopper_barge(fIaB) -> RuleUnitResult:
        """표준호퍼바지선

        Args:
            fIaB (float): 식 (4.18-25)에 규정된 바지선의 이물 손상길이

        Returns:
            fOPb (float): 강교 설계기준(한계상태설계법)  4.18.11 교각에 작용하는 바지선의 충격력 (2)의 값
        """

        assert isinstance(fIaB, float)

        if fIaB < 100:
          fOPb = 6.0 * 10**4 * fIaB
        elif fIaB > 100:
          fOPb = 6.0 * 10**6 + 1600 * fIaB

        return RuleUnitResult(
            result_variables = {
                "fOPb": fOPb,
            }
        )