import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216010_030601_02(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 10 3.6.1.(2)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-26'
    title = '달비계의 체인, 띠장 및 장선의 간격, 작업발판과 철골보의 거리'

    description = """
    비계
    3. 시공
    3.6 기타 비계
    3.6.1 달비계
    (2)
    """

    content = """
    #### 3.6.1 달비계
    (2) 체인을 이용한 달비계의 체인, 띠장 및 장선의 간격은 1.5m 이내로 하며, 작업발판과 철골보와의 거리는 0.5m 이상을 유지하여야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: 달비계의 체인, 띠장 및 장선의 간격, 작업발판과 철골보의 거리"];
    B["KCS 21 60 10 3.6.1 (2)"];
    B ~~~ A
    end

    KCS(["KCS 21 60 10 3.6.1 (2)"])

    subgraph Variable_def
    VarIn1[/입력변수: 달비계의 체인, 띠장 및 장선의 간격/];
    VarIn2[/입력변수: 작업발판과 철골보와의 거리/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"달비계의 체인, 띠장 및 장선의 간격 <= 1.5m"}
    Variable_def --> C2{"작업발판과 철골보와의 거리 >= 0.5m"}
    C1 & C2 --> D([Pass or Fail])
    """

    @rule_method
    def Spacing_between_the_Chain_and_Wale_and_Joist_of_the_Hanging_Scaffolding(fISpaCha, fIDisSte) -> bool:
        """ 달비계의 체인, 띠장 및 장선의 간격, 작업발판과 철골보의 거리
        Args:
            fISpaCha (float): 달비계의 체인, 띠장 및 장선의 간격
            fIDisSte (float): 작업발판과 철골보와의 거리

        Returns:
            pass_fail (bool): 비계 3.6.1 달비계 (2)의 판단 결과
        """
        assert isinstance(fISpaCha, float)
        assert isinstance(fIDisSte, float)

        if fISpaCha <= 1.5 and fIDisSte >= 0.5:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )