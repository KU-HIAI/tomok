import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS115010_030903_02(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 11 50 10 3.9.3 (2)'
    ref_date = '2023-09-11'
    doc_date = '2021-05-12'
    title = '검사용 튜브 설치 수량'

    description = """
    현장타설 콘크리트 말뚝
    3. 시공
    3.9 건전도 시험
    3.9.3 검사용 튜브 설치
    (2)
    """

    content = """
    #### 3.9.3 검사용 튜브 설치
    (2) 검사용 튜브는 철근망 내에 다음 표 3.9-1에 해당하는 수량을 결속하여 매설하여야 한다.
    표 3.9-1 원형말뚝의 크기와 검사용 튜브의 수
    \begin{table}[]
    \begin{tabular}{|
    >{\columncolor[HTML]{FFFFFF}}l |
    >{\columncolor[HTML]{FFFFFF}}l |
    >{\columncolor[HTML]{FFFFFF}}l |}
    \hline
    {\color[HTML]{333333} 원형말뚝의 직경 (D) (m)} & {\color[HTML]{333333} 검사용 튜브의 개수} & {\color[HTML]{333333} 비고} \\ \hline
    {\color[HTML]{333333} D ≤ 0.6}          & {\color[HTML]{333333} 2}          & {\color[HTML]{333333} }   \\ \hline
    {\color[HTML]{333333} 0.6 ＜ D ≤ 1.2}    & {\color[HTML]{333333} 3}          & {\color[HTML]{333333} }   \\ \hline
    {\color[HTML]{333333} 1.2 ＜ D ≤ 1.5}    & {\color[HTML]{333333} 4}          & {\color[HTML]{333333} }   \\ \hline
    {\color[HTML]{333333} 1.5 ＜ D ≤ 2.0}    & {\color[HTML]{333333} 5}          & {\color[HTML]{333333} }   \\ \hline
    {\color[HTML]{333333} 2.0 ＜ D ≤ 2.5}    & {\color[HTML]{333333} 7}          & {\color[HTML]{333333} }   \\ \hline
    {\color[HTML]{333333} 2.5 ＜ D}          & {\color[HTML]{333333} 8}          & {\color[HTML]{333333} }   \\ \hline
    \end{tabular}
    \end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: 검사용 튜브 설치 수량"];
    B["KCS 11 50 10 3.9.3 (2)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 10 3.9.3 (2)"])

    subgraph Variable_def
    VarOut[/"출력변수: 검사용 튜브의 개수"/];
		VarIn1[/"입력변수: 원형 말뚝의 직경(D)"/];

    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{"원형말뚝의 직경(D)"}
		D --> |D <= 0.6|E[2]
		D --> |0.6 < D <= 1.2|F[3]
		D --> |1.2 < D <= 1.5|G[4]
		D --> |1.5 < D <= 2.0|H[5]
		D --> |2.0 < D <= 2.5|J[7]
		D --> |2.5 < D|L[8]

		E --> M([검사용 튜브의 개수])
		F --> M([검사용 튜브의 개수])
		G --> M([검사용 튜브의 개수])
		H --> M([검사용 튜브의 개수])
		J --> M([검사용 튜브의 개수])
		L --> M([검사용 튜브의 개수])

    """

    @rule_method
    def number_of_inspection_tubes(fID) -> str :
        """검사용 튜브 설치 수량

        Args:
            fID (float): 원형 말뚝의 직경

        Returns:
            nONumTub (int) : 검사용 튜브의 개수
        """
        assert isinstance (fID, float)


        if fID <= 0.6:
            nONumTub = 2
        elif 0.6 < fID <= 1.2:
            nONumTub = 3
        elif 1.2 < fID <= 1.5:
            nONumTub = 4
        elif 1.5 < fID <= 2.0:
            nONumTub = 5
        elif 2.0 < fID <= 2.5:
            nONumTub = 7
        else:
            nONumTub = 8

        return RuleUnitResult(
                result_variables = {
                    "nONumTub": nONumTub,
                }
            )