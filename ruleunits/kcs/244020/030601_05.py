import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244020_030601_05(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 40 20 3.6.1 (5)'
    ref_date = '2016-06-30'
    doc_date = '2023-10-17'
    title = '도막식 방수층의 기포'

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량방수
    3. 시공
    3.6 도막식 방수재의 시공
    3.6.1 시공일반
    (5)
    """

    # 건설기준문서내용(text)
    content = """
    #### (5) 도막식 방수층에 발생한 직경 3 mm 이상의 기포는 제거하여야 하며, 3 mm 미만의 기포에 있어서도 포장두께가 얇고 포장층과의 접착력에 악영향을 미친다고 판단될 때에는 제거하여야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 도막식 방수층의 기포];
    B["KCS 24 40 20 3.6.1 (5)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 20 3.6.1 (5)"])

    subgraph Variable_def
    VarOut[/출력변수: 도막식 방수층의 기포/];
    VarIn0[/출력변수: 포장두께가 얇고 포장층과의 접착력에 악영향을 미친다고 판단/];
    VarIn1[/입력변수: 기포 직경/];
    VarOut ~~~ VarIn0 ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"기포 직경 ≥ 3 mm"}
    C --> |"True"|D[기포 제거]
    C --> |"False"|E{포장두께가 얇고 \n 포장층과의 접착력에 \n악영향을 미친다고 판단\n.}
    E --> |"True"|D[기포 제거]
    E --> |"False"|Pass([Pass])
    D --> F([도막식 방수층의 기포])
    """

    @rule_method
    def bubble_waterproof(fIBubDia,bINegAdh)->str:
        """
        Args:
            fIBubDia (float): 기포 직경
            bINegAdh (boolean): 포장두께가 얇고 포장측과의 접착력에 악영향을 미친다고 판단
        Returns:
            sOBubWat (string): 도막식 방수층의 기포
        """
        if fIBubDia >= 3:
            sOBubWat = "기포를 제거해야 한다"
        else:
            if bINegAdh:
                sOBubWat = "기포를 제거해야 한다"
            else:
                sOBubWat = "Pass"
        return sOBubWat