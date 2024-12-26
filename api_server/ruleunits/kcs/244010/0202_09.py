import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244010_0202_09(RuleUnit):

    priority = 1
    author = '국가건설기준센터'
    acc_able = False
    ref_code = 'KCS 24 40 10 2.2 (9)'
    ref_date = '2023-09-11'
    doc_date = '2018-08-30'
    title = '알루미늄계 신축이음장치의 품질기준'

    description = """
    신축이음
    2. 자재
    2.2 재료
    (9)
    """

    content = """
    #### 2.2 재료
    (9) 신축이음장치에 사용하는 알루미늄합금은 부식에 대한 저항성이 있어야 하며, 재료는 표 2.2-2의 품질기준에 적합하여야 한다.
    표 2.2-2 알루미늄계 신축이음장치의 품질기준

    〈알루미늄 합금 몸체〉

\begin{table}[]
\begin{tabular}{|ll|l|l|l|llllll|}
\hline
\multicolumn{2}{|l|}{\begin{tabular}[c]{@{}l@{}}인장강도\\ (MPa)\end{tabular}} & \begin{tabular}[c]{@{}l@{}}항복점\\ (MPa)\end{tabular} & \begin{tabular}[c]{@{}l@{}}연신율\\ (\%)\end{tabular} & 경도                     & \multicolumn{6}{l|}{화학적 성분(\%)}                                                                                                                                                                                                                                                                                              \\ \hline
\multicolumn{2}{|l|}{\multirow{2}{*}{260 이상}}                              & \multirow{2}{*}{260 이상}                             & \multirow{2}{*}{2 \% 이상}                           & \multirow{2}{*}{90 이상} & \multicolumn{1}{l|}{Si}              & \multicolumn{1}{l|}{Fe}                                                & \multicolumn{1}{l|}{Cu}                                                & \multicolumn{1}{l|}{Mn}                                                & \multicolumn{1}{l|}{Mg}              & Ti              \\ \cline{6-11}
\multicolumn{2}{|l|}{}                                                     &                                                     &                                                    &                        & \multicolumn{1}{l|}{6.50 $\sim$7.50} & \multicolumn{1}{l|}{\begin{tabular}[c]{@{}l@{}}0.20\\ 이하\end{tabular}} & \multicolumn{1}{l|}{\begin{tabular}[c]{@{}l@{}}0.10\\ 이하\end{tabular}} & \multicolumn{1}{l|}{\begin{tabular}[c]{@{}l@{}}0.10\\ 이하\end{tabular}} & \multicolumn{1}{l|}{0.45 $\sim$0.70} & 0.08 $\sim$0.25 \\ \hline
\end{tabular}
\end{table}

    〈프리스트레싱 볼트〉

\begin{table}[]
\begin{tabular}{|ll|l|l|lllllll|}
\hline
\multicolumn{2}{|l|}{\begin{tabular}[c]{@{}l@{}}인장강도\\ (MPa)\end{tabular}} & \begin{tabular}[c]{@{}l@{}}항복점\\ (MPa)\end{tabular}               & \begin{tabular}[c]{@{}l@{}}연신율\\ (\%)\end{tabular}                  & \multicolumn{7}{l|}{화학적 성분(\%)}                                                                                                                                                                                                                                                                                                     \\ \hline
\multicolumn{2}{|l|}{\multirow{2}{*}{1080 $\sim$1280}}                     & \multirow{2}{*}{\begin{tabular}[c]{@{}l@{}}850\\ 이상\end{tabular}} & \multirow{2}{*}{\begin{tabular}[c]{@{}l@{}}10 \%\\ 이상\end{tabular}} & \multicolumn{1}{l|}{C}               & \multicolumn{1}{l|}{Si}              & \multicolumn{1}{l|}{Mn}              & \multicolumn{1}{l|}{S}                                                  & \multicolumn{1}{l|}{P}                                                  & \multicolumn{1}{l|}{Cr}              & Me              \\ \cline{5-11}
\multicolumn{2}{|l|}{}                                                     &                                                                   &                                                                     & \multicolumn{1}{l|}{0.39 $\sim$0.45} & \multicolumn{1}{l|}{0.10 $\sim$0.40} & \multicolumn{1}{l|}{0.60 $\sim$0.90} & \multicolumn{1}{l|}{\begin{tabular}[c]{@{}l@{}}0.035\\ 이하\end{tabular}} & \multicolumn{1}{l|}{\begin{tabular}[c]{@{}l@{}}0.035\\ 이하\end{tabular}} & \multicolumn{1}{l|}{0.90 $\sim$1.20} & 0.15 $\sim$0.25 \\ \hline
\end{tabular}
\end{table}

    〈볼트 정착앵커(동 알루미늄)〉

\begin{table}[]
\begin{tabular}{|lllllllll|}
\hline
\multicolumn{2}{|l|}{\begin{tabular}[c]{@{}l@{}}인장강도\\ (MPa)\end{tabular}} & \multicolumn{1}{l|}{\begin{tabular}[c]{@{}l@{}}항복점\\ (MPa)\end{tabular}} & \multicolumn{1}{l|}{\begin{tabular}[c]{@{}l@{}}연신율\\ (\%)\end{tabular}} & \multicolumn{1}{l|}{경도}                      & \multicolumn{4}{l|}{화학적 성분(\%)}                                                                                                                                                                                                            \\ \hline
\multicolumn{2}{|l|}{\multirow{2}{*}{650 이상}}                              & \multicolumn{1}{l|}{\multirow{2}{*}{250 이상}}                             & \multicolumn{1}{l|}{\multirow{2}{*}{20 \% 이상}}                          & \multicolumn{1}{l|}{\multirow{2}{*}{160 이상}} & \multicolumn{1}{l|}{Al}              & \multicolumn{1}{l|}{Fe}                                                & \multicolumn{1}{l|}{Ni}                                                & Mn                                                \\ \cline{6-9}
\multicolumn{2}{|l|}{}                                                     & \multicolumn{1}{l|}{}                                                    & \multicolumn{1}{l|}{}                                                   & \multicolumn{1}{l|}{}                        & \multicolumn{1}{l|}{6.50 $\sim$7.50} & \multicolumn{1}{l|}{\begin{tabular}[c]{@{}l@{}}0.20\\ 이하\end{tabular}} & \multicolumn{1}{l|}{\begin{tabular}[c]{@{}l@{}}0.10\\ 이하\end{tabular}} & \begin{tabular}[c]{@{}l@{}}0.10\\ 이하\end{tabular} \\ \hline
\multicolumn{9}{|l|}{주 1) 신축이음에 사용하는 기타 재료는 제작도면에 따른다.}                                                                                                                                                                                                                                                                                                                                                                                                                                                                     \\ \hline
\end{tabular}
\end{table}

    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 알루미늄계 신축이음장치의 품질기준];
    B["KCS 24 40 10 2.2 (9)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 10 2.2 (9)"])

    subgraph Variable_def
    VarOut[/출력변수: 알루미늄계 신축이음장치의 품질기준/];
		VarIn1[/입력변수: 알루미늄 합금 몸체/];
    VarIn2[/입력변수: 프리스트레싱 볼트/];
    VarIn3[/입력변수: 볼트 정착앵커/];

    VarIn4[/입력변수: 인장강도/];
    VarIn5[/입력변수: 항복점/];
    VarIn6[/입력변수: 연신율/];
    VarIn7[/입력변수: 경도/];
    VarIn8[/입력변수: 화학적 성분/];
    VarOut ~~~ VarIn1 & VarIn2 & VarIn3 ~~~ VarIn4 & VarIn5 & VarIn6 & VarIn7 & VarIn8
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{항목}

    C --> |알루미늄 합금 몸체|D{"표 2.2-2〈알루미늄 합금 몸체>"}
    C --> |프리스트레싱 볼트|E{"표 2.2-2〈프리스트레싱 볼트>"}
    C --> |"볼트 정착앵커(동 알루미늄)"|F{"표 2.2-2〈볼트 정착앵커(동 알루미늄)>"}

		D --> G([알루미늄계 신축이음장치의 품질기준])
		E --> G([알루미늄계 신축이음장치의 품질기준])
		F --> G([알루미늄계 신축이음장치의 품질기준])
    """

    @rule_method
    def joint_drawing(bIAluAll, bIPreBol, bIBolAnc, bITenStr, bIYieStr, bIElo, bIHar, sICheCom) -> str :
        """알루미늄계 신축이음장치의 품질기준

        Args:
            bIAluAll (bool): 알루미늄 합금 몸체
            bIPreBol (bool): 프리스트레싱 볼트
            bIBolAnc (bool): 볼트 정착앵커
            bITenStr (bool): 인장강도
            bIYieStr (bool): 항복점
            bIElo (bool): 연신율
            bIHar (bool): 경도
            sICheCom (str): 화학적 성분

        Returns:
            sOQuaSta (str): 알루미늄계 신축이음장치의 품질기준
        """
        assert isinstance(bIAluAll, bool)
        assert isinstance(bIPreBol, bool)
        assert isinstance(bIBolAnc, bool)
        assert isinstance(bITenStr, bool)
        assert isinstance(bIYieStr, bool)
        assert isinstance(bIElo, bool)
        assert isinstance(bIHar, bool)
        assert isinstance(sICheCom, str)
        assert (bIAluAll + bIPreBol + bIBolAnc) == 1

        sOQuaSta = ""

        if bIAluAll == True:
            if bITenStr == True:
                sOQuaSta = "260 MPa 이상"
            elif bIYieStr == True:
                sOQuaSta = "260 MPa 이상"
            elif bIElo == True:
                sOQuaSta = "2 % 이상"
            elif bIHar == True:
                sOQuaSta = "90 이상"
            elif sICheCom == "Si":
                sOQuaSta = "6.50 ~ 7.50 %"
            elif sICheCom == "Fe":
                sOQuaSta = "0.20 % 이하"
            elif sICheCom == "Cu":
                sOQuaSta = "0.10 % 이하"
            elif sICheCom == "Mn":
                sOQuaSta = "0.10 % 이하"
            elif sICheCom == "Mg":
                sOQuaSta = "0.45 ~ 0.70 %"
            elif sICheCom == "Ti":
                sOQuaSta = "0.08 ~ 0.25 %"

        elif bIPreBol == True:
            if bITenStr == True:
                sOQuaSta = "1080 ~ 1280 MPa"
            elif bIYieStr == True:
                sOQuaSta = "850 MPa 이상"
            elif bIElo == True:
                sOQuaSta = "10 % 이상"
            elif sICheCom == "C":
                sOQuaSta = "0.39 ~ 0.45 %"
            elif sICheCom == "Si":
                sOQuaSta = "0.10 ~ 0.40 %"
            elif sICheCom == "Mn":
                sOQuaSta = "0.60 ~ 0.90 %"
            elif sICheCom == "S":
                sOQuaSta = "0.035 % 이하"
            elif sICheCom == "P":
                sOQuaSta = "0.035 % 이하"
            elif sICheCom == "Cr":
                sOQuaSta = "0.90 ~ 1.20 %"
            elif sICheCom == "Me":
                sOQuaSta = "0.15 ~ 0.25 %"

            return RuleUnitResult(
                  result_variables = {
                      "sOQuaSta": sOQuaSta,
                  }
            )

        elif bIBolAnc == True:
            if bITenStr == True:
                sOQuaSta = "650 MPa 이상"
            elif bIYieStr == True:
                sOQuaSta = "250 MPa 이상"
            elif bIElo == True:
                sOQuaSta = "20 % 이상"
            elif bIHar == True:
                sOQuaSta = "160 이상"
            elif sICheCom == "Al":
                sOQuaSta = "6.50 ~ 7.50 %"
            elif sICheCom == "Fe":
                sOQuaSta = "0.20 % 이하"
            elif sICheCom == "Ni":
                sOQuaSta = "0.10 % 이하"
            elif sICheCom == "Mn":
                sOQuaSta = "0.10 % 이하"

        return RuleUnitResult(
            result_variables = {
                "sOQuaSta": sOQuaSta,
            }
        )