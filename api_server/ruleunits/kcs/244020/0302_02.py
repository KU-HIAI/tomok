import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244020_0302_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 20 3.2 (2)'
    ref_date = '2016-06-30'
    doc_date = '2023-10-12'
    title = '기온 조건에 따른 교량방수 시공'

    description = """
    교량방수
    3. 시공
    3.2 기상 조건
    (2)
    """
    content = """
    #### 3.2 기상 조건
    (2) 시공할 때의 기온은 5 ℃ 이상이어야 한다. 부득이 하여 기온이 5 ℃ 미만에서 시공할 경우는 결로에 주의하여야 하며,
    보온 대책을 수립하여야 한다. 하절기와 같이 시공할 때의 온도가 30 ℃를 넘는 경우 온도에 영향을 받기 쉬운 재료,
    특히 클로로프렌 고무 도막방수재는 새벽이나 야간에 시공하거나 차양을 설치하여 직사광의 영향을 받아 시공면의 온도가 올라가는 것을 막도록 하여야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 기온 조건에 따른 교량방수 시공];
    B["KCS 24 40 20 3.2 (2)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 20 3.2 (2)"])

    subgraph Variable_def
    VarOut[/출력변수: 기온 조건에 따른 교량방수 시공/];
    VarIn1[/입력변수: 기온/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{기온}
    C --> |"5 ℃ ≤ 기온 ≤ 30 ℃"|E[시공이 가능하다]
    C --> |"기온 > 30 ℃"|D[온도에 영향을 받기 쉬운 재료, 특히 클로로프렌 고무 도막방수재는 \n새벽이나 야간에 시공하거나 차양을 설치하여 \n 직사광의 영향을 받아 시공면의 온도가 \n 올라가는 것을 막도록 하여야 한다.\n.]
    C --> |"기온 < 5 ℃"|G[결로에 주의하여야 하며, \n 보온 대책을 수립하여야 한다.]
    D & G & E --> End(["기온 조건에 따른 교량방수 시공"])
    """

    @rule_method

    def temperature(fITem) -> RuleUnitResult:
        """
        Args:
            fITem (float): 기온

        Returns:
            sOTemCon (string): 기온에 따른 시공
        """
        assert isinstance(fITem, float)

        if fITem < 5:
            sOTemCon = "결로에 주의하여야 하며, 보온 대책을 수립하여야 한다"
        elif fITem < 30:
            sOTemCon = "시공이 가능하다"
        else:
            sOTemCon = "온도에 영향을 받기 쉬운 재료, 특히 클로로프렌 고무 도막방수재는새벽이나 야간에 시공하거나 차양을 설치하여 직사광의 영향을 받아 시공면의 온도가 올라가는 것을 막도록 하여야 한다."

        return RuleUnitResult(
            result_variables = {
                "sOTemCon": sOTemCon,
                })