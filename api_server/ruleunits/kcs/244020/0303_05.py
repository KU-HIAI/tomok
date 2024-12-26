import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244020_0303_05(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 20 3.3 (5)'
    ref_date = '2016-06-30'
    doc_date = '2023-10-13'
    title = '1차 도포 후 2차 도포할 때까지 시간'

    description = """
    교량방수
    3. 시공
    3.3 접착층의 시공
    (5)
    """
    content = """
    #### 3.3 접착층의 시공
    (5) 2층 이상 도포할 경우에는 1차 도포 후 2차 도포할 때까지 30분 ∼ 60분 정도 건조시킨다. 이는 제품의 종류에 따라 다소 차이가 있으므로 주의하여야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 1차 도포 후 2차 도포할 때까지 시간];
    B["KCS 24 40 20 3.3 (5)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 20 3.3 (5)"])

    subgraph Variable_def
    VarIn1[/입력변수: 1차 도포 후 2차 도포할 때까지 건조시간/];
    VarIn0 & VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{30분 <1차 도포 후 2차 도포할 때까지 시간 < 60분}
    D --> End([Pass or Fail])
    """

    @rule_method

    def drying_time_application(fITimApp) -> RuleUnitResult:
        """
        Args:
            fITimApp (float): 1차 도포 후 2차 도포할 때까지 건조시간

        Returns:
            pass_fail (bool): 교량방수 3.3 접착층의 시공 (5)의 판단 결과
        """
        assert isinstance(fITimApp, float)

        if fITimApp >=30 and fITimApp <=60:
            pass_fail = True
        else:
            pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })