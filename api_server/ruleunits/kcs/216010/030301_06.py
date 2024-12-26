import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216010_030301_06(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 10 3.3.1.(6)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-25'
    title = '비계기둥에 작용하는 하중'

    description = """
    비계
    3. 시공
    3.3 강관 비계
    3.3.1 비계기둥
    (6)
    """

    content = """
    #### 3.3.1 비계기둥
    (6) 비계기둥 1개에 작용하는 하중은 7.0kN 이내이어야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 비계기둥에 작용하는 하중];
    B["KCS 21 60 10 3.3.1 (6)"];
    B ~~~ A
    end

    KCS(["KCS 21 60 10 3.3.1 (6)"])

    subgraph Variable_def
    VarIn[/입력변수: 비계기둥에 작용하는 하중/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"비계기둥에 작용하는 하중 <= 7.0kN"}
    C --> D([Pass or Fail])
    """

    @rule_method
    def Load_on_the_Scaffolding_Column(fILoaSca) -> bool:
        """ 비계기둥에 작용하는 하중
        Args:
            fILoaSca (float): 비계기둥에 작용하는 하중

        Returns:
            pass_fail (bool): 비계 3.3.1 (6)의 판단 결과
        """
        assert isinstance(fILoaSca, float)

        if fILoaSca <= 7:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )