import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS115015_04010108_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 11 50 15 4.1.1.8 (1)'
    ref_date = '2021-05-12'
    doc_date = '2024-02-07'
    title = '외말뚝 허용인발저항력'

    description = """
    깊은기초 설계기준(일반설계법)
    4. 설계
    4.1 말뚝기초
    4.1.1 말뚝의 축방향 지지력과 변위
    4.1.1.8 말뚝의 축방향 허용인발저항력
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 외말뚝의 허용인발저항력];
    B["KDS 11 50 15 4.1.1.8 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut[/출력변수: 외말뚝의 허용인발저항력/];
    VarIn1[/입력변수: 인발시험 축방향 허용인발저항력/] ;
    VarIn2[/입력변수: 말뚝의 무게/];
    VarIn3[/입력변수: 말뚝본체의 허용인발하중/];

		VarOut~~~VarIn1
		VarOut~~~VarIn2
		VarOut~~~VarIn3
		end

		Python_Class ~~~ C(["KDS 11 50 15 4.1.1.8 (1)"])
		C --> Variable_def;

		D["외말뚝의 허용인발저항력=\n min(인발시험 축방향허용인발저항력+말뚝의 무게, 말뚝본체의 허용인발하중)"]

    Variable_def--->D
    D---->E
    E(["외말뚝의 허용인발저항력"])
    """

    @rule_method
    def allowable_pull_out_resistance_of_single_pile(fIlalpor,fIwepile,fIalpolp) -> RuleUnitResult:
        """외말뚝 허용인발저항력

        Args:
            fIlalpor (float): 축방향 허용인발저항력
            fIwepile (float): 말뚝의 무게
            fIalpolp (float): 말뚝본체의 허용인발하중

        Returns:
            fOaporsp (float): 깊은기초 설계기준(일반설계법)  4.1.1.8 말뚝의 축방향 허용인발저항력 (1)의 값
        """

        assert isinstance(fIlalpor, float)
        assert isinstance(fIwepile, float)
        assert isinstance(fIalpolp, float)

        fOaporsp = min(fIlalpor + fIwepile, fIalpolp)

        return RuleUnitResult(
            result_variables = {
                "fOaporsp": fOaporsp,
            }
        )