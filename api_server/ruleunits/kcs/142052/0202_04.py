import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142052_0202_04(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 20 52 2.2 (4)'
    ref_date = '2023-08-16'
    doc_date = '2021-02-18'
    title = '콘크리트의 배합'

    description = """
    프리캐스트 콘크리트
    2. 자재
    2.2 배합
    (4)
    """

    content = """
    #### 2.2 배합
    (4) 슬럼프가 20 mm 이상인 콘크리트의 배합은 슬럼프 시험을 원칙으로 하며, 슬럼프 20 mm 미만인 콘크리트의 배합은 제조 방법에 적합한 시험 방법에 의한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 콘크리트의 배합];
    B["KCS 14 20 52 2.2 (4)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 52 2.2"])

    subgraph Variable_def
    VarOut[/출력변수: 콘크리트의 배합/];
    VarIn1[/입력변수: 슬럼프/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{슬럼프 => 20 mm}
    C --> |True|D["슬럼프 시험"]
    C --> |False|E["제조 방법에 적합한 시험 방법"]
    D --> F(["콘크리트의 배합"])
    E --> F(["콘크리트의 배합"])
    """

    @rule_method
    def concrete_mix(fISlu) -> str :
        """슬럼프에 따른 콘크리트 배합 시험 방법

        Args:
            fISlu (float): 슬럼프

        Returns:
            sOConMix (str) : 콘크리트의 배합
        """

        if fISlu >= 20:
            sOConMix = "슬럼프 시험"
        else:
            sOConMix = "제조 방법에 적합한 시험 방법"

        return RuleUnitResult(
                result_variables = {
                    "sOConMix": sOConMix,
                }
            )