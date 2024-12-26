import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216015_0303_05(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 15 3.3.(5)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-25'
    title = '발판 끝단의 돌출길이'

    description = """
    작업발판 및 통로
    3. 시공
    3.3 경사로
    (5)
    """

    content = """
    #### 3.3 경사로
    (5) 발판의 끝단 돌출길이는 장선으로부터 200mm 이내가 되도록 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 발판 끝단의 돌출길이];
    B["KCS 21 60 15 3.3 (5)"];
    B ~~~ A
    end

    KCS(["KCS 21 60 15 3.3 (5)"])

    subgraph Variable_def
    VarIn[/입력변수: 발판 끝단의 돌출길이/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"발판 끝단의 돌출길이 <= 200mm"}
    C --> D([Pass or Fail])
    """

    @rule_method
    def Overhang_Length_of_Tread_End(fIOveLen) -> bool:
        """ 발판 끝단의 돌출길이
        Args:
            fIOveLen (float): 발판 끝단의 돌출길이

        Returns:
            pass_fail (bool): 작업발판 및 통로 3.3 경사로 (5)의 판단 결과
        """
        assert isinstance(fIOveLen, float)

        if fIOveLen <= 200:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )