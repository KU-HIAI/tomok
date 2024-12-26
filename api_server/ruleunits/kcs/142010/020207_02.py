import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142010_020207_02(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = False # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 14 20 10 2.2.7 (2)' # 건설기준문서
    ref_date = '2022-09-01'  # 디지털 건설문서 작성일
    doc_date = '2024-02-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '일반콘크리트'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    일반콘크리트
    2. 자재
    2.2 배합
    2.2.7 슬럼프 및 슬럼프 플로
    (2)
    """

    # 건설기준문서내용(text)
    content = """
    #### 2.2.7 슬럼프 및 슬럼프 플로
    (2) 콘크리트를 타설할 때의 슬럼프 값은 표 2.2-5를 표준으로 한다.

표 2.2-5 슬럼프의 표준값(mm)

\begin{table}[]
\begin{tabular}{|
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l |}
\hline
\multicolumn{2}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 종류}}                                                                                                                                                                                                                                                     & {\color[HTML]{333333} 슬럼프 값}                                                                              \\ \hline
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}                                                                                                 & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 일반적인 경우}}                                                                         & {\color[HTML]{333333} 80$\sim$150}                                                                        \\ \cline{2-3}
\multicolumn{1}{|l|}{\multirow{-2}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 철근콘크리트}}}                                                                         & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 단면이 큰 경우}}                                                                        & {\color[HTML]{333333} 60$\sim$120}                                                                        \\ \hline
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}                                                                                                 & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 일반적인 경우}}                                                                         & {\color[HTML]{333333} 50$\sim$150}                                                                        \\ \cline{2-3}
\multicolumn{1}{|l|}{\multirow{-2}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 무근콘크리트}}}                                                                         & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 단면이 큰 경우}}                                                                        & {\color[HTML]{333333} 50$\sim$100}                                                                        \\ \hline
\multicolumn{3}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}주 1) 유동화 콘크리트의 슬럼프는 KCS 14 20 31 (2.2) 의 규정을 표준으로 한다.\\ \\ 2) 여기에서 제시된 슬럼프값은 구조물의 종류에 따른 슬럼프의 범위를 나타낸 것으로 실제로 각종 공사에서 슬럼프값을 정하고자 할 경우에는 구조물의 종류나 부재의 형상, 치수 및 배근상태에 따라 알맞은 값으로 정하되 충전성이 좋고 충분히 다질 수 있는 범위에서 되도록 작은 값으로 정하여야 한다.\\ 3) 콘크리트의 운반시간이 길 경우 또는 기온이 높을 경우에는 슬럼프가 크게 저하하므로 운반중의 슬럼프 저하를 고려한 슬럼프값에 대하여 배합을 정하여야 한다.\end{tabular}}} \\ \hline
\end{tabular}
\end{table}

    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 슬럼프의 표준 값"];
    B["KCS 14 31 30 2.2.7 (2)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 30 2.2.7 (2)"])

    subgraph Variable_def
		VarIn1[/"입력변수: 콘크리트 종류"/];
		VarIn2[/"입력변수: 단면 종류"/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{콘크리트 종류}

		D --> |"철근콘크리트"|E{단면 종류}
		D --> |"무근콘크리트"|F{단면 종류}



		E --> |일반적인 경우|H[80~150]
		E --> |단면이 큰 경우|I[60~120]

		F --> |일반적인 경우|J[50~150]
		F --> |단면이 큰 경우|K[50~100]

		H --> L([슬럼프 값])
		I --> L([슬럼프 값])
		J --> L([슬럼프 값])
		K --> L([슬럼프 값])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def standard_slump_value(sIConTyp, sISecTyp) -> RuleUnitResult:
        """슬럼프의 표준 값

        Args:
            sIConTyp (str): 콘크리트 종류
            sISecTyp (str): 단면 종류

        Returns:
            sOSluVal (str): 슬럼프 값

        """
        assert isinstance(sIConTyp, str)
        assert isinstance(sISecTyp, str)

        if sIConTyp == "철근콘크리트":
            if sISecTyp == "일반적인 경우":
                sOSluVal = "80~150"
                return RuleUnitResult(
                    result_variables = {
                        "sOSluVal": sOSluVal
                }
            )
            if sISecTyp == "단면이 큰 경우":
                sOSluVal = "60~120"
                return RuleUnitResult(
                    result_variables = {
                        "sOSluVal": sOSluVal
                }
            )
        if sIConTyp == "무근콘크리트":
            if sISecTyp == "일반적인 경우":
                sOSluVal = "50~150"
                return RuleUnitResult(
                    result_variables = {
                        "sOSluVal": sOSluVal
                }
            )
            if sISecTyp == "단면이 큰 경우":
                sOSluVal = "50~100"
                return RuleUnitResult(
                    result_variables = {
                        "sOSluVal": sOSluVal
                }
            )
            else:
                assert 1 != 1
        else:
            assert 1 != 1