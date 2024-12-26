import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216010_030602_06(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 10 3.6.2.(6)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-26'
    title = '작업발판의 돌출길이'

    description = """
    비계
    3. 시공
    3.6 기타 비계
    3.6.2 말비계
    (6)
    """

    content = """
    #### 3.6.2. 말비계
    (6) 작업발판의 돌출길이는 100mm ∼ 200mm 정도로 하며, 돌출된 장소에서는 작업을 하지 않아야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 작업발판의 돌출길이];
    B["KCS 21 60 10 3.6.2 (6)"];
    B ~~~ A
    end

    KCS(["KCS 21 60 10 3.6.2 (6)"])

    subgraph Variable_def
    VarOut[/"출력변수: 작업여부"/];
    VarIn[/"입력변수: 작업발판의 돌출길이"/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"100mm <= 작업발판의 돌출길이 <= 200mm"}
    C --> E1([Pass or Fail])
    """

    @rule_method
    def Extrusion_Length_of_Working_Platform(fIExtWor) -> bool:
        """ 작업발판의 돌출길이
        Args:
            fIExtWor (float): 작업발판의 돌출길이

        Returns:
            pass_fail (bool): 비계 3.6.2 말비계 (6)의 판단 결과
        """
        assert isinstance(fIExtWor, float)

        if 100 <= fIExtWor <= 200:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail,
                }
            )