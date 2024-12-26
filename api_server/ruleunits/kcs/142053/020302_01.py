import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142053_020302_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 20 53 2.3.2 (1)'
    ref_date = '2022-01-11'
    doc_date = '2023-09-21'
    title = '그라우트의 품질 검사'

    description = """
    프리스트레스트 콘크리트
    2. 자재
    2.3 재료 품질관리
    2.3.2 프리스트레스트 콘크리트용 그라우트의 품질 검사
    (1)
    """
    content = """
    #### 2.3.2 프리스트레스트 콘크리트용 그라우트의 품질 검사
    (1) 그라우트의 품질 검사는 표 2.3-2에 따른다.
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

    def quality_grout(sIItem, bITesMet, bITesFre, bIJudCri, fICemCon) -> RuleUnitResult:
        """
        Args:
            sIItem (str): 항목
            bITesMet (bool): 시험·검사 방법
            bITesFre (bool): 시기·횟수
            bIJudCri (bool): 판정기준
            fICemCon (float): 단위 시멘트량

        Returns:
            sOQuaIns (sting): 그라우트의 품질검사
        """
        assert isinstance(sIItem, str)
        assert sIItem in ["유동성","블리딩률","체적변화율","압축강도","염화물 함유량"]
        assert isinstance(bITesMet, bool)
        assert isinstance(bITesFre, bool)
        assert isinstance(bIJudCri, bool)
        assert (bITesMet+bITesFre+bIJudCri) == 1
        assert isinstance(fICemCon, float)

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
                sOQuaIns = "24시간 경과 시 (-1 ~ 5) %"
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

        return RuleUnitResult(
            result_variables = {
                "sOQuaIns": sOQuaIns,
                })