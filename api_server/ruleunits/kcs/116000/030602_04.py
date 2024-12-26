import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS116000_030602_04(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 11 60 00 3.6.2 (4)'
    ref_date = '2020-12-03'
    doc_date = '2023-10-06'
    title = '크리프시험'

    description = """
    앵커
    3. 시공
    3.6 현장품질관리
    3.6.2 시험 일반
    (4)
    """

    content = """
    #### 3.6.2. 시험 일반
    (4) 크리프시험
    ③ 시험방법은 특별히 정한 경우를 제외하고 다음과 같이 한다.
    가. 계획 최대시험하중은 설계하중의 1.2∼1.3배로 한다.
    다. 재하 도중에 계획 최대시험하중(Td)의 0.2배, 0.4배, 0.8배, 1.0배, 1.2배, 1.3배의 각 단계로 가압을 정지하고 변위가 안정될 때까지 하중을 유지하며, 안정유지가 안 될 때는 아래 표 3.6-2를 기준하여 하중을 유지한다.
    표 3.6-2 크리프시험의 최소 재하시간
    \begin{table}[]
    \begin{tabular}{ccc}
    \multicolumn{1}{l}{\multirow{2}{*}{\begin{tabular}[c]{@{}l@{}}정착층\\ \\ \\ 하중단계\end{tabular}}} & \multicolumn{2}{l}{최소 관측시간}                       \\
    \multicolumn{1}{l}{}                                                                          & \multicolumn{1}{l}{사질토} & \multicolumn{1}{l}{점성토} \\
    0.2Td                                                                                         &                         &                         \\
    0.4Td                                                                                         & 15분 이상                  & 30분 이상                  \\
    0.8Td                                                                                         & 15분 이상                  & 30분 이상                  \\
    1.0Td                                                                                         & 1시간 이상                  & 2시간 이상                  \\
    1.2Td                                                                                         & 1시간 이상                  & 3시간 이상                  \\
    1.3Td                                                                                         & 2시간 이상                  & 5시간 이상
    \end{tabular}
    \end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 크리프시험];
    B["KCS 11 60 00 3.6.2 (4)"];
    B ~~~ A
    end

    KCS(["KCS 11 60 00 3.6.2 (4)"])

    subgraph Variable_def
    subgraph v1
    VarOut1[/출력변수: 가압 정지 단계의 하중/];
    VarOut2[/출력변수: 최소 관측시간/];
    VarOut3[/출력변수: 가압 정지시 준수사항/];
    VarIn1[/입력변수: 하중단계/];
    VarIn2[/입력변수: 정착층 종류/];
    end
    subgraph v2
    VarIn3[/입력변수: 설계하중/];
    VarIn4[/입력변수: 계획 최대시험하중/];
    end
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C2{"가압 정지 단계의 하중 = 계획 최대시험
하중 * 0.2 or 0.4 or 0.8 or 1.0 or 1.2 or 1.3 "}
    Variable_def --> C1{"설계하중 * 1.2 <= 계획 최대시험하중
<= 설계하중 * 1.3"}
    C1--> D1["계획 최대시험하중"];
    C2--> |"YES"|C3{"변위의 안정 여부"};
    C3--> |"NO"|D3{"KCS 11 60 00 3.6 표 3.6-2"};
    C3--> |"YES"|D2["가압을 정지하고 변위가
안정될 때까지 하중을 유지"]
    D2--> E1(["가압을 정지하고 변위가 안정될 때까지 하중을 유지"])
    D3--> |"정착층 종류, 하중단계 고려"|E3["최소 관측시간"]
    E3--> F1(["최소 관측시간"])
    D1--> E2(["Pass or Fail"])
    """

    @rule_method
    def Design_Load(fIDesLoa, fIMaxLoa, sILoaSta, sITypSet) -> str:
        """ 크리프시험
        Args:
        fIDesLoa (float): 설계하중
        fIMaxLoa (float): 계획 최대시험하중
        sILoaSta (str): 하중 단계
        sITypSet (str): 정착층 종류

        Returns:
        pass_fail (bool): 계획 최대시험하중
        fOLoaHol (float): 가압 정지단계의 하중
        sOShuGui (str): 가압 정지시 준수사항
        sOMinObs (str): 최소 관측시간
        """
        assert isinstance(fIDesLoa, float)
        assert isinstance(fIMaxLoa, float)
        assert isinstance(sITypSet, str)
        assert sITypSet in["사질토","점성토"]
        assert isinstance(sILoaSta, str)
        assert sILoaSta in["0.2Td", "0.4Td", "0.8Td", "1.0Td", "1.2Td", "1.3Td"]

        if 1.2 * fIDesLoa <= fIMaxLoa <= 1.3 * fIDesLoa:
          pass_fail = True
        else:
          pass_fail = False

        if sILoaSta == "0.2Td":
          fOLoaHol = fIMaxLoa * 0.2
          sOShuGui = "범위가 안정될 때까지 하중을 유지"

        elif sILoaSta == "0.4Td":
          fOLoaHol = fIMaxLoa * 0.4
          sOShuGui = "범위가 안정될 때까지 하중을 유지"
          if sITypSet == "사질토":
            sOMinObs = "15분 이상"
          elif sITypSet == "점성토":
            sOMinObs = "30분 이상"

        elif sILoaSta == "0.8Td":
          fOLoaHol = fIMaxLoa * 0.8
          sOShuGui = "범위가 안정될 때까지 하중을 유지"
          if sITypSet == "사질토":
            sOMinObs = "15분 이상"
          elif sITypSet == "점성토":
            sOMinObs = "30분 이상"

        elif sILoaSta == "1.0Td":
          fOLoaHol = fIMaxLoa * 1.0
          sOShuGui = "범위가 안정될 때까지 하중을 유지"
          if sITypSet == "사질토":
            sOMinObs = "1시간 이상"
          elif sITypSet == "점성토":
            sOMinObs = "2시간 이상"

        elif sILoaSta == "1.2Td":
          fOLoaHol = fIMaxLoa * 1.2
          sOShuGui = "범위가 안정될 때까지 하중을 유지"
          if sITypSet == "사질토":
            sOMinObs = "1시간 이상"
          elif sITypSet == "점성토":
            sOMinObs = "3시간 이상"

        elif sILoaSta == "1.3Td":
          fOLoaHol = fIMaxLoa * 1.3
          sOShuGui = "범위가 안정될 때까지 하중을 유지"
          if sITypSet == "사질토":
            sOMinObs = "2시간 이상"
          elif sITypSet == "점성토":
            sOMinObs = "5시간 이상"

        return RuleUnitResult(
               result_variables={
                   "pass_fail": pass_fail,
                   "fOLoaHol": fOLoaHol,
                   "sOShuGui": sOShuGui,
                   "sOMinObs": sOMinObs,
                }
           )