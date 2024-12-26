import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216010_030203_01(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 10 3.2.3.(1)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-25'
    title = '가새재의 설치각도'

    description = """
    비계
    3. 시공
    3.2. 시스템 비계
    3.2.3. 가새재
    (1)
    """

    content = """
    #### 3.2.3. 가새재
    (1) 대각으로 설치하는 가새재는 비계의 외면으로 수평면에 대해 40° ∼ 60° 방향으로 설치하며 수평재 및 수직재에 결속한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 가새재의 설치각도];
    B["KCS 21 60 10 3.2.3 (1)"];
    B ~~~ A
    end

    KCS(["KCS 21 60 10 3.2.3 (1)"])

    subgraph Variable_def
    VarIn[/입력변수: 가새재의 설치각도/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"40° <= 가새재의 설치각도 <= 60"}
    C --> D([Pass or Fail])
    """

    @rule_method
    def Installation_Angle_of_the_Diagonal_Bracing(fIAngBra) -> str:
        """ 가새재의 설치각도
        Args:
            fIAngBra (float): 가새재의 설치각도

        Returns:
            pass_fail (bool): 비계 3.2.3. 가새재 (1)의 판단결과
            sOMetBra (str): 가새재의 설치방법
        """
        assert isinstance(fIAngBra, float)

        if 40 <= fIAngBra <= 60:
          pass_fail = True
          sOMetBra = "수평재 및 수직재에 결속한다"
        else:
          pass_fail = False
          sOMetBra = None

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail,
                    "sOMetBra": sOMetBra,
                }
            )