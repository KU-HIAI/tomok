import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216010_030302_03(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 10 3.3.2.(3)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-25'
    title = '띠장의 이음위치'

    description = """
    비계
    3. 시공
    3.3 강관 비계
    3.3.2 띠장
    (3)
    """

    content = """
    #### 3.3.2 띠장
    (3) 띠장의 이음위치는 각각의 띠장끼리 최소 300mm 이상 엇갈리게 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 띠장의 이음위치];
    B["KCS 21 60 10 3.3.2 (3)"];
    B ~~~ A
    end

    KCS(["KCS 21 60 10 3.3.2 (3)"])

    subgraph Variable_def
    VarIn[/입력변수: 띠장의 엇갈림 길이/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"띠장의 엇갈림 길이 >= 300mm"}
    C --> D([Pass or Fail])
    """

    @rule_method
    def Crossing_Distance_of_the_Wale(fICroWal) -> bool:
        """ 띠장의 이음위치
        Args:
            fICroWal (float): 띠장의 엇갈림 길이

        Returns:
            pass_fail (bool): 비계 3.3.2 띠장 (3)의 판단 결과
        """
        assert isinstance(fICroWal, float)

        if fICroWal >= 300:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )