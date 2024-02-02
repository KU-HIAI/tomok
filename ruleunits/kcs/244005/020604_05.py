import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244005_020604_05(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 40 05 2.6.4 (5)'
    ref_date = '2018-08-30'
    doc_date = '2023-11-07'
    title = '일반적인 PTFE 섬유의 성질'

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량받침
    2. 자재
    2.6.1 받침의 구성부품
    2.6.4 받침용 PTFE판
    (5)
    """

    # 건설기준문서내용(text)
    content = """
    #### (5) 일반적인 PTFE 섬유의 인장강도는 17 MPa 이상, 신장률은 75% 이상이어야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 일반적인 PTFE 섬유의 성질];
    B["KCS 24 40 05 2.6.4 (5)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 05 2.6.4 (5)"])

    subgraph Variable_def
    VarOut[/출력변수: 일반적인 PTFE 섬유의 성질/];
    VarIn1[/입력변수: 인장강도/];
    VarIn2[/입력변수: 신장률/];
    VarOut ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"인장강도 ≥ 17 MPa"}
    C --> |"True"|BB{"신장율 ≥ 200%"}
    C --> |"False"|Fail([Fail])
    BB --> |"True"|P([Pass])
    BB --> |"False"|Fail([Fail])
    """

    @rule_method
    def PTFE_fiber(fITenStr,fIElo)->str:
        """
        Args:
            fITenStr (float): 인장강도
            fIElo (float): 신장률
        Returns:
            sOPtfFib (string): 일반적인 PTFE 섬유의 성질
        """
        if fITenStr >=17 and fIElo >=75:
            sOPtfFib = "Pass"
        else:
            sOPtfFib = "Fail"
        return sOPtfFib