import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244025_0301_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 25 3.1 (3)'
    ref_date = '2018-08-30'
    doc_date = '2023-08-15'
    title = '배수구의 간격'

    description = """
    교량배수시설공
    3. 시공
    3.1 시공일반
    (3)
    """
    content = """
    #### 3.1 시공일반
    (3) 배수구의 간격은 20 m 이하로 되어야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 배수구의 간격];
    B["KCS 24 40 25 3.1 (3)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 25 3.1 (3)"])

    subgraph Variable_def
    VarIn1[/입력변수: 배수구의 간격/];
    VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"배수구의 간격 ≤ 20 m"}
    C --> End([Pass or Fail])
    """

    @rule_method

    def drainage_spacing(fISpaDra) -> RuleUnitResult:
        """
        Args:
            fISpaDra (float): 배수구의 간격

        Returns:
            pass_fail (bool): 교량배수시설공 3.1 시공일반 (3)의 판단 결과
        """
        assert isinstance(fISpaDra, float)

        if fISpaDra <= 20:
            pass_fail = True
        else:
            pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })