import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS115010_010502_02(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 11 50 10 1.5.2 (2)'
    ref_date = '2023-09-06'
    doc_date = '2021-05-12'
    title = '바닥면 지름 허용오차'

    description = """
    현장타설 콘크리트 말뚝
    1. 일반사항
    1.5 일반요건
    1.5.2 허용오차
    (2)
    """

    content = """
    #### 1.5.2 허용오차
    (2) 바닥면 지름: 0 ㎜ ~ 150 ㎜
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: 바닥면 지름 허용오차"];
    B["KCS 11 50 10 1.5.2 (2)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 10 1.5.2 (2)"])

    subgraph Variable_def
		VarIn1[/"입력변수: 바닥면 지름"/];

    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{"0 mm < 바닥면 지름 < 150 mm"}
		D --> End([Pass or Fail])
    """

    @rule_method
    def tolerance_of_diameter_of_bottom_surface(fIDiaBot) -> bool :
        """바닥면 지름
        Args:
            fIDiaBot (float): 바닥면 지름

        Returns:
            pass_fail (bool): 현장타설 콘크리트 말뚝 1.5.2 허용오차 (2)의 판단 결과
        """
        assert isinstance (fIDiaBot, float)

        if 0 < fIDiaBot < 150:
            pass_fail = True
        else:
            pass_fail = False
        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail,
                }
            )