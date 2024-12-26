import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS213000_0204_03(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 30 00 2.4 (3)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-13'
    title = '슬러리의 입도'

    description = """
    가설흙막이 공사
    2. 자재
    2.4 지하연속벽
    (3)
    """

    content = """
    #### 2.4. 지하연속벽
    (3) 슬러리는 천연산의 분말 벤토나이트로서 입도는 90％ 이상이 0.850mm 보다 가늘고, 0.075mm 보다 가는 것은 10％ 미만이어야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 슬러리의 입도];
    B["KCS 21 30 00 2.4 (3)"];
    B ~~~ A
    end

    KCS(["KCS 21 30 00 2.4 (3)"])

    subgraph Variable_def
    VarIn1[/입력변수: 슬러리의 입도/]; VarIn2[/입력변수: 슬러리의 비율/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"슬러리의 입도 < 0.075mm"}
    C --> |"YES"|C1{"슬러리의 비율 = 10%"}
    C --> |"NO"|C2{"슬러리의 입도 < 0.850mm"}
    C2 --> |"YES"|D1{"슬러리의 비율 = 90%"}

    C1 & C2 & D1 --> E([Pass or Fail])
    """

    @rule_method
    def Particle_Size_of_Slurry(fISizSlu, fISluRat) -> RuleUnitResult:
        """ 슬러리의 입도
        Args:
            fISizSlu (float): 슬러리의 입도
            fISluRat (float): 슬러리의 비율

        Returns:
            pass_fail (bool): 가설흙막이 공사 2.4 지하연속벽 (3)의 판단 결과
        """
        assert isinstance(fISizSlu, float)
        assert isinstance(fISluRat, float)

        if fISizSlu <= 0.075:
          if fISluRat < 10:
            pass_fail = True
          else:
            pass_fail = False
        elif 0.075 < fISizSlu <= 0.850:
          if fISluRat >= 90:
            pass_fail = True
          else:
            pass_fail = False
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )