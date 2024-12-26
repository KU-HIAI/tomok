import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS115020_030402_13(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 11 50 20 3.4.2 (13)'
    ref_date = '2021-05-12'
    doc_date = '2023-09-15'
    title = '강널말뚝 항타 시 지수재 도포'

    description = """
    널말뚝
    3. 시공
    3.4 강널말뚝
    3.4.2 강널말뚝 항타
    (13)
    """
    content = """
    ####3.4.2 강널말뚝 항타
    (13) 지수재는 충분한 팽창성을 지닌 것이어야 하며, 지수재의 도포량은 연결부 일면에 200g/m (3mm~4mm 두께)를 도포하고, 도포 후 하절기 12시간~24시간, 동절기 24시간~48시간 경화시켜 사용한다.
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 강널말뚝 항타 시 지수재 도포];
    B["KCS 11 50 20 3.4.2 (13)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 20 3.4.2 (13)"])

    subgraph Variable_def
    VarOut1[/출력변수: 지수재의 도포량/];
    VarIn1[/입력변수: 지수재 도포 후 경화시간/];
    VarIn2[/입력변수: 하절기/];
    VarIn3[/입력변수: 동절기/];
    VarOut1~~~ VarIn1 & VarIn3
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"지수재의 도포량, \n 지수재 도포 후 경화시간 \n."}
    C --> |"지수재의 도포량"|D["200g/m (3mm~4mm 두께)"]
    C --> |"지수재 도포 후 경화시간"|E{동절기 \n 하절기}
    E --> |"하절기"|F{"12시간<=지수재 도포 후 경화시간<=24시간"}
    E --> |"동절기"|G{"24시간<=지수재 도포 후 경화시간<=48시간"}
    D --> End1([강널말뚝 항타 시 지수재 사용])
    F & G --> End2([Pass or Fail])
    """

    @rule_method
    def hardening(bISumSea, bIWinSea, fIHarTim)-> RuleUnitResult:
        """
        Args:
            bISumSea (bool): 하절기
            bIWinSea (bool): 동절기
            fIHarTim (float): 지수재 도포 후 경화시간

        Returns:
            sOSprWat (string): 지수재의 도포량
            pass_fail (bool): 널말뚝 3.4.2 강널말뚝 항타 (13)의 판단 결과

        """
        assert isinstance(bISumSea, bool)
        assert isinstance(bIWinSea, bool)
        assert isinstance(fIHarTim, float)
        assert bISumSea != bIWinSea
        assert 0 <= fIHarTim <200

        sOSprWat = "200g/m (3mm~4mm 두께)"

        if bISumSea:
            if fIHarTim >=12 and fIHarTim <=24:
                return RuleUnitResult(
                    result_variables = {
                        "sOSprWat": sOSprWat,
                        "pass_fail": True,
                    }
                )
            else:
                return RuleUnitResult(
                    result_variables = {
                        "sOSprWat": sOSprWat,
                        "pass_fail": False,
                    }
                )
        if bIWinSea:
            if fIHarTim >=24 and fIHarTim <=48:
                return RuleUnitResult(
                    result_variables = {
                        "sOSprWat": sOSprWat,
                        "pass_fail": True,
                    }
                )
            else:
                return RuleUnitResult(
                    result_variables = {
                        "sOSprWat": sOSprWat,
                        "pass_fail": False,
                    }
                )