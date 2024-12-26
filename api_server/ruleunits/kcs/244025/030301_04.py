import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244025_030301_04(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 25 3.3.1 (4)'
    ref_date = '2018-08-30'
    doc_date = '2023-08-15'
    title = '배수관의 경사'

    description = """
    교량배수시설공
    3. 시공
    3.3 배수관의 설치방법
    3.3.1 시공일반
    (4)
    """
    content = """
    #### 3.3.1 시공일반
    (4) 배수관의 경사는 3% 이상으로 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 배수관의 경사];
    B["KCS 24 40 25 3.3.1 (4)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 25 3.3.1 (4)"])

    subgraph Variable_def
    VarIn1[/입력변수: 배수관의 경사/];
    VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"배수관의 경사 ≥ 3%"}
    C --> End([Pass or Fail])
    """

    @rule_method

    def slope_drainage_pipe(fISloDra) -> RuleUnitResult:
        """
        Args:
            fISloDra (float): 배수관의 경사

        Returns:
            pass_fail (bool): 교량배수시설공 3.3.1 시공일반 (4)의 판단 결과
        """
        assert isinstance(fISloDra, float)

        if fISloDra >= 3:
            pass_fail = True
        else:
            pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })