import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142012_010603_03_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 20 12 1.6.3 (3) ②'
    ref_date = '2022-09-01'
    doc_date = '2023-09-25'
    title = '거푸집의 수평하중'

    description = """
    거푸집 및 동바리
    1. 일반사항
    1.6 거푸집 및 동바리 설계
    1.6.3 거푸집 및 동바리 구조계산
    (3)
    """
    content = """
    #### 1.6.3 거푸집 및 동바리 구조계산
    (3) 수평하중은 고정하중 및 공사 중 발생하는 활하중으로 다음의 값을 적용한다.
    ② 벽체 거푸집의 경우에는 거푸집 측면에 대하여 0.5kN/㎡ 이상의 수평방향 하중이 작용하는 것으로 볼 수 있다.
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 거푸집의 수평하중];
    B["KCS 14 20 12 1.6.3 (3) ②"];
    B ~~~ A
    end

    KCS(["KCS 14 20 12 1.6.3 (3) ②"])

    subgraph Variable_def
    VarOut[/출력변수: 거푸집 측면에 작용하는 수평하중/];
    VarIn[/입력변수: 벽체 거푸집/];
    VarOut ~~~ VarIn
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> E["거푸집 측면에 작용하는 수평하중 = 0.5"]
    E --> End([거푸집의 수평하중])
    """

    @rule_method
    def horizontal_load_form(bIWalFor)-> RuleUnitResult:
        """
        Args:
            bIWalFor (bool): 벽체 거푸집

        Returns:
            fOHorFor (float): 거푸집 측면에 작용하는 수평하중

        """
        assert isinstance(bIWalFor, bool)
        assert bIWalFor == True

        if bIWalFor:
            fOHorFor = 0.5
        else:
            fOHorFor = None

        return RuleUnitResult(
            result_variables = {
                "fOHorFor": fOHorFor,
                })