import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_030602_03(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 3.6.2 (3)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-13'
    title = '아래보기자세의 필릿용접부에 사용하는 전류'

    description = """
    용접
    3. 시공
    3.6 서브머지드아크용접(SAW)
    3.6.2 단일전극 서브머지드아크용접
    """

    content = """
    #### 3.6.2 단일전극 서브머지드아크용접
    (3) 아래보기자세의 필릿용접부에 사용하는 전류는 1000A를 초과하지 않아야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: 아래보기자세의 필릿용접부에 사용하는 전류"];
    B["KCS 14 31 20 3.6.2 (3)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 3.6.2 (3)"])

    subgraph Variable_def
    VarIn[/입력변수: 아래보기자세의 필릿용접부에 사용하는 전류/];
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"아래보기자세의 필릿용접부에 사용하는 전류 ≤ 1000 A"}
    C --> D([Pass or Fail])
    """

    @rule_method
    def Current_Used_for_Fillet_Weld_in_Flat_Position(fICurFla) -> RuleUnitResult:
        """ 아래보기자세의 필릿용접부에 사용하는 전류
        Args:
        fICurFla (float): 아래보기자세의 필릿용접부에 사용하는 전류

        Returns:
        pass_fail (bool): 용접 3.6.2 단일전극 서브머지드아크용접 (3)의 판단 결과
        """
        assert isinstance(fICurFla, float)

        if fICurFla <= 1000:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )