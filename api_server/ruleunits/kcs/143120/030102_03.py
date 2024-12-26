import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_030102_03(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 3.1.2 (3)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-10'
    title = '비드 길이 및 간격'

    description = """
    용접
    3. 시공
    3.1 용접시공에 관한 일반사항
    3.1.2 조립 가용접(가용접, 임시용접과 가용접)
    """

    content = """
    #### 3.1.2 조립 가용접(가용접, 임시용접과 가용접)
    (3) 조립을 위한 가용접 개소는 최소화해야 하며 비드 길이, 간격은 표 3.1-1을 표준으로 한다.
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
    A[Title: 비드 길이 및 간격];
    B["KCS 14 31 20 3.1.2 (3)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 3.1.2 (3)"])

    subgraph Variable_def
    VarOut1[/출력변수: 비드 길이 및 간격/];
    VarIn1[/입력변수: 비드 길이/];
    VarIn2[/입력변수: 인장 강도/];
    VarIn3[/입력변수: 피치/];
    VarIn4[/입력변수: 판두께/];
    VarIn5[/입력변수: 수동, 반자동용접/];
    VarIn6[/입력변수: 자동용접/];
		VarOut1 & VarIn1 & VarIn2 & VarIn3 ~~~ VarIn4
    end


    Python_Class ~~~ KCS
    KCS --> Variable_def
		Variable_def --> C{비드 길이 \n 인장강도 \n 피치 \n 판두께 \n 수동, 반자동용접 \n 자동용접 \n.}
		C --> |표 3.1-1|D[비드 길이 및 간격]
		D --> End([비드 길이 및 간격])
    """

    @rule_method
    def Lenght_of_Bead(bILenBra, bIPit, fITenStr, fIThiPla, bIManWel, bIAutWel) -> RuleUnitResult:
        """ 비드 길이 및 간격
        Args:
        bILenBra (bool): 비드 길이
        bIPit (bool): 피치
        fITenStr (float): 인장 강도
        fIThiPla (float): 판두께
        bIManWel (bool): 수동, 반자동용접
        bIAutWel (bool): 자동용접

        Returns:
        sOLenSpa (str): 비드 길이 및 간격
        """
        assert isinstance(bILenBra, bool)
        assert isinstance(bIPit, bool)
        assert bILenBra != bIPit
        assert isinstance(fITenStr, float)
        assert isinstance(fIThiPla, float)
        assert isinstance(bIManWel, bool)
        assert isinstance(bIAutWel, bool)
        assert bIManWel != bIAutWel

        sOLenSpa = None
        if fITenStr < 500:
          if fIThiPla <= 25:
            if bILenBra == True:
              if bIManWel == True:
                sOLenSpa = "40mm 이상"
              elif bIAutWel == True:
                sOLenSpa = "50m 이상"
            elif bIPit == True:
              sOLenSpa = "300 ~ 400mm"

          elif 25 < fIThiPla <= 50:
            if bILenBra == True:
              if bIManWel == True:
                sOLenSpa = "50mm 이상"
              elif bIAutWel == True:
                sOLenSpa = "70m 이상"
            elif bIPit == True:
              sOLenSpa = "300 ~ 400mm"
        else:
          if bILenBra == True:
            if bIManWel == True:
              sOLenSpa = "50mm 이상"
            elif bIAutWel == True:
              sOLenSpa = "70m 이상"
          elif bIPit == True:
            sOLenSpa = "300 ~ 400mm"

        return RuleUnitResult(
                result_variables = {
                    "sOLenSpa": sOLenSpa
                }
            )