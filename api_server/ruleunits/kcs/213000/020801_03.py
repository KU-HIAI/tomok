import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS213000_020801_03(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 30 00 2.8.1 (3)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-13'
    title = '보강 후 지반의 투수계수'

    description = """
    가설흙막이 공사
    2. 자재
    2.8 지반 그라우팅
    2.8.1 일반사항
    (3)
    """

    content = """
    #### 2.8.1. 일반사항
    (3) 차수용으로 적용된 그라우팅 공법은 지하수의 유입을 방지하기 위하여 보강 후 지반의 투수계수는 k ≤1×10^(-5)cm/s를 확보하여야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 보강 후 지반의 투수계수];
    B["KCS 21 30 00 2.8.1 (3)"];
    B ~~~ A
    end

    KCS(["KCS 21 30 00 2.8.1 (3)"])

    subgraph Variable_def
		VarIn1[/입력변수: 지반의 투수계수/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"지반의 투수계수 <= 1*10^-5cm/s"}
    C --> D([Pass or Fail])
    """

    @rule_method
    def Permeability_Coefficient_of_Soil(fIPerSoi) -> bool:
        """ 보강 후 지반의 투수계수
        Args:
            fIPerSoi (float): 지반의 투수계수

        Returns:
            pass_fail (bool): 가설흙막이 공사 2.8.1 일반사항 (3)의 판단 결과
        """
        assert isinstance(fIPerSoi, float)

        if fIPerSoi <= 0.00001:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )