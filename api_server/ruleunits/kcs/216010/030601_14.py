import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216010_030601_14(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 10 3.6.1.(14)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-26'
    title = '권상기의 지름'

    description = """
    비계
    3. 시공
    3.6. 기타 비계
    3.6.1. 달비계
    (14)
    """

    content = """
    #### 3.6.1. 달비계
    (14) 와이어 로프의 변동 각이 90°보다 작은 권상기의 지름은 와이어 로프 지름의 10배 이상이어야 하며, 변동 각이 90°이상인 경우에는 15배 이상이어야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 권상기의 지름];
    B["KCS 21 60 10 3.6.1 (14)"];
    B ~~~ A
    end

    KCS(["KCS 21 60 10 3.6.1 (14)"])

    subgraph Variable_def
    VarOut1[/출력변수: 권상기의 지름/];
    VarIn1[/입력변수: 와이어 로프의 변동 각/];
    VarIn2[/입력변수: 와이어 로프의 지름/];
    end
    VarOut1 ~~~ VarIn1

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"와이어로프의 변동각 >= 90°"}
    C1 --> |YES|D1["권상기의 지름 >= 와이어 로프의 지름 * 15"]
    C1 --> |NO|D2["권상기의 지름 >= 와이어 로프의 지름 * 10"]
    D1 & D2 --> E1(["권상기의 지름"]);
    """

    @rule_method
    def Angle_of_Variation_of_the_Wire_Rop(fIVarWir, fIDiaWir) -> float:
        """ 권상기의 지름
        Args:
            fIVarWir (float): 와어 로프의 변동각
            fIDiaWir (float): 와이어로프의 지름

        Returns:
            fODiaWin (float): 권상기의 지름
        """
        assert isinstance(fIVarWir, float)
        assert isinstance(fIDiaWir, float)
        assert 0 <= fIVarWir <= 360

        if fIVarWir < 90:
          fODiaWin = 10 * fIDiaWir
        else:
          fODiaWin = 15 * fIDiaWir

        return RuleUnitResult(
                result_variables = {
                    "fODiaWin": fODiaWin
                }
            )