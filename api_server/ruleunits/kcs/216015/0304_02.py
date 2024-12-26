import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216015_0304_02(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 15 3.4 (2)'
    ref_date = '2022-02-23'
    doc_date = '2023-11-15'
    title = '사다리 발판과 벽사이 간격'

    description = """
    작업발판 및 통로
    3. 시공
    3.4 사다리
    (2)
    """

    content = """
    #### 3.4. 사다리
    (2) 발판과 벽의 사이는 밀착되지 않게 150mm 이상의 간격을 유지하여야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 사다리 발판과 벽사이 간격];
    B["KCS 21 60 15 3.4 (2)"];
    B ~~~ A
    end

    KCS(["KCS 21 60 15 3.4 (2)"])

    subgraph Variable_def
    VarIn[/입력변수: 사다리 발판과 벽사이 간격/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"사다리 발판과 벽사이 간격 >= 150mm"}
    C --> D([Pass or Fail])
    """

    @rule_method
    def Gap_between_Tread_and_Wall(fIGapWal) -> bool:
        """ 사다리 발판과 벽사이 간격
        Args:
            fIGapWal (float): 발판과 벽사이 간격

        Returns:
            pass_fail (bool): 작업발판 및 통로 3.4 사다리 (2)의 판단 결과
        """
        assert isinstance(fIGapWal, float)

        if fIGapWal >= 150:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )