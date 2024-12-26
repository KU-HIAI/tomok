import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS212010_030204_03(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 21 20 10 3.2.4 (3)'
    ref_date = '2022-02-23'
    doc_date = '2023-10-06'
    title = '타워크레인 준수사항'

    description = """
    건설지원장비
    3. 시공
    3.2. 양중장비
    3.2.4. 타워크레인
    (3)
    """

    content = """
    #### 3.2.4. 타워크레인
    (3) 타워크레인 사용 중 다음 사항을 준수하여야 한다.
    ④ 순간풍속 10m/s 이상, 강수량 1mm/h 이상, 강설량 10mm/h 이상 시 설치·인상·해체·점검·수리 등을 중지하여야 한다.
    ⑤ 순간풍속 15m/s 이상 시 운전작업을 중지하여야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 타워크레인 준수사항];
    B["KCS 21 20 10 3.2.4 (3)"];
    B ~~~ A
    end

    KCS(["KCS 21 20 10 3.2.4 (3)"])

    subgraph Variable_def
    VarOut[/출력변수: 크레인 작업/];
    VarIn1[/입력변수: 순간풍속/];
    VarIn2[/입력변수: 강수량/];
    VarIn3[/입력변수: 강설량/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"순간풍속 10m/s 이상"}
    Variable_def --> C2{"강수량 1mm/h 이상"}
    Variable_def --> C3{"강설량 10mm/h 이상"}

    C2 & C3 --> |"YES"|D1["설치, 인상, 해체, 점검, 수리 등을 중지"]
    C1 --> |"YES"|D2{"순간풍속 15m/s 이상"}
    D2 --> |"NO"|D1["설치, 인상, 해체, 점검, 수리 등을 중지"]
    D2 --> |"YES"|E1["운전작업을 중지"]

    D1 & E1--> F(["크레인 작업"])
    """

    @rule_method
    def Instantaneous_Wind_Speed(fIInsWin, fIPre, fISno) -> str:
        """ 크레인 작업
        Args:
        fIInsWin (float): 순간 풍속
        fIPre (float): 강수량
        fISno (float): 강설량

        Returns:
        sOCraOpe (str): 크레인 작업
        """
        assert isinstance(fIInsWin, float)
        assert isinstance(fIPre, float)
        assert isinstance(fISno, float)

        if 10 <= fIInsWin < 15 or fIPre >= 1 or fISno >= 10:
          sOCraOpe = '설치·인상·해체·점검·수리 등을 중지'
        elif fIInsWin >= 15:
          sOCraOpe = '운전작업을 중지'
        else:
          sOCraOpe = '정상작업'

        return RuleUnitResult(
                result_variables = {
                    "sOCraOpe": sOCraOpe
                }
            )