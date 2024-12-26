import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS243000_020301_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 24 30 00 2.3.1 (2)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-08'
    title = '강재결함의 보수'

    description = """
    강교량공사
    2. 자재
    2.3 자재의 허용오차
    2.3.1 강판
    (2)
    """
    content = """
    #### 2.3.1 강판
    (2) 강판은 표면에 KS B ISO 4287(표면거칠기 정의 및 표시)에 규정한 100S(0.1 mm)를 초과하는 깊이의 흠이 없는 것을 사용하여야 한다. 강판에 흠이 있을 경우 보수방법은 표 2.3-1에 준하여 시행하되 그라인더 손질 후의 두께는 강판두께의 허용오차 범위 이내로 하며 강판의 손질부분은 깨끗하여야 한다.
    표 2.3-1 강재결함의 보수방법
    \begin{table}[]
    \begin{tabular}{ll}
    홈                & 보수 방법                                                                                 \\
    깊이 0.1 mm ∼ 1 mm & 그라인더로 갈아서 균일하게 한다.                                                                    \\
    깊이 1 mm 이상       & \begin{tabular}[c]{@{}l@{}}덧살용접 후 그라인더로 다듬질하고, 비파괴 검사를 실시하여\\ 건전성을 보장한다.\end{tabular}
    \end{tabular}
    \end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 강재결함의 보수];
    B["KCS 24 30 00 2.3.1 (2)"];
    B ~~~ A
    end

    KCS(["KCS 24 30 00 2.3.1 (2)"])

    subgraph Variable_def
    VarOut[/출력변수: 강재결함의 보수/];
    VarIn1[/입력변수: 홈 깊이/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"홈 깊이"}
    C --> |"홈 깊이 < 0.1"|Pass([Pass])
    C --> |"0.1 < 홈 깊이 < 1"|E["그라인더로 갈아서 균일하게 한다. \n 그라인더 손질 후의 두께는 \n 강판두께의 허용오차 범위 이내로 하며 \n 강판의 손질부분은 깨끗하여야 한다. \n."]
    C --> |"홈 깊이 ≥ 1"|F["덧살용접 후 그라인더로 다듬질하고, \n 비파괴 검사를 실시하여 건전성을 보장한다 \n 그라인더 손질 후의 두께는 \n 강판두께의 허용오차 범위 이내로 하며 \n 강판의 손질부분은 깨끗하여야 한다. \n."]
    E & F --> H(["강재결함의 보수"])
    """

    @rule_method

    def repair_steel(fIGroDep) -> RuleUnitResult:
        """
        Args:
            fIGroDep (float): 홈 깊이

        Returns:
            sORepSte (string): 강재결함의 보수
            pass_fail (bool): 강교량공사 2.3.1 강판 (2)의 판단 결과
        """
        assert isinstance(fIGroDep, float)

        if fIGroDep <=0.1:
            pass_fail = True
            sORepSte = None

        elif fIGroDep <1:
            pass_fail = None
            sORepSte = "그라인더로 갈아서 균일하게 한다."
        else:
            pass_fail = None
            sORepSte = "덧살용접 후 그라인더로 다듬질하고, 비파괴 검사를 실시하여 건전성을 보장한다."

        return RuleUnitResult(
            result_variables = {
                "sORepSte": sORepSte,
                "pass_fail": pass_fail,
                })