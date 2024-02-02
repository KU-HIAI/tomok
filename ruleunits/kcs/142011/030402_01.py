import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS142011_030402_01(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 14 20 11 3.4.2 (1)'
    ref_date = '2022-01-11'
    doc_date = '2023-09-19'
    title = '철근가공의 품질 검사'

    # 건설기준문서항목 (분류체계정보)
    description = """
    철근공사
    3. 시공
    3.4 현장 품질관리
    3.4.2 철근가공의 검사
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    ####(1) 철근가공의 품질 검사는 표 3.4-1에 따른다.
    \begin{table}[]
    \begin{tabular}{lllll}
    \multicolumn{2}{l}{항목}                     & 시험·검사 방법                            & 시기·횟수                                   & 판정기준                                                                                       \\
    \multicolumn{2}{l}{철근의 가공치수}               & 자 등에 의한 측정                          & \multirow{6}{*}{조립 후 및 조립 후 장기간 경과한 경우} & 표 3.1-1의 허용오차 이내                                                                           \\
    \multicolumn{2}{l}{간격재의 종류, 배치, 수량}        & 육안 관찰                               &                                         & 철근의 피복이 바르게 확보되도록 적절히 배치되어 있을 것                                                            \\
    \multicolumn{2}{l}{철근의 고정방법}               & 육안 관찰                               &                                         & 콘크리트를 타설할 때 변형, 이동의 우려가 없을 것                                                               \\
    \multirow{3}{*}{조립된 철근의 배치} & 이음 및 정착 위치   & \multirow{3}{*}{자 등에 의한 측정 및 육안 관찰} &                                         & 철근가공 조립도와 일치할 것                                                                            \\
                                & 콘크리트 최소피복 두께 &                                     &                                         & \begin{tabular}[c]{@{}l@{}}허용오차:\\ d≤200 mm인 경우 -10 mm,\\ d>200 mm인 경우 -13 mm\end{tabular} \\
                                & 유효깊이         &                                     &                                         & \begin{tabular}[c]{@{}l@{}}허용오차:\\ d≤200 mm인 경우 ±10 mm,\\ d>200 mm인 경우 ±13 mm\end{tabular}  \\
    \multicolumn{5}{l}{주 1) 다만, 하단 거푸집까지의 순거리에 대한 허용오차는 -7 mm이며, 피복두께의 허용오차는 도면 또는 설계기준에서 요구하는 최소 피복두께의 -1/3으로 하여야 한다.}
    \end{tabular}
    \end{table}
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 철근가공의 품질 검사];
    B["KCS 14 20 11 3.4.2 (1)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 11 3.4.2 (1)"])

    subgraph Variable_def
    VarOut[/출력변수:  철근가공의 품질 검사/];
    VarIn1[/입력변수: 검토항목/];
    VarIn2[/"입력변수: 시험·검사 방법"/];
    VarIn3[/"입력변수: 시기·횟수"/];
    VarIn4[/입력변수: 판정기준/];
    VarIn5[/입력변수: 철근 지름/];
    VarOut ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"검토항목\n시험·검사 방법\n시기·횟수\n판정기준\n철근 지름\n."}
    C --> |"표 3.4-1"|D["철근가공의 품질 검사"]
    D --> H(["철근가공의 품질 검사"])
    """

    @rule_method
    def quality_inspection(sIRevIte, bITesMet, bITesFre, bIJudCri, fID):
        """
        Args:
            sIRevIte (string): 검토항목
            bITesMet (boolean): 시험·검사 방법
            bITesFre (boolean): 시기·횟수
            bIJudCri (boolean): 판정기준
            fID (float): 철근 지름
        Returns:
            sOQuaIns (sting): 철근가공의 품질 검사
        """
        if sIRevIte == "철근의 가공치수":
            if bITesMet:
                sOQuaIns = "자 등에 의한 측정"
            elif bITesFre:
                sOQuaIns = "조립 후 및 조립 후 장기간 경과한 경우"
            elif bIJudCri:
                sOQuaIns = "표 3.1-1의 허용오차 이내"
        if sIRevIte == "간격재의 종류" or "간격재의 배치" or "간격재의 수량":
            if bITesMet:
                sOQuaIns = "육안 관찰"
            elif bITesFre:
                sOQuaIns = "조립 후 및 조립 후 장기간 경과한 경우"
            elif bIJudCri:
                sOQuaIns = "철근의 피복이 바르게 확보되도록 적절히 배치되어 있을 것"
        if sIRevIte == "철근의 고정방법":
            if bITesMet:
                sOQuaIns = "육안 관찰"
            elif bITesFre:
                sOQuaIns = "조립 후 및 조립 후 장기간 경과한 경우"
            elif bIJudCri:
                sOQuaIns = "콘크리트를 타설할 때 변형, 이동의 우려가 없을 것"
        if sIRevIte == "조립된 철근의 이음 및 정착 위치":
            if bITesMet:
                sOQuaIns = "자 등에 의한 측정 및 육안 관찰"
            elif bITesFre:
                sOQuaIns = "조립 후 및 조립 후 장기간 경과한 경우"
            elif bIJudCri:
                sOQuaIns = "철근가공 조립도와 일치할 것"
        if sIRevIte == "조립된 철근의 콘크리트 최소피복두께":
            if bITesMet:
                sOQuaIns = "자 등에 의한 측정 및 육안 관찰"
            elif bITesFre:
                sOQuaIns = "조립 후 및 조립 후 장기간 경과한 경우"
            elif bIJudCri:
                if fID <= 200:
                    sOQuaIns = "-10 mm"
                else:
                    sOQuaIns = "-13 mm"
        if sIRevIte == "조립된 철근의 유효깊이":
            if bITesMet:
                sOQuaIns = "자 등에 의한 측정 및 육안 관찰"
            elif bITesFre:
                sOQuaIns = "조립 후 및 조립 후 장기간 경과한 경우"
            elif bIJudCri:
                if fID <=200:
                    sOQuaIns = "±10 mm"
                else:
                    sOQuaIns = "±13 mm"
        return sOQuaIns