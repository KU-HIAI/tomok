import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS142010_020209_01(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 14 20 10 2.2.9 (1)' # 건설기준문서
    ref_date = '2023-10-05'  # 디지털 건설문서 작성일
    doc_date = '2022-09-01'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
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
    VarOut1[/"출력변수: 공기연행 콘크리트의 공기량"/];
    VarOut2[/"출력변수: 운반 후 콘크리트 공기량 허용오차"/];

		VarIn1[/"입력변수: 굵은 골재의 최대 치수"/];
		VarIn2[/"노출등급"/];

    VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{노출등급}

		D --> |"'EF2' or 'EF3' or 'EF4'"|E{굵은 골재의 최대 치수}
		D --> |"'EF1'"|F{굵은 골재의 최대 치수}

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
    def air_content_of_air_entrained_concrete(sIClaUne, fISizCoa) -> str:
        """공기연행 콘크리트의 공기량

        Args:
            sIClaUne (string): 노출등급
            fISizCoa (float): 굵은 골재의 최대 치수

        Returns:
            fOAirCon (float): 공기연행 콘크리트의 공기량
            sOAirTol (string): 운반 후 콘크리트 공기량 허용오차

        """

        if (sIClaUne == "심한 노출" or sIClaUne == "EF2" or sIClaUne == "EF3" or sIClaUne == "EF4"):
            if fISizCoa == 10:
                fOAirCon = 7.5
                fOAirTol = "±1.5% 이내"
            if fISizCoa == 15:
                fOAirCon = 7.0
                fOAirTol = "±1.5% 이내"
            if fISizCoa == 20:
                fOAirCon = 6.0
                fOAirTol = "±1.5% 이내"
            if fISizCoa == 25:
                fOAirCon = 6.0
                fOAirTol = "±1.5% 이내"
            if fISizCoa == 40:
                fOAirCon = 5.5
                fOAirTol = "±1.5% 이내"
            return fOAirCon, fOAirTol

        elif (sIClaUne == "일반 노출" or sIClaUne == "EF1"):
            if fISizCoa == 10:
                fOAirCon = 6.0
                fOAirTol = "±1.5% 이내"
            if fISizCoa == 15:
                fOAirCon = 5.5
                fOAirTol = "±1.5% 이내"
            if fISizCoa == 20:
                fOAirCon = 5.0
                fOAirTol = "±1.5% 이내"
            if fISizCoa == 25:
                fOAirCon = 4.5
                fOAirTol = "±1.5% 이내"
            if fISizCoa == 40:
                fOAirCon = 4.5
                fOAirTol = "±1.5% 이내"
            return fOAirCon, fOAirTol


