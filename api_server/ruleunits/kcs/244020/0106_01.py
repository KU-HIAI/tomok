import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244020_0106_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 20 1.6 (1)'
    ref_date = '2016-06-30'
    doc_date = '2023-10-12'
    title = '환경요구사항'

    description = """
    교량방수
    1. 일반사항
    1.6 환경요구사항
    (1)
    """
    content = """
    #### 1.6 환경요구사항
    (1) 기온 5 ℃ 이하 상태에서 시공하지 않아야 하며, 5 ℃ 이하에서 시공이 부득이한 경우 적외선 램프 등을 사용하여
    콘크리트 바닥판 면을 예열하거나 이동식 방풍 판넬 등을 세워 바람에 의한 온도저하를 방지하는 등 보온 대책을 강구하여야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 환경요구사항];
    B["KCS 24 40 20 1.6 (1)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 20 1.6 (1)"])

    subgraph Variable_def
    VarOut[/출력변수: 환경요구사항/];
    VarIn0[/입력변수: 부득이하게 시공/];
    VarIn1[/입력변수: 기온/];
    VarOut ~~~ VarIn0 & VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"기온"}
    C --> |"기온 ≤ 5 ℃"|D{"부득이하게 시공"}
    D --> |"True"|E["적외선 램프 등을 사용하여 콘크리트 바닥판 면을 예열하거나 \n 이동식 방풍 판넬 등을 세워 바람에 의한 온도저하를 방지하는 등 보온 대책을 강구"]
    D --> |"False"|F["시공하지 않아야 한다"]
    C --> |"기온 > 5 ℃"|G["시공이 가능하다"]
    E & F & G --> H(["환경요구사항"])
    """

    @rule_method

    def environment_requirement(fITem,bIUnaCon) -> RuleUnitResult:
        """
        Args:
            fITem (float): 기온
            bIUnaCon (bool): 부득이하게 시공

        Returns:
            sOEnvReq (string): 환경요구사항
        """
        assert isinstance(bIUnaCon, bool)
        assert isinstance(fITem, float)

        if fITem <=5:
            if bIUnaCon:
                sOEnvReq = "적외선 램프 등을 사용하여 콘크리트 바닥판 면을 예열하거나 이동식 방풍 판넬 등을 세워 바람에 의한 온도저하를 방지하는 등 보온 대책을 강구"
            else:
                sOEnvReq = "시공하지 않아야 한다"
        else:
            sOEnvReq = "시공이 가능하다"

        return RuleUnitResult(
            result_variables = {
                "sOEnvReq": sOEnvReq,
                })