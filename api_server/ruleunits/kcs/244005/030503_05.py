import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244005_030503_05(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 05 3.5.3 (5)'
    ref_date = '2018-08-30'
    doc_date = '2023-11-07'
    title = '지진격리받침 탄성중합체의 최대전단변형률'

    description = """
    교량받침
    3. 시공
    3.3 포트받침 및 디스크받침
    3.5.3 품질기준
    (5)
    """
    content = """
    #### 3.3.2 표본선정과 시험
    (5) 지진격리받침 탄성중합체의 최대전단변형률은 상시에는 70%, 지진 시에는 200% 이하이어야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 지진격리받침 탄성중합체의 최대전단변형률];
    B["KCS 24 40 05 3.5.3 (5)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 05 3.5.3 (5)"])

    subgraph Variable_def
    VarIn0[/입력변수: 지진 상황/];
    VarIn1[/입력변수: 지진격리받침 탄성중합체의 전단변형률/];
    VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{지진 상황}
    C --> |False|D{"지진격리받침 탄성중합체의 전단변형률 <= 70%"}
    C --> |True|E{"지진격리받침 탄성중합체의 전단변형률 <= 200%"}
    D & E --> End([Pass or Fail])
    """

    @rule_method

    def strain_seismic_bearing(bISei,fIStrSei) -> RuleUnitResult:
        """
        Args:
            bISei (bool): 지진 상황
            fIStrSei (float): 지진격리받침 탄성중합체의 전단변형률

        Returns:
            pass_fail (bool): 교량받침 3.5.3 품질기준 (5)의 판단 결과
        """
        assert isinstance(bISei, bool)
        assert isinstance(fIStrSei, float)

        if bISei == True:
            if fIStrSei <= 200:
                pass_fail = True
            else:
                pass_fail = False
        else:
            if fIStrSei <= 70:
                pass_fail = True
            else:
                pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })