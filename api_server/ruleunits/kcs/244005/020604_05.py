import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244005_020604_05(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 05 2.6.4 (5)'
    ref_date = '2018-08-30'
    doc_date = '2023-11-07'
    title = '일반적인 PTFE 섬유의 성질'

    description = """
    교량받침
    2. 자재
    2.6 받침의 구성부품
    2.6.4 받침용 PTFE판
    (5)
    """
    content = """
    #### 2.6.4 받침용 PTFE판
    (5) 일반적인 PTFE 섬유의 인장강도는 17 MPa 이상, 신장률은 75% 이상이어야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 일반적인 PTFE 섬유의 성질];
    B["KCS 24 40 05 2.6.4 (5)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 05 2.6.4 (5)"])

    subgraph Variable_def
    VarIn1[/입력변수: 인장강도/];
    VarIn2[/입력변수: 신장률/];
    VarOut ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"인장강도 ≥ 17 MPa
    신장율 ≥ 200%"}
    C --> End([Pass or Fail])
    """

    @rule_method

    def PTFE_fiber(fITenStr,fIElo) -> RuleUnitResult:
        """
        Args:
            fITenStr (float): 인장강도
            fIElo (float): 신장률

        Returns:
            pass_fail (bool): 교량받침 2.6.4 받침용 PTFE판 (5)의 판단 결과
        """
        assert isinstance(fITenStr, float)
        assert isinstance(fIElo, float)

        if fITenStr >=17 and fIElo >=75:
            pass_fail = True
        else:
            pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })