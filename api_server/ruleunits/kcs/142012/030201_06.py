import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142012_030201_06(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 20 12 3.2.1 (6)'
    ref_date = '2022-09-01'
    doc_date = '2023-09-26'
    title = '강관 동바리의 연결'

    description = """
    거푸집 및 동바리
    3. 시공
    3.2 동바리의 시공
    3.2.1 일반 동바리
    (6)
    """
    content = """
    #### 3.2.1 일반 동바리
    (6) 특수한 경우를 제외하고 강관 동바리는 2개 이상을 연결하여 사용하지 말아야 하며, 높이가 3.5 m 이상인 경우에는 높이 2 m 이내마다 수평 연결재를 2개 방향으로 설치하고 수평연결재의 변위가 일어나지 않도록 이음 부분은 견고하게 연결한다.
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 강관 동바리의 연결];
    B["KCS 14 20 12 3.2.1 (6)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 12 3.2.1 (6)"])

    subgraph Variable_def
    VarOut1[/출력변수: 강관 동바리의 연결/];
    VarIn1[/입력변수: 특수한 경우/];
    VarIn2[/입력변수: 높이/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> E{"높이 ≥ 3.5m"}
    E --> |True|F["높이 2 m 이내마다 수평 연결재를 2개 방향으로 설치하고 \n 수평연결재의 변위가 일어나지 않도록 이음 부분은 견고하게 연결"]
    E --> |False|GG{특수한 경우}
    GG --> |False|G["강관 동바리는 2개 이상을 연결하여 사용하지 말아야 한다"]
    GG --> |True|H["강관 동바리는 2개 이상을 연결할 수 있다"]
    G & F & H --> End([강관 동바리의 연결])
    """

    @rule_method

    def connection_steel_shore(bISpeCas, fIHei) -> RuleUnitResult:
        """
        Args:
            bISpeCas (bool): 특수한 경우
            fIHei (float): 높이

        Returns:
            sOConSte (str): 강관동바리의 연결
        """
        assert isinstance(bISpeCas, bool)
        assert isinstance(fIHei, float)

        if fIHei >= 3.5:
            sOConSte = "높이 2 m 이내마다 수평 연결재를 2개 방향으로 설치하고 수평연결재의 변위가 일어나지 않도록 이음 부분은 견고하게 연결"
        else:
            if bISpeCas == False:
                sOConSte = "강관 동바리는 2개 이상을 연결하여 사용하지 말아야 한다"
            else:
                sOConSte = "강관 동바리는 2개 이상을 연결할 수 있다"

        return RuleUnitResult(
            result_variables = {
                "sOConSte": sOConSte,
                })