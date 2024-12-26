import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244010_0104_05(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 10 1.4 (5)'
    ref_date = '2023-09-11'
    doc_date = '2018-08-30'
    title = '신축이음의 제작도면'

    description = """
    신축이음
    1. 일반사항
    1.4 제출물
    (5) 제작도면
    """

    content = """
    #### 1.4 제출물
    (5) 제작도면
    총 이동량이 45 mm 이상인 신축이음에 대해서는 감독자에게 제작도면을 제출하여 사전 승인을 받아야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 신축이음의 제작도면];
    B["KCS 24 40 10 1.4 (5)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 10 1.4 (5)"])

    subgraph Variable_def
    VarOut[/출력변수: 신축이음의 제작도면/];
    VarIn1[/입력변수: 신축이음의 총 이동량/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{신축이음의 총 이동량 => 45mm}
    C --> |True|D["감독자에게 제작도면을 제출하여 사전 승인을 받아야 한다"]
    """

    @rule_method
    def joint_drawing(fIMovJoi) -> str :
        """신축이음의 제작도면
        Args:
            fIMovJoi (float): 신축이음의 총 이동량

        Returns:
            sOJoiDra (str) : 신축이음의 제작도면
        """
        assert isinstance(fIMovJoi, float)

        if fIMovJoi >= 45:
            sOJoiDra = "감독자에게 제작도면을 제출하여 사전 승인을 받아야 한다."
        else:
            sOJoiDra = "감독자에게 제작도면을 제출하여 사전 승인을 받지 않아도 된다."

        return RuleUnitResult(
                result_variables = {
                    "sOJoiDra": sOJoiDra,
                }
            )