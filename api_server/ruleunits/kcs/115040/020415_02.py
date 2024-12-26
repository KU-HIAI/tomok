import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS115040_020415_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 11 50 40 2.4.15 (2)'
    ref_date = '2021-05-12'
    doc_date = '2023-09-18'
    title = '인발시험 시 사용말뚝을 기준점으로 하는 경우 기준점의 위치'

    description = """
    말뚝재하시험
    2. 시험
    2.4 인발재하시험
    2.4.15 기준점 및 기준보
    (2)
    """
    content = """
    #### 2.4.15 기준점 및 기준보
    (2) 사용말뚝을 기준점으로 하는 경우 시험말뚝 및 반력말뚝으로부터 각 말뚝지름의 2.5배 이상 떨어진 위치의 것을 이용하는 것을 원칙으로 한다.
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 인발시험 시 사용말뚝을 기준점으로 하는 경우 기준점의 위치];
    B["KCS 11 50 40 2.4.15 (2)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 40 2.4.15 (2)"])

    subgraph Variable_def
    VarIn1[/입력변수: 기준점과 시험말뚝 및 반력말뚝의 거리/];
    VarIn2[/입력변수: 말뚝지름/];
    VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def -->  D{"기준점과 시험말뚝의 거리 \n >= 말뚝지름 * 2.5"}
    D --> End([Pass or Fail])
    """

    @rule_method
    def distance_reference_point(fIPilDia, fIDisPil)-> RuleUnitResult:
        """
        Args:
            fIPilDia (float): 말뚝지름
            fIDisPil (float): 기준점과 시험말뚝 및 반력말뚝의 거리

        Returns:
            pass_fail (bool): 말뚝재하시험 2.4.15 기준점 및 기준보 (2)의 판단 결과
        """
        assert isinstance(fIPilDia, float)
        assert isinstance(fIDisPil, float)

        if fIDisPil >= fIPilDia * 2.5:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": True,
                    })
        else:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": False,
                    })