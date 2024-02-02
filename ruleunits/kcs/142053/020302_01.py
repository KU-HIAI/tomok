import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS142053_020302_01(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 14 20 53 2.3.2 (1)'
    ref_date = '2022-01-11'
    doc_date = '2023-09-21'
    title = '그라우트의 품질 검사'

    # 건설기준문서항목 (분류체계정보)
    description = """
    프리스트레스트 콘크리트
    2. 자재
    2.3 재료 품질관리
    2.3.2 프리스트레스트 콘크리트용 그라우트의 품질 검사
    (7)
    """

    # 건설기준문서내용(text)
    content = """
    ####(1) 그라우트의 품질 검사는 표 2.3-2에 따른다.
    \begin{table}[]
    \begin{tabular}{llll}
    항목      & 시험 및 검사 방법 & 시기 및 횟수                                      & 판정기준                                                                           \\
    유동성     & KCI-PS102  & \multirow{5}{*}{주입 전, 1회/일 이상 및 품질변화가 인정될 때} & KCI-PS102의 기준 참조                                                               \\
    블리딩률    & KCI-PS102  &                                              & 3시간 경과 시 0.3 % 이하                                                              \\
    체적변화율   & KCI-PS102  &                                              & 24시간 경과 시 (–1 ∼ 5) %                                                           \\
    압축강도    & KCI-PS102  &                                              & \begin{tabular}[c]{@{}l@{}}재령 7일에서 27 MPa 이상\\ 재령 28일에서 30 MPa 이상\end{tabular} \\
    염화물 함유량 & KCI-PS102  &                                              & 단위 시멘트량의 0.08 % 이하(전 염화물 함유량)
    \end{tabular}
    \end{table}
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 그라우트의 품질검사];
    B["KCS 14 20 53 2.3.2 (1)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 53 2.3.2 (1)"])

    subgraph Variable_def
    VarOut[/출력변수: 그라우트의 품질 검사/];
    VarIn0[/입력변수: 항목/]
    VarIn1[/입력변수: 시험·검사 방법/];
    VarIn1[/입력변수: 시기·횟수/];
    VarIn2[/입력변수: 판정기준/]
    VarIn3[/입력변수: 단위 시멘트량/]
    VarOut ~~~ VarIn0 & VarIn1 &  VarIn2 & VarIn3
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"항목 \n 시험·검사 방법 \n 시기·횟수 \n 판정기준 \n 단위 시멘트량\n."}
    C --> |표2.3-2|End([프리스트레스트 콘크리트용 그라우트의 품질 검사])
    """


    @rule_method
    def quality_grout(sIItem, bITesMet, bITesFre, bIJudCri, fICemCon) -> str:
        """
        Args:
            sIItem (string): 항목
            bITesMet (boolean): 시험·검사 방법
            bITesFre (boolean): 시기·횟수
            bIJudCri (boolean): 판정기준
            fICemCon (float): 단위 시멘트량
        Returns:
            sOQuaIns (sting): 그라우트의 품질검사
        """
        if sIItem == "유동성":
            if bITesMet:
                sOQuaIns = "KCI-PS102"
            elif bITesFre:
                sOQuaIns = "주입 전, 1회/일 이상 및 품질변화가 인정될 때"
            elif bIJudCri:
                sOQuaIns = "KCI-PS102의 기준 참조"
        elif sIItem == "블리딩률":
            if bITesMet:
                sOQuaIns = "KCI-PS102"
            elif bITesFre:
                sOQuaIns = "주입 전, 1회/일 이상 및 품질변화가 인정될 때"
            elif bIJudCri:
                sOQuaIns = "3시간 경과 시 0.3 % 이하"
        elif sIItem == "체적변화율":
            if bITesMet:
                sOQuaIns = "KCI-PS102"
            elif bITesFre:
                sOQuaIns = "주입 전, 1회/일 이상 및 품질변화가 인정될 때"
            elif bIJudCri:
                sOQuaIns = "24시간 경과 시 (–1 ∼ 5) %"
        elif sIItem == "압축강도":
            if bITesMet:
                sOQuaIns = "KCI-PS102"
            elif bITesFre:
                sOQuaIns = "주입 전, 1회/일 이상 및 품질변화가 인정될 때"
            elif bIJudCri:
                sOQuaIns = "재령 7일에서 27 MPa 이상 \n 재령 28일에서 30 MPa 이상"
        elif sIItem == "염화물 함유량":
            if bITesMet:
                sOQuaIns = "KCI-PS102"
            elif bITesFre:
                sOQuaIns = "주입 전, 1회/일 이상 및 품질변화가 인정될 때"
            elif bIJudCri:
                sOQuaIns = str(fICemCon*0.0008) + " kg/m3 이하"
        return sOQuaIns