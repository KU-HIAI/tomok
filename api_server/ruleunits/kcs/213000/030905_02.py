import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS213000_030905_02(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 30 00 3.9.5 (2)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-25'
    title = '까치발의 각도'

    description = """
    가설흙막이 공사
    3. 시공
    3.9 띠장, 버팀대, 중간말뚝, X-브레이싱
    3.9.5 까치발
    (2)
    """

    content = """
    #### 3.9.5. 까치발
    (2) 까치발의 각도가 45°를 초과하는 경우에는 유효하지 않은 것으로 본다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 까치발의 각도];
    B["KCS 21 30 00 3.9.5 (2)"];
    B ~~~ A
    end

    KCS(["KCS 21 30 00 3.9.5 (2)"])

    subgraph Variable_def
    VarIn[/입력변수: 까치발의 각도/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"까치발의 각도 <= 45°"}

    C --> D([Pass or Fail])
    """

    @rule_method
    def Angle_of_Bracket(fIAngBra) -> bool:
        """ 까치발의 각도
        Args:
            fIAngBra (float): 까치발의 각도

        Returns:
            pass_fail (bool): 가설흙막이 공사 3.9.5 까치발 (2)의 판단 결과
        """
        assert isinstance(fIAngBra, float)

        if fIAngBra <= 45:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )