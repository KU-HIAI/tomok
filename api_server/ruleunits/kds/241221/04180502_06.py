import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241221_04180502_06(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 21 4.18.5.2 (6)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '선박의 통과경로에 직각방향 유속에 대한 보정계수'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.18 선박충돌하중: CV
    4.18.5 연간파괴빈도
    4.18.5.2 항로이탈확률
    (6)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 선박의 통과경로에 직각방향 유속에 대한 보정계수];
    B["KDS 24 12 21 4.18.5.2 (6)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 통과경로에 직각방향 유속에 대한 보정계수/];
    VarIn1[/입력변수 : 선박의 통과경로에 직각방향 유속성분/];
    end

    Python_Class ~~~ C(["KDS 24 12 21 4.18.5.2 (6)"])
		C --> Variable_def

    D["<img src='https://latex.codecogs.com/svg.image?R_{XC}=1.0&plus;0.54V_{XC}'>--------------------------"];
    E(["통과경로에 직각방향 유속에 대한 보정계수"]);
    Variable_def--->D--->E
    """

    @rule_method
    def correction_factor_for_flow_velocity_vertical_to_the_passing_path_of_the_ship(fIVxc) -> RuleUnitResult:
        """선박의 통과경로에 평행한 유속에 대한 보정계수

        Args:
            fIVxc (float): 선박의 통과경로에 평행한 유속성분

        Returns:
            fORxc (float): 강교 설계기준(한계상태설계법)  4.18.5.2 항로이탈확률 (6)의 값
        """

        assert isinstance(fIVxc, float)

        fORxc = 1+0.54*fIVxc

        return RuleUnitResult(
            result_variables = {
                "fORxc": fORxc,
            }
        )