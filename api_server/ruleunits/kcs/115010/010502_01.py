import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS115010_010502_01(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 11 50 10 1.5.2 (1)'
    ref_date = '2023-09-06'
    doc_date = '2021-05-12'
    title = '지면에서 잰 중심위치의 변동 허용오차'

    description = """
    현장타설 콘크리트 말뚝
    1. 일반사항
    1.5 일반요건
    1.5.2 허용오차
    (1)
    """

    content = """
    #### 1.5.2 허용오차
    (1) 지면에서 잰 중심위치의 변동: 75 ㎜ 미만
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: 지면에서 잰 중심위치의 변동 허용오차"];
    B["KCS 11 50 10 1.5.2 (1)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 10 1.5.2 (1)"])

    subgraph Variable_def
		VarIn1[/"입력변수: 지면에서 잰 중심위치의 변동"/];

    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{"지면에서 잰 중심위치의 변동 < 75 mm"}
		D --> End([Pass or Fail])
    """

    @rule_method
    def tolerance_of_fluctuation_of_center_position(fIFluCen) -> bool :
        """지면에서 잰 중심위치의 변동
        Args:
            fIFluCen (float): 지면에서 잰 중심위치의 변동

        Returns:
            pass_fail (bool): 현장타설 콘크리트 말뚝 1.5.2 허용오차 (1)의 판단 결과
        """
        assert isinstance (fIFluCen, float)

        if fIFluCen >= 75:
            pass_fail = False
        else:
            pass_fail = True
        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail,
                }
            )