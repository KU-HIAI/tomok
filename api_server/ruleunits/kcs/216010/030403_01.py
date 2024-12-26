import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216010_030403_01(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 10 3.4.3.(1)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-26'
    title = '벽 이음재의 수평 및 수직 배치간격'

    description = """
    비계
    3. 시공
    3.4 강관틀 비계
    3.4.3 벽 이음
    (1)
    """

    content = """
    #### 3.4.3 벽 이음
    (1) 벽 이음재의 배치간격은 벽 이음재의 성능과 작용하중을 고려한 구조설계에 따르며, 수직방향 6m, 수평방향 8m 이내로 설치하여야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 벽 이음재의 수평 및 수직 배치간격];
    B["KCS 21 60 10 3.4.3 (1)"];
    B ~~~ A
    end

    KCS(["KCS 21 60 10 3.4.3 (1)"])

    subgraph Variable_def
    VarIn1[/입력변수: 벽 이음재의 수평 배치간격/];
    VarIn2[/입력변수: 벽 이음재의 수직 배치간격/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"벽 이음재의 수평 배치간격 <= 8m"}
    Variable_def --> C2{"벽 이음재의 수직 배치간격 <= 6m"}
    C1 & C2 --> D([Pass or Fail])
    """

    @rule_method
    def Horizontal_Spacing_of_Splice_Members(fIHorSpl, fIVerSpl) -> bool:
        """ 벽 이음재의 수평 및 수직 배치간격
        Args:
            fIHorSpl (float): 벽 이음재의 수평 배치간격
            fIVerSpl (float): 벽 이음재의 수직 배치간격

        Returns:
            pass_fail (bool): 비계 3.4.3 벽 이음 (1)의 판단 결과
        """
        assert isinstance(fIHorSpl, float)
        assert isinstance(fIVerSpl, float)

        if fIHorSpl <= 8 and fIVerSpl <= 6:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )