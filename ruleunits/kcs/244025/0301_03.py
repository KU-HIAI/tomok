import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244025_03010000_03(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 40 25 3.1 (3)'
    ref_date = '2018-08-30'
    doc_date = '2023-08-15'
    title = '배수구의 간격'

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량배수시설공
    3. 시공
    3.1 시공일반
    (3)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.1 시공일반
    (3) 배수구의 간격은 20 m 이하로 되어야 한다

    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 배수구의 간격];
    B["KCS 24 40 25 3.1 (3)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 25 3.1 (3)"])

    subgraph Variable_def
    VarOut[/출력변수: 배수구의 간격/];
    VarIn1[/입력변수: 배수구의 간격/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"배수구의 간격 ≤ 20 m"}
    C --> |"True"|D(["Pass"])
    C --> |False|E(["Fail"])
    """

    @rule_method
    def drainage_spacing(fISpaDra):
        """

        Args:
            fISpaDra (float): 배수구의 간격
        Returns:
            sOSpaDra (string): 배수구의 간격
        """
        if fISpaDra <= 20:
            sOSpaDra = "Pass"
        else:
            sOSpaDra = "Fail"
        return sOSpaDra