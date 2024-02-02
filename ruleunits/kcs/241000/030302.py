import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS241000_030302(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 10 00 3.3.2'
    ref_date = '2018-08-30'
    doc_date = '2023-09-25'
    title = '프리스트레싱 강재 배치의 시공 허용오차'

    # 건설기준문서항목 (분류체계정보)
    description = """
    콘크리트교량공사
    3. 시공
    3.3 가설 및 시공 허용오차
    3.3.2 프리스트레싱 강재 배치의 시공 허용오차
    """

    # 건설기준문서내용(text)
    content = """
    #### 프리스트레싱 강재 배치에 관한 시공 허용오차는 표 3.3-2의 값으로 하여야 한다.
    \begin{table}[]
    \begin{tabular}{lll}
    \multicolumn{2}{l}{항목}                                                   & 시공허용오차                                                                     \\
                                            & 주요한 설계단면의 양측 ℓ/10의 범위 (ℓ:지간) & {\color[HTML]{000000} 설계치수의 ±5% 또는 ±5mm 중에서 작은 값}                          \\
    \multirow{-2}{*}{프리스트레싱 강재 중심과 부재연단과의 거리} & 기타의 범위                       & {\color[HTML]{000000} 설계치수의 ±5% 또는 ±30mm 중에서 작은 값. 다만, 최소 피복두께는 확보하여야 한다.} \\
    \multicolumn{3}{l}{주 1) 주요한 설계단면이란 단면력이 크고, 지간 중앙부근, 지점상 부근 등의 위치의 단면을 말한다.}
    \end{tabular}
    \end{table}}
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 프리스트레싱 강재 배치의 시공 허용오차];
    B["KCS 24 10 00 3.3.2"];
    B ~~~ A
    end

    KCS(["KCS 24 10 00 3.3.2"])

    subgraph Variable_def
    VarOut[/출력변수: 프리스트레싱 강재 배치의 시공 허용오차/];
    VarIn1[/입력변수: 프리스트레싱 강재 중심과 부재연단과의 거리 설계치수/];
    VarIn2[/입력변수: 최소 피복두께/];
    VarIn3[/"입력변수: 주요한 설계단면의 양측 ℓ/10의 범위 (ℓ:지간)"/]
    VarOut ~~~ VarIn1 & VarIn2  ~~~  VarIn3
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"주요한 설계단면의 양측 ℓ/10의 범위 (ℓ:지간)"}
    C --> |False|D["min(프리스트레싱 강재 중심과 부재연단과의 거리 설계치수*±0.05, ±30)"]
    C --> |True|E["min(프리스트레싱 강재 중심과 부재연단과의 거리 설계치수*±0.05, ±5)"]
    D --> F([철프리스트레싱 강재 배치의 시공 허용오차])
    E --> F([프리스트레싱 강재 배치의 시공 허용오차])
    """

    @rule_method
    def tolerance_prestressing_layout(fIDisPre, fIMinCle, bIBotSid) -> str:
        """
        Args:
            fIDisPre (float): 프리스트레싱 강재 중심과 부재연단과의 거리 설계치수
            fIMinCle (float): 최소 피복두께
            bIBotSid (boolean): 주요한 설계단면의 양측 ℓ/10의 범위 (ℓ:지간)
        Returns:
            sOTolLay (string): 프리스트레싱 강재 배치의 시공 허용오차
        """
        if bIBotSid == True:
            sOTolLay =  "±" + str(round(min(fIDisPre*0.05, 5), 5)) + " mm"
        else:
            sOTolLay =  "±" +  str(round(max(min(fIDisPre*0.05, 30), fIMinCle), 5)) + " mm"
        return sOTolLay