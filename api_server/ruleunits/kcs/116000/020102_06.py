import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS116000_020102_06(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 11 60 00 2.1.2 (6)'
    ref_date = '2020-12-03'
    doc_date = '2023-08-16'
    title = '그라우트의 블리딩률'

    description = """
    앵커
    2. 자재
    2.1 재료
    2.1.2 그라우트
    (6)
    """

    content = """
    #### 2.1.2. 그라우트
    (6) 그라우트의 블리딩률은 3시간 후 최대 2%, 24시간 후 최대 3% 이하이어야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 그라우트의 블리딩률];
    B["KCS 11 60 00 2.1.2 (6)"];
    B ~~~ A
    end

    KCS(["KCS 11 60 00 2.1.2 (6)"])

    subgraph Variable_def
    VarOut1[/출력변수: 그라우트의 블리딩률/];
    VarIn1[/입력변수: 시간/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"시간 >= 3시간"}
    C1 --> |Yes|C2{"시간 >= 24시간"}
    C2 --> |Yes|D2["그라우트의 블리딩률 3% 이하"]
    C2 --> |No|D1["그라우트의 블리딩률 2% 이하"]

    D1 & D2 --> E(["그라우트의 블리딩률"]);
    """

    @rule_method
    def Time(fITim) -> float:
        """ 시간에 따른 그라우트의 블리딩률
        Args:
            fITim (float): 시간

        Returns:
            fOBleGro (float): 그라우트의 블리딩률
        """
        assert isinstance(fITim, float)
        assert 3 <= fITim

        if fITim >= 3 and fITim < 24:
            fOBleGro = 3
        elif fITim >= 24:
            fOBleGro = 2

        return RuleUnitResult(
            result_variables={
                "fOBleGro": fOBleGro
            }
        )