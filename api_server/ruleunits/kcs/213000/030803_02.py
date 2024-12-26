import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS213000_030803_02(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 30 00 3.8.3 (2)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-25'
    title = 'SGR공법 천공 및 주입'

    description = """
    가설흙막이 공사
    3. 시공
    3.8 그라우팅
    3.8.3 SGR(Space Grouting Rocket) 공법
    (2)
    """

    content = """
    #### 3.8.3. SGR(Space Grouting Rocket) 공법
    (2) 천공 및 주입
    ③ 급결 그라우트재와 완결 그라우트재의 주입비율은 5:5를 기준으로 하고, 지층 조건에 따라 5:5~3:7로 조정할 수 있다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: SGR공법 천공 및 주입];
    B["KCS 21 30 00 3.8.3 (2)"];
    B ~~~ A
    end

    KCS(["KCS 21 30 00 3.8.3 (2)"])


    subgraph Variable_def
    VarIn1[/입력변수: 급결 그라우트재의 주입비율/];
    VarIn2[/입력변수: 완결 그라우트재의 주입비율/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"그라우트재의 주입비율 =
급결 그라우트재의 주입비율/완결 그라우트재의 주입비율"}
    C1 --> C2{"3/7 <= 그라우트재의 주입비율 <= 1"}
    C2 --> D([Pass or Fail])
    """

    @rule_method
    def Injection_Ratio_of_Quicksetting_Grout_Material(fIInjQui, fIInjSlo) -> RuleUnitResult:
        """SGR공법 천공 및 주입
        Args:
            fIInjQui (float): 급결 그라우트재의 주입비율
            fIInjSlo (float): 완결 그라우트재의 주입비율

        Returns:
            pass_fail (bool): 가설흙막이 공사 3.8.3 SGR(Space Grouting Rocket) 공법 (2)의 판단 결과
        """
        assert isinstance(fIInjQui, float)
        assert isinstance(fIInjSlo, float)
        assert fIInjQui > 0
        assert fIInjSlo > 0

        if 3/7 <= fIInjQui / fIInjSlo <= 1:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )