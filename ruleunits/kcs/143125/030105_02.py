import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS143125_030105_02(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 14 31 25 3.1.5 (2)' # 건설기준문서
    ref_date = '2023-09-11'  # 디지털 건설문서 작성일
    doc_date = '2019-05-20'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '볼트 접합 및 핀 연결'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    볼트 접합 및 핀 연결
    3. 시공
    3.1.5 볼트조임
    (2)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.1.5 볼트조임
    (2) 볼트의 조임 축력
    볼트의 조임은 설계볼트장력에 10%를 증가시켜 표 3.1-4에 명시한 표준볼트장력을 얻을 수 있도록 한다.

표 3.1-4 고장력볼트의 설계볼트장력과 표준볼트장력 및 장력의 범위
\begin{table}[]
\begin{tabular}{|
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l |}
\hline
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 고장력볼트의 등급}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 고장력볼트호칭}}                                                                   & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}공칭단면적\\ (mm2)\end{tabular}}}                     & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}설계볼트장력1)\\ (kN)\end{tabular}}}                   & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}표준볼트장력\\ (kN)\end{tabular}}}                     & {\color[HTML]{333333} 시험볼트 장력의 평균값 범위2) (kN)}                                                                                                          \\ \hline
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} F8T}}       & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}M16\\ M20\\ M22\\ M24\end{tabular}}}             & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}201\\ 314\\ 380\\ 452\end{tabular}}}             & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}84\\ 131\\ 163\\ 189\end{tabular}}}              & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}92\\ 144\\ 179\\ 208\end{tabular}}}              & {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}85$\sim$95\\ 135$\sim$150\\ 170$\sim$185\\ 195$\sim$215\end{tabular}}                                 \\ \hline
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} F10T}}      & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}M16\\ M20\\ M22\\ M24\\ M27\\ M30\end{tabular}}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}201\\ 314\\ 380\\ 452\\ 572\\ 708\end{tabular}}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}105\\ 164\\ 203\\ 236\\ 307\\ 376\end{tabular}}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}116\\ 180\\ 223\\ 260\\ 338\\ 414\end{tabular}}} & {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}105$\sim$120\\ 170$\sim$185\\ 210$\sim$230\\ 245$\sim$270\\ 315$\sim$355\\ 390$\sim$435\end{tabular}} \\ \hline
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} F13T}}      & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}M16\\ M20\\ M22\\ M24\end{tabular}}}             & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}201\\ 314\\ 380\\ 452\end{tabular}}}             & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}136\\ 213\\ 264\\ 307\end{tabular}}}             & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}150\\ 234\\ 290\\ 338\end{tabular}}}             & {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}140$\sim$155\\ 220$\sim$240\\ 275$\sim$300\\ 320$\sim$350\end{tabular}}                               \\ \hline
\multicolumn{6}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}주 1) KS B 1010 표3에 규정된 볼트의 최소 인장하중에 0.67을 곱한 값.\\     2) 시공 전 축력계로 측정한 시험볼트 5세트의 장력 평균값 범위\end{tabular}}}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 \\ \hline
\end{tabular}
\end{table}

    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A[Title: 표준볼트장력];
    B["KCS 14 31 25 3.1.5 (2)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 25 3.1.5"])

    subgraph Variable_def
    VarOut[/출력변수: 표준볼트장력/];
    VarIn1[/입력변수: 고장력볼트호칭/];
    VarIn2[/입력변수: 고장력볼트등급/];
    VarOut ~~~ VarIn1 &  VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{고장력볼트호칭}
    C-->|F8T|D{"고장력볼트등급(F8T)"}
    D-->|M16|E[92]
    D-->|M20|F[144]
    D-->|M22|G[179]
    D-->|M24|H[208]


    C-->|F10T|I{"고장력볼트등급(F10T)"}
    I-->|M16|J[116]
    I-->|M20|K[180]
    I-->|M22|L[223]
    I-->|M24|M[260]
    I-->|M27|N[338]
    I-->|M30|O[414]

    C-->|F10T|P{"고장력볼트등급(F13T)"}
    P-->|M16|Q[150]
    P-->|M20|R[234]
    P-->|M22|S[290]
    P-->|M24|T[338]

		E-->U([표준볼트장력])
		F-->U([표준볼트장력])
		G-->U([표준볼트장력])
		H-->U([표준볼트장력])
		J-->U([표준볼트장력])
		K-->U([표준볼트장력])
		L-->U([표준볼트장력])
		M-->U([표준볼트장력])
		N-->U([표준볼트장력])
		O-->U([표준볼트장력])
		Q-->U([표준볼트장력])
		R-->U([표준볼트장력])
		S-->U([표준볼트장력])
		T-->U([표준볼트장력])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def standard_bolt_tension(sIGraBol, sINamBol) ->str :
        """볼트의 조임 축력

        Args:
            sIGraBol (string): 고장력 볼트의 등급
            sINamBol (string): 고장력 볼트 호칭

        Returns:
            fOBolTen (float): 표준볼트 장력


        """

        if sIGraBol == "F8T":
            if sINamBol == "M16":
                fOBolTen = 92
                return fOBolTen
            elif sINamBol == "M20":
                fOBolTen = 144
                return fOBolTen
            elif sINamBol == "M22":
                fOBolTen = 179
                return fOBolTen
            elif sINamBol == "M24":
                fOBolTen = 208
                return fOBolTen

        elif sIGraBol == "F10T":
            if sINamBol == "M16":
                fOBolTen = 116
                return fOBolTen
            elif sINamBol == "M20":
                fOBolTen = 180
                return fOBolTen
            elif sINamBol == "M22":
                fOBolTen = 223
                return fOBolTen
            elif sINamBol == "M24":
                fOBolTen = 260
                return fOBolTen
            elif sINamBol == "M27":
                fOBolTen = 338
                return fOBolTen
            elif sINamBol == "M30":
                fOBolTen = 414
                return fOBolTen

        elif sIGraBol == "F13T":
            if sINamBol == "M16":
                fOBolTen = 150
                return fOBolTen
            elif sINamBol == "M20":
                fOBolTen = 234
                return fOBolTen
            elif sINamBol == "M22":
                fOBolTen = 290
                return fOBolTen
            elif sINamBol == "M24":
                fOBolTen = 338
                return fOBolTen