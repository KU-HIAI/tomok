import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS115020_010501_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 11 50 20 1.5.1 (1)'
    ref_date = '2021-05-12'
    doc_date = '2023-08-18'
    title = '널말뚝의 연직도'

    description = """
    널말뚝
    1. 일반사항
    1.5 일반요건
    1.5.1 설치허용오차
    (1)
    """
    content = """
    ####1.5.1 설치허용오차
    (1) 연직도는 말뚝길이의 1/100 이내가 되도록 한다.
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 널말뚝의 연직도];
    B["KCS 11 50 20 1.5.1 (1)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 20 1.5.1 (1)"])

    subgraph Variable_def
    VarIn1[/입력변수: 말뚝길이/];
    VarIn2[/입력변수: 연직도/];
    VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"연직도 < 말뚝길이/100"}
    C --> End([Pass or Fail])
    """

    @rule_method
    def verticality_board_pile(fIPilLen, fIVer) -> RuleUnitResult:
        """
        Args:
            fIPilLen (float): 말뚝길이
            fIVer (float): 연직도

        Returns:
            pass_fail (bool): 널말뚝 1.5.1 설치허용오차 (1)의 판단 결과
        """
        assert isinstance(fIPilLen, float)
        assert isinstance(fIVer, float)

        if fIVer <= fIPilLen/100:
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