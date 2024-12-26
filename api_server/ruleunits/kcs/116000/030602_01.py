import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS116000_030602_01(RuleUnit):


    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 11 60 00 3.6.2 (1)'
    ref_date = '2020-12-03'
    doc_date = '2023-08-14'
    title = '인장시험'

    description = """
    앵커
    3. 시공
    3.6 현장품질관리
    3.6.2 시험 일반
    (1)
    """

    content = """
    #### 3.6.2. 시험 일반
    (1) 인장시험
    ② 가압장치는 최대 계획시험하중의 1.2배 이상의 공칭용량을 가지며, 계획하중 단계에 따른 하중의 증감이 가능한 것으로 한다. 인장잭의 하중계는 하중 계측 전에 작동을 시켜, 정확한 하중을 계측할 수 있도록 한다.
    ③ 시험방법은 특별히 정해진 때를 제외하고 다음과 같이 한다.
    가. 계획 최대시험하중은 설계하중의 1.2배 이상, 긴장재의 항복하중의 0.9배 이하로 하고, 설계에 대한 앵커의 안정성을 확인하기 위하여 최소 3개 그리고 전체 그라운드 앵커의 5% 이상에 대해 인장시험을 실시해야 하며, 나머지 앵커는 확인시험 절차에 따라 시험을 실시하여야 한다.
    나. 초기하중은 계획 최대시험하중의 0.1배로 하되 시험하중이 작은 경우에는 미소한 하중의 측정이 곤란하므로 최소 50 kN 이상의 초기하중을 유지하도록 한다.
    라. 각 주기의 재하는 표 3.6-1에 표시한 시간에서 하중을 일정하게 유지한다. 단, 변위가 안정되지 않는 경우에는 표 3.6-1에 기준하여 하중을 유지한다.
    표 3.6-1
    \begin{table}[]
    \begin{tabular}{cccc}
    \hline
    \multicolumn{1}{r}{\begin{tabular}[c]{@{}r@{}}정착층\\ 하중단계\end{tabular}} & \multicolumn{1}{l}{점성토} & \multicolumn{1}{l}{사질토} & \multicolumn{1}{l}{암반} \\ \hline
    초기하중 시                                                                 & 15분 이상의 일정시간            & 10분 이상의 일정시간            & 5분 이상의 일정시간            \\
    이력하중 시                                                                 & 3분 이상의 일정시간             & 2분 이상의 일정시간             & 1분 이상의 일정시간            \\ \hline
    \end{tabular}
    \end{table}
    바. 하중의 증가속도 및 제하속도는 각각 매 분당의 계획 최대시험하중의 0.1배 내지 0.2배로 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 인장시험];
    B["KCS 11 60 00 3.6.2 (1)"];
    B ~~~ A
    end

    KCS(["KCS 11 60 00 3.6.2 (1)"])

    subgraph Variable_def
    subgraph v1
    VarOut1[/출력변수: 가압장치의 공칭용량/];
    VarIn1[/입력변수: 최대 계획시험하중/];
    end
    subgraph v2
    VarOut2[/출력변수: 인장시험 앵커개수/];
    VarIn2[/입력변수: 설계하중/];
    VarIn3[/입력변수: 긴장재의 항복하중/];
    VarIn4[/입력변수: 전체 그라운드 앵커개수/];
    end
    subgraph v3
    VarOut3[/출력변수: 초기하중/];
    VarIn5[/입력변수: 계획 최대시험하중/];
    end
    subgraph v4
    VarOut4[/출력변수: 인장시험 최소하중재하시간/];
    VarIn6[/입력변수: 정착층종류/];
    VarIn7[/입력변수: 하중단계/];
    end
    subgraph v5
    VarOut5[/출력변수: 하중의 증가속도/];
    VarOut6[/입력변수: 하중의 제하속도/];
    VarIn8[/입력변수: 매 분당의 계획 최대시험하중/];
    end
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"가압장치의 공칭용량
>= 최대 계획시험하중 * 1.2"}
    Variable_def --> C2{"계획 최대시험하중 >= 설계하중 * 1.2 and
<= 긴장재의 항복하중 * 0.9"}
    Variable_def --> C3{"인장시험 앵커개수 >= 전체 그라운드 앵커의 5% and
>= 3개"}
    Variable_def --> C4{"초기하중 >= 계획 최대시험하중 * 0.1 and
>= 50kN"}
    Variable_def --> C5{"KCS 11 60 00 3.6 표 3.6-1"}
    Variable_def --> C6{"계획 최대시험하중 * 0.1 <= 증가속도, 제하속도
<= 계획 최대시험하중 * 0.2"}

    C1--> D1["가압장치의 공칭용량"];
    C2--> E2(["Pass or Fail"])
    C3--> D3["인장시험 앵커개수"];
    C3--> D4["전체 그라운드 앵커개수 - 인장시험 앵커개수"];
    C4--> D5["초기하중"];
    C5--> |"정착층종류, 하중단계 고려"|D6["인장시험 최소하중재하시간"];
    C6--> D7["증가속도"];
    C6--> D8["제하속도"];

    D1--> E1(["가압장치의 공칭용량"])
    D3--> E3(["인장시험 앵커개수"])
		D4--> E4(["확인시험 앵커개수"])
		D5--> E5(["초기하중"])
		D6--> E6(["인장시험 최소하중재하시간"])
		D7--> E7(["증가속도"])
		D8--> E8(["제하속도"])
    """

    @rule_method
    def Planned_Maximum_Test_Load(fIMaxLoa, fIDesLoa, fIYieTen, nINumGro, sITypSet, sILoaSta, fILoaMin) -> str:
        """인장시험
        Args:
          fIMaxLoa (float): 계획 최대시험 하중
          fIDesLoa (float): 설계하중
          fIYieTen (float): 긴장재의 항복하중
          nINumGro (int): 전체 그라운드 앵커개수
          sITypSet (str): 정착층 종류
          sILoaSta (str): 하중 단계
          fILoaMin (float): 매 분당의 계획 최대시험하중

        Returns:
          fOCapPre (float): 가압장치의 공칭용량
          pass_fail (bool): 앵커 3.6.2 시험 일반 (1) ③ 가의 판단 결과
          nOAncTen (int): 인장시험 앵커개수
          nOAncVer (int): 확인시험 앵커개수
          fOIniLoa (float): 초기하중
          sOLoaTim (str): 인장시험 최소하중재하시간
          fOLoaInc (float): 하중의 증가속도
          fOLoaRel (float): 하중의 제하속도
        """
        assert isinstance(fIMaxLoa, float)
        assert isinstance(fIDesLoa, float)
        assert isinstance(fIYieTen, float)
        assert isinstance(nINumGro, int)
        assert isinstance(sITypSet, str)
        assert sITypSet in["점성토", "사질토", "암반"]
        assert isinstance(sILoaSta, str)
        assert sILoaSta in["초기하중시", "이력하중시"]
        assert isinstance(fILoaMin, float)

        fOCapPre = 1.2 * fIMaxLoa

        if 1.2 * fIDesLoa <= fIMaxLoa <= 0.9 * fIYieTen:
          pass_fail = True
        else:
          pass_fail = False

        if nINumGro >= 60:
          nOAncTen = int(0.05 * nINumGro)
          nOAncVer = nINumGro - nOAncTen
        else:
          noAncTen = 3
          nOAncVer = nINumGro - nOAncTen

        if fIMaxLoa >= 500:
          fOIniLoa = fIMaxLoa * 0.1
        else:
          fOIniLoa = 50

        if sITypSet == "점성토":
          if sILoaSta == "초기하중시":
            sOLoaTim = "15분 이상의 일정시간"
          elif sILoaSta == "이력하중시":
            sOLoaTim = "3분 이상의 일정시간"

        if sITypSet == "사질토":
          if sILoaSta == "초기하중시":
            sOLoaTim = "10분 이상의 일정시간"
          elif sILoaSta == "이력하중시":
            sOLoaTim = "2분 이상의 일정시간"

        if sITypSet == "암반":
          if sILoaSta == "초기하중시":
            sOLoaTim = "5분 이상의 일정시간"
          elif sILoaSta == "이력하중시":
            sOLoaTim = "1분 이상의 일정시간"

        fOLoaInc = 0.1 * fILoaMin
        fOLoaRel = 0.2 * fILoaMin

        return RuleUnitResult(
                result_variables ={
                    "fOCapPre": fOCapPre,
                    "pass_fail": pass_fail,
                    "nOAncTen": nOAncTen,
                    "nOAncVer": nOAncVer,
                    "fOIniLoa": fOIniLoa,
                    "sOLoaTim": sOLoaTim,
                    "fOLoaInc": fOLoaInc,
                    "fOLoaRel": fOLoaRel,
                }
            )