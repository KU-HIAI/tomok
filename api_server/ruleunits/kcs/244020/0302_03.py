import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244020_0302_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 20 3.2 (3)'
    ref_date = '2016-06-30'
    doc_date = '2023-10-12'
    title = '습도 조건에 따른 교량방수 시공'

    description = """
    교량방수
    3. 시공
    3.2 기상 조건
    (3)
    """
    content = """
    #### 3.2 기상 조건
    (3) 비가 온 직후에는 바닥판 면의 함수율을 반드시 점검하고, 공기 중 상대습도가 85% 이상일 경우에는 공사를 중지하여야 하며,
    도포 작업을 할 때 비가 올 경우 작업을 즉시 중단하고, 도포재의 품질이 우천으로 인하여 저하되는 현상이 발생하지 않도록 조치한다.

    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 습도 조건에 따른 교량방수 시공];
    B["KCS 24 40 20 3.2 (3)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 20 3.2 (3)"])

    subgraph Variable_def
    VarOut[/출력변수: 습도 조건에 따른 교량방수 시공/];
    VarIn1[/입력변수: 상대습도/];
    VarIn2[/입력변수: 비가 온 직후/];
    VarIn3[/입력변수: 비/];
    VarOut ~~~ VarIn1 & VarIn2 & VarIn3
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{비가 온 직후, 비}
    C --> |비가 온 직후|I{"상대습도 ≥ 85%"}
    I --> |True|D[공사를 중지]
    I --> |False|E[공사가 가능하다]
    C --> |비|F[도포 작업을 할 때 작업을 즉시 중단하고, \n 도포재의 품질이 우천으로 인하여 저하되는 현상이 \n 발생하지 않도록 조치\n.]
    D & E & F --> End(["시공할 때의 습도"])
    """

    @rule_method

    def humidity(fIRelHum,bIAftRai,bIRai) -> RuleUnitResult:
        """
        Args:
            fIRelHum (float): 상대습도
            bIAftRai (bool): 비가 온 직후
            bIRai (bool):비

        Returns:
            sOHumCon (str): 습도에 따른 시공
        """
        assert isinstance(fIRelHum, float)
        assert isinstance(bIAftRai, bool)
        assert isinstance(bIRai, bool)
        assert bIAftRai != bIRai

        if bIAftRai:
            if fIRelHum >=85:
                sOHumCon = "공사를 중지"
            else:
                sOHumCon = "공사가 가능하다"
        elif bIRai:
            sOHumCon = "도포 작업을 할 때 작업을 즉시 중단하고, 도포재의 품질이 우천으로 인하여 저하되는 현상이 발생하지 않도록 조치"

        return RuleUnitResult(
            result_variables = {
                "sOHumCon": sOHumCon,
                })