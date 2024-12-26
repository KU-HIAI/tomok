import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142010_020212_06(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = False # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 14 20 10 2.2.12 (6)' # 건설기준문서
    ref_date = '2022-09-01'  # 디지털 건설문서 작성일
    doc_date = '2024-02-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '일반콘크리트'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    일반콘크리트
    2. 자재
    2.2 배합
    2.2.12 재료의 계량
    (6)
    """

    # 건설기준문서내용(text)
    content = """
    #### 2.2.12 재료의 계량
    (6) 계량오차는 1회 계량분에 대하여 표 2.2-9의 값 이하이어야 한다.

표 2.2-9 계량 오차
\begin{table}[]
\begin{tabular}{|
>{\columncolor[HTML]{FFFFFF}}l |
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l |}
\hline
\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }                         & \multicolumn{2}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 측정단위}}                                                                                                                                                                                     \\ \cline{2-3}
\multirow{-2}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 재료의 종류}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}질량\\ 질량\\ 질량 또는 부피\\ 질량\\ 질량 또는 부피\end{tabular}}} & {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}-1\%, +2\%\\ ±3\%\\ -2\%, +1\%\\ ±2\%\\ ±3\%\end{tabular}} \\ \hline
\end{tabular}
\end{table}

    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 재료의 계량 오차"];
    B["KCS 14 31 30 2.2.12 (6)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 30 2.2.12 (6)"])

    subgraph Variable_def
		VarIn1[/"입력변수: 재료의 종류"/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{재료의 종류}

		D --> |"시멘트"|E[질량, -1%, +2%]
		D --> |"골재"|F["질량, ±3%"]
		D --> |"물"|G[질량 또는 부피, -2%, +1%]
		D --> |"혼화재"|H["질량,±2%"]
		D --> |"혼화제"|I["질량 또는 부피, ±3%"]

		E --> J([측정단위, 재료의 계량 오차])
		F --> J([측정단위, 재료의 계량 오차])
		G --> J([측정단위, 재료의 계량 오차])
		H --> J([측정단위, 재료의 계량 오차])
		I --> J([측정단위, 재료의 계량 오차])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def material_quantity_tolerance(sITypMat) -> RuleUnitResult:
        """재료의 계량 오차

        Args:
            sITypMat (str): 재료의 종류

        Returns:
            sOBatErr (str): 재료의 계량 오차
            sOMeaUni (str): 측정단위

        """
        assert isinstance(sITypMat, str)

        if sITypMat == "시멘트":
            sOMeaUni = "질량"
            sOBatErr = "-1%, +2%"
            return RuleUnitResult(
                result_variables = {
                    "sOMeaUni": sOMeaUni,
                    "sOBatErr": sOBatErr
            }
        )
        if sITypMat == "골재":
            sOMeaUni = "질량"
            sOBatErr = "±3%"
            return RuleUnitResult(
                result_variables = {
                    "sOMeaUni": sOMeaUni,
                    "sOBatErr": sOBatErr
            }
        )
        if sITypMat == "물":
            sOMeaUni = "질량 또는 부피"
            sOBatErr = "-2%, +1%"
            return RuleUnitResult(
                result_variables = {
                    "sOMeaUni": sOMeaUni,
                    "sOBatErr": sOBatErr
            }
        )
        if sITypMat == "혼화재":
            sOMeaUni = "질량"
            sOBatErr = "±2%"
            return RuleUnitResult(
                result_variables = {
                    "sOMeaUni": sOMeaUni,
                    "sOBatErr": sOBatErr
            }
        )
        if sITypMat == "혼화제":
            sOMeaUni = "질량 또는 부피"
            sOBatErr = "±3%"
            return RuleUnitResult(
                result_variables = {
                    "sOMeaUni": sOMeaUni,
                    "sOBatErr": sOBatErr
            }
        )
        else:
            assert 1 != 1