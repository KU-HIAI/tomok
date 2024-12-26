import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143130_030302_05(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 30 3.3.2 (5)'
    ref_date = '2023-09-11'
    doc_date = '2019-05-20'
    title = '용접개소에서의 풍속'

    description = """
    조립 및 설치
    3. 시공
    3.3 부재조립 및 설치
    3.3.2 건축물의 현장 조립
    (5)
    """

    content = """
    #### 3.3.2 건축물의 현장 조립
    (5) 현장용접
    ⑦ 용접개소에서의 풍속은 피복아크용접, 실드아크용접에서는 10 m/s, CO2반자동용접에서는 2 m/s를 넘어서지 않아야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: 용접개소에서의 풍속"];
    B["KCS 14 31 30 3.3.2 (5)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 30 3.3.2 (5)"])

    subgraph Variable_def
		VarIn1[/"입력변수: 용접의 종류"/];
		VarIn2[/"입력변수: 풍속"/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{"용접의 종류"}
		D --> |"'피복아크용접' \nor '실드아크용접'"|G{풍속 <= 10 m/s}
		D --> |'CO2반자동용접'|H{풍속 <= 2 m/s}
		G & H --> I([Pass or Fail])
    """

    @rule_method
    def wind_speed_at_welding_site(sITypWel, fIWinSpe) -> bool:
        """용접개소에서의 풍속

        Args:
            sITypWel (str): 용접의 종류
            fIWinSpe (float): 풍속

        Returns:
            pass_fail (bool) : 조립 및 설치 3.3.2 건축물의 현장 조립 (5)의 판단 결과
        """
        assert isinstance(sITypWel, str)
        assert sITypWel in["피복아크용접", "실드아크용접", "CO2반자동용접"]
        assert isinstance(fIWinSpe, float)

        if (sITypWel == "피복아크용접") or (sITypWel == "실드아크용접"):
            if fIWinSpe <= 10:
                pass_fail = True
            else:
                pass_fail = False
        elif sITypWel == "CO2반자동용접":
            if fIWinSpe <= 2:
                pass_fail = True
            else:
                pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
             }
         )