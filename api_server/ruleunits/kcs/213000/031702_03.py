import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS213000_031702_03(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 30 00 3.17.2.(3)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-25'
    title = '매몰되는 말뚝의 유지관리'

    description = """
    가설흙막이 공사
    3. 시공
    3.17 해체 및 철거
    3.17.2 매몰
    (3)
    """

    content = """
    #### 3.17.2. 매몰
    (3) 매몰되는 말뚝은 차후의 유지관리를 위하여 지표면에서 2m 이하 하단까지 절단하여야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 매몰되는 말뚝의 유지관리];
    B["KCS 21 30 00 3.17.2 (3)"];
    B ~~~ A
    end

    KCS(["KCS 21 30 00 3.17.2 (3)"])

    subgraph Variable_def
    VarIn[/입력변수: 매몰되는 말뚝의 지표면에서의 깊이/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"매몰되는 말뚝의 지표면에서의 깊이 <= 2m"}

    C -->  D([Pass or Fail])
    """

    @rule_method
    def Depth_of_Driven_Piles_below_Ground_Surface(fIDepPil) -> bool:
        """ 매몰되는 말뚝의 유지관리
        Args:
            fIDepPil (float): 매몰되는 말뚝의 지표면에서의 깊이

        Returns:
            pass_fail (bool): 가설흙막이 공사 3.17.2 매몰 (3)의 판단 결과
        """
        assert isinstance(fIDepPil, float)

        if fIDepPil <= 2:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )