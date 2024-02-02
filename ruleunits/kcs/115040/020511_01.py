import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS115040_020511_01(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 11 50 40 2.5.11 (1)'
    ref_date = '2021-05-12'
    doc_date = '2023-09-18'
    title = '횡방향 재하시험 측정간격'

    # 건설기준문서항목 (분류체계정보)
    description = """
    말뚝재하시험
    2. 시험
    2.5 횡방향재하시험
    2.5.11 측정간격
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    ####(1) 측정간격은 측정항목과 재하방법에 따라 표 2.5-3 및 표 2.5-4에 정한 바와 같이 측정한다.

    \begin{table}[]
    \begin{tabular}{llll}
    측정항목                          & \multicolumn{2}{l}{하중증가 시 측정시간}    & 하중감소 시 측정시간         \\
    \multirow{2}{*}{하중}           & 처녀 하중, 이력 내 하중 & 0분, 약 2분          & \multirow{2}{*}{0분} \\
                                & 0 하중           & 0, 2, 4, 8, 약 14분 &                     \\
    \multirow{2}{*}{변위, 말뚝두부 경사각} & 처녀 하중, 이력 내 하중 & 0분, 약 2분          & \multirow{2}{*}{0분} \\
                                & 0 하중           & 0, 2, 4, 8, 약 14분 &                     \\
    \multirow{2}{*}{그 외1)}        & 처녀 하중, 이력 내 하중 & 0분                & \multirow{2}{*}{0분} \\
                                & 0 하중           & 0, 8, 약 14분       &
    \end{tabular}
    \end{table}

    \begin{table}[]
    \begin{tabular}{cccc}
    측정항목         & \multicolumn{2}{c}{하중증가 시 측정시간} & 하중감소 시 측정시간 \\
    하중           & 각 하중단계        & 0분, 약 2분        & 0분          \\
    변위, 말뚝두부 경사각 & 각 하중단계        & 0분, 약 2분        & 0분          \\
    그 외1)        & 각 하중단계        & 0분              & 0분
    \end{tabular}
    \end{table}
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 횡방향 재하시험 측정간격];
    B["KCS 11 50 40 2.5.11 (1)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 40 2.5.11 (1)"])

    subgraph Variable_def
    VarOut[/출력변수: 측정간격/];
    VarIn1[/입력변수: 반복재하방법/];
    VarIn2[/입력변수: 1방향 재하방법/];
    VarIn3[/입력변수: 하중증가 시 측정시간/];
    VarIn4[/입력변수: 하중감소 시 측정시간/];
    VarIn5[/입력변수: 처녀하중/];
    VarIn6[/입력변수: 이력내 하중/];
    VarIn7[/입력변수: 0하중/];
    VarIn8[/입력변수: 측정항목/];
    VarOut  ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4 & VarIn5
    VarIn3  ~~~ VarIn6 & VarIn7 & VarIn8
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"반복재하방법 \n 1방향 재하방법"}
    C --> |1방향 재하방법|D{"측정항목"}
    D --> |하중|E{하중증가 시 측정시간\n 하중감소 시 측정시간}
    E --> |하중증가시|F{처녀하중 \n 이력 내 하중 \n 0하중}
    F --> |"처녀하중 \n 이력 내 하중"|G[0분, 약 2분]
    F --> |"0 하중"|H[0, 2, 4, 8, 약 14분]
    E --> |하중감소시|I[0분]
    D --> |변위 \n 말뚝두부 경사각|J{하중증가 시 측정시간\n 하중감소 시 측정시간}
    J --> |하중증가시|K{처녀하중 \n 이력 내 하중 \n 0하중}
    K --> |"처녀하중 \n 이력 내 하중"|L[0분, 약 2분]
    K --> |"0 하중"|M[0, 2, 4, 8, 약 14분]
    J --> |하중감소시|N[0분]
    D --> |그 외|EE{하중증가 시 측정시간\n 하중감소 시 측정시간}
    EE --> |하중증가시|FF{처녀하중 \n 이력 내 하중 \n 0하중}
    FF --> |"처녀하중 \n 이력 내 하중"|GG[0분]
    FF --> |"0 하중"|HH[0, 8, 약 14분]
    EE --> |하중감소시|II[0분]
    C --> |반복재하방법|O{"측정항목"}
    O --> |하중, 변위, \n 말뚝두부 경사각|P{하중증가 시 측정시간\n 하중감소 시 측정시간}
    P --> |하중증가 시 측정시간|Q[0분, 약 2분]
    P --> |하중감소 시 측정시간|R[0분]
    O --> |그 외|S[0분]
    G & H & I & L & M & N & Q & R & GG & HH & II & S--> End([횡방향 재하시험 측정간격])
    """

    @rule_method
    def measurement_interval(bICycLoa, bIOneLoa, bIIncLoa ,bIDecLoa, bIVirLoa, bILoaHIs, bIZerLoa, sIMeaIte):
        """
        Args:
            bICycLoa (boolean): 반복재하방법
            bIOneLoa (boolean): 1방향 재하방법
            bIIncLoa (boolean): 하중증가 시 측정시간
            bIDecLoa (boolean): 하중감소 시 측정시간
            bIVirLoa (boolean): 처녀하중
            bILoaHIs (boolean): 이력내 하중
            bIZerLoa (boolean): 0하중
            sIMeaIte (string): 측정항목

        Returns:
            sOMeaInt (sting): 측정간격
        """
        if bIOneLoa:
            if sIMeaIte == "하중" or "변위" or "말뚝두부 경사각":
                if bIIncLoa:
                    if bIVirLoa or bILoaHIs:
                       sOMeaInt = "0분, 약 2분"
                    if bIZerLoa:
                        sOMeaInt = "0, 2, 4, 8, 약 14분"
                elif bIDecLoa:
                    sOMeaInt = "0 분"
            if sIMeaIte == "그 외":
                if bIIncLoa:
                    if bIVirLoa or bILoaHIs:
                       sOMeaInt = "0분"
                    elif bIZerLoa:
                        sOMeaInt = "0, 8, 약 14분"
                elif bIDecLoa:
                    sOMeaInt = "0 분"
        elif bICycLoa:
            if bIIncLoa:
                if sIMeaIte == "하중" or "변위" or "말뚝두부 경사각":
                    sOMeaInt = "0분, 약 2분"
                elif sIMeaIte == "그 외":
                    sOMeaInt = "0분"
            elif bIDecLoa:
                sOMeaInt = "0분"
        return sOMeaInt