import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143125_0201_05(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = False # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 14 31 25 2.1 (5)' # 건설기준문서
    ref_date = '2022-09-01'  # 디지털 건설문서 작성일
    doc_date = '2024-02-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '볼트 접합 및 핀 연결'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    볼트 접합 및 핀 연결
    2. 자재
    2.1 고장력볼트
    (5)
    """

    # 건설기준문서내용(text)
    content = """
    #### 2.1 고장력볼트
    (5) 와셔의 경도는 표 2.1-4의 규격에 합격한 것이어야 하며, 침탄, 담금질, 뜨임을 하지 않는 것으로 한다.

표 2.1-4 와셔 제품의 기계적 성질

\begin{table}[]
\begin{tabular}{|
>{\columncolor[HTML]{FFFFFF}}l |
>{\columncolor[HTML]{FFFFFF}}l |}
\hline
{\color[HTML]{333333} 와셔의 기계적 성질에 의한 등급} & {\color[HTML]{333333} 경도}             \\ \hline
{\color[HTML]{333333} F35}               & {\color[HTML]{333333} HRC 35$\sim$45} \\ \hline
\end{tabular}
\end{table}
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A[Title: 고장력볼트 와셔의 경도];
    B["KCS 14 31 25 2.1 (5)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 25 2.1 (5)"])

    subgraph Variable_def
    VarIn2[/입력변수: 와셔 등급/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{와셔 등급}

    C --> |F35|D["HRC 35~45"]
		D --> F([와셔의 경도])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def hardness_of_washer(sIWasGra) -> RuleUnitResult:
        """와셔의 경도

        Args:
            sIWasGra (str): 와셔 등급

        Returns:
            sOHarWas (str): 와셔의 경도
        """


        if sIWasGra == "F35":
            sOHarWas = "HRC 35~45"
            return RuleUnitResult(
                result_variables = {
                    "sOHarWas": sOHarWas
                }
            )
        else:
            assert 1 != 1