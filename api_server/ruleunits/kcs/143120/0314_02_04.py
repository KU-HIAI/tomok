import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_0314_02_04(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 3.14 (2) ④'
    ref_date = '2019-05-20'
    doc_date = '2023-11-14'
    title = '응력제거 열처리'

    description = """
    용접
    3. 시공
    3.14 응력제거 열처리
    """

    content = """
    #### 3.14 응력제거 열처리
    (2) 응력제거 열처리는 다음 조건에 준하여 실시해야 한다.
    ④ 315 ℃ 이상에서의 냉각비(℃/hr)는 밀폐된 노(爐) 또는 용기 내에서 가장 두꺼운 부재를 기준으로 25 mm당 1시간에 315 ℃ 이하가 되어야 하며,
    어떠한 경우에도 단위시간당 냉각온도가 260 ℃를 초과해서는 안 된다. 또, 315 ℃ 미만에서는 조립품을 공냉 시킬 수 있다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: 응력제거 열처리"];
    B["KCS 14 31 20 3.14 (2) ④"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 3.14 (2) ④"])

    subgraph Variable_def
    VarOut[/"출력변수: 냉각비"/];
    VarIn1[/입력변수: 온도/];
    VarIn2[/입력변수: 냉각비/];
    VarIn3[/입력변수: 단위시간당 냉각온도/];
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"온도 ≥ 315℃"}
		C --> |True|D{가장 두꺼운 부재의 25mm 당 냉각비 <= 315 \n and 단위시간다 냉각온도 <=260}
    C --> |False|E[조립품을 공냉 시킬 수 있다.]
    E --> End2([냉각비])
    D --> End1([Pass or Fail])
    """

    @rule_method
    def Stress_Relief_Heat_Treatment(fITem, fICooRat, fICooTem) -> RuleUnitResult:
        """ 응력제거 열처리
        Args:
        fITem (float): 온도
        fICooRat (float): 가장 두꺼운 부재의 25mm 당 냉각비
        fICooTem (float): 단위시간당 냉각온도

        Returns:
        sOCooRat (str): 냉각비
        pass_fail (bool): 용접 3.14 응력제거 열처리 (2) ④의 판단 결과
        """
        assert isinstance(fITem, float)
        assert isinstance(fICooRat, float)
        assert isinstance(fICooTem, float)

        if fITem >= 315:
          if fICooRat <= 315 and fICooTem <= 260:
            pass_fail =True
            sOCooRat = None
          else:
            pass_fail = False
            sOCooRat = None
        else:
          pass_fail = False
          sOCooRat = "조립품을 공냉 시킬 수 있다."

        return RuleUnitResult(
                result_variables = {
                    "sOCooRat": sOCooRat,
                    "pass_fail": pass_fail
                }
            )