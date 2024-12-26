import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS243000_020303_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 24 30 00 2.3.3 (1)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-08'
    title = '와이어 로프의 허용오차'

    description = """
    강교량공사
    2. 자재
    2.3 자재의 허용오차
    2.3.3 선재 및 봉강
    (1)
    """
    content = """
    #### 2.3.3 선재 및 봉강
    (1) 와이어 로프의 소선지름의 허용오차는 KS D 3514(와이어로프) 표 6에 의하고
    와이어 로프 지름의 허용오차는 로프의 지름이 10 mm 이하는 로프 지름의 +10% 이내, 로프의 지름이 10 mm 이상은 +7% 이내로 한다.
    와이어 로프용 선재는 KS D 3559(경강선재)로서 선재의 허용오차는 선재지름의 ±0.5 mm 이며 편경차는 0.5 mm 이하로 한다.
    """

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

    def tolerance_wire_rope(bITolWir,bITolRop,bITolLin,bIOva,fIDiaRop,fIDiaLin) -> RuleUnitResult:
        """
        Args:
            bITolWir (bool): 와이어 로프의 소선지름의 허용오차
            bITolRop (bool): 와이어 로프 지름의 허용오차
            bITolLin (bool): 선재의 허용오차
            bIOva (bool): 편경차
            fIDiaRop (float): 로프의 지름
            fIDiaLin (float): 선재지름


        Returns:
            sOTolWir (str): 와이어 로프의 허용오차
        """
        assert isinstance(bITolWir, bool)
        assert isinstance(bITolRop, bool)
        assert isinstance(bITolLin, bool)
        assert isinstance(bIOva, bool)
        assert (bITolWir+bITolRop+bITolLin+bIOva) == 1
        assert isinstance(fIDiaRop, float)
        assert isinstance(fIDiaLin, float)

        if bITolWir:
            sOTolWir = "KS D 3514(와이어로프) 표 6"
        elif bITolRop:
            if fIDiaRop <=10:
                sOTolWir = "+" + str(round(fIDiaRop*0.1,5))+" mm 이내"
            else:
                sOTolWir = "+" + str(round(fIDiaRop*0.07,5))+" mm 이내"
        elif bITolLin:
            sOTolWir = str(fIDiaLin-0.5)+ "~" +str(fIDiaLin+0.5)+" mm"
        elif bIOva:
            sOTolWir = "0.5 mm 이하"

        return RuleUnitResult(
            result_variables = {
                "sOTolWir": sOTolWir,
                })