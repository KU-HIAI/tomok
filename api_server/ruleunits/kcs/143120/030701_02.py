import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_030701_02(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 3.7.1 (2)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-13'
    title = '용접와이어의 최대 직경'

    description = """
    용접
    3. 시공
    3.7 가스메탈아크용접(GMAW) 및 플럭스코어드아크용접(FCAW)
    3.7.1 가스메탈아크용접(GMAW) 및 플럭스코어드아크용접(FCAW)에 관한 일반사항
    """

    content = """
    #### 3.7.1 가스메탈아크용접(GMAW) 및 플럭스코어드아크용접(FCAW)에 관한 일반사항
    (2) 용접와이어의 최대직경은 아래보기자세 및 수평자세의 경우 4.0 mm, 수직자세의 경우 2.4 mm, 위보기 자세의 경우 2.0 mm로 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: 용접와이어의 최대 직경"];
    B["KCS 14 31 20 3.7.1 (2)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 3.7.1 (2)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 용접와이어의 최대 직경"/];
    VarIn1[/입력변수: 아래보기 자세/];
    VarIn2[/입력변수: 수평 자세/];
    VarIn3[/입력변수: 수직 자세/];
    VarIn4[/입력변수: 위보기 자세/];
		VarOut1 ~~~ VarIn1 & VarIn2  & VarIn3  & VarIn4
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"아래보기 자세 \n 수평 자세 \n 수직 자세 \n 위보기 자세"}
    C --> |"아래보기 자세 \n 수평 자세 "|D[4.0 mm]
    C --> |"수직 자세"|E[2.4 mm]
    C --> |"위보기 자세"|F[2.0 mm]
		D & E & F --> End([용접와이어의 최대 직경])
    """

    @rule_method
    def Flat_Postion(bIFlaPos, bIHorPos, bIVerPos, bIOvePos) -> RuleUnitResult:
        """ 용접와이어의 최대 직경
        Args:
        bIFlaPos (bool): 아래보기 자세
        bIHorPos (bool): 수평 자세
        bIVerPos (bool): 수직 자세
        bIOvePos (bool): 위보기 자세

        Returns:
        fOMaxDia (float): 용접와이어의 최대 직경
        """
        assert isinstance(bIFlaPos, bool)
        assert isinstance(bIHorPos, bool)
        assert isinstance(bIVerPos, bool)
        assert isinstance(bIOvePos, bool)
        assert (bIFlaPos + bIHorPos + bIVerPos + bIOvePos) == 1

        if bIFlaPos == True or bIHorPos == True:
          fOMaxDia = 4.0
        elif bIVerPos == True:
          fOMaxDia = 2.4
        elif bIOvePos == True:
          fOMaxDia = 2.0

        return RuleUnitResult(
                result_variables = {
                    "fOMaxDia": fOMaxDia
                }
            )