import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS243000_020201_02(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 30 00 2.2.1 (2)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-08'
    title = '용접구조용 압연강재 강판의 두께'

    # 건설기준문서항목 (분류체계정보)
    description = """
    강교량공사
    2. 자재
    2.2 사용재료
    2.2.1 강판
    (2)
    """

    # 건설기준문서내용(text)
    content = """
    ####(2) 용접구조용 압연강재: KS D 3515
    \begin{table}[]
    \begin{tabular}{llll}
    규격                         & 종류     & 기호                                                       & 두께 t(㎜)                                                                       \\
    \multirow{5}{*}{KS D 3515} & SM400  & \begin{tabular}[c]{@{}l@{}}A\\ B\\ C\end{tabular}        & \begin{tabular}[c]{@{}l@{}}8 ≤ t ≤ 32\\ 8 ＜ t ≤ 40\\ 8 ＜t ≤ 100\end{tabular}  \\
                            & SM490  & \begin{tabular}[c]{@{}l@{}}A\\ B\\ C, C-TMC\end{tabular} & \begin{tabular}[c]{@{}l@{}}8 ＜ t ≤ 25\\ 8 ≤ t ＜ 40\\ 8 ＜ t ≤ 100\end{tabular} \\
                            & SM490Y & \begin{tabular}[c]{@{}l@{}}A\\ B\end{tabular}            & \begin{tabular}[c]{@{}l@{}}8 ≤ t ≤ 16\\ 8 ≤ t ≤ 40\end{tabular}               \\
                            & SM520  & \begin{tabular}[c]{@{}l@{}}B\\ C, C-TMC\end{tabular}     & \begin{tabular}[c]{@{}l@{}}8 ≤ t ≤ 40\\ 8 ≤ t ≤ 100\end{tabular}              \\
                            & SM570  & \begin{tabular}[c]{@{}l@{}}-\\ TMC\end{tabular}          & 8 ≤ t ≤ 100
    \end{tabular}
    \end{table}
    표 2.2-1 강재 사용 규격
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 용접구조용 압연강재 강판의 두께];
    B["KCS 24 30 00 2.2.1 (2)"];
    B ~~~ A
    end

    KCS(["KCS 24 30 00 2.2.1 (2)"])

    subgraph Variable_def
    VarOut[/출력변수: 강판의 두께/];
    VarIn1[/입력변수: 용접구조용 압연강재/];
    VarIn2[/입력변수: 강판의 두께/];
    VarIn3[/입력변수: 종류/];
    VarIn4[/입력변수: 기호/];
    VarOut ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"용접구조용 압연강재"}
    C --> |True|D{용접구조용 압연강재\n 강판의 두께 \n 종류 \n 기호\n.}
    D --> |True|Pass([Pass])
    D --> |False|Fail([Fail])
    """

    @rule_method
    def thickness_steel_plate(bIRolWel, fIThiSte,sITyp,sISym)-> str:
        """
        Args:
            bIRolWel (boolean): 용접구조용 압연강재
            fIThiSte (float): 강판의 두께
            sITyp (string): 종류
            sISym (string): 기호
        Returns:
            sOThiSte (string): 강판의 두께
        """
        if bIRolWel:
            if sITyp == "SM400":
                if sISym == "A":
                    if fIThiSte >=8 and fIThiSte <=32:
                        sOThiSte = "Pass"
                    else:
                        sOThiSte = "Fail"
                elif sISym == "B":
                    if fIThiSte >=8 and fIThiSte <=40:
                        sOThiSte = "Pass"
                    else:
                        sOThiSte = "Fail"
                elif sISym == "C":
                    if fIThiSte >=8 and fIThiSte <=100:
                        sOThiSte = "Pass"
                    else:
                        sOThiSte = "Fail"
                else:
                    return "A, B, C 중에서 선택해주세요"
            elif sITyp == "SM490":
                if sISym == "A":
                    if fIThiSte >=8 and fIThiSte <=25:
                        sOThiSte = "Pass"
                    else:
                        sOThiSte = "Fail"
                elif sISym == "B":
                    if fIThiSte >=8 and fIThiSte < 40:
                        sOThiSte = "Pass"
                    else:
                        sOThiSte = "Fail"
                elif sISym == "C" or sISym == "C-TMC":
                    if fIThiSte >=8 and fIThiSte <=100:
                        sOThiSte = "Pass"
                    else:
                        sOThiSte = "Fail"
                else:
                    return "A, B, C, C-TMC 중에서 선택해주세요"
            elif sITyp == "SM490Y":
                if sISym == "A":
                    if fIThiSte >=8 and fIThiSte <=16:
                        sOThiSte = "Pass"
                    else:
                        sOThiSte = "Fail"
                elif sISym == "B":
                    if fIThiSte >=8 and fIThiSte <=40:
                        sOThiSte = "Pass"
                    else:
                        sOThiSte = "Fail"
                else:
                    return "A, B 중에서 선택해주세요"
            elif sITyp == "SM520":
                if sISym == "B":
                    if fIThiSte >=8 and fIThiSte <=40:
                        sOThiSte = "Pass"
                    else:
                        sOThiSte = "Fail"
                elif sISym == "C" or sISym == "C-TMC":
                    if fIThiSte >=8 and fIThiSte <=100:
                        sOThiSte = "Pass"
                    else:
                        sOThiSte = "Fail"
                else:
                    return "B, C, C-TMC 중에서 선택해주세요"
            elif sITyp == "SM570":
                if fIThiSte >=8 and fIThiSte <=100:
                    sOThiSte = "Pass"
                else:
                    sOThiSte = "Fail"
            else:
                return "SM400, SM490, SM490Y, SM520, SM570 중에서 선택해주세요"
        else:
            return "KCS 24 30 00 2.2.1 (1), (3), (4)를 확인해주세요"
        return sOThiSte