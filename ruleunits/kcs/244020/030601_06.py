import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244020_030601_06(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 40 20 3.6.1 (6)'
    ref_date = '2016-06-30'
    doc_date = '2023-10-17'
    title = '도막식 방수재 시공 시 프라이머의 사용량'

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량방수
    3. 시공
    3.6 도막식 방수재의 시공
    3.6.1 시공일반
    (6)
    """

    # 건설기준문서내용(text)
    content = """
    #### (6) 프라이머의 표준 사용량은 0.2 L/m2 ∼ 0.5 L/m2 이며, 재료사양에 따라 변화할 수 있으므로 시험시공을 실시 후 감독자의 승인을 받은 후 시공하여야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 도막식 방수재 시공 시 프라이머의 사용량];
    B["KCS 24 40 20 3.6.1 (6)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 20 3.6.1 (6)"])

    subgraph Variable_def
    VarOut[/출력변수: 프라이머의 사용량/];
    VarIn1[/입력변수: 프라이머의 사용량/];
    VarIn2[/입력변수: 시험시공 실시 후 감독자의 승인/];
    VarOut ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"0.2 < 프라이머의 사용량 <0.5"}
    C --> |False|D{시험시공 실시 후 감독자의 승인}
    D --> |"True"|Pass([Pass])
    D --> |"False"|Fail([Fail])
    C --> |True|Pass([Pass])
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