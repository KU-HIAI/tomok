import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS115040_020116_01(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 11 50 40 2.1.16 (1)'
    ref_date = '2021-05-12'
    doc_date = '2023-09-15'
    title = '단계재하방식에 의한 재하방법'

    # 건설기준문서항목 (분류체계정보)
    description = """
    말뚝재하시험
    2. 시험
    2.1 압축 정재하시험
    2.1.16 재하방법
    (1)
    """

    # 건설기준문서내용(text)
    content = """
        ####(1) 단계재하방식의 경우 하중단계수, 사이클 수, 재하속도 및 하중유지시간은 표 2.1-1을 따른다.
        표 2.1-1 단계재하방식에 의한 재하방법

        \begin{table}[]
        \begin{tabular}{ccc}
        \hline
        하중단계수                                                 & \multicolumn{2}{c}{8단계 이상}                                            \\ \hline
        \multicolumn{1}{|c|}{사이클 수}                           & \multicolumn{2}{c|}{1사이클 혹은 4사이클 이상}                                  \\ \hline
        \multicolumn{1}{|c|}{\multirow{2}{*}{재하속도}}           & \multicolumn{2}{c|}{하중증가 시: (계획최대하중/하중단계수)/min}                       \\ \cline{2-3}
        \multicolumn{1}{|c|}{}                                & \multicolumn{2}{c|}{하중감소 시 : 하중 증가 시의 2배 정도}                          \\ \hline
        \multicolumn{1}{|c|}{\multirow{3}{*}{각 하중단계의 하중유지시간}} & \multicolumn{1}{c|}{신규하중단계}    & \multicolumn{1}{c|}{30 min 이상의 일정시간} \\ \cline{2-3}
        \multicolumn{1}{|c|}{}                                & \multicolumn{1}{c|}{이력 내 하중단계} & \multicolumn{1}{c|}{2 min 이상의 일정시간} \\ \cline{2-3}
        \multicolumn{1}{|c|}{}                                & 0하중단계                          & 15 min 이상의 일정시간                      \\ \hline
        \end{tabular}
        \end{table}

    """

    # 플로우차트(mermaid)
    flowchart = """
        flowchart TD
        subgraph Python_Class
        A[Title: 단계재하방식에 의한 재하방법];
        B["KCS 11 50 40 2.1.16 (1)"];
        B ~~~ A
        end

        KCS(["KCS 11 50 40 2.1.16 (1)"])

        subgraph Variable_def
        VarOut[/출력변수: 단계재하방식에 의한 재하방법/];
        VarIn1[/입력변수: 하중단계수/];
        VarIn2[/입력변수: 사이클 수/];
        VarIn3[/입력변수: 재하속도/];
        VarIn4[/입력변수: 하중증가 시/];
        VarIn5[/입력변수: 계획최대하중/];
        VarIn6[/입력변수: 하중단계수/];
        VarIn7[/입력변수: 하중감소 시/];
        VarIn8[/입력변수: 하중유지시간/];
        VarIn9[/입력변수: 신규하중단계/];
        VarIn10[/입력변수: 이력 내 하중단계/];
        VarIn11[/입력변수: 0하중단계/];
        VarOut ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4 & VarIn5
        VarIn3 ~~~ VarIn6 & VarIn7 & VarIn8 & VarIn9 & VarIn10
        end

        Python_Class ~~~ KCS
        KCS --> Variable_def
        Variable_def --> C{"하중단계수 \n 사이클 수 \n 재하속도 \n 하중유지시간"}
        C --> |하중단계수|D["8단계 이상"]
        C --> |사이클 수|E["1사이클 혹은 4사이클 이상"]
        C --> |재하속도|F{"하중증가 시 \n 하중감소 시"}
        F --> |하중증가 시|G["계획최대하중/하중단계수/min"]
        F --> |하중감소 시|H["하중 증가 시의 2배 정도"]
        C --> |하중유지시간|I{"신규하중단계 \n 이력 내 하중단계 \n 0하중단계"}
        I --> |신규하중단계|J[30 min 이상의 일정시간]
        I --> |이력 내 하중단계|K[2 min 이상의 일정시간]
        I --> |0하중단계|L[15 min 이상의 일정시간]
        D & E & G & H & J & K & L --> End([말뚝의 허용오차])
    """

    @rule_method
    def incremental_loading(bINumLoa, bINumCyc,bILoaSpe, bIIncLoa,fIDesLoa, nINumLoa, bIDecLoa, bILoaTim, bINewLoa, bILoaHIs, bIZerLoa):
        """
        Args:
            bINumLoa (boolean): 하중단계수
            bINumCyc (boolean): 사이클 수
            bILoaSpe (boolean): 재하속도
            bIIncLoa (boolean): 하중증가 시
            fIDesLoa (float): 계획최대하중
            nINumLoa (integar): 하중단계수
            bIDecLoa (boolean): 하중감소 시
            bILoaTim (boolean): 하중유지시간
            bINewLoa (boolean): 신규하중단계
            bILoaHIs (boolean): 이력 내 하중단계
            bIZerLoa (boolean): 0하중단계
        Returns:
            sOIncLoa (string): 단계재하방식에 의한 재하방법
        """
        if bINumLoa:
            sOIncLoa = "8단계 이상"
        elif bINumCyc:
            sOIncLoa = "1사이클 혹은 4사이클 이상"
        elif bILoaSpe:
            if bIIncLoa:
                sOIncLoa = str(fIDesLoa/nINumLoa)+" kN/min"
            elif bIDecLoa:
                sOIncLoa = str(2*fIDesLoa/nINumLoa)+" kN/min 정도"
        elif bILoaTim:
            if bINewLoa:
                sOIncLoa = "30 min 이상의 일정시간"
            if bILoaHIs:
                sOIncLoa = "2 min 이상의 일정시간"
            if bIZerLoa:
                sOIncLoa = "15 min 이상의 일정시간"
        return sOIncLoa