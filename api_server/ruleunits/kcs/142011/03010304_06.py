import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142011_03010304_06(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 20 11 3.1.3.4 (6)'
    ref_date = '2022-01-11'
    doc_date = '2024-05-17'
    title = '철근 용접이음 시 기온'

    description = """
    철근공사
    3. 시공
    3.1 철근
    3.1.3 철근의 이음
    3.1.3.4 용접 이음
    (6)
    """
    content = """
    #### 3.1.3.4 용접 이음
    (6) 대기의 온도가 영하 18 °C 이하일 때에는 철근을 용접할 수 없으며, 대기의 온도가 영하 18°C보다는 높지만 0 °C 이하일 때는 용접을 시작할 때 철근의 온도가 21°C 이상이 되도록 철근을 예열하는 경우에만 용접할 수 있다.
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 철근 용접이음 시 기온];
    B["KCS 14 20 11 3.1.3.4 (6)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 11 3.1.3.4 (6)"])

    subgraph Variable_def
    VarOut[/출력변수: 철근 용접이음 시공/];
    VarIn1[/입력변수: 기온/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"기온"}
    C --> |"≤ -18"|D["철근을 용접할 수 없다"]
    C --> |"-18<기온≤ 0"|E["용접을 시작할 때 철근의 온도가 21°C 이상이 되도록 \n 철근을 예열하는 경우에만 용접할 수 있다."]
    D  & E --> H(["철근 용접이음 시 기온"])
    C --> |"기온 > 0"|Pass([Pass])
    """

    @rule_method
    def temperature_weld_joint(fITem)-> RuleUnitResult:
        """
        Args:
           fITem (float): 기온

        Returns:
            sOWelJoi (str): 철근 용접이음 시공
            pass_fail (bool): 철근공사 3.1.3.4 용접 이음 (6)의 판단 결과

        """
        assert isinstance(fITem, float)

        if fITem <=-18:
            sOWelJoi = "철근을 용접할 수 없다"
            pass_fail = None
        elif fITem > -18 and fITem <=0:
            sOWelJoi = "용접을 시작할 때 철근의 온도가 21°C 이상이 되도록 철근을 예열하는 경우에만 용접할 수 있다"
            pass_fail = None
        elif fITem > 0:
            sOWelJoi = None
            pass_fail = True
        return RuleUnitResult(
            result_variables = {
                "sOWelJoi": sOWelJoi,
                "pass_fail": pass_fail,
                })