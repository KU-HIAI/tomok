import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS243000_020201_04(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 30 00 2.2.1 (4)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-08'
    title = '교량구조용 압연강재 강판의 두께'

    description = """
    강교량공사
    2. 자재
    2.2 사용재료
    2.2.1 강판
    (4)
    """
    content = """
    #### 2.2.1 강판
    (4) 교량구조용 압연강재: KS D 3868
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

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 교량구조용 압연강재 강판의 두께];
    B["KCS 24 30 00 2.2.1 (4)"];
    B ~~~ A
    end

    KCS(["KCS 24 30 00 2.2.1 (4)"])

    subgraph Variable_def
    VarIn1[/입력변수: 교량구조용 압연강재/];
    VarIn2[/입력변수: 강판의 두께/];
    VarIn3[/입력변수: 종류/];
    VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"교량구조용 압연강재"}
    C --> |True|D{"종류"}
    D --> End([Pass or Fail])
    """

    @rule_method

    def thickness_steel_plate(bIRolBri, fIThiSte,sITyp) -> RuleUnitResult:
        """
        Args:
            bIRolBri (bool): 교량구조용 압연강재
            fIThiSte (float): 강판의 두께
            sITyp (str): 종류

        Returns:
            pass_fail (bool): 강교량공사 2.2.1 강판 (4)의 판단 결과
        """
        assert isinstance(bIRolBri, bool)
        assert isinstance(fIThiSte, float)
        assert isinstance(sITyp, str)
        assert sITyp in ["HSB500","HSB600","HSB800"]
        assert bIRolBri == True

        if bIRolBri:
            if sITyp =="HSB500" or sITyp =="HSB600":
                if fIThiSte >=8 and fIThiSte <=100:
                    pass_fail = True
                else:
                    pass_fail = False
            elif sITyp =="HSB800":
                if fIThiSte >=8 and fIThiSte <=80:
                    pass_fail = True
                else:
                    pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })