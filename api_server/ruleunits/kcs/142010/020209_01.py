import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142010_020209_01(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = False # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 14 20 10 2.2.9 (1)' # 건설기준문서
    ref_date = '2022-09-01'  # 디지털 건설문서 작성일
    doc_date = '2024-02-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '일반콘크리트'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    일반콘크리트
    2. 자재
    2.2 배합
    2.2.9 공기연행콘크리트의 공기량
    (1))
    """

    # 건설기준문서내용(text)
    content = """
    #### 2.2.9 공기연행콘크리트의 공기량
    (1) AE제, AE감수제 또는 고성능AE감수제를 사용한 콘크리트의 공기량은 굵은 골재 최대 치수와 노출등급을 고려하여 표 2.2-6과 같이 정하며, 운반 후 공기량은 이 값에서 ±1.5% 이내이어야 한다.

표 2.2-6 공기연행콘크리트 공기량의 표준값

\begin{table}[]
\begin{tabular}{|
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l |}
\hline
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}                                                               & \multicolumn{2}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 공기량(\%)}}                                                                                                                                                          \\ \cline{2-3}
\multicolumn{1}{|l|}{\multirow{-2}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 굵은 골재의 최대 치수(mm)}}}                             & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 심한 노출1)}}                                                             & {\color[HTML]{333333} 일반 노출2)}                                                             \\ \hline
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}10\\ 15\\ 20\\ 25\\ 40\end{tabular}}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}7.5\\ 7.0\\ 6.0\\ 6.0\\ 5.5\end{tabular}}} & {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}6.0\\ 5.5\\ 5.0\\ 4.5\\ 4.5\end{tabular}} \\ \hline
\multicolumn{3}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}주 1) 노출등급 EF2, EF3, EF4\\ 2) 노출등급 EF1\end{tabular}}}                                                                                                                                                                                                                         \\ \hline
\end{tabular}
\end{table}
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 공기연행 콘크리트의 공기량"];
    B["KCS 14 31 30 2.2.9 (1)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 30 2.2.9 (1)"])

    subgraph Variable_def
		VarIn1[/"입력변수: 굵은 골재의 최대 치수"/];
		VarIn2[/"노출등급"/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{노출등급}

		D --> |"심한 노출"|E{굵은 골재의 최대 치수}
		D --> |"일반 노출"|F{굵은 골재의 최대 치수}

		E --> |10|H[7.5]
		E --> |15|I[7.0]
		E --> |20|J[6.0]
		E --> |25|K[6.0]
		E --> |40|L[5.5]

		F --> |10|M[6.0]
		F --> |15|N[5.5]
		F --> |20|O[5.0]
		F --> |25|P[4.5]
		F --> |40|Q[4.5]



		H --> R([공기연행 콘크리트의 공기량])
		I --> R
		J --> R
		K --> R
		L --> R
		M --> R
		N --> R
		O --> R
		P --> R
		Q --> R

	  D --> |all|S[±1.5]
		S --> T([운반 후 콘크리트 공기량 허용오차])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def air_content_of_air_entrained_concrete(sIClaUne, fISizCoa) -> RuleUnitResult:
        """공기연행 콘크리트의 공기량

        Args:
            sIClaUne (str): 노출등급
            fISizCoa (float): 굵은 골재의 최대 치수

        Returns:
            fOAirCon (float): 공기연행 콘크리트의 공기량
            sOAirTol (str): 운반 후 콘크리트 공기량 허용오차

        """
        assert isinstance(sIClaUne, str)
        assert isinstance(fISizCoa, float)

        if (sIClaUne == "심한 노출" or sIClaUne == "EF2" or sIClaUne == "EF3" or sIClaUne == "EF4"):
            if fISizCoa == 10:
                fOAirCon = 7.5
                return RuleUnitResult(
                    result_variables = {
                        "fOAirCon": fOAirCon,
                        "sOAirTol": "±1.5% 이내"
                }
            )
            if fISizCoa == 15:
                fOAirCon = 7.0
                return RuleUnitResult(
                    result_variables = {
                        "fOAirCon": fOAirCon,
                        "sOAirTol": "±1.5% 이내"
                }
            )
            if fISizCoa == 20:
                fOAirCon = 6.0
                return RuleUnitResult(
                    result_variables = {
                        "fOAirCon": fOAirCon,
                        "sOAirTol": "±1.5% 이내"
                }
            )
            if fISizCoa == 25:
                fOAirCon = 6.0
                return RuleUnitResult(
                    result_variables = {
                        "fOAirCon": fOAirCon,
                        "sOAirTol": "±1.5% 이내"
                }
            )
            if fISizCoa == 40:
                fOAirCon = 5.5
                return RuleUnitResult(
                    result_variables = {
                        "fOAirCon": fOAirCon,
                        "sOAirTol": "±1.5% 이내"
                }
            )
            else:
                assert 1 != 1
        elif (sIClaUne == "일반 노출" or sIClaUne == "EF1"):
            if fISizCoa == 10:
                fOAirCon = 6.0
                return RuleUnitResult(
                    result_variables = {
                        "fOAirCon": fOAirCon,
                        "sOAirTol": "±1.5% 이내"
                }
            )
            if fISizCoa == 15:
                fOAirCon = 5.5
                return RuleUnitResult(
                    result_variables = {
                        "fOAirCon": fOAirCon,
                        "sOAirTol": "±1.5% 이내"
                }
            )
            if fISizCoa == 20:
                fOAirCon = 5.0
                return RuleUnitResult(
                    result_variables = {
                        "fOAirCon": fOAirCon,
                        "sOAirTol": "±1.5% 이내"
                }
            )
            if fISizCoa == 25:
                fOAirCon = 4.5
                return RuleUnitResult(
                    result_variables = {
                        "fOAirCon": fOAirCon,
                        "sOAirTol": "±1.5% 이내"
                }
            )
            if fISizCoa == 40:
                fOAirCon = 4.5
                return RuleUnitResult(
                    result_variables = {
                        "fOAirCon": fOAirCon,
                        "sOAirTol": "±1.5% 이내"
                }
            )
            else:
                assert 1 != 1
        else:
            assert 1 != 1