import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216010_030601_05(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 10 3.6.1.(5)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-26'
    title = '달기틀의 설치간격'

    description = """
    비계
    3. 시공
    3.6 기타 비계
    3.6.1 달비계
    (5)
    """

    content = """
    #### 3.6.1. 달비계
    (5) 달기틀의 설치간격은 1.8m 이하로 하며, 철골보에 확실하게 체결하여야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: 달기틀의 설치간격"];
    B["KCS 21 60 10 3.6.1 (5)"];
    B ~~~ A
    end

    KCS(["KCS 21 60 10 3.6.1 (5)"])

    subgraph Variable_def
    VarIn[/입력변수: 달기틀의 설치간격/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"달기틀의 설치간격 <= 1.8m"}
    C --> D([Pass or Fail])
    """

    @rule_method
    def Scaffold_Frame_Spacing(fIScaSpa) -> bool:
        """ 달기틀의 설치간격
        Args:
            fIScaSpa (float): 달기틀의 설치간격

        Returns:
            pass_fail (bool): 비계 3.6.1 달비계 (5)의 판단 결과
        """
        assert isinstance(fIScaSpa, float)

        if fIScaSpa <= 1.8:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )