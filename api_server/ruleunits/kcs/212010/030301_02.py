import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS212010_030301_02(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 20 10 3.3.1 (2)'
    ref_date = '2022-02-23'
    doc_date = '2023-08-16'
    title = '차량탑재형 고소작업대 준수사항'

    description = """
    건설지원장비
    3. 시공
    3.3 근로자 탑승장비
    3.3.1 고소작업대
    (2)
    """

    content = """
    #### 3.3.1. 고소작업대
    (2) 차량탑재형 고소작업대 준수사항
    ⑤ 작업 중인 작업대의 수평은 작업대 평면으로부터 ±5°이상 변동되지 않아야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 차량탑재형 고소작업대 준수사항];
    B["KCS 21 20 10 3.3.1 (2)"];
    B ~~~ A
    end

    KCS(["KCS 21 20 10 3.3.1 (2)"])

    subgraph Variable_def
    VarIn1[/입력변수: 작업대의 수평/];
    VarIn2[/입력변수: 작업대의 평면/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"|작업대의 수평 - 작업대의 평면| < 5°"}

    C--> D(["Pass or Fail"])
    """

    @rule_method
    def Horizontal_of_Workstation(fIHorWor, fISurWor) -> bool:
        """ 차량탑재형 고소작업대 준수사항
        Args:
        fIHorWor (float): 작업대의 수평
        fISurWor (float): 작업대의 평면

        Returns:
        pass_fail (bool): 건설지원장비 3.3.1 고소작업대 (2)의 판단 결과
        """
        assert isinstance(fIHorWor, float)
        assert isinstance(fISurWor, float)

        if -5 <= fIHorWor - fISurWor <= 5:
          pass_fail = True
        else:
          pass_fail = False
        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )