import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244020_030501_07(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 40 20 3.5.1 (7)'
    ref_date = '2016-06-30'
    doc_date = '2023-10-17'
    title = '프라이머 건조 양생 시간'

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량방수
    3. 시공
    3.5 시트식 방수재 시공
    3.5.1 시공일반
    (7)
    """

    # 건설기준문서내용(text)
    content = """
    #### (7) 프라이머는 도포 후 20분 ∼ 60분 동안 건조 양생시켜야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 프라이머 건조 양생 시간];
    B["KCS 24 40 20 3.5.1 (7)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 20 3.5.1 (7)"])

    subgraph Variable_def
    VarOut[/출력변수: 프라이머 건조 양생 시간/];
    VarIn1[/입력변수: 프라이머 건조 양생 시간/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"20 < 프라이머 건조 양생 시간 < 60"}
    C --> |"True"|Pass([Pass])
    C --> |"False"|Fail([Fail])
    """

    @rule_method
    def curing_time(fICurTim)->str:
        """
        Args:
            fICurTim (float): 프라이머 건조 양생 시간
        Returns:
            sOCurTim (string): 프라이머 건조 양생 시간
        """
        if fICurTim > 20 and fICurTim < 60:
            sOCurTim = "Pass"
        else:
            sOCurTim = "Fail"
        return sOCurTim