import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS213000_0204_04(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 30 00 2.4 (4)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-13'
    title = '슬러리의 비중'

    description = """
    가설흙막이 공사
    2. 자재
    2.4 지하연속벽
    (4)
    """

    content = """
    #### 2.4. 지하연속벽
    (4) 물에 혼합된 벤토나이트 슬러리는 분말 벤토나이트가 안정된 부유 상태에 있어야 하고, 이 때 비중은 1.04~1.36 범위이어야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 슬러리의 비중];
    B["KCS 21 30 00 2.4 (4)"];
    B ~~~ A
    end

    KCS(["KCS 21 30 00 2.4 (4)"])

    subgraph Variable_def
    VarIn1[/입력변수: 슬러리의 비중/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"1.04 <= 슬러리의 비중 <= 1.36"}
    C --> D([Pass or Fail])
    """

    @rule_method
    def Specific_Gravity_of_Slurry(fIGraSlu) -> bool:
        """ 슬러리의 비중
        Args:
            fIGraSlu (float): 슬러리의 비중

        Returns:
            pass_fail (bool): 가설흙막이 공사 2.4 지하연속벽 (4)의 판단 결과
        """
        assert isinstance(fIGraSlu, float)

        if 1.04 <= fIGraSlu <= 1.36:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )