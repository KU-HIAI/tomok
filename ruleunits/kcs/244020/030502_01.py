import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244020_030502_01(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 40 20 3.5.2 (1)'
    ref_date = '2016-06-30'
    doc_date = '2023-10-17'
    title = '시트식 방수재 시공 시 접착용 아스팔트의 용해'

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량방수
    3. 시공
    3.5 시트식 방수재 시공
    3.5.2 접착형 시트 부착
    (7)
    """

    # 건설기준문서내용(text)
    content = """
    #### (1) 접착용 아스팔트의 용해 온도는 210 ℃ 정도이며, 전용 용제를 사용하여야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 시트식 방수재 시공 시 접착용 아스팔트의 용해];
    B["KCS 24 40 20 3.5.2 (1)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 20 3.5.2 (1)"])

    subgraph Variable_def
    VarOut[/출력변수: 접착용 아스팔트의 용해/];
    VarIn1[/입력변수: 용해 온도/];
    VarIn2[/입력변수: 전용 용제/];
    VarOut ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"용해 온도 = 210 ℃"}
    C --> |"True"|D{전용 용제}
    C --> |"False"|Fail([Fail])
    D --> |"False"|Fail([Fail])
    D --> |"True"|Pass([Pass])
    """

    @rule_method
    def melt_adhesive_asphalt(fIMelTem,bIDedSol)->str:
        """
        Args:
            fIMelTem (float): 용해 온도
            bIDedSol (boolean): 전용 용제
        Returns:
            sOMelAsp (string): 프라이머 건조 양생 시간
        """
        if fIMelTem == 210:
            if bIDedSol == True:
                sOMelAsp = "Pass"
            else:
                sOMelAsp = "Fail"
        else:
            sOMelAsp = "Fail"
        return sOMelAsp