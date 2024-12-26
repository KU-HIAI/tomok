import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS115010_010502_03(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 11 50 10 1.5.2 (3)'
    ref_date = '2023-09-06'
    doc_date = '2021-05-12'
    title = '수직축의 변동 허용오차'

    description = """
    현장타설 콘크리트 말뚝
    1. 일반사항
    1.5 일반요건
    1.5.2 허용오차
    (3)
    """

    content = """
    #### 1.5.2 허용오차
    (3) 수직축의 변동: 1/40 미만
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: 수직축의 변동 허용오차"];
    B["KCS 11 50 10 1.5.2 (3)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 10 1.5.2 (3)"])

    subgraph Variable_def
		VarIn1[/"입력변수: 수직축의 변동"/];

    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{"수직축의 변동 < 1/40"}
		D --> End([Pass or Fail])
    """

    @rule_method
    def tolerance_of_vertical_axis_fluctuations(fIAxiFLu) -> bool :
        """수직축의 변동
        Args:
            fIAxiFLu (float): 수직축의 변동

        Returns:
            pass_fail (bool): 현장타설 콘크리트 말뚝 1.5.2 허용오차 (3)의 판단 결과
        """
        assert isinstance (fIAxiFLu, float)

        if fIAxiFLu < 1/40:
            pass_fail = True;
        else:
            pass_fail = False;

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail,
                }
            )