import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS213000_020801_02(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 21 30 00 2.8.1 (2)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-22'
    title = '지반조건에 따른 추정 정압 주입률'

    description = """
    가설흙막이 공사
    2. 자재
    2.8. 지반 그라우팅
    2.8.1. 일반 사항
    (2)
    """

    content = """
    #### 2.8.1. 일반사항
    (2) 약액주입공법(LW, SGR공법 등)은 정압주입을 원칙으로 하며, 정압주입으로 할 경우의 주입률은 지층조건에 따라 표 2.8-1을 참조하여 시공을 할 수 있으며, 이 때 반드시 시험시공을 실시하여 주입효과를 확인한 후 설계조건에 합당한지 검토한 후 본 시공을 시행한다. 다만, 매립지, 유기질토 등 특수지반에서는 반드시 현장주입시험 결과에 의해 주입률을 결정하여야 한다.
    표 2.8-1
    \begin{table}[]
    \begin{tabular}{|c|c|c|c|c|}
    \hline
    지반종류                                                                    & SPT-N 값 & 간극률(n, \%) & 충전율(α, \%) & 주입률(λ, \%)                                                                                                                  \\ \hline
    \multirow{3}{*}{점성토}                                                    & 0∼4     & 65∼75      & 35∼45      & \multirow{10}{*}{\begin{tabular}[c]{@{}c@{}}주입률(λ) = n*α(1+β)\\ 여기서, n: 공극률\\ α: 충전율\\ β: 손실률\\ (5$\sim$10\%)\end{tabular}} \\ \cline{2-4}
                                                                        & 4∼8     & 50∼70      & 25∼35      &                                                                                                                             \\ \cline{2-4}
                                                                        & 8∼15    & 40∼60      & 15∼25      &                                                                                                                             \\ \cline{1-4}
    \multirow{3}{*}{사질토}                                                    & 0∼10    & 46∼50      & 60∼90      &                                                                                                                             \\ \cline{2-4}
                                                                        & 10∼30   & 40∼48      & 55∼80      &                                                                                                                             \\ \cline{2-4}
                                                                        & 30 이상   & 30∼40      & 55∼70      &                                                                                                                             \\ \cline{1-4}
    \multirow{3}{*}{\begin{tabular}[c]{@{}c@{}}사력토\\ (모래, 자갈)\end{tabular}} & 10∼30   & 40∼60      & 60∼85      &                                                                                                                             \\ \cline{2-4}
                                                                        & 30∼50   & 28∼40      & 60∼85      &                                                                                                                             \\ \cline{2-4}
                                                                        & 50 이상   & 22∼30      & 55∼65      &                                                                                                                             \\ \cline{1-4}
    풍화암                                                                     & -       & 18∼22      & 50∼80      &                                                                                                                             \\ \hline
    \end{tabular}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 지반조건에 따른 추정 정압 주입률];
    B["KCS 21 30 00 2.8.1 (2)"];
    B ~~~ A
    end

    KCS(["KCS 21 30 00 2.8.1 (2)"])

    subgraph Variable_def
    VarOut1[/출력변수: 주입률/]; VarOut2[/출력변수: 주입률/];
		VarIn1[/입력변수: 지반종류/]; VarIn2[/입력변수: SPT-N 값/];
		VarIn3[/입력변수: 간극률/]; VarIn4[/입력변수: 충전율/];
		VarIn5[/입력변수: 손실률/];
    VarOut1 & VarOut2 & VarIn1 ~~~ VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"특수지반"}
    C1 --> |Yes|D1["현장주입시험 결과에 의해 주입률 결정"]
    C1 --> |No|C2{"주입률=공극률*충전율*(1+손실률)"}
    C2 --> D2["주입률"]

    D1 & D2 --> E(["지반조건에 따른 추정 정압 주입률"]);
    """

    @rule_method
    def Type_of_Soil(sITypSoi, nISPTVal, fIPor, fIFilRat, fILosRat) -> str:
        """ 지반조건에 따른 추정 정압 주입률
        Args:
            sITypSoi (str): 지반 종류
            nISPTVal (int): SPT-N값
            fIPor (float): 간극률
            fIFilRat (float): 충전율
            fILosRat (float): 손실율

        Returns:
            fOInjRat (float): 주입률
            sOInjRat (str): 주입률
        """
        assert isinstance(sITypSoi, str)
        assert sITypSoi in["점성토", "사질토", "사력토", "풍화암", "특수지반"]
        assert isinstance(nISPTVal, int)
        assert nISPTVal >= 0
        assert isinstance(fIPor, float)
        assert isinstance(fIFilRat, float)
        assert isinstance(fILosRat, float)

        if sITypSoi == "점성토":
          sOInjRat = None
          if 0 <= nISPTVal < 4:
            if 65 <= fIPor <= 75 and 35 <= fIFilRat <= 45:
              fOInjRat = (0.01*fIPor) * (0.01*fIFilRat) * (1 + (0.01* fILosRat)) * 100
          elif 4 <= nISPTVal < 8:
            if 50 <= fIPor <= 70 and 25 <= fIFilRat <= 35:
              fOInjRat = (0.01*fIPor) * (0.01*fIFilRat) * (1 + (0.01* fILosRat)) * 100
          elif 8 <= nISPTVal < 15:
            if 40 <= fIPor <= 60 and 15 <= fIFilRat <= 25:
              fOInjRat = (0.01*fIPor) * (0.01*fIFilRat) * (1 + (0.01* fILosRat)) * 100

        elif sITypSoi == "사질토":
          sOInjRat = None
          if 0 <= nISPTVal < 10:
            if 46 <= fIPor <= 50 and 60 <= fIFilRat <= 90:
              fOInjRat = (0.01*fIPor) * (0.01*fIFilRat) * (1 + (0.01* fILosRat)) * 100
          elif 10 <= nISPTVal < 30:
            if 40 <= fIPor <= 48 and 55 <= fIFilRat <= 80:
              fOInjRat = (0.01*fIPor) * (0.01*fIFilRat) * (1 + (0.01* fILosRat)) * 100
          elif 30 <= nISPTVal:
            if 30 <= fIPor <= 40 and 55 <= fIFilRat <= 70:
              fOInjRat = (0.01*fIPor) * (0.01*fIFilRat) * (1 + (0.01* fILosRat)) * 100

        elif sITypSoi == "사력토":
          sOInjRat = None
          if 10 <= nISPTVal < 30:
            if 40 <= fIPor <= 60 and 60 <= fIFilRat <= 85:
              fOInjRat = (0.01*fIPor) * (0.01*fIFilRat) * (1 + (0.01* fILosRat)) * 100
          elif 30 <= nISPTVal < 50:
            if 28 <= fIPor <= 40 and 60 <= fIFilRat <= 85:
              fOInjRat = (0.01*fIPor) * (0.01*fIFilRat) * (1 + (0.01* fILosRat)) * 100
          elif 50 <= nISPTVal:
            if 22 <= fIPor <= 30 and 55 <= fIFilRat <= 65:
              fOInjRat = (0.01*fIPor) * (0.01*fIFilRat) * (1 + (0.01* fILosRat)) * 100

        elif sITypSoi == "풍화암":
          sOInjRat = None
          if 18 <= fIPor <= 22 and 50 <= fIFilRat <= 80:
              fOInjRat = (0.01*fIPor) * (0.01*fIFilRat) * (1 + (0.01* fILosRat)) * 100

        elif sITypSoi == "특수지반":
          sOInjRat = "반드시 현장주입시험 결과에 의해 주입률을 결정하여야 한다."
          fOInjRat = None

        return RuleUnitResult(
            result_variables={
                "fOInjRat": fOInjRat,
                "sOInjRat": sOInjRat,
            }
        )