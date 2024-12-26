import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143140_031502_07(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 40 3.15.2 (7)'
    ref_date = '2019-05-20'
    doc_date = '2023-10-31'
    title = '도막 두께의 허용오차'

    description = """
    도장
    3. 시공
    3.15 도막외관 및 도막두께
    3.15.2 도막두께
    (7)
    """

    content = """
    #### 3.15.2 도막두께
    (7) 도막두께의 관리기준은 표 3.15-1에 따른다.
    표 3.15-1 도막 두께의 허용 오차
    \begin{table}[]
    \begin{tabular}{
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l }
    \multicolumn{2}{l}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}기준 도막 두께\\ {[}μm(mils){]}\end{tabular}}} &
      \multicolumn{2}{l}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}최소(Spot)\\ {[}μm(mils){]}\end{tabular}}} &
      \multicolumn{2}{l}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}최대(평균)\\ {[}μm(mils){]}\end{tabular}}} &
      \multicolumn{2}{l}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}최대(Spot)\\ {[}μm(mils){]}\end{tabular}}} \\
    {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}25 \\ 50 \\ 75 \\ 100 \\ 125 \\ 150 \\ 175 \\ 200 \\ 250 \\ 275 \\ 500 \\ 625\end{tabular}} &
      {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}(1.0)\\ (2.0)\\ (3.0)\\ (4.0)\\ (5.0)\\ (6.0)\\ (7.0)\\ (8.0)\\ (10.0)\\ (15.0)\\ (20.0)\\ (25.0)\end{tabular}} &
      {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}20 \\ 40 \\ 60\\ 80 \\ 100 \\ 120 \\ 140 \\ 160 \\ 200 \\ 300 \\ 400 \\ 500\end{tabular}} &
      {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}(0.8)\\ (1.6)\\ (2.4)\\ (3.2)\\ (4.0)\\ (4.8)\\ (5.6)\\ (6.4)\\ (8.0)\\ (12.0)\\ (16.0)\\ (20.0)\end{tabular}} &
      {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}50 \\ 100 \\ 150 \\ 175 \\ 200 \\ 225 \\ 250 \\ 275 \\ 325 \\ 500 \\ 650 \\ 800\end{tabular}} &
      {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}(2.0)\\ (4.0)\\ (6.0)\\ (7.0)\\ (8.0)\\ (9.0)\\ (10.0)\\ (11.0)\\ (13.0)\\ (20.0)\\ (26.0)\\ (32.0)\end{tabular}} &
      {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}75 \\ 125 \\ 175 \\ 213 \\ 238 \\ 263 \\ 288 \\ 313 \\ 363 \\ 575 \\ 725 \\ 900\end{tabular}} &
      {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}(3.0)\\ (5.0)\\ (7.0)\\ (8.5)\\ (9.5)\\ (10.5)\\ (11.5)\\ (12.5)\\ (14.5)\\ (23.0)\\ (29.0)\\ (36.0)\end{tabular}}
    \end{tabular}
    \end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 도막 두께의 허용오차];
    B["KCS 14 31 40 3.15.2 (7)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 40 3.15.2 (7)"])

    subgraph Variable_def
    VarOut[/출력변수: 도막 두께의 허용오차/];
    VarIn1[/입력변수: 단위/];
    VarIn2[/"입력변수: 최소(Spot)"/];
    VarIn3[/"입력변수: 최대(평균)"/];
    VarIn4[/"입력변수: 최대(Spot)"/];
    VarIn5[/입력변수: 기준 도막 두께/];
    VarIn6[/입력변수: 기준 도막 두께/];
		VarOut ~~~ VarIn1 & VarIn2 & VarIn3
		VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
		Variable_def --> C{"단위, 기준 도막 두께 \n 최소(Spot), 최대(평균) \n 최대(Spot) \n."}
		C --> |표 3.15-1|D["도막 두께의 허용오차"]
		D --> End([도막 두께의 허용오차])
    """

    @rule_method
    def Minimum_Spot(sIUni, bIMinSpo, bIMaxAve, bIMaxSpo, fISkiThi_1, fISkiThi_2) -> float:
        """ 도막 두께의 허용오차
        Args:
        sIUni (str): 단위
        bIMinSpo (bool): 최소(Spot)
        bIMaxAve (bool): 최대(평균)
        bIMaxSpo (bool): 최대(Spot)
        fISkiThi_1 (float): 기준 도막 두께
        fISkiThi_2 (float): 기준 도막 두께

        Returns:
        fOTolThi (float): 도막 두께의 허용오차
        """
        assert isinstance(sIUni, str)
        assert sIUni in["μm", "mils"]
        assert isinstance(bIMinSpo, bool)
        assert isinstance(bIMaxAve, bool)
        assert isinstance(bIMaxSpo, bool)
        assert (bIMinSpo + bIMaxAve + bIMaxSpo) == 1
        assert isinstance(fISkiThi_1, float)
        assert fISkiThi_1 in[25, 50, 75, 100, 125, 150, 175, 200, 250, 275, 500, 625]
        assert isinstance(fISkiThi_2, float)
        assert fISkiThi_2 in[1, 2, 3, 4, 5, 6, 7, 8, 10, 15, 20, 25]

        if sIUni == "μm":
          if fISkiThi_1 == 25:
            if bIMinSpo == True and bIMaxAve == False and bIMaxSpo == False:
              fOTolThi = 20
            elif bIMinSpo == False and bIMaxAve == True and bIMaxSpo == False:
              fOTolThi = 50
            elif bIMinSpo == False and bIMaxAve == False and bIMaxSpo == True:
              fOTolThi = 75

          if fISkiThi_1 == 50:
            if bIMinSpo == True and bIMaxAve == False and bIMaxSpo == False:
              fOTolThi = 40
            elif bIMinSpo == False and bIMaxAve == True and bIMaxSpo == False:
              fOTolThi = 100
            elif bIMinSpo == False and bIMaxAve == False and bIMaxSpo == True:
              fOTolThi = 125

          if fISkiThi_1 == 75:
            if bIMinSpo == True and bIMaxAve == False and bIMaxSpo == False:
              fOTolThi = 60
            elif bIMinSpo == False and bIMaxAve == True and bIMaxSpo == False:
              fOTolThi = 150
            elif bIMinSpo == False and bIMaxAve == False and bIMaxSpo == True:
              fOTolThi = 175

          if fISkiThi_1 == 100:
            if bIMinSpo == True and bIMaxAve == False and bIMaxSpo == False:
              fOTolThi = 80
            elif bIMinSpo == False and bIMaxAve == True and bIMaxSpo == False:
              fOTolThi = 175
            elif bIMinSpo == False and bIMaxAve == False and bIMaxSpo == True:
              fOTolThi = 213

          if fISkiThi_1 == 125:
            if bIMinSpo == True and bIMaxAve == False and bIMaxSpo == False:
              fOTolThi = 100
            elif bIMinSpo == False and bIMaxAve == True and bIMaxSpo == False:
              fOTolThi = 200
            elif bIMinSpo == False and bIMaxAve == False and bIMaxSpo == True:
              fOTolThi = 238

          if fISkiThi_1 == 150:
           if bIMinSpo == True and bIMaxAve == False and bIMaxSpo == False:
            fOTolThi = 120
           elif bIMinSpo == False and bIMaxAve == True and bIMaxSpo == False:
            fOTolThi = 225
           elif bIMinSpo == False and bIMaxAve == False and bIMaxSpo == True:
            fOTolThi = 263

          if fISkiThi_1 == 175:
            if bIMinSpo == True and bIMaxAve == False and bIMaxSpo == False:
              fOTolThi = 140
            elif bIMinSpo == False and bIMaxAve == True and bIMaxSpo == False:
              fOTolThi = 250
            elif bIMinSpo == False and bIMaxAve == False and bIMaxSpo == True:
              fOTolThi = 288

          if fISkiThi_1 == 200:
            if bIMinSpo == True and bIMaxAve == False and bIMaxSpo == False:
              fOTolThi = 160
            elif bIMinSpo == False and bIMaxAve == True and bIMaxSpo == False:
              fOTolThi = 275
            elif bIMinSpo == False and bIMaxAve == False and bIMaxSpo == True:
              fOTolThi = 313

          if fISkiThi_1 == 250:
            if bIMinSpo == True and bIMaxAve == False and bIMaxSpo == False:
              fOTolThi = 200
            elif bIMinSpo == False and bIMaxAve == True and bIMaxSpo == False:
              fOTolThi = 325
            elif bIMinSpo == False and bIMaxAve == False and bIMaxSpo == True:
              fOTolThi = 363

          if fISkiThi_1 == 275:
            if bIMinSpo == True and bIMaxAve == False and bIMaxSpo == False:
              fOTolThi = 300
            elif bIMinSpo == False and bIMaxAve == True and bIMaxSpo == False:
              fOTolThi = 500
            elif bIMinSpo == False and bIMaxAve == False and bIMaxSpo == True:
              fOTolThi = 575

          if fISkiThi_1 == 500:
            if bIMinSpo == True and bIMaxAve == False and bIMaxSpo == False:
              fOTolThi = 400
            elif bIMinSpo == False and bIMaxAve == True and bIMaxSpo == False:
              fOTolThi = 650
            elif bIMinSpo == False and bIMaxAve == False and bIMaxSpo == True:
              fOTolThi = 725

          if fISkiThi_1 == 625:
            if bIMinSpo == True and bIMaxAve == False and bIMaxSpo == False:
              fOTolThi = 500
            elif bIMinSpo == False and bIMaxAve == True and bIMaxSpo == False:
              fOTolThi = 800
            elif bIMinSpo == False and bIMaxAve == False and bIMaxSpo == True:
              fOTolThi = 900

        elif sIUni == "mils":
          if fISkiThi_2 == 1.0:
             if bIMinSpo == True and bIMaxAve == False and bIMaxSpo == False:
               fOTolThi = 0.8
             elif bIMinSpo == False and bIMaxAve == True and bIMaxSpo == False:
               fOTolThi = 2.0
             elif bIMinSpo == False and bIMaxAve == False and bIMaxSpo == True:
               fOTolThi = 3.0

          if fISkiThi_2 == 2.0:
             if bIMinSpo == True and bIMaxAve == False and bIMaxSpo == False:
               fOTolThi = 1.6
             elif bIMinSpo == False and bIMaxAve == True and bIMaxSpo == False:
               fOTolThi = 4.0
             elif bIMinSpo == False and bIMaxAve == False and bIMaxSpo == True:
               fOTolThi = 5.0

          if fISkiThi_2 == 3.0:
             if bIMinSpo == True and bIMaxAve == False and bIMaxSpo == False:
               fOTolThi = 2.4
             elif bIMinSpo == False and bIMaxAve == True and bIMaxSpo == False:
               fOTolThi = 6.0
             elif bIMinSpo == False and bIMaxAve == False and bIMaxSpo == True:
               fOTolThi = 7.0

          if fISkiThi_2 == 4.0:
             if bIMinSpo == True and bIMaxAve == False and bIMaxSpo == False:
               fOTolThi = 3.2
             elif bIMinSpo == False and bIMaxAve == True and bIMaxSpo == False:
               fOTolThi = 7.0
             elif bIMinSpo == False and bIMaxAve == False and bIMaxSpo == True:
               fOTolThi = 8.5

          if fISkiThi_2 == 5.0:
             if bIMinSpo == True and bIMaxAve == False and bIMaxSpo == False:
               fOTolThi = 4.0
             elif bIMinSpo == False and bIMaxAve == True and bIMaxSpo == False:
               fOTolThi = 8.0
             elif bIMinSpo == False and bIMaxAve == False and bIMaxSpo == True:
               fOTolThi = 9.5

          if fISkiThi_2 == 6.0:
             if bIMinSpo == True and bIMaxAve == False and bIMaxSpo == False:
               fOTolThi = 4.8
             elif bIMinSpo == False and bIMaxAve == True and bIMaxSpo == False:
               fOTolThi = 9.0
             elif bIMinSpo == False and bIMaxAve == False and bIMaxSpo == True:
               fOTolThi = 10.5

          if fISkiThi_2 == 7.0:
             if bIMinSpo == True and bIMaxAve == False and bIMaxSpo == False:
               fOTolThi = 5.6
             elif bIMinSpo == False and bIMaxAve == True and bIMaxSpo == False:
               fOTolThi = 10.0
             elif bIMinSpo == False and bIMaxAve == False and bIMaxSpo == True:
               fOTolThi = 11.5

          if fISkiThi_2 == 8.0:
             if bIMinSpo == True and bIMaxAve == False and bIMaxSpo == False:
               fOTolThi = 6.4
             elif bIMinSpo == False and bIMaxAve == True and bIMaxSpo == False:
               fOTolThi = 11.0
             elif bIMinSpo == False and bIMaxAve == False and bIMaxSpo == True:
               fOTolThi = 12.5

          if fISkiThi_2 == 10.0:
             if bIMinSpo == True and bIMaxAve == False and bIMaxSpo == False:
               fOTolThi = 8.0
             elif bIMinSpo == False and bIMaxAve == True and bIMaxSpo == False:
               fOTolThi = 13.0
             elif bIMinSpo == False and bIMaxAve == False and bIMaxSpo == True:
               fOTolThi = 14.5

          if fISkiThi_2 == 15.0:
             if bIMinSpo == True and bIMaxAve == False and bIMaxSpo == False:
               fOTolThi = 12.0
             elif bIMinSpo == False and bIMaxAve == True and bIMaxSpo == False:
               fOTolThi = 20.0
             elif bIMinSpo == False and bIMaxAve == False and bIMaxSpo == True:
               fOTolThi = 23.0

          if fISkiThi_2 == 20.0:
             if bIMinSpo == True and bIMaxAve == False and bIMaxSpo == False:
               fOTolThi = 16.0
             elif bIMinSpo == False and bIMaxAve == True and bIMaxSpo == False:
               fOTolThi = 26.0
             elif bIMinSpo == False and bIMaxAve == False and bIMaxSpo == True:
               fOTolThi = 29.0

          if fISkiThi_2 == 25.0:
             if bIMinSpo == True and bIMaxAve == False and bIMaxSpo == False:
               fOTolThi = 20.0
             elif bIMinSpo == False and bIMaxAve == True and bIMaxSpo == False:
               fOTolThi = 32.0
             elif bIMinSpo == False and bIMaxAve == False and bIMaxSpo == True:
               fOTolThi = 36.0

        return RuleUnitResult(
                result_variables = {
                    "fOTolThi": fOTolThi,
                }
            )