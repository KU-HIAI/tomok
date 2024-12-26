import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216015_0304_09_03(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 15 3.4 (9) ③'
    ref_date = '2022-02-23'
    doc_date = '2023-11-15'
    title = '고정식 사다리의 설치'

    description = """
    작업발판 및 통로
    3. 시공
    3.4 사다리
    (9)
    ③
    """

    content = """
    #### 3.4 사다리
    (9) 고정식 사다리는 다음 항에 적합하여야 한다.
    ③ 벽면 상부로부터 0.6m 이상의 여장길이가 있어야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 고정식 사다리의 설치];
    B["KCS 21 60 15 3.4 (9) ③"];
    B ~~~ A
    end

    KCS(["KCS 21 60 15 3.4 (9) ③"])

    subgraph Variable_def
    VarIn1[/입력변수: 여장길이/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"여장길이 >= 0.6m"}

    C1 --> D([Pass or Fail])
    """

    @rule_method
    def Height_of_Fixed_Ladder(fICleLen) -> RuleUnitResult:
        """ 고정식 사다리의 설치
        Args:
        fICleLen (float): 여장길이

        Returns:
        pass_fail (bool): 작업 발판 및 통로 3.4 (9) ③의 판단 결과
        """
        assert isinstance(fICleLen, float)

        if fICleLen >= 0.6:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail,
                }
            )