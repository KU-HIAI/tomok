import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244020_030601_09(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 20 3.6.1 (9)'
    ref_date = '2016-06-30'
    doc_date = '2023-10-17'
    title = '도막방수공사의 시공두께'

    description = """
    교량방수
    3. 시공
    3.6 도막식 방수재의 시공
    3.6.1 시공일반
    (9)
    """
    content = """
    #### 3.6.1 시공일반
    (9) 도막방수공사에 있어서 방수성능을 확보하기 위한 시공두께는 재료의 성능면에서 1.0 mm 이상이 되어야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 도막방수공사의 시공두께];
    B["KCS 24 40 20 3.6.1 (9)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 20 3.6.1 (9)"])

    subgraph Variable_def
    VarIn1[/입력변수: 도막방수공사의 시공두께/];
    VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"도막방수공사의 시공두께 ≥ 1.0 mm"}
    C --> End([Pass or Fail])
    """

    @rule_method

    def thickness_waterproof(fIThiCoa) -> RuleUnitResult:
        """
        Args:
            fIThiCoa (float): 도막방수공사의 시공두께

        Returns:
            pass_fail (bool): 교량방수 3.6.1 시공일반 (9)의 판단 결과
        """
        assert isinstance(fIThiCoa, float)

        if fIThiCoa >=1.0:
            pass_fail = True
        else:
            pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })