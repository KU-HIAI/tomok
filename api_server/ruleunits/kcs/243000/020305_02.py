import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS243000_020305_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 30 00 2.3.5 (2)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-08'
    title = '핀 및 롤러 지름의 허용오차'

    description = """
    강교량공사
    2. 자재
    2.3 자재의 허용오차
    2.3.5 주조품
    (2)
    """
    content = """
    #### 2.3.5 주조품
    (2) 핀 및 롤러 지름의 허용오차는 ±0.2 mm 이내이어야 하며, 서로 이웃하는 롤러의 지름의 허용오차는 0.1 mm 이내이어야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 핀 및 롤러 지름의 허용오차];
    B["KCS 24 30 00 2.3.5 (2)"];
    B ~~~ A
    end

    KCS(["KCS 24 30 00 2.3.5 (2)"])

    subgraph Variable_def
    VarIn1[/입력변수: 서로 이웃하는 롤러의 지름/];
    VarIn2[/입력변수: 핀 및 롤러 지름의 설계값/];
    VarIn3[/입력변수: 핀 및 롤러 지름의 시공값/];
    VarIn1 ~~~ VarIn2 & VarIn3
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"서로 이웃하는 롤러의 지름"}
    C --> |"True"|D{"|핀 및 롤러 지름의 설계값-핀 및 롤러 지름의 시공값| \n < 0.2 mm \n."}
    C --> |"False"|E{"|핀 및 롤러 지름의 설계값-핀 및 롤러 지름의 시공값| \n < 0.1 mm \n."}
    D & E --> End([Pass or Fail])
    """

    @rule_method

    def tolerance_pin_roller(bIAdjRol,fIDesDia,fIConDia) -> RuleUnitResult:
        """
        Args:
            bIAdjRol (bool): 서로 이웃하는 롤러의 지름
            fIDesDia (float): 핀 및 롤러 지름의 설계값
            fIConDia (float): 핀 및 롤러 지름의 시공값

        Returns:
            pass_fail (bool): 강교량공사 2.3.5 주조품 (2)의 판단 결과
        """
        assert isinstance(bIAdjRol, bool)
        assert isinstance(fIDesDia, float)
        assert isinstance(fIConDia, float)

        if bIAdjRol == False:
            if abs(fIDesDia - fIConDia)<0.2:
                pass_fail = True
            else:
                pass_fail = False
        else:
            if abs(fIDesDia - fIConDia)<0.1:
                pass_fail = True
            else:
                pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })