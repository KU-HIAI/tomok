import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142011_030101_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 20 11 3.1.1 (4)'
    ref_date = '2022-01-11'
    doc_date = '2024-05-17'
    title = '철근가공의 허용오차'

    description = """
    철근공사
    3. 시공
    3.1 철근
    3.1.1 철근의 가공
    (4)
    """
    content = """
    #### 3.1.1 철근의 가공
    (4) 철근가공의 허용오차는 표 3.1-1에 따른다.
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
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{"철근의 종류"}
    D --> |"스터럽, 띠철근, 나선철근"|H["허용오차 = ±5"]
    D --> |"D25 이하의 이형철근"|E["허용오차 = ±15"]
    D --> |"D29 이상 D32 이하의 이형철근"|F["허용오차 = ±20"]
    D --> |"가공 후의 전 길이"|G["허용오차 = ±20"]
    H & E & F & G --> End(["철근가공의 허용오차"])
    """

    @rule_method
    def tolerance_reinforcement(sIReiTyp)-> RuleUnitResult:
        """
        Args:
            sIReiTyp (str): 철근의 종류

        Returns:
            sOTolRei (str): 철근가공의 허용오차
        """
        assert isinstance(sIReiTyp, str)
        assert sIReiTyp in ["스터럽", "띠철근","나선철근", "D25 이하의 이형철근","D29 이상 D32 이하의 이형철근","가공 후의 전 길이"]

        if sIReiTyp == "스터럽" or sIReiTyp == "띠철근" or sIReiTyp == "나선철근":
            sOTolRei = "±5 mm"
        elif sIReiTyp == "D25 이하의 이형철근":
            sOTolRei = "±15 mm"
        elif sIReiTyp == "D29 이상 D32 이하의 이형철근":
            sOTolRei = "±20 mm"
        elif sIReiTyp == "가공 후의 전 길이":
            sOTolRei = "±20 mm"
        return RuleUnitResult(
            result_variables = {
                "sOTolRei": sOTolRei,
                })