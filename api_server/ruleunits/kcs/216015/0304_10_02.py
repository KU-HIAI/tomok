import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216015_0304_10_02(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 15 3.4 (10) ②'
    ref_date = '2022-02-23'
    doc_date = '2023-11-15'
    title = '이동식 사다리의 설치'

    description = """
    작업발판 및 통로
    3. 시공
    3.4 사다리
    (10)
    ②
    """

    content = """
    #### 3.4 사다리
    (10) 이동식 사다리는 다음 항에 적합하여야 한다.
    ② 이동식 사다리의 경사는 수평면으로부터 75°이하로 하는 것을 원칙으로 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 이동식 사다리의 설치];
    B["KCS 21 60 15 3.4 (10) ②"];
    B ~~~ A
    end

    KCS(["KCS 21 60 15 3.4 (10) ②"])

    subgraph Variable_def
    VarIn1[/입력변수: 이동식 사다리의 경사/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"이동식 사다리의 경사 <= 75°"}

    C1 --> D([Pass or Fail])
    """

    @rule_method
    def Length_of_Portable_Ladder(fISloPor) -> bool:
        """ 이동식 사다리의 설치
        Args:
        fISloPor (float): 이동식 사다리 경사

        Returns:
        pass_fail (bool): 작업발판 및 통로 3.4 사다리 (10) ②의 판단 결과
        """
        assert isinstance(fISloPor, float)

        if fISloPor <= 75:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )