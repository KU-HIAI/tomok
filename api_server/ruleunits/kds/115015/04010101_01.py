import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS115015_04010101_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 11 50 15 4.1.1.1 (1)'
    ref_date = '2021-05-12'
    doc_date = '2024-02-07'
    title = '말뚝기초의 축방향 허용지지력'

    description = """
    깊은기초 설계기준(일반설계법)
    4. 설계
    4.1 말뚝기초
    4.1.1 말뚝의 축방향 지지력과 변위
    4.1.1.1 말뚝기초의 축방향 허용지지력과 허용변위
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 말뚝기초의 축방향 허용지지력];
    B["KDS 11 50 15 4.1.1.1 (1)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarOut[/출력변수: 말뚝기초의 축방향 허용지지력/];
    VarIn1[/입력변수: 말뚝본체의 허용압축하중/] ;
    VarIn2[/입력변수: 지반의 허용지지력/];
    VarOut ~~~ VarIn1
    VarOut ~~~ VarIn2
    end

    Python_Class ~~~ C(["KDS 11 50 15 4.1.1.1 (1)"])
		C --> Variable_def

    D["말뚝기초의 축방향 허용지지력 =\n min (허용압축하중과, 허용지지력)"];

    Variable_def --> D
    D --> E([말뚝기초의 축방향 허용지지력]);
    """

    @rule_method
    def longitudinal_allowable_bearing_capacity_of_pile_foundation(fIalclpb,fIlalbcg) -> RuleUnitResult:
        """말뚝기초의 축방향 허용지지력

        Args:
            fIalclpb (float): 말뚝본체의 허용압축하중
            fIlalbcg (float): 지반의 허용지지력

        Returns:
            fOlalbcp (float): 깊은기초 설계기준(일반설계법)  4.1.1.1 말뚝기초의 축방향 허용지지력과 허용변위 (1)의 값
        """

        assert isinstance(fIalclpb, float)
        assert isinstance(fIlalbcg, float)

        fOlalbcp = min(fIalclpb,fIlalbcg)

        return RuleUnitResult(
            result_variables = {
                "fOlalbcp": fOlalbcp,
            }
        )