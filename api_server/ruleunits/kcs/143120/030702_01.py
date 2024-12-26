import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_030702_01(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 3.7.2 (1)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-13'
    title = '단일패스로 이루어진 필릿용접부의 최대 용접 목두께'

    description = """
    용접
    3. 시공
    3.7 가스메탈아크용접(GMAW) 및 플럭스코어드아크용접(FCAW)
    3.7.2 용접층 두께
    """

    content = """
    #### 3.7.2 용접층 두께
    (1) 단일패스로 이루어진 필릿용접부의 최대 용접 목두께는 아래보기자세 및 수직자세의 경우 12 mm, 수평자세의 경우 10 mm, 위보기자세의 경우 8 mm로 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: 단일패스로 이루어진 필릿용접부의 최대 용접 목두께"];
    B["KCS 14 31 20 3.7.2 (1)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 3.7.2 (1)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 단일패스로 이루어진 필릿용접부의 최대 용접 목두께"/];
    VarIn1[/입력변수: 아래보기 자세/];
    VarIn2[/입력변수: 수평 자세/];
    VarIn3[/입력변수: 수직 자세/];
    VarIn4[/입력변수: 위보기 자세/];
		VarOut1 ~~~ VarIn1 & VarIn2  & VarIn3  & VarIn4
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"아래보기 자세 \n 수평 자세 \n 수직 자세 \n 위보기 자세"}
    C --> |"아래보기 자세 \n 수평 자세 "|D[12 mm]
    C --> |"수직 자세"|E[10 mm]
    C --> |"위보기 자세"|F[8 mm]
		D & E & F --> End([단일패스로 이루어진 필릿용접부의 최대 용접 목두께])
    """

    @rule_method
    def Flat_Postion(bIFlaPos, bIHorPos, bIVerPos, bIOvePos) -> RuleUnitResult:
        """ 단일패스로 이루어진 필릿용접부의 최대 용접 목두께
        Args:
        bIFlaPos (bool): 아래보기 자세
        bIHorPos (bool): 수평 자세
        bIVerPos (bool): 수직 자세
        bIOvePos (bool): 위보기 자세

        Returns:
        fOMaxThr (float): 단일패스로 이루어진 필릿용접부의 최대 용접 목두께
        """
        assert isinstance(bIFlaPos, bool)
        assert isinstance(bIHorPos, bool)
        assert isinstance(bIVerPos, bool)
        assert isinstance(bIOvePos, bool)
        assert (bIFlaPos + bIHorPos + bIVerPos + bIOvePos) == 1

        if bIFlaPos == True or bIVerPos == True:
          fOMaxThr = 12
        elif bIHorPos == True:
          fOMaxThr = 10
        elif bIOvePos == True:
          fOMaxThr = 8

        return RuleUnitResult(
                result_variables = {
                    "fOMaxThr": fOMaxThr
                }
            )