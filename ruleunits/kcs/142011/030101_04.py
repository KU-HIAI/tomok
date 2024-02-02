import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS142011_030101_04(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 14 20 11 3.1.1 (4)'
    ref_date = '2022-01-11'
    doc_date = '2023-09-19'
    title = '횡방향 재하시험 재하장치'

    # 건설기준문서항목 (분류체계정보)
    description = """
    철근공사
    3. 시공
    3.1 철근
    3.1.1 철근의 가공
    (4)
    """

    # 건설기준문서내용(text)
    content = """
    ####(4) 철근가공의 허용오차는 표 3.1-1에 따른다.
        \begin{table}[]
        \begin{tabular}{lllll}
        \multicolumn{2}{l}{철근의 종류}                     & 부호(오른쪽 그림) & 허용오차 (mm) & \multirow{5}{*}{\includegraphics{<img src='http://drive.google.com/uc?export=view&id=1hFRW11p-DGoy2Y1mCO9IsVmELhpdHbHu_link' /><br>}} \\
        \multicolumn{2}{l}{스터럽, 띠철근, 나선철근}             & a, b       & ±5        &                   \\
        \multirow{2}{*}{그 밖의 철근} & D25 이하의 이형철근        & a, b       & ±15       &                   \\
                                & D29 이상 D32 이하의 이형철근 & a, b       & ±20       &                   \\
        \multicolumn{2}{l}{가공 후의 전 길이}                 & L          & ±20       &
        \end{tabular}
        \end{table}
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 철근가공의 허용오차];
    B["KCS 14 20 11 3.1.1 (4)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 11 3.1.1 (4)"])

    subgraph Variable_def
    VarOut[/출력변수: 철근가공의 허용오차/];
    VarIn1[/입력변수: 철근의 종류/];
    VarIn2[/입력변수: 부호/];
    VarIn3[/입력변수: 허용오차/];

    VarOut ~~~ VarIn1 & VarIn2 & VarIn3
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"부호 \n 허용오차"}
    C --> |허용오차|D{"철근의 종류"}
    D --> |"스터럽, 띠철근, 나선철근"|H["허용오차 = ±5"]
    D --> |"D25 이하의 이형철근"|E["허용오차 = ±15"]
    D --> |"D29 이상 D32 이하의 이형철근"|F["허용오차 = ±20"]
    D --> |"가공 후의 전 길이"|G["허용오차 = ±20"]
    C --> |부호|I{"철근의 종류"}
    I --> |"스터럽, 띠철근, 나선철근 \n D25 이하의 이형철근 \n D29 이상 D32 이하의 이형철근 \n."|J["a, b"]
    I --> |"가공 후의 전 길이"|K["L"]
    H & E & F & G & J & K --> End(["철근가공의 허용오차"])
    """

    @rule_method
    def tolerance_reinforcement(sIReiTyp,bISig,bITol):
        """
        Args:
            sIReiTyp (string): 철근의 종류
            bISig (boolean): 부호
            bITol (boolean): 허용오차
        Returns:
            sOTolRei (sting): 철근가공의 허용오차
        """
        if bISig:
            if sIReiTyp == "스터럽" or sIReiTyp == "띠철근" or sIReiTyp == "나선철근" or sIReiTyp =="D25 이하의 이형철근" or sIReiTyp =="D29 이상 D32 이하의 이형철근":
                sOTolRei = "a, b"
            elif sIReiTyp == "가공 후의 전 길이":
                sOTolRei = "L"
        elif bITol:
            if sIReiTyp == "스터럽" or sIReiTyp == "띠철근" or sIReiTyp == "나선철근":
                sOTolRei = "±5 mm"
            elif sIReiTyp == "D25 이하의 이형철근":
                sOTolRei = "±15 mm"
            elif sIReiTyp == "D29 이상 D32 이하의 이형철근":
                sOTolRei = "±20 mm"
            elif sIReiTyp == "가공 후의 전 길이":
                sOTolRei = "±20 mm"
        return sOTolRei