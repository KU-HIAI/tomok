import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244020_0302_05(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 20 3.2 (5)'
    ref_date = '2016-06-30'
    doc_date = '2023-10-12'
    title = '콘크리트 바닥판면의 함수율'

    description = """
    교량방수
    3. 시공
    3.2 기상 조건
    (5)
    """
    content = """
    #### 3.2 기상 조건
    (5) 우기 중에는 습도가 높아 콘크리트 바닥판면의 함수율이 10% 이하로 떨어지지 않는 경우도 시공을 피하여야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 콘크리트 바닥판면의 함수율];
    B["KCS 24 40 20 3.2 (5)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 20 3.2 (5)"])

    subgraph Variable_def
    VarIn1[/입력변수: 콘크리트 바닥판면의 함수율/];
    VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{콘크리트 바닥판면의 함수율 ≤ 10%}
    C --> End([Pass or Fail])
    """

    @rule_method

    def moisture_contents(fIMoiDec) -> RuleUnitResult:
        """
        Args:
            fIMoiDec (float): 콘크리트 바닥판면의 함수율

        Returns:
            pass_fail (bool): 교량방수 3.2 기상 조건 (5)의 판단 결과
        """
        assert isinstance(fIMoiDec, float)

        if fIMoiDec <= 10:
            pass_fail = True
        else:
            pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })