import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244005_020604_01(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 40 05 2.6.4 (1)'
    ref_date = '2018-08-30'
    doc_date = '2023-10-31'
    title = '받침용 PTFE 수지의 성질'

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량받침
    2. 자재
    2.6.1 받침의 구성부품
    2.6.4 받침용 PTFE판
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    #### (1) PTFE 수지는 신생재료이어야 하며, 비중은 2.13 ~ 2.19, 녹는점은 328 ℃ ± 1 ℃이어야 한다..
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 받침용 PTFE 수지의 성질];
    B["KCS 24 40 05 2.6.4 (1)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 05 2.6.4 (1)"])

    subgraph Variable_def
    VarOut[/출력변수: 받침용 PTFE 수지의 성질/];
    VarIn1[/입력변수: 신생재료/];
    VarIn2[/입력변수: 비중/];
    VarIn3[/입력변수: 녹는점/];
    VarOut ~~~ VarIn1 & VarIn2 & VarIn3
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{신생재료}
    C --> |"True"|BB{2.13 < 비중 < 2.19}
    C --> |"False"|Fail([Fail])
    BB --> |"True"|MM{"327 ℃ < 녹는점 < 327 ℃"}
    BB --> |"False"|Fail([Fail])
    MM --> |"False"|Fail([Fail])
    MM --> |"True"|P([Pass])
    """
    @rule_method
    def PTFE_resin(bINewMat,fISpeGra,fIMelPoi)->str:
        """
        Args:
            bINewMat (boolean): 신생재료
            fISpeGra (float): 비중
            fIMelPoi (float): 녹는점
        Returns:
            sOPtfBac (string): 받침용 PTFE 수지의 성질
        """
        if bINewMat == True:
            if fISpeGra >= 2.13 and fISpeGra <=2.19:
                if fIMelPoi >=327 and fIMelPoi <=329:
                    sOPtfBac = "Pass"
                else:
                    sOPtfBac = "Fail"
            else:
                sOPtfBac = "Fail"
        else:
            sOPtfBac = "Fail"
        return sOPtfBac