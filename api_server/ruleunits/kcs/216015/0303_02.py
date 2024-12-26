import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216015_0303_02(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 15 3.3.(2)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-25'
    title = '경사로 폭과 인접 발판간의 틈새'

    description = """
    작업발판 및 통로
    3. 시공
    3.3 경사로
    (2)
    """

    content = """
    #### 3.3 경사로
    (2) 경사로 폭은 0.9m 이상이어야 하며, 인접 발판간의 틈새는 30mm 이내가 되도록 설치하여야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 경사로 폭과 인접 발판간의 틈새];
    B["KCS 21 60 15 3.3 (2)"];
    B ~~~ A
    end

    KCS(["KCS 21 60 15 3.3 (2)"])

    subgraph Variable_def
    VarIn1[/입력변수: 경사로 폭/];
    VarIn2[/입력변수: 인접발판 간의 틈새/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"경사로 폭 >= 0.9m"}
    Variable_def --> C2{"인접발판 간의 틈새 <= 30mm"}
    C1 & C2 --> D([Pass or Fail])
    """

    @rule_method
    def Width_of_Ramp(fIWidRam, fIGapAdj) -> RuleUnitResult:
        """ 경사로 폭과 인접 발판간의 틈새
        Args:
            fIWidRam (float): 경사로 폭
            fIGapAdj (float): 인접 발판간의 틈새

        Returns:
            pass_fail (bool): 작업발판 및 통로 3.3 경사로 (2)의 판단 결과
        """
        assert isinstance(fIWidRam, float)
        assert isinstance(fIGapAdj, float)

        if fIWidRam >= 0.9 and fIGapAdj <= 30:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )