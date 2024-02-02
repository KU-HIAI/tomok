import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244005_020604_03(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 40 05 2.6.4 (3)'
    ref_date = '2018-08-30'
    doc_date = '2023-11-07'
    title = '채움재를 넣지 않은 PTFE판의 성질'

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량받침
    2. 자재
    2.6.1 받침의 구성부품
    2.6.4 받침용 PTFE판
    (3)
    """

    # 건설기준문서내용(text)
    content = """
    #### (3) 채움재를 넣지 않은 PTFE판은 신생 PTFE 수지로 만들어져야 하며, 인장강도는 최소 17.9 MPa 이상, 신장율은 최소 200% 이상이어야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 채움재를 넣지 않은 PTFE판의 성질];
    B["KCS 24 40 05 2.6.4 (3)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 05 2.6.4 (3)"])

    subgraph Variable_def
    VarOut[/출력변수: 채움재를 넣지 않은 PTFE판의 성질/];
    VarIn1[/입력변수: 신생 PTFE 수지/];
    VarIn2[/입력변수: 인장강도/];
    VarIn3[/입력변수: 신장율/];
    VarOut ~~~ VarIn1 & VarIn2 & VarIn3
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{신생 PTFE 수지}
    C --> |"True"|BB{"인장강도 ≥ 17.9 MPa"}
    C --> |"False"|Fail([Fail])
    BB --> |"True"|MM{"신장율 ≥ 200%"}
    BB --> |"False"|Fail([Fail])
    MM --> |"False"|Fail([Fail])
    MM --> |"True"|P([Pass])
    """

    @rule_method
    def PTFE_without_backfill(bINewPtf,fITenStr,fIElo)->str:
        """
        Args:
            bINewPtf (boolean): 신생 PTFE 수지
            fITenStr (float): 인장강도
            fIElo (float): 신장율
        Returns:
            sOPtfPla (string): 채움재를 넣지 않은 PTFE판의 성질
        """
        if bINewPtf == True:
            if fITenStr >= 17.9:
                if fIElo >= 200:
                    sOPtfPla = "Pass"
                else:
                    sOPtfPla = "Fail"
            else:
                sOPtfPla = "Fail"
        else:
            sOPtfPla = "Fail"
        return sOPtfPla