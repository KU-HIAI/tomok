import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS142011_03010304_06(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 14 20 11 3.1.3.4 (6)'
    ref_date = '2022-01-11'
    doc_date = '2023-09-19'
    title = '철근 용접이음 시 기온'

    # 건설기준문서항목 (분류체계정보)
    description = """
    철근공사
    3. 시공
    3.1 철근
    3.1.3 철근의 이음
    3.1.3.4 용접 이음
    (6)
    """

    # 건설기준문서내용(text)
    content = """
    ####(6) 대기의 온도가 영하 18 °C 이하일 때에는 철근을 용접할 수 없으며, 대기의 온도가 영하 18°C보다는 높지만 0 °C 이하일 때는 용접을 시작할 때 철근의 온도가 21°C 이상이 되도록 철근을 예열하는 경우에만 용접할 수 있다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 철근 용접이음 시 기온];
    B["KCS 14 20 11 3.1.3.4 (6)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 11 3.1.3.4 (6)"])

    subgraph Variable_def
    VarOut[/출력변수: 철근 용접이음 시공/];
    VarIn1[/입력변수: 기온/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"기온"}
    C --> |"≤ -18"|D["철근을 용접할 수 없다"]
    C --> |"-18<기온≤ 0"|E["용접을 시작할 때 철근의 온도가 21°C 이상이 되도록 \n 철근을 예열하는 경우에만 용접할 수 있다 \n."]
    D  & E --> H(["철근 용접이음 시 기온"])
    C --> |"기온 > 0"|Pass([Pass])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def temperature_weld_joint(fITem):
        """
        Args:
            fITem (float): 기온
        Returns:
            sOWelJoi (sting): 철근 용접이음 시공
        """
        if fITem <=-18:
            sOWelJoi = "철근을 용접할 수 없다"
        elif fITem > -18 and fITem <=0:
            sOWelJoi = "용접을 시작할 때 철근의 온도가 21°C 이상이 되도록 철근을 예열하는 경우에만 용접할 수 있다"
        elif fITem > 0:
            sOWelJoi = "Pass"
        return sOWelJoi