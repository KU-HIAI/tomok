import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS243000_020201_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 30 00 2.2.1 (2)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-08'
    title = '용접구조용 압연강재 강판의 두께'

    description = """
    강교량공사
    2. 자재
    2.2 사용재료
    2.2.1 강판
    (2)
    """
    content = """
    #### 2.2.1 강판
    (2) 용접구조용 압연강재: KS D 3515
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

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 용접구조용 압연강재 강판의 두께];
    B["KCS 24 30 00 2.2.1 (2)"];
    B ~~~ A
    end

    KCS(["KCS 24 30 00 2.2.1 (2)"])

    subgraph Variable_def
    VarIn1[/입력변수: 용접구조용 압연강재/];
    VarIn2[/입력변수: 강판의 두께/];
    VarIn3[/입력변수: 종류/];
    VarIn4[/입력변수: 기호/];
    VarIn1 & VarIn2 ~~~ VarIn3 & VarIn4
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"용접구조용 압연강재"}
    C --> |True|D{용접구조용 압연강재\n 강판의 두께 \n 종류 \n 기호\n.}
    D --> End([Pass or Fail])
    """

    @rule_method

    def thickness_steel_plate(bIRolWel, fIThiSte,sITyp,sISym) -> RuleUnitResult:
        """
        Args:
            bIRolWel (bool): 용접구조용 압연강재
            fIThiSte (float): 강판의 두께
            sITyp (str): 종류
            sISym (str): 기호

        Returns:
            pass_fail (bool): 강교량공사 2.2.1 강판 (2)의 판단 결과
        """
        assert isinstance(bIRolWel, bool)
        assert isinstance(fIThiSte, float)
        assert isinstance(sITyp, str)
        assert sITyp in ["SM400","SM490","SM490Y","SM520","SM570"]
        assert isinstance(sISym, str)
        if sITyp == "SM400":
            assert sISym in ["A","B","C"]
        if sITyp == "SM490":
            assert sISym in ["A","B","C","C-TMC"]
        if sITyp == "SM490Y":
            assert sISym in ["A","B"]
        if sITyp == "SM520":
            assert sISym in ["B","C","C-TMC"]
        if sITyp == "SM570":
            assert sISym == "TMC"
        assert bIRolWel == True

        if bIRolWel:
            if sITyp == "SM400":
                if sISym == "A":
                    if fIThiSte >=8 and fIThiSte <=32:
                        pass_fail = True
                    else:
                        pass_fail = False
                elif sISym == "B":
                    if fIThiSte >=8 and fIThiSte <=40:
                        pass_fail = True
                    else:
                        pass_fail = False
                elif sISym == "C":
                    if fIThiSte >=8 and fIThiSte <=100:
                        pass_fail = True
                    else:
                        pass_fail = False
            elif sITyp == "SM490":
                if sISym == "A":
                    if fIThiSte >=8 and fIThiSte <=25:
                        pass_fail = True
                    else:
                        pass_fail = False
                elif sISym == "B":
                    if fIThiSte >=8 and fIThiSte < 40:
                        pass_fail = True
                    else:
                        pass_fail = False
                elif sISym == "C" or sISym == "C-TMC":
                    if fIThiSte >=8 and fIThiSte <=100:
                        pass_fail = True
                    else:
                        pass_fail = False
            elif sITyp == "SM490Y":
                if sISym == "A":
                    if fIThiSte >=8 and fIThiSte <=16:
                        pass_fail = True
                    else:
                        pass_fail = False
                elif sISym == "B":
                    if fIThiSte >=8 and fIThiSte <=40:
                        pass_fail = True
                    else:
                        pass_fail = False
            elif sITyp == "SM520":
                if sISym == "B":
                    if fIThiSte >=8 and fIThiSte <=40:
                        pass_fail = True
                    else:
                        pass_fail = False
                elif sISym == "C" or sISym == "C-TMC":
                    if fIThiSte >=8 and fIThiSte <=100:
                        pass_fail = True
                    else:
                        pass_fail = False
            elif sITyp == "SM570":
                if fIThiSte >=8 and fIThiSte <=100:
                    pass_fail = True
                else:
                    pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })