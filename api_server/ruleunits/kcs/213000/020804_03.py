import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS213000_020804_03(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 30 00 2.8.4 (3)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-25'
    title = 'SGR(Space Grouting Rocket)공법 주입재'

    description = """
    가설흙막이 공사
    2. 자재
    2.8. 지반 그라우팅
    2.8.4. 일반사항
    (3)
    """

    content = """
    #### 2.8.4. 일반사항
    (3) SGR(Space Grouting Rocket)공법 주입재
    ③ 주입재의 배합은 표 2.8-5를 표준으로 하며, 현장에서 시험시공 후 재조정할 수 있다.
    표 2.8-5 주입재의 배합기준
    \begin{table}[]
    \begin{tabular}{llllllll}
    \multicolumn{2}{l}{\multirow{2}{*}{A액(200ℓ당)}}                                                       & \multicolumn{6}{l}{B액(200ℓ당)}                                                                                                                                                                                                                                                                                                    \\
    \multicolumn{2}{l}{}                                                                                 & \multicolumn{3}{l}{B1액(급결형)}                                                                                                                                   & \multicolumn{3}{l}{B2액(완결형)}                                                                                                                                    \\
    \begin{tabular}[c]{@{}l@{}}규산소다\\ (ℓ)\end{tabular} & \begin{tabular}[c]{@{}l@{}}물\\ (ℓ)\end{tabular} & \begin{tabular}[c]{@{}l@{}}SGR-7,9호\\ (kg)\end{tabular} & \begin{tabular}[c]{@{}l@{}}시멘트\\ (kg)\end{tabular} & \begin{tabular}[c]{@{}l@{}}물\\ (ℓ)\end{tabular} & \begin{tabular}[c]{@{}l@{}}SGR-8,10호\\ (kg)\end{tabular} & \begin{tabular}[c]{@{}l@{}}시멘트\\ (kg)\end{tabular} & \begin{tabular}[c]{@{}l@{}}물\\ (ℓ)\end{tabular} \\
    100                                                & 100                                             & 24                                                      & 60                                                 & 168                                             & 23                                                       & 60                                                 & 169
    \end{tabular}
    \end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: SGR(Space Grouting Rocket) 공법 주입재 배합기준"];
    B["KCS 21 30 00 2.8.4 (3)"];
    B ~~~ A
    end

    KCS(["KCS 21 30 00 2.8.4 (3)"])

    subgraph Variable_def
    VarOut1[/출력변수: 규산소다/]; VarOut2[/출력변수: 물/];
    VarOut3[/출력변수: 시멘트/]; VarOut4[/출력변수: SGR-7, 9호/];
    VarOut5[/출력변수: SGR-8, 10호/]
    VarIn1[/입력변수: 주입재의 종류/];
    end
    VarOut1 & VarOut2 & VarOut3 ~~~ VarOut4

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"주입재의 종류"}
    C1 --> |A액|C2{"A액 배합기준 <200l 당>"}
    C1 --> |B1액|C3{"B1 배합기준 <200l 당>"}
    C1 --> |B2액|C4{"B2 배합기준 <200l 당>"}
    C2 --> E1["규산소다 = 100l"]
    C2 --> E2["물 = 100l"]
    C3 --> E3["SGR-7, 9호 = 24kg"]
    C3 --> E4["물 = 168l"]
    C3 --> E5["시멘트 = 60kg"]
    C4 --> E5
    C4 --> E6["SGR-8, 10호 = 23kg"]
    C4 --> E8["물 = 169l"]



    E1 & E2 & E3 & E4 & E5 & E6 & E7 & E8 --> |YES|F1(["Pass"]);
    E1 & E2 & E3 & E4 & E5 & E6 & E7 & E8 --> |No|F2(["Fail"]);
    """

    @rule_method
    def Type_of_Injection_Material(sITypInj) -> float:
        """ SGR(Space Grouting Rocket)공법 주입재
        Args:
            sITypInj (str): 주입재의 종류

        Returns:
            fOSod (float): 규산소다
            fOWat (float): 물
            fOSGRSev (float): SGR 7, 9호
            fOSGREig (float): SGR 8, 10호
            fOCem (float): 시멘트
        """
        assert isinstance(sITypInj, str)
        assert sITypInj in["A", "B1", "B2"]

        if sITypInj == "A":
          fOSod = 100; fOWat = 100; fOSGRSev = None; fOSGREig = None; fOCem = None
        elif sITypInj == "B1":
          fOSod= None; fOWat = 168; fOSGRSev = 24; fOSGREig = None; fOCem = 60
        elif sITypInj == "B2":
          fOSod= None; fOWat = 169; fOSGREig = 23; fOSGREig = None; fOCem = 60

        return RuleUnitResult(
                result_variables = {
                    "fOSod": fOSod,
                    "fOWat": fOWat,
                    "fOSGRSev": fOSGRSev,
                    "fOSGREig": fOSGREig,
                    "fOCem": fOCem,
                }
            )