import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244020_030501_01(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 40 20 3.5.1 (1)'
    ref_date = '2016-06-30'
    doc_date = '2023-10-13'
    title = '시트식 방수재의 시공두께'

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량방수
    3. 시공
    3.5 시트식 방수재 시공
    3.5.1 시공일반
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    #### (1) 시트식 방수재의 시공두께는 3.5 mm 이상을 확보하여야 하고 접착공법을 사용한 경우는 융착형 보다 다소 작은 3.0 mm 이상이 되어야한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 시트식 방수재의 시공두께];
    B["KCS 24 40 20 3.5.1 (1)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 20 3.5.1 (1)"])

    subgraph Variable_def
    VarOut[/출력변수: 시트식 방수재의 시공두께/];
    VarIn1[/입력변수: 시트식 방수재의 시공두께/];
    VarIn2[/입력변수: 접착공법/];
    VarOut ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{접착공법}
    C --> |False|D{시트식 방수재의 시공두께}
    D --> |"≥ 3.5 mm"|Pass([Pass])
    D --> |"< 3.5 mm"|Fail([Fail])
    C --> |True|E{시트식 방수재의 시공두께}
    E --> |"≥ 3.0 mm"|Pass([Pass])
    E --> |"< 3.0 mm"|Fail([Fail])
    """

    @rule_method
    def thickness_sheet_waterproof(fIThiWat,bIAdhMet)->str:
        """
        Args:
            fIThiWat (float): 시트식 방수재의 시공두께
            bIAdhMet (boolean): 접착공법
        Returns:
            sOThiWat (string): 시트식 방수재의 시공두께
        """
        if bIAdhMet == False:
            if fIThiWat >=3.5:
                sOThiWat = "Pass"
            else:
                sOThiWat = "Fail"
        else:
            if fIThiWat >=3.0:
                sOThiWat = "Pass"
            else:
                sOThiWat = "Fail"
        return sOThiWat