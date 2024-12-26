import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS115040_020415_04(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 11 50 40 2.4.15 (4)'
    ref_date = '2021-05-12'
    doc_date = '2023-09-18'
    title = '인발시험 시 기준점과 반력판의 거리'

    description = """
    말뚝재하시험
    2. 시험
    2.4 인발재하시험
    2.4.15 기준점 및 기준보
    (4)
    """
    content = """
    #### 2.4.15 기준점 및 기준보
    (4) 기준점은 반력판으로부터 2.5 m 이상 떨어진 곳으로 한다.
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 인발시험 시 기준점과 반력판의 거리];
    B["KCS 11 50 40 2.4.15 (4)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 40 2.4.15 (4)"])

    subgraph Variable_def
    VarIn1[/입력변수: 기준점과 반력판의 거리/];
    VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"기준점과 반력판의 거리 ≥ 2.5 m"}
    C --> End([Pass or Fail])
    """

    @rule_method
    def distance_reference_plate(fIDisPla)-> RuleUnitResult:
        """
        Args:
            fIDisPla (float): 기준점과 반력판의 거리

        Returns:
            pass_fail (bool): 말뚝재하시험 2.4.15 기준점 및 기준보 (4)의 판단 결과
        """
        assert isinstance(fIDisPla, float)
        assert fIDisPla < 100

        if fIDisPla >= 2.5:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": True,
                    })
        else:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": False,
                    })