import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244020_030501_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 20 3.5.1 (1)'
    ref_date = '2016-06-30'
    doc_date = '2023-10-13'
    title = '시트식 방수재의 시공두께'

    description = """
    교량방수
    3. 시공
    3.5 시트식 방수재 시공
    3.5.1 시공일반
    (1)
    """
    content = """
    #### 3.5.1 시공일반
    (1) 시트식 방수재의 시공두께는 3.5 mm 이상을 확보하여야 하고 접착공법을 사용한 경우는 융착형 보다 다소 작은 3.0 mm 이상이 되어야한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 시트식 방수재의 시공두께];
    B["KCS 24 40 20 3.5.1 (1)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 20 3.5.1 (1)"])

    subgraph Variable_def
    VarIn1[/입력변수: 시트식 방수재의 시공두께/];
    VarIn2[/입력변수: 접착공법/];
    VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{접착공법}
    C --> |False|D{"시트식 방수재의 시공두께≥ 3.5 mm"}
    D --> End([Pass or Fail])
    C --> |True|E{"시트식 방수재의 시공두께 ≥ 3.0 mm"}
    E --> End([Pass or Fail])
    """

    @rule_method

    def thickness_sheet_waterproof(fIThiWat,bIAdhMet) -> RuleUnitResult:
        """
        Args:
            fIThiWat (float): 시트식 방수재의 시공두께
            bIAdhMet (bool): 접착공법

        Returns:
            pass_fail (bool): 교량방수 3.5.1 시공일반 (1)의 판단 결과
        """
        assert isinstance(fIThiWat, float)
        assert isinstance(bIAdhMet, bool)

        if bIAdhMet == False:
            if fIThiWat >=3.5:
                pass_fail = True
            else:
                pass_fail = False
        else:
            if fIThiWat >=3.0:
                pass_fail = True
            else:
                pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })