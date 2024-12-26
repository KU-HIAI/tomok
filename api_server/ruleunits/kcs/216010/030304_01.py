import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216010_030304_01(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 10 3.3.4.(1)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-26'
    title = '가새재의 설치각도 및 배치간격'

    description = """
    비계
    3. 시공
    3.3 강관 비계
    3.3.4 가새재
    (1)
    """

    content = """
    #### 3.3.4 가새재
    (1) 대각으로 설치하는 가새재는 비계의 외면으로 수평면에 대해 40° ∼ 60° 방향으로 설치하며, 비계기둥에 결속한다. 가새재의 배치간격은 약 10m 마다 교차하는 것으로 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 가새재의 설치각도 및 배치간격];
    B["KCS 21 60 10 3.3.4 (1)"];
    B ~~~ A
    end

    KCS(["KCS 21 60 10 3.3.4 (1)"])

    subgraph Variable_def
    VarIn1[/입력변수: 가새재의 설치각도/];
    VarIn2[/입력변수: 가새재의 배치간격/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"40°<= 가새재의 설치각도 <= 60°"}
    Variable_def --> C2{"가새재의 배치간격 = 10m"}
    C1 & C2 --> D([Pass or Fail])
    """

    @rule_method
    def Installation_Angle_of_the_Diagonal_Bracing(fIAngBra, fISpaBra) -> bool:
        """ 가새재의 설치각도 및 배치간격
        Args:
            fIAngBra (float): 가새재의 설치각도
            fISpaBra (float): 가새재의 배치간격

        Returns:
            pass_fail (bool): 비계 3.3.4 가새재 (1)의 판단 결과
        """
        assert isinstance (fIAngBra, float)
        assert isinstance (fISpaBra, float)

        if 40 <= fIAngBra <= 60 and fISpaBra == 10:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )