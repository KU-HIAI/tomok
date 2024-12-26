import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142053_020103_07(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 20 53 2.1.3 (7)'
    ref_date = '2022-01-11'
    doc_date = '2023-09-19'
    title = '그라우트의 물-결합재비'

    description = """
    프리스트레스트 콘크리트
    2. 자재
    2.1 구성재료
    2.1.3 프리스트레스트 콘크리트용 그라우트
    (7)
    """
    content = """
    #### 2.1.3 프리스트레스트 콘크리트용 그라우트
    (7) 그라우트의 물-결합재비는 45 % 이하로 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 그라우트의 물-결합재비];
    B["KCS 14 20 53 2.1.3 (7)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 53 2.1.3 (7)"])

    subgraph Variable_def
    VarIn1[/입력변수: 그라우트의 물-결합재비/];
    VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"그라우트의 물-결합재비 ≤ 45"}
    C --> End([Pass or Fail])
    """

    @rule_method

    def water_binder_ratio(fIWatRat) -> RuleUnitResult:
        """
        Args:
            fIWatRat (float): 그라우트의 물-결합재비

        Returns:
            pass_fail (bool): 프리스트레스트 콘크리트 2.1.3 프리스트레스트 콘크리트용 그라우트 (7)의 판단 결과
        """
        assert isinstance(fIWatRat, float)
        assert fIWatRat > 1

        if fIWatRat <= 45:
            pass_fail = True
        else:
            pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })