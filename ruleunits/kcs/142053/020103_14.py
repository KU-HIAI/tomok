import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS142053_020103_14(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 14 20 53 2.1.3 (14)'
    ref_date = '2022-01-11'
    doc_date = '2023-09-19'
    title = '덕트의 최소 내면 지름'

    # 건설기준문서항목 (분류체계정보)
    description = """
    프리스트레스트 콘크리트
    2. 자재
    2.1 구성재료
    2.1.3 프리스트레스트 콘크리트용 그라우트
    (14)
    """

    # 건설기준문서내용(text)
    content = """
    ####(14) 그라우트되는 단독 강선, 강연선 또는 강봉을 배치하기 위한 덕트는 내면 지름이 긴장재 지름보다 6 mm 이상 커야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 덕트의 최소 내면 지름];
    B["KCS 14 20 53 2.1.4 (14)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 53 2.1.4 (14)"])

    subgraph Variable_def
    VarOut[/출력변수: 덕트의 최소 내면 지름의 만족 여부/];
    VarIn1[/입력변수: 긴장재 지름/];
    VarIn2[/입력변수: 덕트 내면 지름/];

    VarOut ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"덕트의 최소 내면 지름 \n - 긴장재 지름 >= 6mm"}
    C --> |True|Pass([Pass])
    C --> |False|Fail([Fail])
    """

    @rule_method
    def internal_diameter_duct(fIIntDia,fITenDia):
        """
        Args:
            fIIntDia (float): 덕트의 내면 지름
            fITenDia (float): 긴장재 지름
        Returns:
            sODiaInt (sting): 덕트의 최소 내면 지름
        """
        if (fIIntDia-fITenDia)>=6:
            sODiaInt = "Pass"
        else:
            sODiaInt = "Fail"
        return sODiaInt