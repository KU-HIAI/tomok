import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216015_0304_11(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 15 3.4 (11)'
    ref_date = '2022-02-23'
    doc_date = '2023-11-15'
    title = '연장 사다리의 길이'

    description = """
    작업발판 및 통로
    3. 시공
    3.4 사다리
    (11)
    """

    content = """
    #### 3.4. 사다리
   (11) 연장 사다리는 다음 항에 적합하여야 한다.
   ① 총 길이는 15m 이내이어야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 연장 사다리의 길이];
    B["KCS 21 60 15 3.4 (11)"];
    B ~~~ A
    end

    KCS(["KCS 21 60 15 3.4 (11)"])

    subgraph Variable_def
    VarIn[/입력변수: 연장 사다리의 길이/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"연장 사다리의 길이 <= 15m"}
    C --> D([Pass or Fail])
    """

    @rule_method
    def Length_of_Extended_Ladder(fILenExt) -> bool:
        """ 연장 사다리의 길이
        Args:
            fILenExt (float): 연장 사다리 길이

        Returns:
            pass_fail (bool): 작업발판 및 통로 3.4 사다리 (11)의 판단 결과
        """
        assert isinstance(fILenExt, float)

        if fILenExt <= 15:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )