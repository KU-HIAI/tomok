import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS115020_010501_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 11 50 20 1.5.1 (2)'
    ref_date = '2021-05-12'
    doc_date = '2023-08-18'
    title = '말뚝이음 설치'

    description = """
    널말뚝
    1. 일반사항
    1.5 일반요건
    1.5.1 설치허용오차
    (2)
    """
    content = """
    ####1.5.1 설치허용오차
    (2) 말뚝이음은 이음위치가 동일 높이에서 시공되지 않도록 하여야 한다.
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 말뚝이음 설치];
    B["KCS 11 50 20 1.5.1 (2)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 20 1.5.1 (2)"])

    subgraph Variable_def
    VarIn1[/입력변수: 동일 높이의 이음위치/];
    VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"동일 높이의 이음위치"}
    C --> End([Pass or Fail])
    """

    @rule_method
    def pile_joint_install(bIIdeJoi) -> RuleUnitResult:
        """
        Args:
            bIIdeJoi (bool): 동일 높이의 이음위치

        Returns:
            pass_fail (bool): 널말뚝 1.5.1 설치허용오차 (2)의 판단 결과
        """
        assert isinstance(bIIdeJoi, bool)

        if bIIdeJoi:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": False,
                }
            )
        else:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": True,
                }
            )