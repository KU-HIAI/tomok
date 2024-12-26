import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_031103_01(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 3.11.3 (1)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-14'
    title = '비파괴시험의 최소 지체시간'

    description = """
    용접
    3. 시공
    3.11 용접검사
    3.11.3 비파괴시험
    """

    content = """
    #### 3.11.3 비파괴시험
    (1) 비파괴시험은 육안검사에 합격한 용접부에 실시한다. 일반적으로 용접 후 표 3.11-4에 명시된 최소 지체시간이 경과한 이후에 실시한다.
    표 3.11-4 비파괴시험의 용접 후 최소 지체시간
    \begin{table}[]
\begin{tabular}{llll}
\multirow{3}{*}{\begin{tabular}[c]{@{}l@{}}용접 목두께\\ (mm)\end{tabular}} & \multirow{3}{*}{\begin{tabular}[c]{@{}l@{}}용접 입열량\\ (J/mm)\end{tabular}} & \multicolumn{2}{l}{지체시간 (시간, h)1)} \\
 &  & \multicolumn{2}{l}{인장강도 (MPa)} \\
 &  & 420 이하 & 420 초과 \\
a ≤ 6 & 모든 경우 & 냉각시간 & 24 \\
\multirow{2}{*}{6 < a ≤ 12} & 3000 이하 & 8 & 24 \\
 & 3000 초과 & 16 & 40 \\
\multirow{2}{*}{12 ≤ a} & 3000 이하 & 16 & 40 \\
 & 3000 초과 & 40 & 48 \\
\multicolumn{4}{l}{주 1) 여기서 지체시간은 용접완료 후부터 비파괴시험 시작 때까지의 시간을 뜻함}
\end{tabular}
\end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: 비파괴시험의 최소 지체시간"];
    B["KCS 14 31 20 3.11.3 (1)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 3.11.3 (1)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 최소 지체시간"/];
    VarIn1[/입력변수: 육안검사에 합격/];
    VarIn2[/입력변수: 용접 목두께/];
    VarIn3[/입력변수: 용접 입열량/];
    VarIn4[/입력변수: 인장강도/];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"육안검사에 합격"}
		C --> |True|D{용접 목두께\n용접 입열량\n인장강도}
    D --> |표 3.11-4|E[최소 지체시간]
		E --> End([비파괴시험의 최소 지체시간])
    """

    @rule_method
    def Passed_Visual_Inspection(bIPasVis, fIWelThr, fIWelHea, fITenStr) -> RuleUnitResult:
        """ 비파괴시험의 최소 지체시간
        Args:
        bIPasVis (bool): 육안검사에 합격
        fIWelThr (float): 용접 목두께
        fIWelHea (float): 용접 입열량
        fITenStr (float): 인장강도

        Returns:
        sOMinDel (str): 최소 지체시간
        """
        assert isinstance(bIPasVis, bool)
        assert isinstance(fIWelThr, float)
        assert isinstance(fIWelHea, float)
        assert isinstance(fITenStr, float)

        if bIPasVis == True:
          if fIWelThr <= 6:
            if fITenStr <= 420:
              sOMinDel = "냉각시간"
            else:
              sOMinDel = "24시간"

          elif 6 < fIWelThr <= 12:
            if fIWelHea <= 3000:
              if fITenStr <= 420:
                sOMinDel = "8시간"
              else:
                sOMinDel = "24시간"
            else:
              if fITenStr <= 420:
                sOMinDel = "16시간"
              else:
                sOMinDel = "40시간"

          else:
            if fIWelHea <= 3000:
              if fITenStr <= 420:
                sOMinDel = "16시간"
              else:
                sOMinDel = "40시간"
            else:
              if fITenStr <= 420:
                sOMinDel = "40시간"
              else:
                sOMinDel = "48시간"
        else:
          sOMinDel = None

        return RuleUnitResult(
                result_variables = {
                    "sOMinDel": sOMinDel
                }
            )