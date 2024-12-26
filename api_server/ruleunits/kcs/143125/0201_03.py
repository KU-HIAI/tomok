import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143125_0201_03(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = False # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 14 31 25 2.1 (3)' # 건설기준문서
    ref_date = '2022-09-01'  # 디지털 건설문서 작성일
    doc_date = '2024-02-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '볼트 접합 및 핀 연결'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    볼트 접합 및 핀 연결
    2. 자재
    2.1 고장력볼트
    (3)
    """

    # 건설기준문서내용(text)
    content = """
    #### 2.1 고장력볼트
    (3) 토크계수값은 표 2.1-2의 규정에 적합해야 한다. 고장력볼트 조임 시 토크계수값 시험은 1.3의 (2)목에 준하여 시행한다.
    표 2.1-2 토크계수값
\begin{table}[]
\begin{tabular}{|
>{\columncolor[HTML]{FFFFFF}}l |
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l |}
\hline
\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }                     & \multicolumn{2}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 토크계수값에 따른 세트의 종류}}                                           \\ \cline{2-3}
\multirow{-2}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 구분}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} A}}                & {\color[HTML]{333333} B}                \\ \hline
{\color[HTML]{333333} 토크계수값의 평균값}                                   & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0.110$\sim$0.150}} & {\color[HTML]{333333} 0.150$\sim$0.190} \\ \hline
{\color[HTML]{333333} 토크계수값의 표준편차}                                  & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0.010 이하}}         & {\color[HTML]{333333} 0.013 이하}         \\ \hline
\end{tabular}
\end{table}
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A[Title: 고장력볼트의 토크계수값];
    B["KCS 14 31 25 2.1 (3)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 25 2.1 (3)"])

    subgraph Variable_def
    VarIn1[/입력변수: 세트의 종류/];
    VarIn2[/입력변수: 토크계수값의 평균값/];
    VarIn3[/입력변수: 토크계수값의 표준편차/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{세트의 종류}

    C --> |A|D{토크계수값의\n 평균값}
    C --> |A|E{토크계수값의\n 표준편차}
    C --> |B|F{토크계수값의\n 평균값}
    C --> |B|G{토크계수값의\n 표준편차}

    D --> H["0.110 < 토크계수값의 평균값 < 0.150"]
    E --> I["토크계수값의 표준편차 <= 0.010"]

    F --> J["0.150< 토크계수값의 평균값 < 0.190"]
    G --> K["토크계수값의 표준편차 <= 0.013"]

		H --> L([고장력볼트의 토크계수값])
		I --> L([고장력볼트의 토크계수값])
		J --> L([고장력볼트의 토크계수값])
		K --> L([고장력볼트의 토크계수값])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def torque_coefficient_of_high_strength_bolts(sISetTyp) -> RuleUnitResult:
        """고장력볼트의 토크계수값

        Args:
            sISetTyp (str): 세트의 종류


        Returns:
            sOMeaVal (str): 토크계수값의 평균값
            sOStaDev (str): 토크계수값의 표준편차
        """
        assert isinstance(sISetTyp, str)

        if sISetTyp == "A":
            sOMeaVal = "0.110~0.150"
            sOStaDev = "0.010 이하"
            return RuleUnitResult(
                result_variables = {
                    "sOMeaVal": sOMeaVal,
                    "sOStaDev": sOStaDev,
                }
            )
        if sISetTyp == "B":
            sOMeaVal = "0.150~0.190"
            sOStaDev = "0.013 이하"
            return RuleUnitResult(
                result_variables = {
                    "sOMeaVal": sOMeaVal,
                    "sOStaDev": sOStaDev,
                }
            )
        else:
            assert 1 != 1