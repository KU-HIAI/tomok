import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS212010_030302_02(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 21 20 10 3.3.2 (2)'
    ref_date = '2022-02-23'
    doc_date = '2023-08-16'
    title = '건설용 리프트 준수사항'

    description = """
    건설지원장비
    3. 시공
    3.3 근로자 탑승장비
    3.3.2 건설용 리프트
    (2)
    """

    content = """
    #### 3.3.2. 건설용 리프트
    (2) 리프트의 설치·인상·해체작업 중 다음 사항을 준수하여야 한다.
    ⑤ 순간풍속 10m/s 초과 시에는 설치·인상·해체작업을 해서는 안 된다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 건설용 리프트 준수사항];
    B["KCS 21 20 10 3.3.2 (2)"];
    B ~~~ A
    end

    KCS(["KCS 21 20 10 3.3.2 (2)"])

    subgraph Variable_def
    VarOut[/출력변수:건설용 리프트 작업/];
    VarIn1[/입력변수: 순간풍속/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"순간풍속 > 10m/s"}

    C--> |"YES"|D1["설치, 인상, 해체작업 금지"];
    C--> |"No"|D2["정상"];

		D1 & D2--> E(["건설용 리프트 준수사항"])
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

        if fIInsWin > 10:
          sOLifOpe = "설치·인상·해체작업을 해서는 안 된다."
        else:
          sOLifOpe = "정상운행"

        return RuleUnitResult(
                result_variables = {
                    "sOLifOpe": sOLifOpe
                }
            )