import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS243000_020201_04(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 30 00 2.2.1 (4)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-08'
    title = '교량구조용 압연강재 강판의 두께'

    # 건설기준문서항목 (분류체계정보)
    description = """
    강교량공사
    2. 자재
    2.2 사용재료
    2.2.1 강판
    (4)
    """

    # 건설기준문서내용(text)
    content = """
    ####(4) 교량구조용 압연강재: KS D 3868
    \begin{table}[]
    \begin{tabular}{llll}
    규격                         & 종류     & 기호                                                & 두께 t(㎜)     \\
    \multirow{3}{*}{KS D 3868} & HSB500 & \begin{tabular}[c]{@{}l@{}}-\\ L\\ W\end{tabular} & 8 ≤ t ≤ 100 \\
                            & HSB600 & \begin{tabular}[c]{@{}l@{}}-\\ L\\ W\end{tabular} & 8 ≤ t ≤ 100 \\
                            & HSB800 & \begin{tabular}[c]{@{}l@{}}-\\ L\\ W\end{tabular} & 8 ≤ t ≤ 80
    \end{tabular}
    \end{table}
    표 2.2-1 강재 사용 규격
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 교량구조용 압연강재 강판의 두께];
    B["KCS 24 30 00 2.2.1 (4)"];
    B ~~~ A
    end

    KCS(["KCS 24 30 00 2.2.1 (4)"])

    subgraph Variable_def
    VarOut[/출력변수: 강판의 두께/];
    VarIn1[/입력변수: 교량구조용 압연강재/];
    VarIn2[/입력변수: 강판의 두께/];
    VarIn3[/입력변수: 종류/];
    VarOut ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"교량구조용 압연강재"}
    C --> |True|D{"종류"}
    D --> E{표2.2-1}
    E --> |True|P([Pass])
    E --> |False|Fail([Fail])
    """

    @rule_method
    def thickness_steel_plate(bIRolBri, fIThiSte,sITyp)-> str:
        """
        Args:
            bIRolBri (boolean): 용접구조용 내후성 열간 압연강재
            fIThiSte (float): 강판의 두께
            sITyp (string): 종류
        Returns:
            sOThiSte (string): 강판의 두께
        """
        if bIRolBri:
            if sITyp =="HSB500" or sITyp =="HSB600":
                if fIThiSte >=8 and fIThiSte <=100:
                    sOThiSte = "Pass"
                else:
                    sOThiSte = "Fail"
            elif sITyp =="HSB800":
                if fIThiSte >=8 and fIThiSte <=80:
                    sOThiSte = "Pass"
                else:
                    sOThiSte = "Fail"
            else:
                return "HSB500, HSB600, HSB800 중에서 선택해주세요"
        else:
            return "KCS 24 30 00 2.2.1 (1), (2), (3)를 확인해주세요"
        return sOThiSte