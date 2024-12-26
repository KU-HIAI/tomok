import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_030502_04(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 3.5.2 (4)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-13'
    title = '루트 패스의 최대치수'

    description = """
    용접
    3. 시공
    3.5 피복아크용접(SMAW)
    3.5.2 용접절차
    """

    content = """
    #### 3.5.2 용접절차
    (4) 단일패스 필릿용접과 다중패스 필릿용접 루트패스의 최대치수는 다음에 준한다.
    ① 아래보기자세: 10 mm
    ② 수평자세 및 위보기자세: 8 mm
    ③ 수직자세: 12 mm
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: 루트 패스의 최대치수"];
    B["KCS 14 31 20 3.5.2 (4)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 3.5.2 (4)"])

    subgraph Variable_def
		subgraph V1
    VarOut1[/"출력변수: 루트 패스의 최대치수"/];
    VarIn1[/입력변수: 아래보기 자세/];
		end
		subgraph V2
    VarOut2[/"출력변수: 루트 패스의 최대치수"/];
    VarIn2[/입력변수: 수평 자세/];
    VarIn3[/입력변수: 위보기 자세/];
		end
		subgraph V3
    VarOut3[/"출력변수: 루트 패스의 최대치수"/];
    VarIn4[/입력변수: 수직 자세/];
		end
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"아래보기 자세 \n 수평 자세 \n 위보기 자세 \n 수직 자세\n."}
    C --> |"아래보기 자세"|D[10 mm]
    C --> |"수평 자세 \n 위보기 자세"|E[8 mm]
    C --> |"수직 자세"|F[12 mm]
		D & E & F --> End([루트 패스의 최대치수])
    """

    @rule_method
    def Flat_Position(bIFlaPos, bIHorPos, bIOvePos, bIVerPos) -> float:
        """ 루트 패스의 최대치수
        Args:
        bIFlaPos (bool): 아래보기 자세
        bIHorPos (bool): 수평 자세
        bIOvePos (bool): 위보기 자세
        bIVerPos (bool): 수직 자세

        Returns:
        fOMaxRoo (float): 루트 패스의 최대치수
        """
        assert isinstance(bIFlaPos, bool)
        assert isinstance(bIHorPos, bool)
        assert isinstance(bIOvePos, bool)
        assert isinstance(bIVerPos, bool)
        assert (bIFlaPos + bIHorPos + bIOvePos + bIVerPos) == 1

        if bIFlaPos == True:
          fOMaxRoo = 10
        elif bIHorPos  == True:
          fOMaxRoo = 8
        elif bIOvePos == True:
          fOMaxRoo = 8
        elif bIVerPos == True:
          fOMaxRoo = 12

        return RuleUnitResult(
                result_variables = {
                    "fOMaxRoo": fOMaxRoo
                }
            )