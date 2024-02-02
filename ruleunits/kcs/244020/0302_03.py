import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244020_0302_03(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 40 20 3.2 (3)'
    ref_date = '2016-06-30'
    doc_date = '2023-10-13'
    title = '시공할때의 습도'

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량방수
    3. 시공
    3.2 기상 조건
    (3)
    """

    # 건설기준문서내용(text)
    content = """
    #### (3)
    비가 온 직후에는 바닥판 면의 함수율을 반드시 점검하고, 공기 중 상대습도가 85% 이상일 경우에는 공사를 중지하여야 하며, 도포 작업을 할 때 비가 올 경우 작업을 즉시 중단하고, 도포재의 품질이 우천으로 인하여 저하되는 현상이 발생하지 않도록 조치한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 시공할 때의 습도];
    B["KCS 24 40 20 3.2 (3)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 20 3.2 (3)"])

    subgraph Variable_def
    VarOut[/출력변수: 시공할 때의 습도/];
    VarIn1[/입력변수: 상대습도/];
    VarIn2[/입력변수: 비가 온 직후/];
    VarIn3[/입력변수: 비/];
    VarIn4[/입력변수: 도포 작업/];
    VarOut ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{비가 온 직후, 비}
    C --> |비가 온 직후|D[바닥판 면의 함수율을 반드시 점검]
    D --> I{"상대습도 ≥ 85%"}
    I --> E[공사를 중지]
    C --> |비|F{도포 작업}
    F --> H[작업을 즉시 중단하고, \n 도포재의 품질이 우천으로 인하여 저하되는 현상이 \n 발생하지 않도록 조치]
    D & E & H --> End(["시공할 때의 습도"])
    """

    @rule_method
    def humidity(fIRelHum,bIAftRai,bIRai,bISprOpe)->str:
        """
        Args:
            fIRelHum (float): 상대습도
            bIAftRai (boolean): 비가 온 직후
            bIRai (boolean):비
            bISprOpe (boolean): 도포 작업
        Returns:
            sOHumCon (string): 습도에 따른 시공
        """
        if bIAftRai:
            if fIRelHum >=85:
                sOHumCon = "공사를 중지"
            else:
                sOHumCon = "바닥판 면의 함수율을 반드시 점검"
        elif bIRai:
            if bISprOpe:
                sOHumCon = "작업을 즉시 중단하고, 도포재의 품질이 우천으로 인하여 저하되는 현상이 발생하지 않도록 조치"
            else:
                sOHumCon = "Pass"
        else:
            sOHumCon = "Pass"
        return sOHumCon