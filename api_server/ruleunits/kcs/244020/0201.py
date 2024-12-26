import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244020_0201(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 20 2.1 '
    ref_date = '2016-06-30'
    doc_date = '2023-10-12'
    title = '흡수방지식 방수재의 품질기준'

    description = """
    교량배수시설공
    2. 자재
    2.1 흡수방지식 방수재
    """
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

    def quality_absorbent_waterproof(sITesIte) -> RuleUnitResult:
        """
        Args:
            sITesIte (str): 시험항목

        Returns:
            sOQuaMat (str): 흡수방지식 방수재의 품질기준
        """
        assert isinstance(sITesIte, str)
        assert sITesIte in ["침투 깊이","염화물 이온 침투성","내산성","표준 흡수성", "내알칼리성 시험 후 흡수성", "온⋅냉 반복에 대한 저항성 시험 후 흡수성"," 촉진 내후성 시험 후 흡수성","투수비"]

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
            sOQuaMat = "0.1 이하"

        return RuleUnitResult(
            result_variables = {
                "sOQuaMat": sOQuaMat,
                })