import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS116000_020302_03(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 11 60 00 2.3.2 (3)'
    ref_date = '2020-12-03'
    doc_date = '2023-08-16'
    title = '그라우트 펌프 및 호스의 압력'

    description = """
    앵커
    2. 자재
    2.3 장비
    2.3.2 그라우트 믹서 및 펌프
    (3)
    """

    content = """
    #### 2.3.2. 그라우트 믹서 및 펌프
    (3) 그라우트 펌프는 최소 주입압력이 0.5MPa 이상이어야 하며, 그라우트 호스 및 연결구는 최대 2MPa의 압력에 견딜 수 있는 자재를 사용하여야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 그라우트 펌프 및 호스의 압력];
    B["KCS 11 60 00 2.3.2 (3)"];
    B ~~~ A
    end

    KCS(["KCS 11 60 00 2.3.2 (3)"])

    subgraph Variable_def
    VarIn1[/입력변수: 그라우트펌프의 최소 주입압력/];
    VarIn2[/입력변수: 그라우트 호스 및 연결구의 허용압력/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"그라우트 펌프의 최소 주입압력 >= 0.5MPa and
그라우트 호스 및 연결구의 허용압력 >= 2MPa"}
    C--> D(["Pass or Fail"])
    """

    @rule_method
    def Minimim_Injection_Pressure_of_Grout_Pump(fIMinPre, fIPerPre) -> bool:
        """ 그라우트 펌프 및 호스의 압력
        Args:
          fIMinPre (float): 그라우트 펌프의 최소 주입압력
          fIPerPre (float): 그라우트 호스 및 연결구의 허용 압력

        Returns:
          pass_fail (bool): 앵커 2.3.2 그라우트 믹서 및 펌프 (3)의 판단 결과
        """
        assert isinstance(fIMinPre, float)
        assert isinstance(fIPerPre, float)

        if fIMinPre >= 0.5 and fIPerPre >= 2:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )