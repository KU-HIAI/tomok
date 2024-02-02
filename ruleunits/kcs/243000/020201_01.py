import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS243000_020201_01(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 30 00 2.2.1 (1)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-08'
    title = '일반구조용 압연강재 강판의 두께'

    # 건설기준문서항목 (분류체계정보)
    description = """
    강교량공사
    2. 자재
    2.2 사용재료
    2.2.1 강판
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    ####(1) 일반구조용 압연강재: KS D 3503
    \begin{table}[]
    \begin{tabular}{llll}
    규격        & 종류    & 기호 & 두께 t(㎜)     \\
    KS D 3503 & SS400 & -  & 8 ≤ t ≤ 100
    \end{tabular}
    \end{table}
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 일반구조용 압연강재 강판의 두께];
    B["KCS 24 30 00 2.2.1 (1)"];
    B ~~~ A
    end

    KCS(["KCS 24 30 00 2.2.1 (1)"])

    subgraph Variable_def
    VarOut[/출력변수: 강판의 두께/];
    VarIn1[/입력변수: 강판의 두께/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"일반구조용 압연강재"}
    C --> |True|D{"8 ≤ 강판의 두께 ≤ 100"}
    D --> |True|E(["Pass"])
    D --> |True|F(["Fail"])
    """

    @rule_method
    def thickness_steel_plate(bIRolGen, fIThiSte)-> str:
        """
        Args:
            bIRolGen (boolean): 일반구조용 압연강재
            fIThiSte (float): 강판의 두께
        Returns:
            sOThiSte (string): 강판의 두께
        """
        if bIRolGen:
            if fIThiSte >=8 and fIThiSte <=100:
                sOThiSte = "Pass"
            else:
                sOThiSte = "Fail"
        else:
            return None
        return sOThiSte