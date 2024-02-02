import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS243000_020305_02(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 30 00 2.3.5 (2)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-08'
    title = '핀 및 롤러 지름의 허용오차'

    # 건설기준문서항목 (분류체계정보)
    description = """
    강교량공사
    2. 자재
    2.3 자재의 허용오차
    2.3.5 주조품
    (2)
    """

    # 건설기준문서내용(text)
    content = """
    ####(2) 핀 및 롤러 지름의 허용오차는 ±0.2 mm 이내이어야 하며, 서로 이웃하는 롤러의 지름의 허용오차는 0.1 mm 이내이어야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 와이어 로프의 허용오차];
    B["KCS 24 30 00 2.3.3 (1)"];
    B ~~~ A
    end

    KCS(["KCS 24 30 00 2.3.3 (1)"])

    subgraph Variable_def
    VarOut[/출력변수: 와이어 로프의 허용오차/];
    VarIn0[/입력변수: 와이어 로프의 소선지름의 허용오차/];
    VarIn1[/입력변수: 와이어 로프 지름의 허용오차/];
    VarIn2[/입력변수: 선재의 허용오차/];
    VarIn3[/입력변수: 편경차/];
    VarIn4[/입력변수: 로프의 지름/];
    VarIn5[/입력변수: 선재지름/];
    VarOut ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"와이어 로프의 소선지름의 허용오차\n 와이어 로프 지름의 허용오차 \n 선재의 허용오차 \n 편경차 \n."}
    C --> |"와이어 로프의 소선지름의 허용오차"|CC["KS D 3514(와이어로프) 표 6"]
    C --> |"와이어 로프 지름의 허용오차"|D{로프의 지름}
    D --> |"로프의 지름 ≤ 10mm"|E["로프 지름 * 10% 이내"]
    D --> |"로프의 지름 ≥ 10mm"|F["로프 지름 * 7% 이내"]
    C --> |"선재의 허용오차"|G["선재지름 ±0.5 mm"]
    C --> |"편경차"|H["0.5 mm 이하"]
    CC & E & F & G & H --> I(["와이어 로프의 허용오차"])
    """

    @rule_method
    def tolerance_pin_roller(bIAdjRol,fIDesDia,fIConDia)-> str:
        """
        Args:
            bIAdjRol (boolean): 서로 이웃하는 롤러의 지름
            fIDesDia (float): 핀 및 롤러 지름의 설계값
            fIConDia (float): 핀 및 롤러 지름의 시공값
        Returns:
            sOTolWir (string)): 와이어 로프의 허용오차
        """
        if bIAdjRol == False:
            if abs(fIDesDia - fIConDia)<0.2:
                sOTolWir = "Pass"
            else:
                sOTolWir = "Fail"
        else:
            if abs(fIDesDia - fIConDia)<0.1:
                sOTolWir = "Pass"
            else:
                sOTolWir = "Fail"
        return sOTolWir