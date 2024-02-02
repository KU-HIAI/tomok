import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244020_0201(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 40 20 2.1 '
    ref_date = '2016-06-30'
    doc_date = '2023-10-12'
    title = '환경요구사항'

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량방수
    2. 자재
    2.1 흡수방지식 방수재
    """

    # 건설기준문서내용(text)
    content = """
    #### 2.1 흡수방지식 방수재
    흡수방지식 방수재의 품질기준은 다음 표 2.1-1과 같다.
    \begin{table}[]
    \begin{tabular}{cccc}
    \multicolumn{2}{l}{시험항목}                   & \multicolumn{1}{l}{시험방법}   & \multicolumn{1}{l}{규격값}        \\
    \multicolumn{2}{c}{침투 깊이 (㎜)}              & KS F 4930                  & 4 이상                           \\
    \multicolumn{2}{c}{염화물 이온 침투성 (㎜)}         & KS F 4930                  & 3 이하                           \\
    \multicolumn{2}{c}{내 산 성}                  & KS F 4930                  & 이상무                            \\
    \multirow{4}{*}{흡수성} & 표준                  & \multirow{4}{*}{KS F 4930} & \multirow{3}{*}{물흡수계수비 0.1 이하} \\
                        & 내알칼리성 시험 후          &                            &                                \\
                        & 온⋅냉 반복에 대한 저항성 시험 후 &                            &                                \\
                        & 촉진 내후성 시험 후         &                            & 물흡수계수비 0.2 이하                  \\
    \multicolumn{2}{c}{투수비 (%)}                & KS F 4930                  & 0.1 이하
    \end{tabular}
    \end{table}
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 흡수방지식 방수재의 품질기준];
    B["KCS 24 40 20 2.1"];
    B ~~~ A
    end

    KCS(["KCS 24 40 20 2.1"])

    subgraph Variable_def
    VarOut[/출력변수: 흡수방지식 방수재의 품질기준/];
    VarIn1[/입력변수: 시험항목/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{시험항목}
    C --> |"표 2.1-1"|End([흡수방지식 방수재의 품질기준])
    """

    @rule_method
    def quality_absorbent_waterproof(sITesIte)->str:
        """
        Args:
            sITesIte (string): 시험항목
        Returns:
            sOQuaMat (string): 흡수방지식 방수재의 품질기준
        """
        if sITesIte == "침투 깊이":
            sOQuaMat = "4 mm 이상"
        elif sITesIte == "염화물 이온 침투성":
            sOQuaMat = "3 mm 이하"
        elif sITesIte == "내산성":
            sOQuaMat = "이상무"
        elif sITesIte =="표준 흡수성" or "내알칼리성 시험 후 흡수성" or "온⋅냉 반복에 대한 저항성 시험 후 흡수성":
            sOQuaMat = "물흡수계수비 0.1 이하"
        elif sITesIte ==" 촉진 내후성 시험 후 흡수성":
            sOQuaMat = "물흡수계수비 0.2 이하"
        elif sITesIte =="투수비":
            sOQuaMAt = "0.1 이하"
        return sOQuaMat