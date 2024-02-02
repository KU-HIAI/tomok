import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244020_030501_06(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 40 20 3.5.1 (6)'
    ref_date = '2016-06-30'
    doc_date = '2023-10-17'
    title = '프라이머의 사용량'

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
    #### (6) 프라이머의 표준 사용량은 0.2 L/m2 ∼ 0.5 L/m2 이며, 재료사양에 따라 변화할 수 있으므로 시험시공을 실시 후 감독자의 승인을 받은 후 시공하여야 한다.
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
    def primer_usage(fIPriUsa,bIAppTri)->str:
        """
        Args:
            fIPriUsa (float): 프라이머의 사용량
            bIAppTri (boolean): 시험시공 실시 후 감독자의 승인
        Returns:
            sOPriUsa (string): 프라이머의 사용량
        """
        if fIPriUsa > 0.2 and fIPriUsa < 0.5:
            sOPriUsa = "Pass"
        else:
            if bIAppTri:
                sOPriUsa = "Pass"
            else:
                sOPriUsa = "Fail"
        return sOPriUsa