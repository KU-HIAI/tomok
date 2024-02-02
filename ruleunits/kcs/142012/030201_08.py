import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS142012_030201_08(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 14 20 12 3.2.1 (8)'
    ref_date = '2022-09-01'
    doc_date = '2023-09-26'
    title = '시스템 동바리의 사용'

    # 건설기준문서항목 (분류체계정보)
    description = """
    거푸집 및 동바리
    3. 시공
    3.2 동바리의 시공
    3.2.1 일반 동바리
    (8)
    """

    # 건설기준문서내용(text)
    content = """
    ####(8) 강관 동바리 설치높이가 4.0 m를 초과하거나 슬래브 두께가 1 m를 초과하는 경우에는 하중을 안전하게 지지할 수 있는 구조의 시스템 동바리로 사용한다
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 시스템 동바리의 사용];
    B["KCS 14 20 12 3.2.1 (8)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 12 3.2.1 (8)"])

    subgraph Variable_def
    VarOut1[/출력변수: 시스템 동바리의 사용/];
    VarIn1[/입력변수: 설치 높이/];
    VarIn2[/입력변수: 슬래브 두께/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> E{"설치 높이 > 4.0 \n or \n 슬래브 두께 > 1 m \n ."}
    E --> |True|F["하중을 안전하게 지지할 수 있는 구조의 시스템 동바리 사용"]
    E --> |False|G["시스템 동바리를 사용할 필요가 없다"]
    F & G --> End([시스템 동바리의 사용])
    """

    @rule_method
    def prefabricated_shoring_system(fIInsHei, fISlaThi) -> str:
        """
        Args:
            fIInsHei (float): 설치 높이
            fISlaThi (float): 슬래브 두께
        Returns:
            sOPreSho (string)): 시스템 동바리의 사용
        """
        if fIInsHei > 4.0 or fISlaThi > 1.0:
            sOPreSho = "하중을 안전하게 지지할 수 있는 구조의 시스템 동바리 사용"
        else:
            sOPreSho = "시스템 동바리를 사용할 필요가 없다"
        return sOPreSho