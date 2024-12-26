import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS213000_020502_05(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 30 00 2.5.2 (5)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-13'
    title = '그라우트의 블리딩률'

    description = """
    가설흙막이 공사
    2. 자재
    2.5. 지반앵커, 타이로드
    2.5.2. 주입재
    (5)
    """

    content = """
    #### 2.5.2. 주입재
    (5) 그라우트의 블리딩률은 3시간 후 최대 2％, 24시간 후 최대 3％ 이하이어야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 그라우트의 블리딩률];
    B["KCS 21 30 00 2.5.2 (5)"];
    B ~~~ A
    end

    KCS(["KCS 21 30 00 2.5.2 (5)"])

    subgraph Variable_def
    VarOut1[/출력변수: 그라우트의 블리딩률/];
    VarIn1[/입력변수: 시간/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"시간 > 3시간"}
    C1 --> |Yes|C2{"시간 > 24시간"}
    C1 <--> |No|C3["3시간 경과후 재시도"]
    C2 --> |Yes|D2["그라우트의 블리딩률 3% 이하"]
    C2 --> |No|D1["그라우트의 블리딩률 2% 이하"]
    D1 & D2 --> E(["그라우트의 블리딩률"]);
    """

    @rule_method
    def Time(fITim) -> float:
        """ 그라우트의 블리딩률
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