import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS213000_030703_10(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 30 00 3.7.3 (10)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-25'
    title = '철근망과 트렌치 측면의 피복두께'

    description = """
    가설흙막이 공사
    3. 시공
    3.7 흙막이 벽 공법
    3.7.3 지하연속벽 공법
    (10)
    """

    content = """
    #### 3.7.3. 지하연속벽 공법
    (10) 철근 또는 보강재 등의 이동방지와 피복 확보를 위하여 간격재를 부착하여야 하며, 철근망과 트랜치 측면은 80mm 이상의 피복이 유지되어야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 철근망과 트렌치 측면의 피복두께];
    B["KCS 21 30 00 3.7.3 (10)"];
    B ~~~ A
    end

    KCS(["KCS 21 30 00 3.7.3 (10)"])

    subgraph Variable_def
    VarIn[/입력변수: 철근망과 트렌치 측면의 피복두께/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"철근망과 트렌치 측면의 피복두께 >= 80mm"}

    C --> D([Pass or Fail])
    """

    @rule_method
    def Reinforcement_Cover_Thickness_of_Steel_Mesh_and_Trench_Sidewalls(fIConThi) -> bool:
        """ 철근망과 트렌치 측면의 피복두께
        Args:
            fIConThi (float): 철근망과 트랜치 측면의 피복두께

        Returns:
            pass_fail (bool): 가설흙막이 공사 3.7.3 지하연속벽 공법 (10)의 판단 결과
        """
        assert isinstance(fIConThi, float)

        if fIConThi >= 80:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )