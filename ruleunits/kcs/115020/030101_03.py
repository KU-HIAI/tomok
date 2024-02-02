import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS115020_030101_03(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 11 50 20 3.1.1 (3)'
    ref_date = '2021-05-12'
    doc_date = '2023-08-18'
    title = '강널말뚝의 운반 및 보관'

    # 건설기준문서항목 (분류체계정보)
    description = """
    널말뚝
    3. 시공
    3.1 일반사항
    3.1.1 운반 및 보관
    (3)
    """

    # 건설기준문서내용(text)
    content = """
    ####3.1.1 운반 및 보관
    (3) 강널말뚝의 적치 높이는 2m 이하로 하되 1층의 단수는 5매 이하로 하여 고임목으로 괴어야하며, 이 때 고임목은 100mm 각목으로 하고 각목의 간격은 4m 이내로 한다
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 강널말뚝의 운반 및 보관];
    B["KCS 11 50 20 3.1.1 (3)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 20 3.1.1 (3)"])

    subgraph Variable_def
    VarOut[/출력변수: 강널말뚝의 운반 및 보관/];
    VarIn1[/입력변수: 적치 높이/];
    VarIn2[/입력변수: 1층의 단수/];
    VarIn3[/입력변수: 고임목/];
    VarIn4[/입력변수: 각목 길이/];
    VarIn5[/입력변수: 각목의 간격/];
    VarOut ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4 & VarIn5
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"적치 높이"}
    C --> |"≤ 2 m"|D{"1층의 단수"}
    C --> |"> 2 m"|Fail([Fail])
    D --> |"≤ 5매"|E{"고임목"}
    D --> |"> 5매"|Fail([Fail])
    E --> |"True"|F{"각목 길이 = 100 mm"}
    E --> |"False"|Fail([Fail])
    F --> |"True"|G{"각목의 간격 < 4m"}
    F --> |"False"|Fail([Fail])
    G --> |"True"|Pass([Pass])
    G --> |"False"|Fail([Fail])
    """

    @rule_method
    def storage_steel(fICumHei,nINumBun,bIOldTre,fILenLum,fISpaLum):
        """
        Args:
            fICumHei (float): 적치 높이
            nINumBun (integer): 1층의 단수
            bIOldTre (boolean): 고임목
            fILenLum (float): 각목 길이
            fISpaLum (float): 각목의 간격
        Returns:
            sOConSto (string): 강널말뚝의 운반 및 보관
        """
        if fICumHei <= 2:
            if nINumBun <= 5:
                if bIOldTre == True:
                    if fILenLum == 100:
                        if fISpaLum < 4:
                            sOConSto = "Pass"
                        else:
                            sOConSto = "Fail"
                    else:
                        sOConSto = "Fail"
                else:
                    sOConSto = "Fail"
            else:
                sOConSto = "Fail"
        else:
            sOConSto = "Fail"
        return sOConSto