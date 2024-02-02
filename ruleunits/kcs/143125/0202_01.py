import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS143125_0202_01(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 14 31 25 2.2 (1)' # 건설기준문서
    ref_date = '2023-09-11'  # 디지털 건설문서 작성일
    doc_date = '2019-05-20'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '볼트 접합 및 핀 연결'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    볼트 접합 및 핀 연결
    2. 자재
    2.2 일반볼트
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    #### 2.2 일반볼트
    (1) 볼트, 너트, 와셔의 품질은 다음의 KS 규격에 따른다.
    ① 볼트 : KS B 1002
    ② 너트 : KS B 1012
    ③ 와셔 : KS B 1326
    ④ 볼트의 기계적 성질은 KS B 0233에서 규정한 표 2.2-1의 기계적 성질을 따른다.

표 2.2-1 볼트의 기계적 성질

\begin{table}[]
\begin{tabular}{|
>{\columncolor[HTML]{FFFFFF}}l |
>{\columncolor[HTML]{FFFFFF}}l |
>{\columncolor[HTML]{FFFFFF}}l |
>{\columncolor[HTML]{FFFFFF}}l |}
\hline
{\color[HTML]{333333} 구분}          & {\color[HTML]{333333} 4T}          & {\color[HTML]{333333} 5T}           & {\color[HTML]{333333} 6T}           \\ \hline
{\color[HTML]{333333} 인장강도(N/mm2)} & {\color[HTML]{333333} 392 이상}      & {\color[HTML]{333333} 490 이상}       & {\color[HTML]{333333} 588 이상}       \\ \hline
{\color[HTML]{333333} 브리넬경도(HB)}   & {\color[HTML]{333333} 05$\sim$229} & {\color[HTML]{333333} 135$\sim$241} & {\color[HTML]{333333} 170$\sim$255} \\ \hline
\end{tabular}
\end{table}


    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A[Title: 일반볼트의 기계적 성질];
    B["KCS 14 31 25 2.2 (1)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 25 2.2 (1)"])

    subgraph Variable_def
    VarOut1[/출력변수: 인장강도/];
    VarOut2[/출력변수: 브리넬경도/];

    VarIn1[/입력변수: 볼트 구분/];
    VarIn2[/입력변수: 인장강도/];
    VarIn3[/입력변수: 브리넬경도/];

    VarOut1 & VarOut2  ~~~ VarIn1  &  VarIn2  &  VarIn3
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{구분}

    C --> |인장강도|D{볼트}
    C --> |브리넬강도|E{볼트}


		D --> |4T|H([392 이상])
		D --> |5T|I([490 이상])
		D --> |6T|J([588 이상])

		E --> |4T|K([105~229])
		E --> |5T|L([135~241])
		E --> |6T|M([170~255])

		H --> N([인장강도])
		I --> N([인장강도])
		J --> N([인장강도])

		K -->O([브리넬강도])
		L -->O([브리넬강도])
		M -->O([브리넬강도])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def mechanical_properties_of_common_bolts(sIBolCla) ->str :
        """일반볼트의 기계적 성질

        Args:
            sIBolCla (string): 볼트 구분
            bITenStr (boolean): 인장강도
            bIBriHar (boolean): 브리넬경도

        Returns:
            sOTenStr (string): 인장강도
            sOBriHar (string): 브리넬경도

        """

        if sIBolCla == "4T":
            sOTenStr = "392 N/mm2 이상"
            sOBriHar = "105~229 HB"
            return sOTenStr, sOBriHar

        if sIBolCla == "5T":
            sOTenStr = "490  N/mm2 이상"
            sOBriHar = "135~241 HB"
            return sOTenStr, sOBriHar

        if sIBolCla == "6T":
            sOTenStr = "588 N/mm2 이상"
            sOBriHar = "170~255 HB"
            return sOTenStr, sOBriHar