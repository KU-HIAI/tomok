import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS213000_030702_10(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 21 30 00 3.7.2 (10)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-22'
    title = 'SCW의 교반'

    description = """
    가설흙막이 공사
    3. 시공
    3.7. 흙막이 벽 공법
    3.7.2. SCW공법
    (10)
    """

    content = """
    #### 3.7.1. SCW공법
    (10) SCW의 교반은 다음 사항을 참조한다.
    ① 교반속도 : 사질토(1m/min), 점성토(0.5~1m/min)
    ③ 벽체하단부 : 하부 2m는 2회 교반 실시
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: SCW의 교반];
    B["KCS 21 30 00 3.7.2 (10)"];
    B ~~~ A
    end

    KCS(["KCS 21 30 00 3.7.2 (10)"])

    subgraph Variable_def
    VarOut1[/출력변수: 교반 속도/];
    VarOut2[/출력변수: 교반 횟수/];
    VarIn1[/입력변수: 토양의 종류/];
    VarIn2[/입력변수: SCW의 깊이/];
    end
    VarOut1 & VarOut2 ~~~ VarIn1

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"토양의 종류"}
    C1 --> |사질토|D1["= 1m/min"]
    C1 --> |점성토|D2["0.5m/min <= <= 1m/min"]
    Variable_def --> C2{"SCW의 깊이 >= 2m"}
    C2 --> |YES|D3["2회"]

    D1 & D2 --> E1(["교반 속도"]);
    D3 --> E2(["교반 횟수"]);
    """
    @rule_method
    def Type_of_Soil(sITypSoi, fIDepSCW) -> str:
        """ SCW의 교반
        Args:
            sITypSoi (str): 토양의 종류
            fIDepSCW (float): SCW의 깊이

        Returns:
            sOMixSpe (str): 교반속도
            nONumMix (int): 교반 횟수
        """
        assert isinstance(sITypSoi, str)
        assert sITypSoi in["사질토", "점성토"]
        assert isinstance(fIDepSCW, float)

        if sITypSoi == "사질토":
          sOMixSpe = "1m/min"
        elif sITypSoi == "점성토":
          sOMixSpe = "0.5~1m/min"

        if fIDepSCW >= 2:
          nONumMix = 2
        else:
          nONumMix = 1

        return RuleUnitResult(
                result_variables = {
                    "sOMixSpe": sOMixSpe,
                    "nONumMix": nONumMix,
                }
            )