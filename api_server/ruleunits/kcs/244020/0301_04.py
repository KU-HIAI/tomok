import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244020_0301_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 20 3.1 (4)'
    ref_date = '2016-06-30'
    doc_date = '2023-10-12'
    title = '바닥판면의 요철부위'

    description = """
    교량방수
    3. 시공
    3.1 시공 전 준비사항
    (4)
    """
    content = """
    #### 3.1 시공 전 준비사항
    (4) 바닥판면의 요철부위 중 직경 10 mm 이상이며 깊이 3 mm 이상 패인부분은 이물질을 제거하고 적합한 충전재를 사용하여 공극 메움(퍼티작업)을 하여야 한다.

    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 바닥판면의 요철부위];
    B["KCS 24 40 20 3.1 (4)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 20 3.1 (4)"])

    subgraph Variable_def
    VarOut[/출력변수: 바닥판면의 요철부위/];
    VarIn1[/입력변수: 패인부분의 직경/];
    VarIn2[/입력변수: 패인부분의 깊이/];
    VarOut ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"패인부분의 직경 ≥ 10 mm
    패인부분의 깊이 ≥ 3 mm"}
    C --> E["이물질을 제거하고 적합한 충전재를 사용하여 \n 공극 메움(퍼티작업)을 하여야 한다."]
    E --> End([바닥판면의 요철부위])
    """

    @rule_method

    def unevenness_deck(fIDiaInd,fIDepInd) -> RuleUnitResult:
        """
        Args:
            fIDiaInd (float): 패인부분의 직경
            fIDepInd (float): 패인부분의 깊이

        Returns:
            sOUneDec (string): 바닥판면의 요철부위 정리
        """
        assert isinstance(fIDiaInd, float)
        assert isinstance(fIDiaInd, float)

        if fIDiaInd >= 10:
            if fIDepInd >=3:
                sOUneDec = "이물질을 제거하고 적합한 충전재를 사용하여 공극 메움(퍼티작업)을 하여야 한다."
            else:
                sOUneDec = None
        else:
            sOUneDec = None

        return RuleUnitResult(
            result_variables = {
                "sOUneDec": sOUneDec,
                })