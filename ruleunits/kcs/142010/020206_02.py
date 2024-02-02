import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS142010_020206_02(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 14 20 10 2.2.6 (2)' # 건설기준문서
    ref_date = '2023-10-05'  # 디지털 건설문서 작성일
    doc_date = '2022-09-01'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '일반콘크리트'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    일반콘크리트
    2. 자재
    2.2 배합
    2.2.6 굵은 골재의 최대 치수
    (2)
    """

    # 건설기준문서내용(text)
    content = """
    #### 2.2.6 굵은 골재의 최대 치수
    (2) 굵은 골재의 최대 치수는 표 2.2-4의 값을 표준으로 한다.

표 2.2-4 굵은 골재의 최대 치수

\begin{table}[]
\begin{tabular}{|
>{\columncolor[HTML]{FFFFFF}}l |
>{\columncolor[HTML]{FFFFFF}}l |}
\hline
{\color[HTML]{333333} 구조물의 종류}  & {\color[HTML]{333333} 굵은 골재의 최대 치수(mm)}                                                       \\ \hline
{\color[HTML]{333333} 일반적인 경우}  & {\color[HTML]{333333} 20 또는 25}                                                               \\ \hline
{\color[HTML]{333333} 단면이 큰 경우} & {\color[HTML]{333333} 40}                                                                     \\ \hline
{\color[HTML]{333333} 무근콘크리트}   & {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}40\\ 부재 최소 치수의 1/4을 초과해서는 안 됨.\end{tabular}} \\ \hline
\end{tabular}
\end{table}
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 굵은 골재의 최대 치수"];
    B["KCS 14 31 30 2.2.6 (2)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 30 2.2.6 (2)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 굵은 골재의 최대 치수"/];
		VarIn1[/"입력변수: 구조물의 종류"/];

    VarOut1  ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{구조물의 종류}

		D --> |"'일반적인 경우'"|E[20 또는 25]
		D --> |"'단면이 큰 경우'"|F[40]
		D --> |"'무근콘크리트'"|G["40, 부재 최소 치수의 1/4을 초과해서는 안 됨."]


		E --> H([굵은 골재의 최대 치수])
		F --> H([굵은 골재의 최대 치수])
		G --> H([굵은 골재의 최대 치수])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def max_size_of_coarse_aggregates(sITypStr) -> str:
        """굵은 골재의 최대 치수

        Args:
            sITypStr (string): 구조물의 종류


        Returns:
            sOSizCoa (string): 굵은 골재의 최대 치수

        """

        if sITypStr == "일반적인 경우":
            sOSizCoa = "20 또는 25"
            return sOSizCoa

        if sITypStr == "단면이 큰 경우":
            sOSizCoa = "40"
            return sOSizCoa

        if sITypStr == "무근콘크리트":
            sOSizCoa = "40, 부재 최소 치수의 1/4을 초과해서는 안 됨."
            return sOSizCoa