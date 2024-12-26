import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS212010_030302_01(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 21 20 10 3.3.2 (1)'
    ref_date = '2022-02-23'
    doc_date = '2023-08-16'
    title = '건설용 리프트 준수사항'

    description = """
    건설지원장비
    3. 시공
    3.3 근로자 탑승장비
    3.3.2 건설용 리프트
    (1)
    """

    content = """
    #### 3.3.2. 건설용 리프트
    (1) 리프트의 사용 중 다음 사항을 준수하여야 한다.
    ④ 순간풍속이 10m/s 초과 시에는 점검을 금지하고 15m/s 초과 시는 운행을 해서는 안 된다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 건설용 리프트 준수사항];
    B["KCS 21 20 10 3.3.2 (1)"];
    B ~~~ A
    end

    KCS(["KCS 21 20 10 3.3.2 (1)"])

    subgraph Variable_def
    VarOut[/출력변수:건설용 리프트 작업/];
    VarIn1[/입력변수: 순간풍속/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"순간풍속 > 10m/s"}

    C--> |"YES"|D1{"순강풍속 > 15m/s"};
    C--> |"No"|D2["정상"];
    D1--> |"YES"|E1["운행을 금지"];
    D1--> |"No"|E2["점검을 금지"];

    D2 & E1 & E2--> F(["건설용 리프트 작업"])
    """

    @rule_method
    def Construction_Lift_Operation(fIInsWin) -> str:
        """ 건설용 리프트 준수사항
        Args:
        fIInsWin (float): 순간풍속

        Returns:
        sOLifOpe (str): 건설용 리프트 작업
        """
        assert isinstance(fIInsWin, float)

        if 10 < fIInsWin <= 15:
          sOLifOpe = "점검을 금지한다."
        elif fIInsWin > 15:
          sOLifOpe = "운행을 해서는 안 된다."
        else:
          sOLifOpe = "정상운행"

        return RuleUnitResult(
                result_variables = {
                    "sOLifOpe": sOLifOpe
                }
            )