import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244020_030604_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 20 3.6.4 (4)'
    ref_date = '2016-06-30'
    doc_date = '2023-10-17'
    title = '합성수지계 도포 시 기포 제거'

    description = """
    교량방수
    3. 시공
    3.6 도막식 방수재 시공
    3.6.4 합성수지계의 도포
    (4)
    """
    content = """
    #### 3.6.4 합성수지계의 도포
    (4) 직경 3 mm 이상의 큰 기포는 터트린 후에 다음 층의 도포를 시행한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 합성수지계 도포 시 기포 제거];
    B["KCS 24 40 20 3.6.4 (4)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 20 3.6.4 (4)"])

    subgraph Variable_def
    VarOut[/출력변수: 합성수지계 도포 시 기포 제거/];
    VarIn1[/입력변수: 기포 직경/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"기포 직경 ≥ 3mm"}
    C --> |"True"|D[기포는 터트려 제거한 뒤에 다음 층의 도포 시행]
    D --> End([합성수지계 도포 시 기포 제거])
    """

    @rule_method

    def bubble_spreading(fIBubDia) -> RuleUnitResult:
        """
        Args:
            fIBubDia (float): 기포 직경

        Returns:
            sOBubSpr (str): 합성수지계 도포 시 기포 제거
        """
        assert isinstance(fIBubDia, float)

        if fIBubDia >= 3.0:
            sOBubSpr = "기포를 터트려 제거한 후에 다음 층의 도포를 시행"
        else:
            sOBubSpr = None

        return RuleUnitResult(
            result_variables = {
                "sOBubSpr": sOBubSpr,
                })