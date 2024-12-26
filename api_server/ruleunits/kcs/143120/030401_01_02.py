import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_030401_01_02(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 3.4.1 (1) ②'
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
    ② 경도시험에 있어서 예열하지 않고 최고 경도(H_{v})가 370을 초과 할 때
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 예열에 관한 일반사항];
    B["KCS 14 31 20 3.4.1 (1) ②"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 3.4.1 (1) ②"])

    subgraph Variable_def
    VarIn1[/입력변수: 예열/];
    VarIn2[/입력변수: 최고 경도/];
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
		Variable_def --> C{예열}
		C --> |True|E([Pass or Fail])
		C --> |False|D{최고경도 > 370}
		D --> E
    """

    @rule_method
    def General_About_Preheating(bIPre, fIMaxHar) -> RuleUnitResult:
        """ 예열에 관한 일반사항
        Args:
        bIPre (bool): 예열
        fIMaxHar (float): 최고 경도

        Returns:
        pass_fail (bool): 용접 3.4.1 예열에 관한 일반사항 (1) ②의 판단 결과
        """
        assert isinstance(bIPre, bool)
        assert isinstance(fIMaxHar, float)

        if bIPre == False:
          if fIMaxHar > 370:
            pass_fail = True
          else:
            pass_fail = False
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )