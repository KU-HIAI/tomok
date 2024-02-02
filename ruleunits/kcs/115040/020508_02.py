import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS115040_020508_02(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 11 50 40 2.5.8 (2)'
    ref_date = '2021-05-12'
    doc_date = '2023-09-18'
    title = '횡방향 재하시험 재하방법'

    # 건설기준문서항목 (분류체계정보)
    description = """
    말뚝재하시험
    2. 시험
    2.5 횡방향재하시험
    2.5.8 시험방법
    (2)
    """

    # 건설기준문서내용(text)
    content = """
    ####(2) 재하방법은 다음 사항을 고려하여 선정한다.
    ① 구조물의 종류, 외력의 종류 및 시험목적을 고려하여 재하방법을 결정한다.
    ② 재하방법으로 반복재하와 1방향재하가 있다.
    ③ 각각의 재하방법을 표 2.5-1과 표 2.5-2에 나타내었다.
    \begin{table}[]
    \begin{tabular}{ccc}
    항목     & 하중증가 시                & 하중감소 시                \\
    하중단계   & 8단계 이상                & 8단계 이상                \\
    하중속도   & (계획최대하중)/(5~20) (톤/분) & (계획최대하중)/(4~10) (톤/분) \\
    하중지속시간 & 각 하중 단계 3분            & 각 하중 단계 3분
    \end{tabular}
    \end{table}


    \begin{table}[]
    \begin{tabular}{cccc}
    항목                      & \multicolumn{2}{c}{하중증가 시} & 하중감소 시              \\
    \multirow{2}{*}{하중유지시간} & 처녀 하중, 이력 내 하중    & 3분     & \multirow{2}{*}{3분} \\
                            & 0 하중              & 15분    &
    \end{tabular}
    \end{table}
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 횡방향 재하시험 재하방법];
    B["KCS 11 50 40 2.5.8 (2)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 40 2.5.8 (2)"])

    subgraph Variable_def
    VarOut[/출력변수: 재하방법/];
    VarIn1[/입력변수: 반복재하방법/];
    VarIn2[/입력변수: 1방향 재하방법/];
    VarIn3[/입력변수: 하중증가 시/];
    VarIn4[/입력변수: 하중감소 시/];
    VarIn5[/입력변수: 하중단계/];
    VarIn6[/입력변수: 하중속도/];
    VarIn7[/입력변수: 하중지속시간/];
    VarIn8[/입력변수: 하중유지시간/];
    VarIn9[/입력변수: 계획최대하중/];
    VarIn10[/입력변수: 처녀하중/];
    VarIn11[/입력변수: 이력내 하중/];
    VarOut  ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4 & VarIn5
    VarIn3  ~~~ VarIn6 & VarIn7 & VarIn8 & VarIn9 & VarIn10 & VarIn11
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"반복재하방법 \n 1방향 재하방법"}
    C --> |반복재하방법|D{"하중단계\n 하중속도 \n 하중지속시간"}
    D --> |하중단계|E{하중증가시\n 하중감소시}
    E --> |하중증가시|F[8단계 이상]
    E --> |하중감소시|G[8단계 이상]
    D --> |하중속도|H{하중증가시\n 하중감소시}
    H --> |하중증가시|I["계획최대하중/20 ~ 계획최대하중/8"]
    H --> |하중감소시|J["계획최대하중/10 ~ 계획최대하중/4"]
    D --> |하중지속시간|K[각 하중 단계 3분]
    C --> |1방향 재하방법|L{"하중유지시간"}
    L --> |하중유지시간|M{하중증가시\n 하중감소시}
    M --> |하중증가시|N{"처녀하중 \n 이력 내 하중 \n 0하중"}
    N --> |"처녀하중 \n 이력 내 하중"|O[3분]
    N --> |"0 하중"|P[15분]
    M --> |"하중감소시"|Q[3분]
    F & G & I & J & K & O & P & Q --> End([횡방향 재하시험 재하방법])
    """

    @rule_method
    def loading_method(bICycLoa, bIOneLoa, bIIncLoa ,bIDecLoa,bILoaSte,bILoaSpe,bISusTim, bIMaiTim, fIDesLoa, bIVirLoa, bILoaHIs, bIZerLoa):
        """
        Args:
            bICycLoa (boolean): 반복재하방법
            bIOneLoa (boolean): 1방향 재하방법
            bIIncLoa (boolean): 하중증가 시
            bIDecLoa (boolean): 하중감소 시
            bILoaSte (boolean): 하중단계
            bILoaSpe (boolean): 하중속도
            bISusTim (boolean): 하중지속시간
            bIMaiTim (boolean): 하중유지시간
            fIDesLoa (float): 계획최대하중
            bIVirLoa (boolean): 처녀하중
            bILoaHIs (boolean): 이력내 하중
            bIZerLoa (boolean): 0하중

        Returns:
            sOLoaMet (sting): 재하방법
        """
        if bICycLoa:
            if bILoaSte:
                sOLoaMet = "8단계 이상"
            elif bILoaSpe:
                if bIIncLoa:
                    sOLoaMet = str(round(fIDesLoa/20,3)) + " ~ " + str(round(fIDesLoa/8,3)) +" 톤/분"
                elif bIDecLoa:
                    sOLoaMet = str(round(fIDesLoa/10,3)) + " ~ " + str(round(fIDesLoa/4,3)) +" 톤/분"
            elif bISusTim:
                sOLoaMet = "각 하중 단계 3분"
        elif bIOneLoa:
            if bIMaiTim:
                if bIIncLoa:
                    if bIVirLoa or bILoaHIs:
                        sOLoaMet = "3분"
                    elif bIZerLoa:
                        sOLoaMet = "15분"
                if bIDecLoa:
                    sOLoaMet = "3분"
        return sOLoaMet