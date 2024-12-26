import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244020_0302_06(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 20 3.2 (6)'
    ref_date = '2016-06-30'
    doc_date = '2023-10-12'
    title = '직사광선에 의한 작업'

    description = """
    교량방수
    3. 시공
    3.2 기상 조건
    (6)
    """
    content = """
    #### 3.2 기상 조건
    (6) 직사광선에 의한 급격한 양생을 방지하고 기포의 발생 억제를 위하여 해가 있는 경우는 15시 이전, 해가 없는 경우는 13시 이전에 작업을 할 경우에는 감독자의 지시에 따라야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 직사광선에 의한 작업];
    B["KCS 24 40 20 3.2 (6)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 20 3.2 (6)"])

    subgraph Variable_def
    VarOut[/출력변수: 직사광선에 의한 작업/];
    VarIn1[/입력변수: 해/];
    VarIn2[/입력변수: 작업시각/];
    VarOut ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{해가 있는 경우}
    C --> |"True"|D{작업시각}
    D --> |작업시각 < 15시|E[급격한 양생을 방지하고 기포의 발생 억제를 위하여 \n 감독자의 지시에 따라야 한다.]
    C --> |"False"|F{작업시각}
    F --> |작업시각 < 13시|E[급격한 양생을 방지하고 기포의 발생 억제를 위하여 \n 감독자의 지시에 따라야 한다.]
    D --> |작업시각 > 15시|G[시공이 가능하다]
    F --> |작업시각 > 13시|G[시공이 가능하다]
    E & G --> End([직사광선에 의한 작업])
    """

    @rule_method

    def working_in_sunlight(bISun,fIWorTim) -> RuleUnitResult:
        """
        Args:
            bISun (bool): 해
            fIWorTim (float): 작업시각

        Returns:
            sOWorSun (str): 직사광선에 의한 작업
        """
        assert isinstance(bISun, bool)
        assert isinstance(fIWorTim, float)
        assert 0<=fIWorTim<=24

        if bISun:
            if fIWorTim < 15:
                sOWorSun ="감독자의 지시에 따라야 한다."
            else:
                sOWorSun = "시공이 가능하다"
        else:
            if fIWorTim <13:
                sOWorSun ="감독자의 지시에 따라야 한다."
            else:
                sOWorSun = "시공이 가능하다"

        return RuleUnitResult(
            result_variables = {
                "sOWorSun": sOWorSun,
                })