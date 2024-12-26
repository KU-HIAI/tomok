import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142053_030805_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 20 53 3.8.5 (1)'
    ref_date = '2022-01-11'
    doc_date = '2023-09-21'
    title = '정착장치 및 접속장치의 배치의 검사'


    description = """
    프리스트레스트 콘크리트
    3. 시공
    3.8 현장 품질관리
    3.8.5 정착장치, 접속장치의 조립 및 배치의 검사
    (1)
    """
    content = """
    #### 3.8.5 정착장치, 접속장치의 조립 및 배치의 검사
    (1) 정착장치 및 접속장치의 조립 및 배치의 검사는 표 3.8-5에 따른다.
    \begin{table}[]
    \begin{tabular}{llll}
    항목         & 시험 및 검사 방법           & 시기 및 횟수                    & 판정기준                                                                                                                                                          \\
    종류, 지름, 수량 & 육안 관찰, 지름의 측정        & 배치 후                       & 설계도서와 일치할 것                                                                                                                                                   \\
    고정 방법      & 육안 관찰                & \multirow{2}{*}{콘크리트 타설 전} & \begin{tabular}[c]{@{}l@{}}콘크리트를 타설할 때 변형 및\\ 이동의 우려가 없을 것\end{tabular}                                                                                       \\
    배치 위치      & 스케일 등에 의한 측정 및 육안 관찰 &                            & \begin{tabular}[c]{@{}l@{}}허용오차 : 설계도서와 일치할 것, 또는 긴장재 중심과 부재 가장자리와의 거리가 1 m 미만인 경\\ 우에는 ±5 mm, 1 m이상의 경우에는 부재치수의 1/200 이하 또는 ±10 mm 가운데 작은 값(표준)\end{tabular} \\
    보강철근의 배치   & 육안 관찰                & 배치 후                       & 설계도서와 일치할 것
    \end{tabular}
    \end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 정착장치 및 접속장치의 조립 및 배치 검사];
    B["KCS 14 20 53 3.8.4 (1)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 53 3.8.4 (1)"])

    subgraph Variable_def
    VarOut[/출력변수: 정착장치 및 접속장치의 조립 및 배치 검사/];
    VarIn0[/입력변수: 항목/]
    VarIn1[/입력변수: 시험·검사 방법/];
    VarIn2[/입력변수: 시기·횟수/];
    VarIn3[/입력변수: 판정기준/]
    VarIn4[/입력변수: 설계도서/];
    VarIn5[/입력변수: 긴장재 중심과 부재 가장자리의 거리/];
    VarIn6[/입력변수: 부재치수/];
    VarOut ~~~ VarIn0 & VarIn1 & VarIn2
    VarIn1 ~~~ VarIn3 & VarIn4 & VarIn5 & VarIn6
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"항목 \n 시험·검사 방법 \n 시기·횟수 \n 판정기준\n."}
    C --> |표 3.8-5|D[정착장치 및 접속장치의 조립 및 배치 검사]
    D --> End(["정착장치 및 접속장치의 조립 및 배치 검사"])
    """

    @rule_method

    def anchorage_coupler(sIItem, bITesMet, bITesFre, bIJudCri, bIDesDoc, fIDisTen, fIEleSiz) -> RuleUnitResult:
        """
        Args:
            sIItem (str): 항목
            bITesMet (bool): 시험·검사 방법
            bITesFre (bool): 시기·횟수
            bIJudCri (bool): 판정기준
            bIDesDoc (bool): 설계도서
            fIDisTen (float): 긴장재 중심과 부재 가장자리의 거리
            fIEleSiz (float): 부재치수

        Returns:
            sOArrAnc (str): 정착장치 및 접속장치의 배치의 검사
        """
        assert isinstance(sIItem, str)
        assert sIItem in [ "종류", "지름", "수량", "고정 방법", "배치 위치","보강철근의 배치"]
        assert isinstance(bITesMet, bool)
        assert isinstance(bITesFre, bool)
        assert isinstance(bIJudCri, bool)
        assert (bITesMet+bITesFre+bIJudCri) == 1
        assert isinstance(bIDesDoc, bool)
        assert isinstance(fIDisTen, float)
        assert isinstance(fIEleSiz, float)
        assert fIDisTen > 1
        assert fIEleSiz > 1


        if sIItem == "종류" or sIItem == "지름" or sIItem == "수량":
            if bITesMet:
                sOArrAnc = "육안 관찰, 지름의 측정"
            elif bITesFre:
                sOArrAnc = "배치 후"
            elif bIJudCri:
                sOArrAnc = "설계도서와 일치할 것"
        elif sIItem == "고정 방법":
            if bITesMet:
                sOArrAnc = "육안 관찰"
            elif bITesFre:
                sOArrAnc = "콘크리트 타설 전"
            elif bIJudCri:
                sOArrAnc = "콘크리트를 타설할 때 변형 및 이동의 우려가 없을 것"
        elif sIItem == "배치 위치":
            if bITesMet:
                sOArrAnc = "스케일 등에 의한 측정 및 육안 관찰"
            elif bITesFre:
                sOArrAnc = "콘크리트 타설 전"
            elif bIJudCri:
                if bIDesDoc:
                    sOArrAnc = "허용오차: 설계도서와 일치할 것"
                else:
                    if fIDisTen < 1000:
                        sOArrAnc = "허용오차: ±5 mm"
                    else:
                        sOArrAnc = "허용오차: ±" + str(round(min(fIEleSiz/200,10),5)) + " mm"
        elif sIItem == "보강철근의 배치":
            if bITesMet:
                sOArrAnc = "육안 관찰"
            elif bITesFre:
                sOArrAnc = "배치 후"
            elif bIJudCri:
                sOArrAnc = "설계도서와 일치할 것"

        return RuleUnitResult(
            result_variables = {
                "sOArrAnc": sOArrAnc,
                })