import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244020_0303_05(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 40 20 3.2 (6)'
    ref_date = '2016-06-30'
    doc_date = '2023-10-13'
    title = '1차 도포 후 2차 도포할 때까지 시간'

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량방수
    3. 시공
    3.3 접착층의 시공
    (5)
    """

    # 건설기준문서내용(text)
    content = """
    #### (5) 2층 이상 도포할 경우에는 1차 도포 후 2차 도포할 때까지 30분 ∼ 60분 정도 건조시킨다. 이는 제품의 종류에 따라 다소 차이가 있으므로 주의하여야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 1차 도포 후 2차 도포할 때까지 시간];
    B["KCS 24 40 20 3.3 (5)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 20 3.3 (5)"])

    subgraph Variable_def
    VarOut[/출력변수: 1차 도포 후 2차 도포할 때까지 건조시간/];
    VarIn0[/입력변수: 2층 이상 도포/];
    VarIn1[/입력변수: 1차 도포 후 2차 도포할 때까지 건조시간/];
    VarOut ~~~ VarIn0 & VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{2층 이상 도포}
    C --> D{30분 <1차 도포 후 2차 도포할 때까지 시간 < 60분}
    D --> |True|Pass([Pass])
    D --> |False|Fail([Fail])
    """

    @rule_method
    def drying_time_application(fITimApp)->str:
        """
        Args:
            fITimApp (float): 1차 도포 후 2차 도포할 때까지 건조시간
        Returns:
            sOTimApp (string): 1차 도포 후 2차 도포할 때까지 건조시간
        """
        if fITimApp >30 and fITimApp < 60:
            sOTimApp = "Pass"
        else:
            sOTimApp = "Fail"
        return sOTimApp