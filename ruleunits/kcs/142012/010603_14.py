import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS142012_010603_14(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 14 20 12 1.6.3 (14)'
    ref_date = '2022-09-01'
    doc_date = '2023-09-26'
    title = '동바리의 안전율'

    # 건설기준문서항목 (분류체계정보)
    description = """
    거푸집 및 동바리
    1. 일반사항
    1.6 거푸집 및 동바리 설계
    1.6.3 거푸집 및 동바리 구조계산
    (14)
    """

    # 건설기준문서내용(text)
    content = """
    ####(14) 거푸집 및 동바리는 부재의 허용응력에 대한 설계하중으로 인한 응력의 비인 안전율을 고려하여 설계한다. 지주형식 동바리 중 단품 동바리는 3.0, 조립형 동바리는 2.5의 안전율을 적용하고, 보형식 동바리에 대하여는 안전율 2.0을 적용한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 동바리의 안전율];
    B["KCS 14 20 12 1.6.3 (14)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 12 1.6.3 (14)"])

    subgraph Variable_def
    VarOut1[/출력변수: 동바리의 안전율/];
    VarIn1[/입력변수: 동바리의 종류/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"동바리의 종류"}
    C --> |지주형식 단품 동바리|D[3.0]
    C --> |지주형식 조립형 동바리|E[2.5]
    C --> |보형식 동바리|F[2.0]
    D & E & F --> End([동바리의 안전율])
    """


    @rule_method
    def safety_factor(sIShoTyp) -> float:
        """
        Args:
            sIShoTyp (string): 동바리의 종류
        Returns:
            fOSafFac (float): 동바리의 안전율
        """
        if sIShoTyp == "지주형식 단품 동바리":
            fOSafFac = 3.0
        elif sIShoTyp == "지주형식 조립형 동바리":
            fOSafFac = 2.5
        elif sIShoTyp == "보형식 동바리":
            fOSafFac = 2.0
        return fOSafFac