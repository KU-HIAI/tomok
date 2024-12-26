import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216015_0301_03(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 15 3.1.(3)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-25'
    title = '작업발판의 폭'

    description = """
    작업발판 및 통로
    3. 시공
    3.1 작업발판
    (3)
    """

    content = """
    #### 3.1 작업발판
    (3) 작업발판의 전체 폭은 0.4m 이상이어야 하고, 재료를 저장할 때는 폭이 최소한 0.6m 이상이어야 한다. 최대 폭은 1.5m 이내로 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 작업발판의 폭];
    B["KCS 21 60 15 3.1 (3)"];
    B ~~~ A
    end

    KCS(["KCS 21 60 15 3.1 (3)"])

    subgraph Variable_def
    VarIn[/입력변수: 작업발판의 폭/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"재료를 저장할 때"}
    C1 --> |YES|D1{"0.4m <= 작업발판의 폭 <= 1.5m"}
    C1 --> |NO|D2{"0.6m <= 작업발판의 폭 <= 1.5m"}
    D1 & D2 --> E1([Pass or Fail])
    """

    @rule_method
    def Width_of_Working_Platform(bIStoIng, fIWidWor) -> bool:
        """ 작업발판의 폭
        Args:
            bIStoIng (bool): 재료를 저장
            fIWidWor (float): 작업발판의 폭

        Returns:
            pass_fail (bool): 작업발판 및 통로 3.1 작업발판 (3)의 판단 결과
        """
        assert isinstance(fIWidWor, float)
        assert isinstance(bIStoIng, bool)

        if bIStoIng == True:
          if 0.6 <= fIWidWor <= 1.5:
            pass_fail = True
          else:
            pass_fail = False

        elif bIStoIng == False:
          if 0.4 <= fIWidWor <= 1.5:
            pass_fail = True
          else:
            pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )