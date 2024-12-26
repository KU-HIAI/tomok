import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244020_030601_06(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 20 3.6.1 (6)'
    ref_date = '2016-06-30'
    doc_date = '2023-10-17'
    title = '도막식 방수재 시공 시 프라이머의 사용량'

    description = """
    교량방수
    3. 시공
    3.6 도막식 방수재의 시공
    3.6.1 시공일반
    (6)
    """
    content = """
    #### 3.6.1 시공일반
    (6) 프라이머의 표준 사용량은 0.2 L/m2 ∼ 0.5 L/m2 이며, 재료사양에 따라 변화할 수 있으므로 시험시공을 실시 후 감독자의 승인을 받은 후 시공하여야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 도막식 방수재 시공 시 프라이머의 사용량];
    B["KCS 24 40 20 3.6.1 (6)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 20 3.6.1 (6)"])

    subgraph Variable_def
    VarIn1[/입력변수: 프라이머의 사용량/];
    VarIn2[/입력변수: 시험시공 실시 후 감독자의 승인/];
    VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"0.2 < 프라이머의 사용량 <0.5
    and 시험시공 실시 후 감독자의 승인"}
    C --> End([Pass or Fail])
    """

    @rule_method

    def primer_usage(fIPriUsa,bIAppTri) -> RuleUnitResult:
        """
        Args:
            fIPriUsa (float): 프라이머의 사용량
            bIAppTri (bool): 시험시공 실시 후 감독자의 승인

        Returns:
            pass_fail (bool): 교량방수 3.6.1 시공일반 (6)의 판단 결과
        """
        assert isinstance(fIPriUsa, float)
        assert isinstance(bIAppTri, bool)

        if fIPriUsa > 0.2 and fIPriUsa < 0.5 and bIAppTri:
            pass_fail = True
        else:
            pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })