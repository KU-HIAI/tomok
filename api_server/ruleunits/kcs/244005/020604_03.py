import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244005_020604_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 05 2.6.4 (3)'
    ref_date = '2018-08-30'
    doc_date = '2023-11-07'
    title = '채움재를 넣지 않은 PTFE판의 성질'

    description = """
    교량받침
    2. 자재
    2.6 받침의 구성부품
    2.6.4 받침용 PTFE판
    (3)
    """
    content = """
    #### 2.6.4 받침용 PTFE판
    (3) 채움재를 넣지 않은 PTFE판은 신생 PTFE 수지로 만들어져야 하며, 인장강도는 최소 17.9 MPa 이상, 신장율은 최소 200% 이상이어야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 채움재를 넣지 않은 PTFE판의 성질];
    B["KCS 24 40 05 2.6.4 (3)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 05 2.6.4 (3)"])

    subgraph Variable_def
    VarIn1[/입력변수: 신생 PTFE 수지/];
    VarIn2[/입력변수: 인장강도/];
    VarIn3[/입력변수: 신장율/];
    VarIn1 & VarIn2 & VarIn3
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"신생 PTFE 수지 \n 인장강도 ≥ 17.9 MPa \n 신장율 ≥ 200%\n."}
    C --> End([Pass or Fail])
    """

    @rule_method

    def PTFE_without_backfill(bINewPtf,fITenStr,fIElo) -> RuleUnitResult:
        """
        Args:
            bINewPtf (bool): 신생 PTFE 수지
            fITenStr (float): 인장강도
            fIElo (float): 신장율

        Returns:
            pass_fail (bool): 교량받침 2.6.4 받침용 PTFE판 (3)의 판단 결과
        """
        assert isinstance(bINewPtf, bool)
        assert isinstance(fITenStr, float)
        assert isinstance(fIElo, float)

        if bINewPtf == True and fITenStr >= 17.9 and fIElo >= 200:
            pass_fail = True
        else:
            pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })