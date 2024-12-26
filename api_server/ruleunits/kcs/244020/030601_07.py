import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244020_030601_07(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 20 3.6.1 (7)'
    ref_date = '2016-06-30'
    doc_date = '2023-10-17'
    title = '도막식 방수재 시공 시 프라이머 건조 양생 시간'

    description = """
    교량방수
    3. 시공
    3.6 도막식 방수재의 시공
    3.6.1 시공일반
    (7)
    """
    content = """
    #### 3.6.1 시공일반
    (7) 프라이머는 도포 후 20분 ∼ 60분 동안 건조 양생시켜야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 도박식 방수재 시공 시 프라이머 건조 양생 시간];
    B["KCS 24 40 20 3.6.1 (7)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 20 3.5.1 (7)"])

    subgraph Variable_def
    VarIn1[/입력변수: 프라이머 건조 양생 시간/];
    VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"20 < 프라이머 건조 양생 시간 < 60"}
    C --> End([Pass or Fail])
    """

    @rule_method

    def curing_time(fICurTim) -> RuleUnitResult:
        """
        Args:
            fICurTim (float): 프라이머 건조 양생 시간

        Returns:
            pass_fail (bool): 교량방수 3.6.1 시공일반 (7)의 판단 결과
        """
        assert isinstance(fICurTim, float)

        if fICurTim > 20 and fICurTim < 60:
            pass_fail = True
        else:
            pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })