import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244005_030201_01(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 40 05 3.2.1 (1)'
    ref_date = '2018-08-30'
    doc_date = '2023-11-07'
    title = '탄성받침의 치수 허용차'

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량받침
    3. 시공
    3.2 탄성받침
    3.2.1 조립
    """

    # 건설기준문서내용(text)
    content = """
        #### (1) 형상 및 치수는 도면에 의한다.
        표 3.2-1 치수 허용차
        \begin{table}[]
        \begin{tabular}{ccc}
        \multicolumn{3}{r}{\textbf{(단위:mm)}}                                                                                                                                    \\
        \multicolumn{2}{l}{구분}                                                                & \multicolumn{1}{l}{허용차}                                                         \\
        \multirow{3}{*}{완제품 치수}      & 길이                                                     & \multirow{2}{*}{+6, -0}                                                         \\
                                    & 폭                                                      &                                                                                 \\
                                    & 전체 평균두께(H)                                             & \begin{tabular}[c]{@{}c@{}}H ≤ 32: -0, +3\\ H ＞ 32: -0, +6\end{tabular}         \\
        내부 고무층 두께(t)                 & \begin{tabular}[c]{@{}c@{}}받침 내부의 \\ 모든 곳\end{tabular} & \begin{tabular}[c]{@{}c@{}}설계값의 ±20%\\ (다만 ±3mm 이하)\end{tabular}                \\
        \multirow{2}{*}{반대편 면과의 평행성} & 상단과 하단                                                 & 0.005rad 이하                                                                     \\
                                    & 측면                                                     & 0.002rad 이하                                                                     \\
        연결 부재의 노출 위치                 & 구멍, 끼움새나 홈                                             & ±3mm                                                                            \\
        \multirow{2}{*}{고무 덮개층}      & 상하 두께                                                  & \begin{tabular}[c]{@{}c@{}}설계값의 –0, ±2.0mm와 공칭표층두께의 \\ ±20% 중 작은 값\end{tabular} \\
                                    & 측면 두께                                                  & 설계값의 –0, -3mm                                                                   \\
        크기                           & 구멍, 끼움새나 홈                                             & 설계값의 ±3mm                                                                       \\
        \multirow{2}{*}{내부 보강 강판}    & 길이                                                     & 설계값의 ±3mm                                                                       \\
                                    & 폭                                                      & +2, -1(최소두께:2mm)
        \end{tabular}
        \end{table}
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 탄성받침의 치수 허용차];
    B["KCS 24 40 05 3.2.1 (1)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 05 3.2.1 (1)"])

    subgraph Variable_def
    VarOut1[/출력변수: 탄성받침의 치수 허용차/];
    VarIn1[/입력변수: 검사항목/];
    VarOut1 ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> I{"검사항목"}
    I --> |"표 3.2-1"|C[탄성받침의 치수 허용차]
    C --> OO(["탄성받침의 치수 허용차"])
    """

    @rule_method
    def elastometric_bearing(sIRevIte,fIH,fIThiRub,fISurThi)->str:
        """
        Args:
            sIRevIte (string): 검사항목
            fIH (float): 완제품의 전체 평균 두께
            fIThiRub (float): 내부 고무층 두께의 설계값
            fISurThi (float): 공칭표층두께
        Returns:
            sOSizBea (string): 탄성받침의 치수 허용차
        """
        if sIRevIte == "완제품 길이" or sIRevIte == "완제품 폭":
            sOSizBea = "+6, -0 mm "
        elif sIRevIte == "완제품 전체 평균두께":
            if fIH <= 32:
                sOSizBea = "-0, +3 mm"
            else:
                sOSizBea = "-0, +6 mm"
        elif sIRevIte == "내부 고무층 두께":
            sOSizBea = "±" + str(round(min(3,fIThiRub*0.2),3)) + " mm"
        elif sIRevIte == "상단과 하단의 평행성":
            sOSizBea = "0.005 rad 이하"
        elif sIRevIte == "측면의 평행성":
            sOSizBea = "0.002 rad 이하"
        elif sIRevIte == "연결 부재의 노출 위치":
            sOSizBea = "±3mm"
        elif sIRevIte == "고무 덮개층의 상하 두께":
            sOSizBea = "±" + str(round(min(2.0, fISurThi*0.2),3)) + "mm"
        elif sIRevIte == "고무 덮개층의 측면 두께":
            sOSizBea = "–0, -3mm"
        elif sIRevIte == "구멍 끼움새 홈의 크기":
            sOSizBea = "±3mm"
        elif sIRevIte == "내부 보강 강판 길이":
            sOSizBea = "±3mm"
        elif sIRevIte == "내부 보강 강판 폭":
            sOSizBea = "+2, -1(최소두께:2mm)"
        else:
            return "검사항목은 완제품 길이, 완제품 폭, 완제품 전체 평균두께, 내부 고무층 두께, 상단과 하단의 평행성, 측면의 평행성, 연결 부재의 노출 위치, 고무 덮개층의 상하 두께, 고무 덮개층의 측면 두께, 구멍 끼움새 홈의 크기, 내부 보강 강판 길이, 내부 보강 강판 폭 중에서 선택해주세요."
        return sOSizBea