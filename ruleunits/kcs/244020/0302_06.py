import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244020_0302_06(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 40 20 3.2 (6)'
    ref_date = '2016-06-30'
    doc_date = '2023-10-13'
    title = '직사광선에 의한 작업'

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량방수
    3. 시공
    3.2 기상 조건
    (6)
    """

    # 건설기준문서내용(text)
    content = """
    #### (6) 직사광선에 의한 급격한 양생을 방지하고 기포의 발생 억제를 위하여 해가 있는 경우는 15시 이전, 해가 없는 경우는 13시 이전에 작업을 할 경우에는 감독자의 지시에 따라야 한다.
    """

    # 플로우차트(mermaid)
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

    Python_Class ~~~ KCS3
    KCS --> Variable_def
    Variable_def --> C{해가 있는 경우}
    C --> |"True"|D{작업시각}
    D --> |작업시각 < 15시|E[급격한 양생을 방지하고 기포의 발생 억제를 위하여 \n 감독자의 지시에 따라야 한다.]
    C --> |"False"|F{작업시각}
    F --> |작업시각 < 13시|E[급격한 양생을 방지하고 기포의 발생 억제를 위하여 \n 감독자의 지시에 따라야 한다.]
    D --> |작업시각 > 15시|Pass([Pass])
    F --> |작업시각 > 13시|Pass([Pass])
    E --> End([직사광선에 의한 작업])
    """

    @rule_method
    def working_in_sunlight(bISun,fIWorTim)->str:
        """
        Args:
            bISun (boolean): 해
            fIWorTim (float): 작업시각
        Returns:
            sOWorSun (string): 직사광선에 의한 작업
        """
        if bISun:
            if fIWorTim < 15:
                sOWorSun ="감독자의 지시에 따라야 한다."
            else:
                sOWorSun = "Pass"
        else:
            if fIWorTim <13:
                sOWorSun ="감독자의 지시에 따라야 한다."
            else:
                sOWorSun = "Pass"
        return sOWorSun