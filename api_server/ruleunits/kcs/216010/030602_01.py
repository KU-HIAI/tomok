import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216010_030602_01(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 10 3.6.2.(1)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-26'
    title = '말비계의 설치높이와 작업발판의 폭'

    description = """
    비계
    3. 시공
    3.6 기타 비계
    3.6.2 말비계
    (1)
    """

    content = """
    #### 3.6.2. 말비계
    (1) 말비계의 설치높이는 2m 이하이어야 하며, 2m를 초과하는 경우에는 작업발판의 폭을 0.4m 이상으로 하여야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 말비계의 설치높이와 작업발판의 폭];
    B["KCS 21 60 10 3.6.2 (1)"];
    B ~~~ A
    end

    KCS(["KCS 21 60 10 3.6.2 (1)"])

    subgraph Variable_def
    VarIn1[/입력변수: 말비계의 설치 높이/];
    VarIn2[/입력변수: 작업발판의 폭/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"말비계의 설치높이 <= 2m"}
    C1 --> |NO|C2{"작업발판의 폭 >= 0.4m"}
    C1 --> |YES|D1([Pass or Fail])
		C2 --> D1([Pass or Fail])
    """

    @rule_method
    def Height_of_Horse_Scaffold(fIHeiHor, fIWidWor) -> bool:
        """ 말비계의 설치높이와 작업발판의 폭
        Args:
            fIHeiHor (float): 말비계의 설치 높이
            fIWidWor (float): 작업발판의 폭

        Returns:
            pass_fail (bool): 비계 3.6.2 말비계 (1)의 판단 결과
        """
        assert isinstance(fIHeiHor, float)

        if fIHeiHor <= 2:
          pass_fail = True
        elif  fIHeiHor > 2:
          if fIWidWor >= 0.4:
            pass_fail = True
          else:
            pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )