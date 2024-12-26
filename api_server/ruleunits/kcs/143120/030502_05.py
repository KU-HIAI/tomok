import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_030502_05(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 3.5.2 (5)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-13'
    title = '루트 패스 후속 용접층의 최대두께'

    description = """
    용접
    3. 시공
    3.5 피복아크용접(SMAW)
    3.5.2 용접절차
    """

    content = """
    #### 3.5.2 용접절차
    (5) 그루브용접 및 필릿용접부의 루트패스 후속 용접층의 최대두께는 다음을 기본으로 한다.
    ① 아래보기자세: 3 mm
    ② 수평자세, 수직자세, 위보기자세: 5 mm
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: 루트 패스 후속 용접층의 최대두께"];
    B["KCS 14 31 20 3.5.2 (5)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 3.5.2 (5)"])

    subgraph Variable_def
		subgraph V1
    VarOut1[/"출력변수: 루트 패스 후속 용접층의 최대두께"/];
    VarIn1[/입력변수: 아래보기 자세/];
		end
		subgraph V2
    VarOut2[/"출력변수: 루트 패스 후속 용접층의 최대두께"/];
    VarIn2[/입력변수: 수평 자세/];
    VarIn3[/입력변수: 수직 자세/];
    VarIn4[/입력변수: 위보기 자세/];
		end
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"아래보기 자세 \n 수평 자세 \n 수직 자세 \n 위보기 자세 \n."}
    C --> |"아래보기 자세"|D[3 mm]
    C --> |"수평 자세  \n 수직 자세 \n 위보기 자세"|E[5 mm]
		D & E --> End([루트 패스 후속 용접층의 최대두께])
    """

    @rule_method
    def Flat_Position(bIFlaPos, bIHorPos, bIVerPos, bIOvePos) -> float:
        """ 루트 패스 후속 용접층의 최대두께
        Args:
        bIFlaPos (bool): 아래보기 자세
        bIHorPos (bool): 수평 자세
        bIVerPos (bool): 수직 자세
        bIOvePos (bool): 위보기 자세

        Returns:
        fOMaxSub (float): 루트 패스 후속 용접층의 최대두께
        """
        assert isinstance(bIFlaPos, bool)
        assert isinstance(bIHorPos, bool)
        assert isinstance(bIVerPos, bool)
        assert isinstance(bIOvePos, bool)
        assert (bIFlaPos + bIHorPos + bIVerPos + bIOvePos) == 1

        if bIFlaPos == True:
          fOMaxSub = 3
        elif bIFlaPos == False:
          if bIHorPos == True or bIVerPos == True or bIOvePos == True:
            fOMaxSub = 5

        return RuleUnitResult(
                result_variables = {
                    "fOMaxSub": fOMaxSub
                }
            )