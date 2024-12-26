import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216010_030602_04(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 10 3.6.2.(4)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-26'
    title = '말비계용 사다리 기둥재의 설치각도'

    description = """
    비계
    3. 시공
    3.6 기타 비계
    3.6.2 말비계
    (4)
    """

    content = """
    #### 3.6.2. 말비계
    (4) 말비계용 사다리는 기둥재와 수평면과의 각도는 75°이하, 기둥재와 받침대와의 각도는 85°이하가 되도록 설치한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 말비계용 사다리 기둥재의 설치각도];
    B["KCS 21 60 10 3.6.2 (4)"];
    B ~~~ A
    end

    KCS(["KCS 21 60 10 3.6.2 (4)"])

    subgraph Variable_def
    VarIn1[/"입력변수: 말비계용 사다리 기둥재와 수평면과의 각도"/];
    VarIn2[/"입력변수: 말비계용 사다리 기둥재와 받침대와의 각도"/];
    end
    VarIn1 ~~~ VarIn2

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"말비계용 사다리 기둥재와 </br> 수평면과의 각도 <= 75°"}
    Variable_def --> C2{"말비계용 사다리 기둥재와 </br> 받침대와의 각도 <= 85°"}
    C1 & C2 --> D([Pass or Fail])
    """

    @rule_method
    def Angle_between_the_Ladder_Rung_and_the_Horizontal_Plane(fIAngHor, fIAngBea) -> bool:
        """ 말비계용 사다리 기둥재의 설치각도
        Args:
            fIAngHor (float): 말비계용 사다리 기둥재와 수평면과의 각도
            fIAngBea (float): 말비계용 사다리 기둥재와 받침대와의 각도

        Returns:
            pass_fail (bool): 비계 3.6.2 말비계 (4)의 판단 결과
        """
        assert isinstance(fIAngHor, float)
        assert isinstance(fIAngBea, float)

        if fIAngHor <= 75 and fIAngBea <= 85:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
            result_variables={
                "pass_fail": pass_fail
            }
        )