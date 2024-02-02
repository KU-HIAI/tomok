import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS142012_010603_10(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 14 20 12 1.6.3 (10)'
    ref_date = '2022-09-01'
    doc_date = '2023-09-26'
    title = '전단검토 시 형상계수'

    # 건설기준문서항목 (분류체계정보)
    description = """
    거푸집 및 동바리
    1. 일반사항
    1.6 거푸집 및 동바리 설계
    1.6.3 거푸집 및 동바리 구조계산
    (10)
    """

    # 건설기준문서내용(text)
    content = """
    ####(10) 전단검토 시 형상계수(K)는 1.5(사각형단면), 4/3(원형단면), 1.0(각형 강관단면), 2.0(원형 강관단면)을 적용한다.
    """

    # 플로우차트(mermaid)
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
    def shape_factor(sICroSec) -> float:
        """
        Args:
            sICroSec (string): 단면의 종류
        Returns:
            fOK (float): 전단검토 시 형상계수
        """
        if sICroSec == "사각형단면":
            fOK = 1.5
        elif sICroSec == "원형단면":
            fOK = 4/3
        elif sICroSec == "각형 강관단면":
            fOK = 1.0
        elif sICroSec == "원형 강관단면":
            fOK = 2.0
        return fOK