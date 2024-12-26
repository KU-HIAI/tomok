import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS115015_04010101_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 11 50 15 4.1.1.1 (2)'
    ref_date = '2021-05-12'
    doc_date = '2024-02-07'
    title = '말뚝기초의 축방향 허용변위'

    description = """
    깊은기초 설계기준(일반설계법)
    4. 설계
    4.1 말뚝기초
    4.1.1 말뚝의 축방향 지지력과 변위
    4.1.1.1 말뚝기초의 축방향 허용지지력과 허용변위
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 말뚝기초의 축방향 허용변위];
    B["KDS 11 50 15 4.1.1.1 (2)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarIn1[/입력변수: 말뚝기초의 축방향 허용변위/];
    VarIn2[/입력변수: 상부 구조물의 허용변위량/] ;
    VarIn1 ~~~ VarIn2
    end

		Python_Class ~~~ C(["KDS 11 50 15 4.1.1.1 (2)"])
		C --> Variable_def

    D{"말뚝기초의 축방향 허용변위 < 상부 구조물의 허용변위량"};

    Variable_def --> D
    D --> E([PASS or Fail]);
    """

    @rule_method
    def longitudinal_allowable_displacement_of_pile_foundation(fIlaldip,fIaldits) -> RuleUnitResult:
        """말뚝기초의 축방향 허용변위

        Args:
            fIlaldip (float): 말뚝기초의 축방향 허용변위
            fIaldits (float): 상부구조물의 허용변위량

        Returns:
            pass_fail (bool): 깊은기초 설계기준(일반설계법)  4.1.1.1 말뚝기초의 축방향 허용지지력과 허용변위 (2)의 판단 결과
        """

        assert isinstance(fIlaldip, float)
        assert isinstance(fIaldits, float)

        if fIlaldip <= fIaldits:
          return RuleUnitResult(
                result_variables = {
                    "pass_fail": True,
                }
            )
        else:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": False,
                }
            )