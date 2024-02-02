import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS142012_030301_04(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 14 20 12 3.3.1 (4)'
    ref_date = '2022-09-01'
    doc_date = '2023-09-26'
    title = '슬래브 및 보의 밑면, 아치 내면의 거푸집널 해체 시기'

    # 건설기준문서항목 (분류체계정보)
    description = """
    거푸집 및 동바리
    3. 시공
    3.3 거푸집 및 동바리의 해체
    3.3.1 거푸집 및 동바리의 해체
    (4)
    """

    # 건설기준문서내용(text)
    content = """
    ####(4) 슬래브 및 보의 밑면, 아치 내면의 거푸집은 콘크리트의 압축강도가 표 3.3-1을 만족할 때 해체할 수 있다.

    표 3.3-1 콘크리트의 압축강도를 시험할 경우 거푸집널의 해체 시기
    \begin{table}[]
    \begin{tabular}{lll}
    \multicolumn{2}{l}{부재}                                                                   & 콘크리트 압축강도($$f_{ck}$$)                                                                                                            \\
    \multicolumn{2}{l}{\begin{tabular}[c]{@{}l@{}}기초, 보, 기둥, 벽\\ 등의 측면\end{tabular}}         & 5 MPa이상1)                                                                                                                        \\
    \multirow{2}{*}{\begin{tabular}[c]{@{}l@{}}슬래브 및 보의 밑면,\\ 아치 내면\end{tabular}} & 단층구조인 경우 & \begin{tabular}[c]{@{}l@{}}설계기준압축강도의 2/3배 이상\\ 또한, 최소강도 14MPa 이상\end{tabular}                                                    \\
                                                                                & 다층구조인 경우 & \begin{tabular}[c]{@{}l@{}}설계기준 압축강도 이상\\ (필러 동바리 구조를 이용할 경우는 구조계산에 의해 기간을 단축할 수 있음. 단, 이 경우라도 최소강도는 14 MPa 이상으로 함)\end{tabular} \\
    \multicolumn{3}{l}{주 1) 내구성이 중요한 구조물의 경우 10MPa 이상}
    \end{tabular}
    \end{table}

    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 슬래브 및 보의 밑면, 아치 내면의 거푸집널 해체 시기];
    B["KCS 14 20 12 3.3.1 (4)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 12 3.3.1 (4)"])

    subgraph Variable_def
    VarOut1[/출력변수: 슬래브 및 보의 밑면, 아치 내면의 거푸집널 해체 시기/];
    VarIn1[/입력변수: 설계기준 압축강도/];
    VarIn2[/입력변수: 단층구조/];
    VarIn3[/입력변수: 다층구조/];
    VarIn4[/입력변수: 필터 동바리 구조/];
    end
    VarOut1 ~~~  VarIn1 & VarIn2 & VarIn3 & VarIn4

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> E{"단층구조\n다층구조"}
    E --> |단층구조|C["max(설계기준압축강도*2/3, 14MPa) 이상"]
    E --> |다층구조|G{필러 동바리 구조}
    G --> |False|H["설계기준압축강도 이상"]
    G --> |"True"|I["구조계산에 의해 기간을 단축할 수 있음 \n 단, 이 경우라도 최소강도는 14 MPa 이상"]
    C & H & I --> End([슬래브 및 보의 밑면, 아치 내면의 거푸집널 해체 시기])
    """

    @rule_method
    def dismantling_sheathing(bIFauStr,bIMulStr,bIFilSho,fIfck) -> str:
        """
        Args:
            bIFauStr (boolean): 단층구조
            bIMulStr (boolean): 다층구조
            bIFilSho (boolean): 필러 동바리 구조
            fIfck (float): 설계기준 압축강도
        Returns:
            sODisShe (string)): 슬래브 및 보의 밑면, 아치 내면의 거푸집널 해체 시기
        """
        if bIFauStr:
            sODisShe = "콘크리트 압축강도가 "+str(round(max(fIfck*2/3,14),5)) +"MPa 를 만족할 때"
        elif bIMulStr:
            if bIFilSho:
                sODisShe = "구조계산에 의해 기간을 단축할 수 있음. 단, 최소강도 14 MPa 이상"
            else:
                sODisShe = "콘크리트 압축강도가 "+str(round(max(fIfck,14),5)) +"MPa 를 만족할 때"
        return sODisShe