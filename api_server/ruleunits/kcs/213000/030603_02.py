import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS213000_030603_02(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 30 00 3.6.3 (2)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-22'
    title = '흙막이 판의 걸침길이'

    description = """
    가설흙막이 공사
    3. 시공
    3.6 (엄지말뚝 + 흙막이 판)공법
    3.6.3 흙막이 판
    (2)
    """

    content = """
    #### 3.6.3. 흙막이 판
    (2) 흙막이 판은 엄지말뚝 내부로 40mm 이상 걸침길이를 확보하고 끼워 넣는다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 흙막이 판의 걸침길이];
    B["KCS 21 30 00 3.6.3 (2)"];
    B ~~~ A
    end

    KCS(["KCS 21 30 00 3.6.3 (2)"])

    subgraph Variable_def
    VarIn[/입력변수: 흙막이 판의 걸침길이/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"흙막이 판의 걸침길이 >= 40mm"}
    C --> D([Pass or Fail])
    """

    @rule_method
    def Covered_Length_of_Lagging_Board(fILenLag) -> bool:
        """ 흙막이 판의 걸침길이
        Args:
            fILenLag (float): 흙막이 판의 걸침길이

        Returns:
            pass_fail (bool): 가설흙막이 공사 3.6.3 흙막이 판 (2)의 판단 결과
        """
        assert isinstance(fILenLag, float)

        if fILenLag >= 40:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )