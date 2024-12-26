import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS213000_031601_05(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 30 00 3.16.1.(5)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-25'
    title = '굴착에 따른 인접지반의 영향범위'

    description = """
    가설흙막이 공사
    3. 시공
    3.16. 계측관리
    3.16.1 공통사항
    (5)
    """

    content = """
    #### 3.16.1 공통사항
    (5) 굴착에 따른 인접지반의 영향범위는 주변현황, 토질 및 지하수위 등의 조사결과와 흙막이 구조물의 형식에 따라 검토하여 정하도록 하며, 달리 명시된 것이 없는 경우에는 표 3.16-1을 참고할 수 있다.
    표 3.16-1
    \begin{table}[]
    \begin{tabular}{ll}
    지반 구분 & 수평영향거리                       \\
    사질토   & 굴착 깊이의 2배                    \\
    점성토   & 굴착 깊이의 4배                    \\
    암반    & 굴착 깊이의 1배 (불연속면이 있을 경우에는 2배)
    \end{tabular}
    \end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 굴착에 따른 인접지반의 영향범위];
    B["KCS 21 30 00 3.16.1 (5)"];
    B ~~~ A
    end

    KCS(["KCS 21 30 00 3.16.1 (5)"])

    subgraph Variable_def
    VarOut1[/출력변수: 수평영향 거리/];
    VarIn1[/입력변수: 지반 구분/];
    VarIn2[/입력변수: 굴착 깊이/];
    VarIn3[/입력변수: 불연속면이 있는 경우/];
    end
    VarOut1 ~~~ VarIn1

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"지반구분"}
    C1 --> |사질토|E1["굴착 깊이 * 2"]
    C1 --> |점성토|E2["굴착 깊이 * 4"]
    C1 --> |일반|D3{"불연속면이 있을 경우"}
    D3 --> |YES|E3["굴착깊이 * 2"]
    D3 --> |NO|E4["굴착깊이 * 1"]

    E1 & E2 & E3 & E4 --> F1(["수평영향 거리"])
    """

    @rule_method
    def Type_of_Soil(sITypSoi, fIExcDep, bINonCon) -> float:
        """ 굴착에 따른 인접지반의 영향범위
        Args:
            sITypSoi (str): 지반의 종류
            fIExcDep (float): 굴착 깊이
            bINonCon (bool): 불연속면이 있는 경우

        Returns:
            fOHorDis (float): 수평영향거리
        """
        assert isinstance(sITypSoi, str)
        assert sITypSoi in["사질토", "점성토", "암반"]
        assert isinstance(fIExcDep, float)
        assert isinstance(bINonCon, bool)

        if sITypSoi == "사질토":
          fOHorDis = fIExcDep * 2
        elif sITypSoi == "점성토":
          fOHorDis = fIExcDep * 4
        elif sITypSoi == "암반":
          if bINonCon == True:
            fOHorDis = fIExcDep *2
          elif bINonCon == False:
            fOHorDis = fIExcDep

        return RuleUnitResult(
                result_variables = {
                    "fOHorDis": fOHorDis
                }
            )