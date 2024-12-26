import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS115040_020214_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 11 50 40 2.2.14 (2)'
    ref_date = '2021-05-12'
    doc_date = '2023-09-18'
    title = '양방향 재하시험 시 가설말뚝을 기준점으로 하는 경우 기준점과 시험말뚝의 거리'

    description = """
    말뚝재하시험
    2. 시험
    2.2 양방향재하시험
    2.2.14 기준점 및 기준보
    (2)
    """
    content = """
    ####
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 양방향 재하시험 시 \n 가설말뚝을 기준점으로 하는 경우 \n 기준점과 시험말뚝의 거리\n.];
    B["KCS 11 50 40 2.2.14 (3)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 40 2.2.14 (3)"])

    subgraph Variable_def
    VarIn1[/입력변수: 기준점과 시험말뚝의 거리/];
    VarIn2[/입력변수: 말뚝지름/];
    VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{"기준점과 시험말뚝의 거리 \n >= max(말뚝지름 * 5, 2000mm)"}
    D --> End(["Pass or Fail"])
    """

    @rule_method
    def distance_reference_point(fIPilDia,fIDisPil)-> RuleUnitResult:
        """
        Args:
            fIPilDia (float): 말뚝지름
            fIDisPil (float): 기준점과 시험말뚝의 거리

        Returns:
            pass_fail (bool): 말뚝재하시험 2.2.14 기준점 및 기준보 (3)의 판단 결과
        """
        assert isinstance(fIPilDia, float)
        assert isinstance(fIDisPil, float)

        if fIDisPil >= max(fIPilDia * 5, 2000):
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": True,})
        else:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": False,})