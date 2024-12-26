import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244020_030603_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 20 3.6.3 (1)'
    ref_date = '2016-06-30'
    doc_date = '2023-10-17'
    title = '도막식 방수재 시공 시 접착용 아스팔트의 용해'

    description = """
    교량방수
    3. 시공
    3.6 도막식 방수재 시공
    3.6.3 고무아스팔트계의 도포
    (1)
    """
    content = """
    #### 3.6.3 고무아스팔트계의 도포
    (1) 접착용 아스팔트의 용해 온도는 210 ℃ 정도이며, 전용 용제를 사용하여야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 도막식 방수재 시공 시 접착용 아스팔트의 용해];
    B["KCS 24 40 20 3.6.3 (1)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 20 3.6.3 (1)"])

    subgraph Variable_def
    VarIn1[/입력변수: 용해 온도/];
    VarIn2[/입력변수: 전용 용해 가마/];
    VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"용해 온도 = 210 ℃
    and 전용 용해 가마"}
    C --> End([Pass or Fail])
    """

    @rule_method

    def melt_adhesive_asphalt(fIMelTem,bIDedKil) -> RuleUnitResult:
        """
        Args:
            fIMelTem (float): 용해 온도
            bIDedKil (bool): 전용 용해 가마

        Returns:
            pass_fail (bool): 교량방수 3.6.3 고무아스팔트계의 도포 (1)의 판단 결과
        """
        assert isinstance(fIMelTem, float)
        assert isinstance(bIDedKil, bool)

        if fIMelTem == 210 and bIDedKil == True:
            pass_fail = True
        else:
            pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })