import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241221_04090201_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 21 4.9.2.1 (1)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '하부구조물에 종방향으로 작용되는 유수에 의한 압력'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.9 정수압, 유수압, 부력, 파압: WA, BP, WP
    4.9.2 유수압
    4.9.2.1 종방향
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 하부구조물에 종방향으로 작용되는 유수에 의한 압력];
    B["KDS 24 12 21 4.9.2.1 (1)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 유수에 의한 압력/];
    VarIn1[/입력변수 : 교각의 기하학적 형상에 따른 항력계수/];
    VarIn2[/입력변수 : 설계홍수시의 설계유속/];
    VarOut ~~~ VarIn1
    VarOut ~~~ VarIn2
    end

    Python_Class ~~~ C(["KDS 24 12 21 4.9.2.1 (1)"])
		C --> Variable_def

    D["<img src='https://latex.codecogs.com/svg.image?p=0.514C_{D}V^{2}'>-----------------"];
    E(["유수에 의한 압력"]);
    Variable_def--->D--->E
    """

    @rule_method
    def Longitudinal_pressure_caused_by_running_water(fICD,fIV) -> RuleUnitResult:
        """유수에 의한 종방향 압력

        Args:
            fICD (float): 교각의 기하학적 형상에 따른 항력계수
            fIV (float): 설계홍수시의 설계유속

        Returns:
            fOp (float): 강교 설계기준(한계상태설계법)  4.9.2.1 종방향 (1)의 값
        """

        assert isinstance(fICD, float)
        assert isinstance(fIV, float)

        fOp = 0.514 * fICD * (fIV**2)

        return RuleUnitResult(
            result_variables = {
                "fOp": fOp,
            }
        )