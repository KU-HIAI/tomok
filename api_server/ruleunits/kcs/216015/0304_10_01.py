import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216015_0304_10_01(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 15 3.4 (10) ①'
    ref_date = '2022-02-23'
    doc_date = '2023-11-15'
    title = '이동식 사다리의 설치'

    description = """
    작업발판 및 통로
    3. 시공
    3.4 사다리
    (10)
    ①
    """

    content = """
    #### 3.4 사다리
    (10) 이동식 사다리는 다음 항에 적합하여야 한다.
    ① 이동식 사다리의 길이는 6m 이내이어야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 이동식 사다리의 설치];
    B["KCS 21 60 15 3.4 (10) ①"];
    B ~~~ A
    end

    KCS(["KCS 21 60 15 3.4 (10) ①"])

    subgraph Variable_def
    VarIn1[/입력변수: 이동식 사다리의 길이/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"이동식 사다리의 길이 <= 6m"}

    C1 --> D([Pass or Fail])
    """

    @rule_method
    def Length_of_Portable_Ladder(fILenPor) -> bool:
        """ 이동식 사다리의 설치
        Args:
        fILenPor (float): 이동식 사다리 길이

        Returns:
        pass_fail (bool): 작업발판 및 통로 3.4 사다리 (10) ①의 판단 결과
        """
        assert isinstance(fILenPor, float)

        if fILenPor <= 6:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )