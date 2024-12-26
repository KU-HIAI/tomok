import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04061004_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.6.10.4 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-22'
    title = '쪼갬력'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.10 기초판
    4.6.10.4 암반 위 기둥의 기초
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 쪼갬력];
    B["KDS 24 14 21 4.6.10.4 (2)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수:단면의 압축 연단에서 중립축까지 깊이/];
		VarIn2[/입력변수:부재의 전체 깊이/];
		VarIn3[/입력변수:계수하중에 의한 축력값/];

		VarOut1[/출력변수:쪼갬력/];
		VarOut1~~~VarIn1 & VarIn2 & VarIn3

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.6.10.4 (2)"])
		C --> Variable_def

		Variable_def--->E--->D--->F

		E["h=min(b,H)"]
		D["<img src='https://latex.codecogs.com/svg.image?\inline&space;\LARGE&space;F_s=0.25(1-c/h)N_u'>---------------------------------"]

		F(["쪼갬력"])
    """

    @rule_method
    def cleaving_force(fIc,fIh,fINu) -> RuleUnitResult:
        """쪼갬력

        Args:
            fIc (float): 단면의 압축 연단에서 중립축까지 깊이
            fIh (float): 부재의 전체 깊이
            fINu (float): 계수하중에 의한 축력값

        Returns:
            fOFs (float):  콘크리트교 설계기준 (한계상태설계법)  4.6.10.4 암반 위 기둥의 기초 (2)의 값
        """

        assert isinstance(fIc, float)
        assert isinstance(fIh, float)
        assert fIh != 0
        assert isinstance(fINu, float)

        fOFs = 0.25 * (1 - fIc / fIh) * fINu

        return RuleUnitResult(
            result_variables = {
                "fOFs": fOFs,
            }
        )