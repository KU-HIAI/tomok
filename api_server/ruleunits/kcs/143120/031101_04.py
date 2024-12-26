import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_031101_04(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 3.11.1 (4)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-14'
    title = '비파괴시험의 범위'

    description = """
    용접
    3. 시공
    3.11 용접검사
    3.11.1 용접검사의 종류 및 범위
    """

    content = """
    #### 3.11.1 용접검사의 종류 및 범위
    (4) 비파괴시험의 범위는 표 3.11-1과 같으며, 강도로교 및 강철도교에 대해서는 ‘3.11.4 강도로교 및 강철도교 비파괴시험’을 적용한다.
    표 3.11-1 비파괴시험의 범위
    \begin{table}[]
\begin{tabular}{llllll}
\multirow{2}{*}{용접부 종류1)} & \multicolumn{4}{l}{품질관리 구분} & \multirow{2}{*}{\begin{tabular}[c]{@{}l@{}}시험\\ 방법\end{tabular}} \\
 & 가 & 나 & 다 & 라 &  \\
인장응력을 받는 완전용입 또는 부분용입 횡방향 맞대기 용접부 & 해당 없음. & 10% & 20% & 100% & RT, UT \\
\begin{tabular}[c]{@{}l@{}}완전용입 또는 부분용입 횡방향 맞대기 용접부\\  - 십자이음부\\  - T-이음부\end{tabular} & 해당 없음. & \begin{tabular}[c]{@{}l@{}}10%\\ 5%\end{tabular} & \begin{tabular}[c]{@{}l@{}}20%\\ 10%\end{tabular} & \begin{tabular}[c]{@{}l@{}}100%\\ 50%\end{tabular} & UT \\
\begin{tabular}[c]{@{}l@{}}인장 또는 전단을 받는 횡방향 필릿용접부 \\  - a > 12 mm or t > 20 mm \\  - a ≤ 12 mm and t ≤ 20 mm\end{tabular} & 해당 없음. & \begin{tabular}[c]{@{}l@{}}5%\\ 0%\end{tabular} & \begin{tabular}[c]{@{}l@{}}10%\\ 5%\end{tabular} & \begin{tabular}[c]{@{}l@{}}20%\\ 10%\end{tabular} & MT \\
종방향 용접과 보강재 용접부 & 해당 없음. & 0% & 5% & 10% & MT \\
\multicolumn{6}{l}{주 1) 이 표에서 종방향 용접은 부재의 축방향과 평행인 용접이며, 그 이외의 경우에는 횡방향 용접으로 간주한다. 또한 a는 용접의 목두께이며, t는 모재의 두께 (mm)}
\end{tabular}
\end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: 비파괴시험의 범위"];
    B["KCS 14 31 20 3.11.1 (4)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 3.11.1 (4)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 비파괴시험의 범위"/];
    VarIn1[/입력변수: 강도로교 및 강철도교/];
    VarIn2[/입력변수: 용접부 종류/];
    VarIn3[/입력변수: 품질관리 구분/];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"강도로교 및 강철도교"}
    C --> |"True"|D["‘3.11.4 강도로교 및 강철도교 비파괴시험’을 적용"]
		C --> |False|E{용접부 종류 \n 품질관리 구분}
		E --> |표 3.11-1|F[비파괴시험의 범위]
		D & F --> End([비파괴시험의 범위])
    """

    @rule_method
    def Steel_Roadway_Bridge_and_Steel_Railroad_Bridge(bIRoaRai, sITypWel, sIClaQua, fIWelThr, fIThiMet) -> RuleUnitResult:
        """ 비파괴시험의 범위
        Args:
        bIRoaRai (bool): 강도로교 및 강철도교
        sITypWel (str): 용접부의 종류
        sIClaQua (str): 품질관리 구분
        fIWelThr (float): 용접의 목두께
        fIThiMet (float): 모재의 두께

        Returns:
        sORanNon (str): 비파괴시험의 범위
        """
        assert isinstance(bIRoaRai, bool)
        assert isinstance(sITypWel, str)
        assert sITypWel in["인장응력을 받는 완전용입 또는 부분용입 횡방향 맞대기 용접부", "완전용입 또는 부분용입 횡방향 맞대기 용접부, 십자이음부", "완전용입 또는 부분용입 횡방향 맞대기 용접부, T-이음부", "인장 또는 전단을 받는 횡방향 필릿용접부", "종방향 용접과 보강재 용접부"]
        assert isinstance(sIClaQua, str)
        assert sIClaQua in["가", "나", "다", "라"]
        assert isinstance(fIWelThr, float)
        assert isinstance(fIThiMet, float)

        if bIRoaRai == True:
          sORanNon = "'3.11.4 강도로교 및 강철도교 비파괴시험'을 적용"
        else:
          if sITypWel == "인장응력을 받는 완전용입 또는 부분용입 횡방향 맞대기 용접부":
            if sIClaQua == "가":
              sORanNon ="해당없음"
            elif sIClaQua == "나":
              sORanNon ="10%"
            elif sIClaQua == "다":
              sORanNon ="20%"
            elif sIClaQua == "라":
              sORanNon ="100%"
          elif sITypWel == "완전용입 또는 부분용입 횡방향 맞대기 용접부, 십자이음부":
            if sIClaQua == "가":
              sORanNon ="해당없음"
            elif sIClaQua == "나":
              sORanNon ="10%"
            elif sIClaQua == "다":
              sORanNon ="20%"
            elif sIClaQua == "라":
              sORanNon ="100%"
          elif sITypWel == "완전용입 또는 부분용입 횡방향 맞대기 용접부, T-이음부":
            if sIClaQua == "가":
              sORanNon ="해당없음"
            elif sIClaQua == "나":
              sORanNon ="5%"
            elif sIClaQua == "다":
              sORanNon ="10%"
            elif sIClaQua == "라":
              sORanNon ="50%"
          elif sITypWel == "인장 또는 전단을 받는 횡방향 필릿용접부":
            if fIWelThr > 12 or fIThiMet > 20:
              if sIClaQua == "가":
                sORanNon ="해당없음"
              elif sIClaQua == "나":
                sORanNon ="5%"
              elif sIClaQua == "다":
                sORanNon ="10%"
              elif sIClaQua == "라":
                sORanNon ="20%"
            elif fIWelThr <= 12 and fIThiMet <= 20:
              if sIClaQua == "가":
                sORanNon ="해당없음"
              elif sIClaQua == "나":
                sORanNon ="0%"
              elif sIClaQua == "다":
                sORanNon ="5%"
              elif sIClaQua == "라":
                sORanNon ="10%"
          elif sITypWel == "종방향 용접과 보강재 용접부":
            if sIClaQua == "가":
              sORanNon ="해당없음"
            elif sIClaQua == "나":
              sORanNon ="0%"
            elif sIClaQua == "다":
              sORanNon ="5%"
            elif sIClaQua == "라":
              sORanNon ="10%"

        return RuleUnitResult(
                result_variables = {
                    "sORanNon": sORanNon
                }
            )