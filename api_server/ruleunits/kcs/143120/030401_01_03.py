import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_030401_01_03(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 3.4.1 (1) ③'
    ref_date = '2019-05-20'
    doc_date = '2023-11-10'
    title = '예열에 관한 일반사항'

    description = """
    용접
    3. 시공
    3.4 예열
    3.4.1 예열에 관한 일반사항
    """

    content = """
    #### 3.4.1 예열에 관한 일반사항
    (1) 다음의 경우는 예열을 해야 한다.
    ③ 모재의 표면온도가 0℃ 이하일 때
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 예열에 관한 일반사항];
    B["KCS 14 31 20 3.4.1 (1) ③"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 3.4.1 (1) ③"])

    subgraph Variable_def
		VarIn[/입력변수: 모재의 표면온도/]
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
		Variable_def --> C{"모재의 표면온도 ≤ 0℃"}
		C --> D([Pass or Fail])
    """

    @rule_method
    def General_About_Preheating(fISurMet) -> RuleUnitResult:
        """ 예열에 관한 일반사항
        Args:
        fISurMet (float): 모재의 표면온도

        Returns:
        pass_fail (bool): 용접 3.4.1 예열에 관한 일반사항 (1) ③의 판단 결과
        """
        assert isinstance(fISurMet, float)

        if fISurMet <= 0:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )