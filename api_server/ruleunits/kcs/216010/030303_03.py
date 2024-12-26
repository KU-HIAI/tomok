import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216010_030303_03(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 10 3.3.3.(3)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-26'
    title = '작업발판의 내민부분'

    description = """
    비계
    3. 시공
    3.3 강관 비계
    3.3.3 장선
    (3)
    """

    content = """
    #### 3.3.3 장선
    (3) 작업발판을 맞댐 형식으로 깔 경우, 장선은 작업발판의 내민 부분이 100mm ∼ 200mm의 범위가 되도록 간격을 정하여 설치하여야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 작업발판의 내민부분];
    B["KCS 21 60 10 3.3.3 (3)"];
    B ~~~ A
    end

    KCS(["KCS 21 60 10 3.3.3 (3)"])

    subgraph Variable_def
    VarIn[/입력변수: 작업발판의 내민 부분/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"100mm <= 작업발판의 내민부분 <= 200mm"}
    C --> D([Pass or Fail])
    """

    @rule_method
    def Overhanging_of_the_Working_Platform(fIOveWor) -> bool:
        """ 작업발판의 내민부분
        Args:
            fIOveWor (float): 작업발판의 내민부분

        Returns:
            pass_fail (bool): 비계 3.3.3 장선 (3)의 판단 결과
        """
        assert isinstance(fIOveWor, float)

        if 100 <= fIOveWor <= 200:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )