import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS112015_030306_02(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 11 20 15 3.3.6 (2)'
    ref_date = '2023-08-16'
    doc_date = '2020-12-03'
    title = '암반기초 터파기 표면의 기울기'

    description = """
    터파기
    3. 시공
    3.3 시공기준
    3.3.6 암반기초 터파기
    (2)
    """

    content = """
    #### 3.3.6 암반기초 터파기
    (2) 터파기한 표면의 기울기가 1 : 4 이상일 경우에는 계단, 톱니형상 또는 요철처리 등의 방법으로 시공하여야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 암반기초 터파기 표면의 기울기];
    B["KCS 11 20 15 3.3.6 (2)"];
    B ~~~ A
    end

    KCS(["KCS 11 20 15 3.3.6 (2)"])

    subgraph Variable_def
    VarOut[/출력변수: 암반기초 터파기/];
    VarIn1[/입력변수: 터파기한 표면의 기울기/];

    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{터파기한 표면의 기울기 => 1/4}

    C --> D["계단, 톱니형상 또는 요철처리 등의 방법으로 시공"]
		D --> F([암반기초 터파기])
    """

    @rule_method
    def rock_foundation_excavation(fISloSur) -> str:
        """암반기초 터파기 기울기가 1:4 이상일 경우의 시공 방법

        Args:
            fISloSur (float): 터파기한 표면의 기울기

        Returns:
            sOFouExc (str) : 암반기초 터파기
        """
        assert isinstance (fISloSur, float)

        if fISloSur >= 1/4:
            sOFouExc = "계단, 톱니형상 또는 요철처리 등의 방법으로 시공하여야 한다."
        else:
            sOFouExc = None

        return RuleUnitResult(
                result_variables = {
                    "sOFouExc": sOFouExc,
                }
            )