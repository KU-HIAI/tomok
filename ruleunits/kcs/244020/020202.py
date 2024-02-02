import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244020_020202(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 40 20 2.2.2  '
    ref_date = '2016-06-30'
    doc_date = '2023-10-12'
    title = '시트식 방수재의 품질기준'

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량방수
    2. 자재
    2.2.2 시트식 방수재의 품질 및 시험
    """

    # 건설기준문서내용(text)
    content = """
    #### 2.2.2 시트식 방수재의 품질 및 시험
    시트식 방수재의 품질기준은 다음 표 2.2-1과 같다.
    \begin{table}[]
    \begin{tabular}{lllll}
    \multicolumn{3}{l}{항목}                                                                                                      & 시험방법                       & 규격값                                   \\
    \multirow{6}{*}{인장 성능}    & \multirow{3}{*}{\begin{tabular}[c]{@{}l@{}}인장강도\\ (N/㎟)\end{tabular}}   & 무 처리                  & \multirow{3}{*}{KS F 4931} & \multirow{3}{*}{13.0 이상}              \\
                            &                                                                         & 알칼리 처리                &                            &                                       \\
                            &                                                                         & 가열 처리                 &                            &                                       \\
                            & \multirow{3}{*}{\begin{tabular}[c]{@{}l@{}}신장률\\ (%)\end{tabular}}      & \multirow{4}{*}{무 처리} & \multirow{3}{*}{KS F 4931} & \multirow{3}{*}{33 이상}                \\
                            &                                                                         &                       &                            &                                       \\
                            &                                                                         &                       &                            &                                       \\
    \multirow{4}{*}{전단 접착 성능} & \multirow{2}{*}{\begin{tabular}[c]{@{}l@{}}전단접착강도\\ (N/㎟)\end{tabular}} &                       & \multirow{2}{*}{KS F 4931} & 0.80이상                                \\
                            &                                                                         & 20 ℃                  &                            & 0.15이상                                \\
                            & \multirow{2}{*}{\begin{tabular}[c]{@{}l@{}}전단접착변형률\\ (%)\end{tabular}}  & -20 ℃                 & \multirow{2}{*}{KS F 4931} & 0.5이상                                 \\
                            &                                                                         & 20 ℃                  &                            & 1.0이상                                 \\
    \multicolumn{2}{l}{\multirow{2}{*}{인장접착강도 (N/㎟)}}                                                   & -20 ℃                 & \multirow{2}{*}{KS F 4931} & 1.2이상                                 \\
    \multicolumn{2}{l}{}                                                                                & 20 ℃                  &                            & 0.6이상                                 \\
    \multicolumn{3}{l}{내투수성}                                                                                                    & KS F 4931                  & 투수되지 않을 것                             \\
    \multicolumn{3}{l}{염화물 이온 침투 저항성(coulombs)}                                                                                 & KS F 4931                  & 100 이하                                \\
    \multicolumn{3}{l}{내움푹패임}                                                                                                   & KS F 4931                  & 구멍이 생기지 않을 것                          \\
    \multicolumn{2}{l}{내열 치수 안정성(%)}                                                                    & 150 ℃, 30분            & KS F 4931                  & ±2.0 이내                               \\
    \multicolumn{2}{l}{저온굴곡성}                                                                           & -20 ℃                 & KS F 4931                  & 균열이 없을 것                              \\
    \multicolumn{3}{l}{접합강도(N/㎜)}                                                                                               & KS F 4931                  & 5.0 이상                                \\
    \multicolumn{3}{l}{내피로성}                                                                                                    & KS F 4931                  & \multirow{2}{*}{잔금, 찢김, 파단이 생기지 않을 것} \\
    \multicolumn{2}{l}{내균열성}                                                                            & -20 ℃                 & KS F 4931                  &
    \end{tabular}
    \end{table}
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 시트식 방수재의 품질기준];
    B["KCS 24 40 20 2.2.2"];
    B ~~~ A
    end

    KCS(["KCS 24 40 20 2.2.2"])

    subgraph Variable_def
    VarOut[/출력변수: 시트식 방수재의 품질기준/];
    VarIn1[/입력변수: 항목/];
    VarIn2[/입력변수: 시험방법/];
    VarIn3[/입력변수: 규격값/];
    VarOut ~~~ VarIn1 & VarIn2 & VarIn3
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{항목\n시험방법\n규격값}
    C --> |"표 2.2-1"|D[시트식 방수재의 품질기준]
    D --> End([시트식 방수재의 품질기준])
    """

    @rule_method
    def quality_sheeted_waterproof(sIIte,bITesMet,bIStaVal)->str:
        """
        Args:
            sIIte (string): 항목
            bITesMet (boolean): 시험방법
            bIStaVal (boolean): 규격값
        Returns:
            sOQuaMat (string): 시트식 방수재의 품질기준
        """
        if bITesMet:
            sOQuaMet =  "KS F 4931"
        elif bIStaVal:
            if sIIte == "인장강도":
                sOQuaMat = "13.0 N/㎟ 이상"
            elif sIIte == "신장률":
                sOQuaMat = "33 % 이상"
            elif sIIte == "-20 ℃ 전단접착강도":
                sOQuaMat = "0.80 N/㎟ 이상"
            elif sIIte == "20 ℃ 전단접착강도":
                sOQuaMat = "0.15 N/㎟ 이상"
            elif sIIte == "-20 ℃ 전단접착변형률":
                sOQuaMat = "0.5 % 이상"
            elif sIIte == "20 ℃ 전단접착변형률":
                sOQuaMat = "1.0 % 이상"
            elif sIIte == "-20 ℃ 인장접착강도":
                sOQuaMat = "1.2 N/㎟ 이상"
            elif sIIte == "20 ℃ 인장접착강도":
                sOQuaMat = "0.6 N/㎟ 이상"
            elif sIIte == "내투수성":
                sOQuaMat = "투수되지 않을 것"
            elif sIIte == "염화물 이온 침투 저항성":
                sOQuaMat = "100 coulombs 이하"
            elif sIIte == "내움푹패임":
                sOQuaMat = "구멍이 생기지 않을 것"
            elif sIIte == "내열 치수 안정성":
                sOQuaMat = "±2.0 % 이내"
            elif sIIte == "저온굴곡성":
                sOQuaMat = "균열이 없을 것"
            elif sIIte == "접합강도":
                sOQuaMat = "5.0 N/㎜ 이상"
            elif sIIte == "내피로성" or "내균열성":
                sOQuaMat = "잔금, 찢김, 파단이 생기지 않을 것"
        return sOQuaMat