import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244020_030601_05(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 20 3.6.1 (5)'
    ref_date = '2016-06-30'
    doc_date = '2023-10-17'
    title = '도막식 방수층의 기포 제거'

    description = """
    교량방수
    3. 시공
    3.6 도막식 방수재의 시공
    3.6.1 시공일반
    (5)
    """
    content = """
    #### 3.6.1 시공일반
    (5) 도막식 방수층에 발생한 직경 3 mm 이상의 기포는 제거하여야 하며, 3 mm 미만의 기포에 있어서도 포장두께가 얇고 포장층과의 접착력에 악영향을 미친다고 판단될 때에는 제거하여야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 도막식 방수층의 기포 제거];
    B["KCS 24 40 20 3.6.1 (5)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 20 3.6.1 (5)"])

    subgraph Variable_def
    VarOut[/출력변수: 도막식 방수층의 기포 제거/];
    VarIn1[/입력변수: 기포 직경/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"기포 직경 ≥ 3 mm"}
    C --> |"True"|D[기포 제거]
    C --> |"False"|E[포장두께가 얇고 \n 포장층과의 접착력에 \n악영향을 미친다고 판단될 때에는 기포 제거\n.]
    D & E --> F([도막식 방수층의 기포 제거])
    """

    @rule_method

    def bubble_waterproof(fIBubDia) -> RuleUnitResult:
        """
        Args:
            fIBubDia (float): 기포 직경

        Returns:
            sOBubWat (str): 도막식 방수층의 기포 제거
        """
        assert isinstance(fIBubDia, float)

        if fIBubDia >= 3:
            sOBubWat = "기포를 제거해야 한다"
        else:
            sOBubWat = "포장두께가 얇고 포장층과의 접착력에 악영향을 미친다고 판단될 때에는 제거"

        return RuleUnitResult(
            result_variables = {
                "sOBubWat": sOBubWat,
                })