import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241221_04100102_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 21 4.10.1.2 (1)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '설계기준풍속'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.10 풍하중
    4.10.1 풍속
    4.10.1.2 설계기준풍속
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 일반 중소지간 교량의 설계기준풍속];
    B["KDS 24 12 21 4.10.1.2 (1)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 설계기준풍속/];
    end

    Python_Class ~~~ C(["KDS 24 12 21 4.10.1.2 (1)"])
		C --> Variable_def

    D["<img src='https://latex.codecogs.com/svg.image?V_{D}=40m/s'>"];
    E(["설계기준풍속"]);
    Variable_def--->D--->E
    """

    @rule_method
    def design_wind_speed(fOVD) -> RuleUnitResult:
        """설계기준풍속

        Args:
            fOVD (float): 설계기준풍속

        Returns:
            fOVD (float): 강교 설계기준(한계상태설계법)  4.10.1.2 설계기준풍속 (1)의 값
        """

        fOVD = 40

        return RuleUnitResult(
            result_variables = {
                "fOVD": fOVD,
            }
        )