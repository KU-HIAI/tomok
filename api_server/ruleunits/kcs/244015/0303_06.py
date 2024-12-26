import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244015_0303_06(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 15 3.3 (6)'
    ref_date = '2018-08-30'
    doc_date = '2023-10-20'
    title = '앵커볼트 구멍의 크기'

    description = """
    교량난간
    3. 시공
    3.3 강재 난간
    (6)
    """
    content = """
    #### 3.3 강재 난간
    (6) 앵커볼트의 구멍은 볼트의 정상 직경보다 50%까지 크게 할 수 있으며, 최대 13 mm까지 크게 할 수 있다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 앵커볼트 구멍의 크기];
    B["KCS 24 40 15 3.3 (6)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 15 3.3 (6)"])

    subgraph Variable_def
    VarOut[/입력변수: 앵커볼트 구멍의 크기/];
    VarIn1[/입력변수: 볼트의 정상직경/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"앵커볼트 구멍의 크기 <= min(볼트의 정상 직경 * 1.5, 13)"}
    C --> End([Pass or Fail])
    """

    @rule_method

    def anchor_bolt_hole(fIDiaBol,fIAncHol) -> RuleUnitResult:
        """
        Args:
            fIDiaBol (float): 볼트의 정상직경
            fIAncHol (float): 앵커볼트 구멍의 크기

        Returns:
            pass_fail (bool): 교량난간 3.3 강재 난간 (6)의 판단 결과
        """
        assert isinstance(fIDiaBol, float)
        assert isinstance(fIAncHol, float)

        if fIAncHol <= min(fIDiaBol*1.5, 13):
            pass_fail = True
        else:
            pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })