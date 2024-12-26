import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244005_020604_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 05 2.6.4 (1)'
    ref_date = '2018-08-30'
    doc_date = '2023-10-31'
    title = '받침용 PTFE 수지의 성질'

    description = """
    교량받침
    2. 자재
    2.6 받침의 구성부품
    2.6.4 받침용 PTFE판
    (1)
    """
    content = """
    #### 2.6.4 받침용 PTFE판
    (1) PTFE 수지는 신생재료이어야 하며, 비중은 2.13 ~ 2.19, 녹는점은 328 ℃ ± 1 ℃이어야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 받침용 PTFE 수지의 성질];
    B["KCS 24 40 05 2.6.4 (1)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 05 2.6.4 (1)"])

    subgraph Variable_def
    VarIn1[/입력변수: 신생재료/];
    VarIn2[/입력변수: 비중/];
    VarIn3[/입력변수: 녹는점/];
    VarIn1 & VarIn2 & VarIn3
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{신생재료\n2.13 < 비중 < 2.19 \n 327 ℃ < 녹는점 < 327 ℃\n.}
    C --> End([Pass or Fail])
    """

    @rule_method

    def PTFE_resin(bINewMat,fISpeGra,fIMelPoi) -> RuleUnitResult:
        """
        Args:
            bINewMat (bool): 신생재료
            fISpeGra (float): 비중
            fIMelPoi (float): 녹는점

        Returns:
            pass_fail (bool): 교량받침 2.6.4 받침용 PTFE판 (1)의 판단 결과
        """
        assert isinstance(bINewMat, bool)
        assert isinstance(fISpeGra, float)
        assert isinstance(fIMelPoi, float)

        if bINewMat == True:
            if fISpeGra >= 2.13 and fISpeGra <=2.19:
                if fIMelPoi >=327 and fIMelPoi <=329:
                    pass_fail = True
                else:
                    pass_fail = False
            else:
                pass_fail = False
        else:
            pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })