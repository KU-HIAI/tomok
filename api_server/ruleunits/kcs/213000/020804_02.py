import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS213000_020804_02(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 30 00 2.8.4 (2)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-25'
    title = 'LW(Labiles Wasser Glass) 공법 주입재'

    description = """
    가설흙막이 공사
    2. 자재
    2.8 지반 그라우팅
    2.8.4 일반사항
    (2)
    """

    content = """
    #### 2.8.4. 일반사항
    (2) LW(Labiles Wasser glass) 공법 주입재
    ② 규산소다(물유리)는 비중이 1.38 이상인 3호를 사용하여야 한다.
    ⑤ 주입재의 배합은 표 2.8-3 을 표준으로 하되 배합 시 겔타임은 통상 60~120초가 확보되어야 하며, 현장에서 시험시공 후 재조정할 수 있다.
    표 2.8-3 주입재의 배합기준(m3당)
    \begin{table}[]
    \begin{tabular}{llllllll}
    \multicolumn{3}{l}{실(seal)재(m3당)}                                                                                                                                                                              & \multicolumn{5}{l}{LW(0.5m3당)}                                                                                                                                                                                                                                     \\
    \multirow{2}{*}{\begin{tabular}[c]{@{}l@{}}시멘트\\ (kg)\end{tabular}} & \multirow{2}{*}{\begin{tabular}[c]{@{}l@{}}벤토나이트\\ (kg)\end{tabular}} & \multirow{2}{*}{\begin{tabular}[c]{@{}l@{}}물\\ (ℓ)\end{tabular}} & \multicolumn{2}{l}{A액}                                                                               & \multicolumn{3}{l}{B액}                                                                                                                                      \\
                                                                        &                                                                       &                                                                  & \begin{tabular}[c]{@{}l@{}}규산소다\\ (ℓ)\end{tabular} & \begin{tabular}[c]{@{}l@{}}물\\ (ℓ)\end{tabular} & \begin{tabular}[c]{@{}l@{}}시멘트\\ (kg)\end{tabular} & \begin{tabular}[c]{@{}l@{}}벤토나이트\\ (kg)\end{tabular} & \begin{tabular}[c]{@{}l@{}}물\\ (ℓ)\end{tabular} \\
    200                                                                 & 62.5                                                                  & 910                                                              & 315                                                & 185                                             & 250                                                & 22                                                   & 428
    \end{tabular}
    \end{table
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: LW(Labiles Wasser Glass) 공법 주입재"];
    B["KCS 21 30 00 2.8.4 (2)"];
    B ~~~ A
    end

    KCS(["KCS 21 30 00 2.8.4 (2)"])

    subgraph Variable_def
    VarOut1[/출력변수: 규산소다의 비중/]; VarOut2[/출력변수: 시멘트/];
    VarOut3[/출력변수: 벤토나이트/]; VarOut4[/출력변수: 물/];
    VarOut5[/출력변수: 규산소다/]; VarOut6[/출력변수: 겔타임/];
    VarIn1[/입력변수: 규산소다의 비중/]; VarIn2[/입력변수: 주입재의 종류/];
    end
    VarOut1 & VarOut2 & VarOut3 & VarOut4 ~~~ VarOut5

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"규산소다의 비중 >= 1.38"}
    Variable_def --> C2{"60초 <= 겔타임 <= 120초"}
    C1 & C2 --> |YES|C3{"Seal재의 배합기준<1m^3>"}
    C1 & C2 --> |YES|C4{"LW 배합기준<0.5m^3>"}
    C3 --> D1["시멘트 = 200kg"]
    C3 --> D2["벤토나이트 = 62.5kg"]
    C3 --> D3["물 = 910l"]
    C4 --> |A액|E1["규산소다 = 315l"]
    C4 --> |B액|E2["물 = 185l"]
    C4 --> |B액|E3["시멘트 = 250kg"]
    C4 --> |B액|E4["벤토나이트 = 22kg"]
    C4 --> |B액|E5["anf = 428l"]


    D1 & D2 & D3 & D4 & E1 & E2 & E3 & E4 & E5 --> |YES|F1(["Pass"]);
    C1 & C2 & D1 & D2 & D3 & D4 & E1 & E2 & E3 & E4 & E5 --> |No|F2(["Fail"]);
    """

    @rule_method
    def Specific_Gravity_of_Sodium_Silicate(fIGraSod, sITypInj) -> str:
        """ LW(Labiles Wasser Glass) 공법 주입재
        Args:
            fIGraSod (float): 규산소다의 비중
            sITypInj (str): 주입재의 종류

        Returns:
            pass_fail (bool): 가설흙막이 공사 2.8.4 일반사항 (2) ②의 판단 결과
            fOCem (float): 시멘트
            fOBen (float): 벤토나이트
            fOWat (float): 물
            fOSod (float): 규산소다
            sOGel (str): 겔타임
        """
        assert isinstance(fIGraSod, float)
        assert isinstance(sITypInj, str)
        assert sITypInj in["Seal", "LW-A", "LW-B"]

        if fIGraSod >= 1.38:
            pass_fail = True
        else:
            pass_fail = False

        if sITypInj == "Seal":
          fOCem = 200; fOBen = 62.5; fOWat = 910; fOSod = None; sOGel = "60~120초 확보"
        elif sITypInj == "LW-A":
          fOCem = None; fOBen = None; fOWat = 185; fOSod = 315; sOGel = "60~120초 확보"
        elif sITypInj == "LW-B":
          fOCem = 250; fOBen = 22; fOWat = 428; fOSod = None; sOGel = "60~120초 확보"

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail,
                    "fOCem": fOCem,
                    "fOBen": fOBen,
                    "fOWat": fOWat,
                    "fOSod": fOSod,
                    "sOGel": sOGel,
                }
            )