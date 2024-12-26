import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241221_041805_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 21 4.18.5 (1)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '연간파괴빈도'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.18 선박충돌하중: CV
    4.18.5 연간파괴빈도
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 교량구성부재의 연간파괴빈도];
    B["KDS 24 12 21 4.18.5 (1)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 연간파괴빈도/];
    VarIn1[/입력변수 : 형태, 크기 및 하중조건에 의해 분류된 수로를 이용하는 연간선ㅂ가의 수/];
    VarIn2[/입력변수 : 선박의 항로이탈확률/];
    VarIn3[/입력변수 : 항로이탈한 선박이 교각이나 상부구조와 충돌할 기하학적 확률/];
    VarIn4[/입력변수 : 항로이탈한 선박과 충돌할 때 교량이 파괴될 확률/];
    VarOut~~~VarIn3
    VarIn1~~~VarIn4

    end

    Python_Class ~~~ C(["KDS 24 12 21 4.18.5 (1)"])
		C --> Variable_def

    D["AF=(N)(PA)(PG)(PC)"];
    E(["연간파괴빈도"]);
    Variable_def--->D--->E
    """

    @rule_method
    def annual_destruction_frequency(iIN,fIPA,fIPG,fIPC) -> RuleUnitResult:
        """연간파괴빈도

        Args:
            iIN (int): 형태, 크기 및 하중조건에 의해 분류된 수로를 이용하는 연간선박의수
            fIPA (float): 선박의 항로이탈 확률
            fIPG (float): 항로이탈한 선박이 교각이나 상부구조와 충돌할기하학적확률
            fIPC (float): 항로이탈한 선박과 충돌할 때 교량이 파괴될 확률

        Returns:
            fOAF (float): 강교 설계기준(한계상태설계법)  4.18.5 연간파괴빈도 (1)의 값
        """

        assert isinstance(iIN, int)
        assert isinstance(fIPA, float)
        assert isinstance(fIPG, float)
        assert isinstance(fIPC, float)

        fOAF = iIN * fIPA * fIPG * fIPC

        return RuleUnitResult(
            result_variables = {
                "fOAF": fOAF,
            }
        )