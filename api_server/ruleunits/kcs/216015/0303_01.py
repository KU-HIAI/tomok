import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216015_0303_01(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 15 3.3.(1)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-25'
    title = '경사로 지지기둥 설치간격'

    description = """
    작업발판 및 통로
    3. 시공
    3.3. 경사로
    (1)
    """

    content = """
    #### 3.3. 경사로
    (1) 경사로 지지기둥은 3m 이내마다 설치하여야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 경사로 지지기둥 설치간격];
    B["KCS 21 60 15 3.3 (1)"];
    B ~~~ A
    end

    KCS(["KCS 21 60 15 3.3 (1)"])

    subgraph Variable_def
    VarIn1[/입력변수: 경사로 지지기둥 설치간격/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"경사로 지지기둥 설치간격 <= 3m"}
    C1 --> D1([Pass or Fail]);
    """

    @rule_method
    def Spacing_between_Ramp_Support_Pillars(fISpaSup) -> bool:
        """ 경사로 지지기둥 설치간격
        Args:
            fISpaSup (float): 경사로 지지기둥 간격

        Returns:
            pass_fail (bool): 작업발판 및 통로 3.3. 경사로 (1)의 판단 결과
        """
        assert isinstance(fISpaSup, float)

        if fISpaSup <= 3:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )