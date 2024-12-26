import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244020_0303_06(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 20 3.3 (6)'
    ref_date = '2016-06-30'
    doc_date = '2023-10-13'
    title = '표준 양생시간'

    description = """
    교량방수
    3. 시공
    3.3 접착층의 시공
    (6)
    """
    content = """
    #### 3.3 접착층의 시공
    (6) 양생시간은 고무아스팔트계 및 합성고무계는 20 ℃에서 1시간 정도, 5 ℃에서 2시간 정도이고, 수지계는 20 ℃에서 15분 이내, 5 ℃에서 30분 이내를 표준으로 하며,
    접착제의 종류⋅기온⋅바람⋅지촉건조시간 등을 고려하여 결정한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 표준 양생시간];
    B["KCS 24 40 20 3.3 (6)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 20 3.3 (6)"])

    subgraph Variable_def
    VarOut[/출력변수: 표준 양생시간/];
    VarIn1[/입력변수: 고무아스팔트계/];
    VarIn2[/입력변수: 합성고무계/];
    VarIn3[/입력변수: 수지계/];
    VarIn4[/입력변수: 기온/];
    VarOut ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{수지계, 고무아스팔트계, 합성고무계}
    C --> |고무아스팔트계, 합성고무계|D{기온}
    D --> |"20℃"|E[60분]
    D --> |"5℃"|F[120분]
    C --> |수지계|G{기온}
    G --> |"20℃"|H[ 15분]
    G --> |"5℃"|I[30분]
    E & F & H & I --> End([표준 양생시간])
    """

    @rule_method

    def curing_time(bIRubAsp, bISynRub,bIRes,nITem) -> RuleUnitResult:
        """
        Args:
            bIRubAsp (bool): 고무아스팔트계
            bISynRub (bool): 합성고무계
            bIRes (bool): 수지계
            nITem (int): 기온

        Returns:
            fOCurTim (float): 표준양생시간
        """
        assert isinstance(bIRubAsp, bool)
        assert isinstance(bISynRub, bool)
        assert isinstance(bIRes, bool)
        assert (bIRubAsp+bISynRub+bIRes) == 1
        assert isinstance(nITem, int)
        assert nITem == 20 or nITem == 5

        if bIRubAsp == True or bISynRub == True:
            if nITem == 20:
                fOCurTim = 60
            elif nITem == 5:
                fOCurTim = 120
        elif bIRes:
            if nITem == 20:
                fOCurTim = 15
            elif nITem == 5:
                fOCurTim = 60

        return RuleUnitResult(
            result_variables = {
                "fOCurTim": fOCurTim,
                })