import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143140_032002(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 40 3.20.2'
    ref_date = '2019-05-20'
    doc_date = '2023-10-31'
    title = '실제도포율 산출방법'

    description = """
    도장
    3. 시공
    3.20 도료소요량의 산출방법
    3.20.2 실제도포율 산출방법
    """

    content = """
    #### 3.20.2 실제도포율 산출방법
    \text { 실제도포율 }\left(\mathrm{m}^2 / l\right)=\text { 이론도포율 }\left(\mathrm{m}^2 / l\right) \times(1 - \text { 손실률 } / 100)
    \text { 실제도포율 }\left(\mathrm{m}^2 / l\right)=\text { 이론도포율 }\left(\mathrm{m}^2 / l\right) \times \text { 표면조도인자 } \times \text { 작업조도인자 }
    여기서 표면조도인자는 표면정리의 상태, 도장재의 종류를 구분하여 결정된 인자이며, 작업조도인자는 도장기구 및 도장작업장의 조건에 따른 차이를 감안한 인자이다.
    """

    flowchart = """
    flowchart TD
        subgraph Python_Class
        A[Title: 실제도포율 산출방법];
        B["KCS 14 31 40 3.20.1"];
        B ~~~ A
        end

        KCS(["KCS 14 31 40 3.20.1"])

        subgraph Variable_def
        VarOut1[/출력변수: 실제 도포율/];
        VarIn1[/입력변수: 이론 도포율/];
        VarIn2[/입력변수: 손실률/];
        VarIn3[/입력변수: 표면조도인자/];
        VarIn4[/입력변수: 작업조도인자/];
		    VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4
		    end

        Python_Class ~~~ KCS
        KCS --> Variable_def
		    Variable_def --> C{손실률}
		    C --> |True|D["실제 도포율 = 이론도포율 * (1-손실률/100)"]
		    C --> |False|E["실제 도포율 = 이론도포율 * 표면조도인자 * 작업조도인자"]
		    D & E --> End([실제 도포율])
    """

    @rule_method
    def Theoric_Spreading_Rate(fITheSpr, fILosRat, bILosRat, fISurPar, fIWorRou) -> float:
        """ 실제도포율 산출방법
        Args:
        fITheSpr (float): 이론 도포율
        fILosRat (float): 손실률
        bILosRat (bool): 손실률
        fISurPar (float): 표면조도인자
        fIWorRou (float): 작업조도인자

        Returns:
        fORSprRa (float): 실제 도포율
        """
        assert isinstance(fITheSpr, float)
        assert isinstance(fILosRat, float)
        assert isinstance(bILosRat, bool)
        assert isinstance(fISurPar, float)
        assert isinstance(fIWorRou, float)

        if bILosRat == True:
          fORSprRa = fITheSpr * (1 - fILosRat/100)
        elif bILosRat == False:
          fORSprRa = fITheSpr * fISurPar * fIWorRou

        return RuleUnitResult(
                result_variables = {
                    "fORSprRa": fORSprRa
                }
            )