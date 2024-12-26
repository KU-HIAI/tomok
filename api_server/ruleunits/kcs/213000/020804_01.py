import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS213000_020804_01(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 30 00 2.8.4 (1)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-19'
    title = '장비의 재료 및 조건'

    description = """
    가설흙막이 공사
    2. 자재
    2.8 지반 그라우팅
    2.8.4 그라우팅 장비 및 재료
    (1)
    """

    content = """
    #### 2.8.4. 그라우팅 장비 및 재료
    (1) JSP(Jumbo Special Pattern) 장비 및 재료
    ① 펌프는 20MPa 이상의 토출압력과 토출량 60/min 이상인 것을 사용하여야 한다.
    ③ 발전기(generator)는 220V, 150kWh 이상의 것을 사용하여야 한다.
    ④ 콤프레셔(compressor)는 10.3m3/min(365CFM), 100Psi 이상의 것을 사용하여야 한다.
    ⑤ 시멘트 믹서(cement mixer)는 1m3 이상의 것을 사용하여야 한다.
    ⑦ 시멘트와 물의 배합은 중량 배합비로 1:1을 원칙으로 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: JSP 장비 및 재료];
    B["KCS 21 30 00 2.8.4 (1)"];
    B ~~~ A
    end

    KCS(["KCS 21 30 00 2.8.4 (1)"])

    subgraph Variable_def
    VarIn1[/입력변수: 펌프 토출압력/]; VarIn2[/입력변수: 펌프 토출량/];
    VarIn3[/입력변수: 발전기 전압/]; VarIn4[/입력변수: 발전기 전력량/];
    VarIn5[/입력변수: 콤프레셔 압력/]; VarIn6[/입력변수: 콤프레셔 풍량/];
    VarIn7[/입력변수: 시멘트 믹서 용량/]; VarIn8[/입력변수: 시멘트와 물의 중량 배합비/];
    end
		VarIn1 & VarIn2 & VarIn3 & VarIn4 ~~~ VarIn5

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"장비 및 재료의 조건"}
    C1 --> |"토출압력"|D1{">= 20 Mpa"}
    C1 --> |"토출량"|D2{">= 60 l/min"}
    C1 --> |"발전기 전압"|D3{">= 220V"}
    C1 --> |"발전기 전력량"|D4{">= 150kWh"}
    C1 --> |"콤프레셔 압력"|D5{">= 100Psi"}
    C1 --> |"콤프레셔 풍량"|D6{">= 365CFM"}
    C1 --> |"시멘트 믹서 용량"|D7{">= 1m^3"}
    C1 --> |"시멘트와 물의 중량 배합비"|D8{"= 1:1"}

    D1 & D2 & D3 & D4 & D5 & D6 & D7 & D8--> E([Pass or Fail])
    """

    @rule_method
    def Discharge_Pressure_of_Pump(fIPrePum, fIPumVol, fIGenVol, fIGenPow, fIComPre, fIComAir, fICapCem, fICemWat) -> bool:
        """ 장비의 재료 및 조건
        Args:
            fIPrePum (float): 펌프 토출압력
            fIPumVol (float): 펌프 토출량
            fIGenVol (float): 발전기 전압
            fIGenPow (float): 발전기 전력량
            fIComPre (float): 콤프레셔 압력
            fIComAir (float): 콤프레셔 풍량
            fICapCem (float): 시멘트 믹서 용량
            fICemWat (float): 시멘트와 물의 중량 배합비

        Returns:
            pass_fail (bool): 가설흙막이 공사 2.8.4 그라우팅 장비 및 재료 (1)의 판단 결과
        """
        assert isinstance(fIPrePum, float)
        assert isinstance(fIPumVol, float)
        assert isinstance(fIGenVol, float)
        assert isinstance(fIGenPow, float)
        assert isinstance(fIComPre, float)
        assert isinstance(fIComAir, float)
        assert isinstance(fICapCem, float)
        assert isinstance(fICemWat, float)

        if fIPrePum >= 20 and fIPumVol >= 60 and fIGenVol >= 220 and fIGenPow >= 150 and fIComPre >= 10.3 and fIComAir >= 100 and fICapCem >= 1 and fICemWat == 1:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )