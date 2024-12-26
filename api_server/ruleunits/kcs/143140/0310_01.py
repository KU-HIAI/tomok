import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143140_0310_01(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 40 3.10 (1)'
    ref_date = '2019-05-20'
    doc_date = '2023-10-31'
    title = '일반적인 도장작업 시 기후조건'

    description = """
    도장
    3. 시공
    3.10 도장작업 시의 기후조건
    (1)
    """

    content = """
    #### 3.10 도장작업 시의 기후조건
    (1) 일반적인 도장작업은 대기온도가 5 ℃ 이상, 상대습도 85% 이하인 조건에서 작업해야 한다.
    """

    flowchart ="""
    flowchart TD
    subgraph Python_Class
    A[Title: 일반적인 도장작업 시 기후조건];
    B["KCS 14 31 40 3.10 (1)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 40 3.10 (1)"])

    subgraph Variable_def
    VarIn1[/입력변수: 대기온도/];
    VarIn2[/입력변수: 상대습도/];
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"대기온도≥ 5 ℃ \n & \n 상대습도≤ 85% \n."}
		C --> End([Pass or Fail])
    """


    @rule_method
    def Atmospheric_Temperature(fIAtmTem, fIRelHum) -> bool:
        """ 일반적인 도장작업 시 기후조건
        Args:
        fIAtmTem (float): 대기온도
        fIRelHum (float): 상대습도

        Returns:
        pass_fail (bool): 도장 3.10 도장작업 시의 기후조건 (1)의 판단 결과
        """
        assert isinstance(fIAtmTem, float)
        assert isinstance(fIRelHum, float)

        if fIAtmTem >= 5 and fIRelHum <= 85:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )