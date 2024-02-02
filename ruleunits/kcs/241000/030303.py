import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS241000_030303(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 10 00 3.3.3'
    ref_date = '2018-08-30'
    doc_date = '2023-09-25'
    title = '부재치수의 시공 허용오차'

    # 건설기준문서항목 (분류체계정보)
    description = """
    콘크리트교량공사
    3. 시공
    3.3 가설 및 시공 허용오차
    3.3.3 부재치수의 시공 허용오차
    """

    # 건설기준문서내용(text)
    content = """
    #### 부재치수의 시공 허용오차는 표 3.3-3의 값을 표준으로 한다.
    \begin{table}[]
    \begin{tabular}{ll}
    항목           & 시공허용오차                                              \\
    수직부재의 길이치수   & {\color[HTML]{333333} 설계치수의 ±1% 또는 ±30 mm 중에서 작은 값} \\
    수평부재의 길이치수   & {\color[HTML]{333333} 설계치수의 ±1% 또는 ±30 mm 중에서 작은 값} \\
    기둥 및 보의 단면치수 & {\color[HTML]{333333} 설계치수의 ±2% 또는 ±20 mm 중에서 작은 값} \\
    바닥판의 두께      & {\color[HTML]{333333} +20 mm ~ -10 mm}
    \end{tabular}
    \end{table}
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 부재치수의 시공 허용오차];
    B["KCS 24 10 00 3.3.3"];
    B ~~~ A
    end

    KCS(["KCS 24 10 00 3.3.3"])

    subgraph Variable_def
    VarOut[/출력변수: 부재치수의 시공 허용오차/];
    VarIn0[/입력변수: 항목/]
    VarIn1[/입력변수: 수직부재의 설계치수/];
    VarIn2[/입력변수: 수평부재의 설계치수/];
    VarIn3[/입력변수: 기둥의 설계치수/];
    VarIn4[/입력변수: 보의 설계치수/]
    VarOut ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{항목}
    C --> |수직부재의 길이치수|D["부재치수의 시공 허용오차 \n = min(수직부재의 설계치수*±0.01, ±30 mm)"]
    C --> |수평부재의 길이치수|E["부재치수의 시공 허용오차 \n = min(수평부재의 설계치수*±0.01, ±30 mm)"]
    C --> |기둥 및 보의 단면치수|F["부재치수의 시공 허용오차 \n = min(기둥의 설계치수*±0.02, ±20 mm) \n 부재치수의 시공 허용오차 \n = min(보의 설계치수*0.02, ±20 mm) \n."]
    C --> |바닥판의 두께|H["부재치수의 시공 허용오차 \n = +20 mm ~ -10 mm"]
    D & E & F & H --> I([부재치수의 시공 허용오차])
    """

    @rule_method
    def tolerance_member_dimension(sIIte, fIDimVer, fIDimHor, fIDimCol, fIDimWei) -> str:
        """
        Args:
            sIIte (string): 항목
            fIDimVer (float): 수직부재의 설계치수
            fIDimHor (float): 수평부재의 설계치수
            fIDimCol (float): 기둥의 설계치수
            fIDimWei (float): 보의 설계치수
        Returns:
            sOTolDim (string): 부재치수의 시공 허용오차
        """
        if sIIte == "수직부재의 길이치수":
            sOTolDim = "±" + str(round(min(fIDimVer*0.01, 30), 5)) + " mm"
        elif sIIte =="수평부재의 길이치수":
            sOTolDim = "±" + str(round(min(fIDimHor*0.01, 30), 5)) + " mm"
        elif sIIte =="기둥의 단면치수":
            sOTolDim = "±" + str(round(min(fIDimCol*0.02, 20), 5)) + " mm"
        elif sIIte =="보의 단면치수":
            sOTolDim = "±" + str(round(min(fIDimWei*0.02, 20), 5)) + " mm"
        elif sIIte == "바닥판의 두께":
            sOTolDim =  "+20 mm ~ -10 mm"
        return sOTolDim