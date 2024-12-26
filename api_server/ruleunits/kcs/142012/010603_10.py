import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142012_010603_10(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 20 12 1.6.3 (10)'
    ref_date = '2022-09-01'
    doc_date = '2023-09-25'
    title = '전단검토 시 형상계수'

    description = """
    거푸집 및 동바리
    1. 일반사항
    1.6 거푸집 및 동바리 설계
    1.6.3 거푸집 및 동바리 구조계산
    (10)
    """
    content = """
    #### 1.6.3 거푸집 및 동바리 구조계산
    (10) 전단검토 시 형상계수(K)는 1.5(사각형단면), 4/3(원형단면), 1.0(각형 강관단면), 2.0(원형 강관단면)을 적용한다.
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 전단검토 시 형상계수];
    B["KCS 14 20 12 1.6.3 (10)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 12 1.6.3 (10)"])

    subgraph Variable_def
    VarOut1[/출력변수: 전단검토 시 형상계수/];
    VarIn1[/입력변수: 단면의 종류/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"단면의 종류"}
    C --> |사각형단면|D[1.5]
    C --> |원형단면|E[4/3]
    C --> |각형 강관단면|F[1.0]
    C --> |원형 강관단면|G[2.0]
    D & E & F & G --> End([전단검토 시 형상계수])
    """

    @rule_method

    def shape_factor(sICroSec) -> RuleUnitResult:
        """
        Args:
            sICroSec (str): 단면의 종류

        Returns:
            fOK (float): 전단검토 시 형상계수
        """
        assert isinstance(sICroSec, str)
        assert sICroSec in ["사각형단면", "원형단면", "각형 강관단면", "원형 강관단면"]

        if sICroSec == "사각형단면":
            fOK = 1.5
        elif sICroSec == "원형단면":
            fOK = 4/3
        elif sICroSec == "각형 강관단면":
            fOK = 1.0
        elif sICroSec == "원형 강관단면":
            fOK = 2.0
        return RuleUnitResult(
            result_variables = {
                "fOK": fOK,
                })