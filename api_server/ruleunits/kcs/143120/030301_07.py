import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_030301_07(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 3.3.1 (7)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-10'
    title = '차폐가스의 이슬점'

    description = """
    용접
    3. 시공
    3.3 용접준비
    3.3.1 용접재료 선택 및 주의사항
    """

    content = """
    #### 3.3.1 용접재료 선택 및 주의사항
    (7) 가스메탈아크용접 또는 플럭스코어드아크용접의 보호가스 및 용접와이어에 대해 다음 규정을 적용한다.
    ① 차폐가스(shield gas)는 이슬점이 –40 ℃ 이하이어야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 차폐가스의 이슬점];
    B["KCS 14 31 20 3.3.1 (7)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 3.3.1 (7)"])

    subgraph Variable_def
    VarIn[/입력변수: 차폐가스의 이슬점/];
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
		Variable_def --> C{"차폐가스의 이슬점 ≤ –40 ℃"}
		C --> D([Pass or Fail])
    """

    @rule_method
    def Dew_Point_of_Shield_Gas(fIDewShi) -> bool:
        """ 차폐가스의 이슬점
        Args:
        fIDewShi (float): 차폐가스의 이슬점

        Returns:
        pass_fail (bool): 용접 3.3.1 용접재료 선택 및 주의사항 (7)의 판단 결과
        """
        assert isinstance(fIDewShi, float)

        if fIDewShi <= -40:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )