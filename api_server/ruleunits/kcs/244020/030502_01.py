import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244020_030502_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 20 3.5.2 (1)'
    ref_date = '2016-06-30'
    doc_date = '2023-10-17'
    title = '시트식 방수재 시공 시 접착용 아스팔트의 용해'

    description = """
    교량방수
    3. 시공
    3.5 시트식 방수재 시공
    3.5.2 접착형 시트 부착
    (1)
    """
    content = """
    #### 3.5.2 접착형 시트 부착
    (1) 접착용 아스팔트의 용해 온도는 210 ℃ 정도이며, 전용 용제를 사용하여야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 시트식 방수재 시공 시 접착용 아스팔트의 용해];
    B["KCS 24 40 20 3.5.2 (1)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 20 3.5.2 (1)"])

    subgraph Variable_def
    VarIn1[/입력변수: 용해 온도/];
    VarIn2[/입력변수: 전용 용제/];
    VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"용해 온도 = 210 ℃
    and 전용 용제"}
    C --> End([Pass or Fail])
    """

    @rule_method

    def melt_adhesive_asphalt(fIMelTem,bIDedSol) -> RuleUnitResult:
        """
        Args:
            fIMelTem (float): 용해 온도
            bIDedSol (bool): 전용 용제

        Returns:
            pass_fail (bool): 교량방수 3.5.2 접착형 시트 부착 (1)의 판단 결과
        """
        assert isinstance(fIMelTem, float)
        assert isinstance(bIDedSol, bool)

        if fIMelTem == 210 and bIDedSol == True:
            pass_fail = True
        else:
            pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })