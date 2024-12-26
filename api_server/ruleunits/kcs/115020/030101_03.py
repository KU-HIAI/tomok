import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS115020_030101_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 11 50 20 3.1.1 (3)'
    ref_date = '2021-05-12'
    doc_date = '2023-08-18'
    title = '강널말뚝의 운반 및 보관'

    description = """
    널말뚝
    3. 시공
    3.1 일반사항
    3.1.1 운반 및 보관
    (3)
    """
    content = """
    ####3.1.1 운반 및 보관
    (3) 강널말뚝의 적치 높이는 2m 이하로 하되 1층의 단수는 5매 이하로 하여 고임목으로 괴어야하며, 이 때 고임목은 100mm 각목으로 하고 각목의 간격은 4m 이내로 한다
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 강널말뚝의 운반 및 보관];
    B["KCS 11 50 20 3.1.1 (3)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 20 3.1.1 (3)"])

    subgraph Variable_def
    VarIn1[/입력변수: 적치 높이/];
    VarIn2[/입력변수: 1층의 단수/];
    VarIn3[/입력변수: 고임목/];
    VarIn4[/입력변수: 각목 길이/];
    VarIn5[/입력변수: 각목의 간격/];
    VarIn1 & VarIn2 & VarIn3 ~~~ VarIn4 & VarIn5
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"적치 높이 ≤ 2 m & 1층의 단수≤ 5매 & 고임목
    각목 길이 = 100 mm & 각목의 간격 < 4m"}
    C --> End([Pass or Fail])
    """

    @rule_method
    def storage_steel_pile(fICumHei,nINumBun,bIOldTre,fILenLum,fISpaLum) -> RuleUnitResult:
        """
        Args:
            fICumHei (float): 적치 높이
            nINumBun (int): 1층의 단수
            bIOldTre (bool): 고임목
            fILenLum (float): 각목 길이
            fISpaLum (float): 각목의 간격

        Returns:
            pass_fail (bool): 널말뚝 3.1.1 운반 및 보관 (3)의 판단 결과
        """
        assert isinstance(fICumHei, float)
        assert isinstance(nINumBun, int)
        assert isinstance(bIOldTre, bool)
        assert isinstance(fILenLum, float)
        assert isinstance(fISpaLum, float)


        if fICumHei <= 2 and nINumBun <= 5 and bIOldTre == True and fILenLum == 100 and fISpaLum <= 4:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": True,
                }
            )
        else:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": False,
                }
            )