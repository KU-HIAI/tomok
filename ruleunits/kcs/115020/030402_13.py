import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS115020_030402_13(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 11 50 20 3.4.2 (13)'
    ref_date = '2021-05-12'
    doc_date = '2023-09-15'
    title = '지수재의 도포량'

    # 건설기준문서항목 (분류체계정보)
    description = """
    널말뚝
    3. 시공
    3.4 강널말뚝
    3.4.1 강널말뚝 항타
    (13)
    """

    # 건설기준문서내용(text)
    content = """
        ####3.4.2 강널말뚝 항타
        (13) 지수재는 충분한 팽창성을 지닌 것이어야 하며, 지수재의 도포량은 연결부 일면에 200g/m (3mm~4mm 두께)를 도포하고, 도포 후 하절기 12시간~24시간, 동절기 24시간~48시간 경화시켜 사용한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
        flowchart TD
        subgraph Python_Class
        A[Title: 지수재];
        B["KCS 11 50 20 3.4.2 (13)"];
        B ~~~ A
        end

        KCS(["KCS 11 50 20 3.4.2 (13)"])

        subgraph Variable_def
        VarOut[/출력변수: 지수재의 도포량/];
        VarIn1[/입력변수: 지수재 도포 후 경화시간/];
        VarIn2[/입력변수: 하절기/];
        VarIn3[/입력변수: 동절기/];
        VarOut ~~~ VarIn1 & VarIn3
        end

        Python_Class ~~~ KCS
        KCS --> Variable_def
        Variable_def --> C{"지수재의 도포량, \n 지수재 도포 후 경화시간"}
        C --> |"지수재의 도포량"|D["200g/m (3mm~4mm 두께)"]
        C --> |"지수재 도포 후 경화시간"|E{동절기 \n 하절기}
        E --> |"하절기"|F["12시간~24시간"]
        E --> |"동절기"|G["24시간~48시간"]
        D & F & G --> End([지수재])
    """

    @rule_method
    def hardening(bISumSea, bIWinSea):
        """
        Args:
            bISumSea (boolean): 하절기
            bIWinSea (boolean): 동절기
        Returns:
            sOSprWat (string): 지수재의 도포량
            sOHarTim (string): 지수재 도포 후 경화시간
        """
        sOSprWat = "200g/m (3mm~4mm 두께)"

        if bISumSea == True:
            sOHarTim = "12시간~24시간"
        elif bIWinSea == True:
            sOHarTim = "24시간~48시간"
        else:
            sOHarTim = "입력 오류: 하절기 또는 동절기를 선택해야 합니다."
        sOSprWat = "200g/m (3mm~4mm 두께)"
        return "지수재의 도포량: " + sOSprWat + ", " + "지수재 도포 후 경화시간: " + sOHarTim