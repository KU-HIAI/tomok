import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_031005_03_07(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 3.10.5 (3) ⑦'
    ref_date = '2019-05-20'
    doc_date = '2023-11-13'
    title = '스터드의 필릿용접'

    description = """
    용접
    3. 시공
    3.10 스터드의 용접
    3.10.5 스터드필릿용접
    """

    content = """
    #### 3.10.5 스터드필릿용접
    (3) 스터드의 필릿용접은 다음 규정에 준하여 시행한다.
    ⑦ 모재의 최소 예열온도는 표 3.4-1에 의한다.
    \begin{table}[]
\begin{tabular}{llllll}
\multirow{2}{*}{강종} & \multirow{2}{*}{용접 방법} & \multicolumn{4}{l}{판두께(mm)에 따른 최소 예열온도(℃)} \\
 &  & t≤25 & 25<t≤40 & 40<t≤50 & 50<t≤100 \\
\multirow{3}{*}{SM275} & \begin{tabular}[c]{@{}l@{}}저수소계 이외의 용접봉에 의한\\ 피복아크용접(SMAW)\end{tabular} & 예열 없음. & 50 & - & - \\
 & 저수소계 용접봉에 의한 피복아크용접 & 예열 없음. & 예열 없음. & 50 & 50 \\
 & \begin{tabular}[c]{@{}l@{}}SAW, 가스실드아크용접\\ (GMAW 또는 FCAW)\end{tabular} & 예열 없음. & 예열 없음. & 예열 없음. & 예열 없음. \\
\multirow{2}{*}{SMA275} & 저수소계 용접봉에 의한 피복아크용접 & 예열 없음. & 예열 없음. & 50 & 50 \\
 & \begin{tabular}[c]{@{}l@{}}SAW, 가스실드아크용접\\ (GMAW 또는 FCAW)\end{tabular} & 예열 없음. & 예열 없음. & 예열 없음. & 예열 없음. \\
\multirow{2}{*}{SM355} & 저수소계 용접봉에 의한 피복아크용접 & 예열 없음. & 50 & 80 & 80 \\
 & \begin{tabular}[c]{@{}l@{}}SAW, 가스실드아크용접\\ (GMAW 또는 FCAW)\end{tabular} & 예열 없음. & 예열 없음. & 50 & 50 \\
\multirow{2}{*}{\begin{tabular}[c]{@{}l@{}}SM420\\ SM460\\ SN355\end{tabular}} & 저수소계 용접봉에 의한 피복아크용접 & 예열 없음. & 80 & 80 & 100 \\
 & \begin{tabular}[c]{@{}l@{}}SAW, 가스실드아크용접\\ (GMAW 또는 FCAW)\end{tabular} & 예열 없음. & 50 & 50 & 80
\end{tabular}
\end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: 스터드의 필릿용접"];
    B["KCS 14 31 20 3.10.5 (3) ⑦"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 3.10.5 (3) ⑦"])

    subgraph Variable_def
		VarOut3[/"출력변수: 최소 예열온도"/];
    VarIn4[/입력변수: 강종/];
    VarIn5[/입력변수: 용접방법/];
    VarIn6[/입력변수: 판두께/];
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{강종, 용접 방법, 판두께}
		C --> |표 3.4-1|D[최소 예열온도]
		D  --> End([최소 예열온도])
    """

    @rule_method
    def Stud_Fillet_Welding(sIWelMet, sISteGra, fIThiPla) -> RuleUnitResult:
        """ 스터드의 필릿용접
        Args:
        sIWelMet (str): 용접방법
        sISteGra (str): 강종
        fIThiPla (float): 판두께

        Returns:
        sOMinPre (str): 최소 예열온도
        """
        assert isinstance(sIWelMet, str)
        assert sIWelMet in["저수소계 이외의 용접봉에 의한 피복아크용접(SMAW)", "저수소계 용접봉에 의한 피복아크용접", "SAW, 가스실드아크용접(GMAW 또는 FCAW)"]
        assert isinstance(sISteGra, str)
        assert sISteGra in["SM275", "SMA275", "SM355", "SM420", "SM460", "SN355", "SMA355W", "SMA460W", "HSB380", "HSB380L", "HSB380W", "HSB460", "HSB460L", "HSB460W", "HSB690", "HSB690L", "HSB690W"]
        assert isinstance(fIThiPla, float)

        if sIWelMet == "저수소계 이외의 용접봉에 의한 피복아크용접(SMAW)":
          if sISteGra == "SM275":
            if fIThiPla <= 25:
              sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
            elif 25 < fIThiPla <= 40:
              sOPreInt = "50"
            elif 40 < fIThiPla <= 50:
              sOMinPre = "-"
            elif fIThiPla > 50:
              sOMinPre = "-"
        elif sIWelMet == "저수소계 용접봉에 의한 피복아크용접":
          if sISteGra == "SM275":
            if fIThiPla <= 25:
              sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
            elif 25 < fIThiPla <= 40:
              sOPreInt = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
            elif 40 < fIThiPla <= 50:
              sOMinPre = "50"
            elif fIThiPla > 50:
              sOMinPre = "50"
          elif sISteGra == "SMA275":
            if fIThiPla <= 25:
              sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
            elif 25 < fIThiPla <= 40:
              sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
            elif 40 < fIThiPla <= 50:
              sOMinPre = "50"
            elif fIThiPla > 50:
              sOMinPre = "50"
          elif sISteGra == "SM355":
            if fIThiPla <= 25:
              sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
            elif 25 < fIThiPla <= 40:
              sOMinPre = "50"
            elif 40 < fIThiPla <= 50:
              sOMinPre = "80"
            elif fIThiPla > 50:
              sOMinPre = "80"
          elif sISteGra == "SM420" or "SM460" or "SN355":
            if fIThiPla <= 25:
              sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
            elif 25 < fIThiPla <= 40:
              sOMinPre = "80"
            elif 40 < fIThiPla <= 50:
              sOMinPre = "80"
            elif fIThiPla > 50:
              sOMinPre = "100"
          elif sISteGra == "SMA355W" or "SMA460W":
            if fIThiPla <= 25:
              sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
            elif 25 < fIThiPla <= 40:
              sOMinPre = "80"
            elif 40 < fIThiPla <= 50:
              sOMinPre = "80"
            elif fIThiPla > 50:
              sOMinPre = "100"
          elif sISteGra == "HSB380" or "HSB380L" or "HSB380W" or "HSB460" or "HSB460L" or "HSB460W":
            sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
          elif sISteGra == "HSB690" or "HSB690L":
            if fIThiPla <= 25:
              sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
            elif 25 < fIThiPla <= 40:
              sOMinPre = "50"
            elif 40 < fIThiPla <= 50:
              sOMinPre = "50"
            elif fIThiPla > 50:
              sOMinPre = "50"
          elif sISteGra == "HSB690W":
            if fIThiPla <= 25:
              sOMinPre = "50"
            elif 25 < fIThiPla <= 40:
              sOMinPre = "80"
            elif 40 < fIThiPla <= 50:
              sOMinPre = "80"
            elif fIThiPla > 50:
              sOMinPre = "80"
        elif sIWelMet == "SAW, 가스실드아크용접(GMAW 또는 FCAW)":
          if sISteGra == "SM275":
            sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
          elif sISteGra == "SMA275":
            sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
          elif sISteGra == "SM355":
            if fIThiPla <= 25:
              sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
            elif 25 < fIThiPla <= 40:
              sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
            elif 40 < fIThiPla <= 50:
              sOMinPre = "50"
            elif fIThiPla > 50:
              sOMinPre = "50"
          elif sISteGra == "SM420" or "SM460" or "SN355":
            if fIThiPla <= 25:
              sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
            elif 25 < fIThiPla <= 40:
              sOMinPre = "50"
            elif 40 < fIThiPla <= 50:
              sOMinPre = "50"
            elif fIThiPla > 50:
              sOMinPre = "80"
          elif sISteGra == "SMA355W" or "SMA460W":
            if fIThiPla <= 25:
              sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
            elif 25 < fIThiPla <= 40:
              sOMinPre = "50"
            elif 40 < fIThiPla <= 50:
              sOMinPre = "50"
            elif fIThiPla > 50:
              sOMinPre = "80"
          elif sISteGra == "HSB380" or "HSB380L" or "HSB380W" or "HSB460" or "HSB460L" or "HSB460W":
            sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
          elif sISteGra == "HSB690" or "HSB690L":
            if fIThiPla <= 25:
              sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
            elif 25 < fIThiPla <= 40:
              sOMinPre = "50"
            elif 40 < fIThiPla <= 50:
              sOMinPre = "50"
            elif fIThiPla > 50:
              sOMinPre = "50"
          elif sISteGra == "HSB690W":
            if fIThiPla <= 25:
              sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
            elif 25 < fIThiPla <= 40:
              sOMinPre = "50"
            elif 40 < fIThiPla <= 50:
              sOMinPre = "50"
            elif fIThiPla > 50:
              sOMinPre = "50"

        return RuleUnitResult(
                result_variables = {
                    "sOMinPre": sOMinPre,
                }
            )