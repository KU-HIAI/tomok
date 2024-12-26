import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_031005_02(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 3.10.5 (2)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-13'
    title = '필릿용접의 최소치수'

    description = """
    용접
    3. 시공
    3.10 스터드의 용접
    3.10.5 스터드필릿용접
    """

    content = """
    #### 3.10.5 스터드필릿용접
    (2) 필릿용접의 최소치수는 표 3.10-1에 준한다.
    표 3.10-1 필릿용접의 최소치수(단위:mm)
    \begin{table}[]
\begin{tabular}{
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l }
{\color[HTML]{333333} 스터드 지름}                    & {\color[HTML]{333333} 최소치수} \\
{\color[HTML]{333333} \# ≤ 10 mm}                & {\color[HTML]{333333} 6}    \\
{\color[HTML]{333333} 10mm \textless \# ≤ 25 mm} & {\color[HTML]{333333} 8}    \\
{\color[HTML]{333333} \# \textgreater 25 mm}     & {\color[HTML]{333333} 10}
\end{tabular}
\end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: 필릿용접의 최소치수"];
    B["KCS 14 31 20 3.10.5 (2)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 3.10.5 (2)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 필릿용접의 최소치수"/];
    VarIn1[/입력변수: 스터드 지름/];
		VarOut1 ~~~ VarIn1
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"스터드 지름"}
    C --> |"≤ 10 mm"|D[6 mm]
    C --> |"10mm <스터드 지름≤ 25 mm"|E[8 mm]
    C --> |">25 mm "|F[10 mm]
		D & E & F  --> End([필릿용접의 최소치수])
    """

    @rule_method
    def Diameter_Of_Stud(fIDiaStu) -> RuleUnitResult:
        """ 필릿용접의 최소치수
        Args:
        fIDiaStu (float): 스터드 지름

        Returns:
        fOMinFil (float): 필릿용접의 최소치수
        """
        assert isinstance(fIDiaStu, float)

        if fIDiaStu <= 10:
          fOMinFil = 6
        elif 10 < fIDiaStu <= 25:
          fOMinFil = 8
        elif fIDiaStu > 25:
          fOMinFil = 10

        return RuleUnitResult(
                result_variables = {
                    "fOMinFil": fOMinFil
                }
            )