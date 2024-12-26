import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_030102_12(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 3.1.2 (12)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-10'
    title = '가용접의 길이'

    description = """
    용접
    3. 시공
    3.1 용접시공에 관한 일반사항
    3.1.2 조립 가용접(가용접, 임시용접과 가용접)
    """

    content = """
    #### 3.1.2 조립 가용접(가용접, 임시용접과 가용접)
    (12) 가용접 길이는 표 3.1-1에서와 같이 40 mm 이상으로 하고, 본용접과 동일한 방법을 적용하여 본용접 개소에 시공해야 한다. 다만 가용접의 다리길이는 4 mm 이상으로 하고 그 간격은 400 mm 이하로 한다.
    표 3.1-1 비드 길이 및 간격
\begin{table}[]
\begin{tabular}{
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l }
\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
  \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
  \multicolumn{2}{l}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 비드 길이}} &
  \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } \\
\multirow{-2}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}판두께 t1)\\ (mm)\end{tabular}}} &
  \multirow{-2}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}인장강도\\ (MPa)\end{tabular}}} &
  {\color[HTML]{333333} 수동, 반자동용접} &
  {\color[HTML]{333333} 자동용접} &
  \multirow{-2}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}피치\\ (mm)\end{tabular}}} \\
{\color[HTML]{333333} t  ≤ 25} &
  {\color[HTML]{333333} 500 미만} &
  {\color[HTML]{333333} 40 mm 이상} &
  {\color[HTML]{333333} 50 mm 이상} &
  \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } \\
{\color[HTML]{333333} 25 〈 t ≤ 50} &
  {\color[HTML]{333333} 500 미만} &
  \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
  \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
  \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } \\
{\color[HTML]{333333} 모든 두께} &
  {\color[HTML]{333333} 500 이상} &
  \multirow{-2}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 50 mm 이상}} &
  \multirow{-2}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 70 mm 이상}} &
  \multirow{-3}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}300\\ $\sim$400\end{tabular}}} \\
\multicolumn{5}{l}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 주 1) 판두께 t는 두꺼운 쪽의 판두께임.}}
\end{tabular}
\end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 가용접의 길이]
    B["KCS 14 31 20 3.1.2 (12)"]
    B ~~~ A
    end

    KCS(["KCS 14 31 20 3.1.2 (12)"])

    subgraph Variable_def
    VarOut1[/출력변수: 가용접의 길이/]
    VarIn1[/입력변수: 인장 강도/]
    VarIn2[/입력변수: 판두께/]
    VarIn3[/입력변수: 수동, 반자동용접/]
    VarIn4[/입력변수: 자동용접/]
    VarIn5[/입력변수: 가용접 다리길이/]
    VarIn6[/입력변수: 가용접의 간격/]
		VarOut1 & VarIn1 & VarIn2 & VarIn3 ~~~ VarIn4
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
		Variable_def --> C{"가용접 다리길이 ≥ 4 mm \n 가용접의 간격 ≤ 400 mm \n"}
		C --> |표 3.1-1|D[가용접의 길이]
		D --> E([가용접의 길이])
    """

    @rule_method
    def Lenght_of_Tack_Welding(fITenStr, fIThiPla, bIManWel, bIAutWel, fILegLen, fISpaTac) -> RuleUnitResult:
        """ 가용접의 길이
        Args:
        fITenStr (float): 인장 강도
        fIThiPla (float): 판두께
        bIManWel (bool): 수동, 반자동용접
        bIAutWel (bool): 자동용접
        fILegLen (float): 가용접 다리길이
        fISpaTac (float): 가용접의 간격

        Returns:
        sOLenTac (str): 가용접 길이
        """
        assert isinstance(fITenStr, float)
        assert isinstance(fIThiPla, float)
        assert isinstance(bIManWel, bool)
        assert isinstance(bIAutWel, bool)
        assert (bIManWel + bIAutWel) == 1
        assert isinstance(fILegLen, float)
        assert isinstance(fISpaTac, float)

        if fILegLen >= 4 and fISpaTac <= 400:
          if fITenStr < 500:
            if fIThiPla <= 25:
              if bIManWel == True:
                sOLenTac = "40mm 이상"
              elif bIAutWel == True:
                sOLenTac = "50m 이상"

            elif 25 < fIThiPla <= 50:
              if bIManWel == True:
                sOLenTac = "50mm 이상"
              elif bIAutWel == True:
                sOLenTac = "70m 이상"
            else:
              sOLenTac = None
          else:
            if bIManWel == True:
              sOLenTac = "50mm 이상"
            elif bIAutWel == True:
              sOLenTac = "70m 이상"
        else:
          sOLenTac = None

        return RuleUnitResult(
                result_variables = {
                    "sOLenTac": sOLenTac
                }
            )