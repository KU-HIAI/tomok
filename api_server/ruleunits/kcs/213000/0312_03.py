import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS213000_0312_03(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 30 00 3.12. (3)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-25'
    title = '타이지지 방식의 흙파기 깊이'

    description = """
    가설흙막이 공사
    3. 시공
    3.12 타이 로드와 케이블
    (3)
    """

    content = """
    #### 3.12 타이 로드와 케이블
    (3) 타이지지 방식으로 지지할 수 있는 흙파기 깊이는 6m 이내이어야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 타이지지 방식의 흙파기 깊이];
    B["KCS 21 30 00 3.12 (3)"];
    B ~~~ A
    end

    KCS(["KCS 21 30 00 3.12 (3)"])

    subgraph Variable_def
    VarIn1[/입력변수: 흙파기 깊이/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"흙파기 깊이 <= 6m"}
    C --> D([Pass or Fail])
    """

    @rule_method
    def Depth_of_Excavation(fIDepExc) -> bool:
        """ 타이지지 방식의 흙파기 깊이
        Args:
            fIDepExc (float): 흙파기 깊이

        Returns:
            pass_fail (bool): 가설흙막이 공사 3.12 타이 로드와 케이블 (3)의 판단 결과
        """
        assert isinstance(fIDepExc, float)

        if fIDepExc <= 6:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )