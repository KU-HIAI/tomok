import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244025_03010000_04(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 40 25 3.3.1 (4)'
    ref_date = '2018-08-30'
    doc_date = '2023-08-15'
    title = '배수관의 경사'

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량배수시설공
    3. 시공
    3.3 배수관의 설치방법
    3.3.1 시공일반
    (4)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.3.1 시공 일반
    (4) 배수관의 경사는 3% 이상으로 한다.

    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 배수관의 경사];
    B["KCS 24 40 25 3.3.1 (4)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 25 3.3.1 (4)"])

    subgraph Variable_def
    VarOut[/출력변수: 배수관의 경사/];
    VarIn1[/입력변수: 배수관의 경사/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"배수관의 경사 ≥ 3%"}
    C --> |"True"|D(["Pass"])
    C --> |False|E(["Fail"])

    """

    @rule_method
    def slope_drainage_pipe(fISloDra) -> bool:
        """

        Args:
            sOSloDra (string): 배수관의 경사
            fISloDra (float): 배수관의 경사
        Returns:
            sOSloDra (string): 배수관의 경사
        """
        if fISloDra >= 3:
            sOSloDra = "Pass"
        else:
            sOSloDra = "Fail"
        return sOSloDra