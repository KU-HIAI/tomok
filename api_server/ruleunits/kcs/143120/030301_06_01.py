import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_030301_06_01(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 3.3.1 (6) ①'
    ref_date = '2019-05-20'
    doc_date = '2023-11-10'
    title = '용접와이어의 직경'

    description = """
    용접
    3. 시공
    3.3 용접준비
    3.3.1 용접재료 선택 및 주의사항
    """

    content = """
    #### 3.3.1 용접재료 선택 및 주의사항
    (6) 서브머지드아크용접의 용접와이어와 플럭스에 대해 다음 규정을 적용한다.
    ① 용접와이어의 직경은 6.4 mm를 초과하지 않아야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 용접와이어의 직경];
    B["KCS 14 31 20 3.3.1 (6 ①)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 3.3.1 (6) ①"])

    subgraph Variable_def
    VarIn[/입력변수: 용접와이어의 직경/];
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
		Variable_def --> C{"용접와이어의 직경 ≤ 6.4"}
		C --> D([Pass or Fail])
    """

    @rule_method
    def Diameter_of_Welding_Wire(fIDiaWel) -> RuleUnitResult:
        """ 용접와이어의 직경
        Args:
        fIDiaWel (float): 용접와이어의 직경

        Returns:
        pass_fail (bool): 용접 3.3.1 용접재료 선택 및 주의사항 (6) ①의 판단 결과
        """
        assert isinstance(fIDiaWel, float)

        if fIDiaWel <= 6.4:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )