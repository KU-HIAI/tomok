import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS115040_020116_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 11 50 40 2.1.16 (1)'
    ref_date = '2021-05-12'
    doc_date = '2023-09-15'
    title = '단계재하방식에 의한 재하방법'

    description = """
    말뚝재하시험
    2. 시험
    2.1 압축 정재하시험
    2.1.16 재하방법
    (1)
    """
    content = """
    ####2.1.16 재하방법
    (1) 단계재하방식의 경우 하중단계수, 사이클 수, 재하속도 및 하중유지시간은 표 2.1-1을 따른다.
    표 2.1-1 단계재하방식에 의한 재하방법
    \begin{tabular}{|c|c|c|}
    \hline 하중단계수 & \multicolumn{2}{|c|}{ 8단계 이상 } \\
    \hline 사이클 수 & \multicolumn{2}{|c|}{ 1사이클 혹은 4사이클 이상 } \\
    \hline \multirow{2}{*}{ 재하속도 } & \multicolumn{2}{|c|}{ 하중증가 시 : $\frac{\text { 계획최대하중 }}{\text { 하중단계수 }} / \mathrm{min}$} \\
    \hline & \multicolumn{2}{|c|}{ 하중감소 시 : 하중 증가 시의 2배 정도 } \\
    \hline \multirow{3}{*}{\begin{tabular}{l}
    각 하중단계의 \\
    하중유지시간
    \end{tabular}} & 신규하중단계 & $30 \mathrm{~min}$ 이상의 일정시간 \\
    \hline & 이력 내 하중단계 & $20 \mathrm{~min}$ 이상의 일정시간 \\
    \hline & 0 하중단계 & $15 \mathrm{~min}$ 이상의 일정시간 \\
    \hline
    \end{tabular}
    """
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
    D & E & G & H & J & K & L --> End([단계재하방식에 의한 재하방법])
    """

    @rule_method
    def incremental_loading(bINumLoa, bINumCyc,bILoaSpe,bILoaTim, bIIncLoa,bIDecLoa, fIDesLoa, nINumLoa, bINewLoa, bILoaHIs, bIZerLoa)-> RuleUnitResult:
        """
        Args:
            bINumLoa (bool): 하중단계수
            bINumCyc (bool): 사이클 수
            bILoaSpe (bool): 재하속도
            bILoaTim (bool): 하중유지시간
            bIIncLoa (bool): 하중증가 시
            bIDecLoa (bool): 하중감소 시
            fIDesLoa (float): 계획최대하중
            nINumLoa (int): 하중단계수
            bINewLoa (bool): 신규하중단계
            bILoaHIs (bool): 이력 내 하중단계
            bIZerLoa (bool): 0하중단계

        Returns:
            sOIncLoa (str): 단계재하방식에 의한 재하방법
        """
        assert isinstance(bINumLoa, bool)
        assert isinstance(bINumCyc, bool)
        assert isinstance(bILoaSpe, bool)
        assert isinstance(bIIncLoa, bool)
        assert isinstance(fIDesLoa, float)
        assert isinstance(nINumLoa, int)
        assert isinstance(bIDecLoa, bool)
        assert isinstance(bILoaTim, bool)
        assert isinstance(bINewLoa, bool)
        assert isinstance(bILoaHIs, bool)
        assert isinstance(bIZerLoa, bool)
        assert (bINumLoa+bINumCyc+bILoaSpe+bILoaTim) ==1
        assert bIIncLoa != bIDecLoa
        assert (bINewLoa+bILoaHIs+bIZerLoa) ==1

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
        return RuleUnitResult(
            result_variables = {
                "sOIncLoa": sOIncLoa,})