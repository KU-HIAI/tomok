import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS142010_02010303_01(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 14 20 10 2.1.3.3 (1)' # 건설기준문서
    ref_date = '2023-09-26'  # 디지털 건설문서 작성일
    doc_date = '2022-09-01'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '일반콘크리트'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    일반콘크리트
    2. 자재
    2.1 구성재료
    2.1.3 잔골재
    2.1.3.3 입도
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    #### 2.1.3.3 입도
    (1) 잔골재는 크고 작은 입자가 알맞게 혼합되어 있는 것으로서, 그 입도는 표 2.1-1의 범위를 표준으로 한다. 체가름 시험은 KS F 2502에 따른다.

표 2.1-1 잔골재의 표준 입도

\begin{table}[]
\begin{tabular}{|
>{\columncolor[HTML]{FFFFFF}}l |
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l |}
\hline
\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }                                                                          & \multicolumn{2}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 체를 통과한 것의 질량 백분율(\%)}}                                                                                                                                                                                               \\ \cline{2-3}
\multirow{-2}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}체의 호칭 치수\\ (mm)\end{tabular}}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 부순 잔골재}}                                                                                       & {\color[HTML]{333333} 부순 잔골재 이외의 잔골재}                                                                               \\ \hline
{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}10\\ 5\\ 2.5\\ 1.2\\ 0.6\\ 0.3\\ 0.15\end{tabular}}                     & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}100\\ 95-100\\ 80-100\\ 50-90\\ 25-65\\ 10-35\\ 2-15\end{tabular}}} & {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}100\\ 95-100\\ 80-100\\ 50-85\\ 25-60\\ 10-30\\ 2-10\end{tabular}} \\ \hline
\end{tabular}
\end{table}
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 잔골재의 표준입도"];
    B["KCS 14 31 30 2.1.3.3 (1)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 30 2.1.3.3 (1)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 부순 잔골재의 체 통과량"/];
		VarOut2[/"출력변수: 부순 잔골재 이외 잔골재의 체 통과량"/];

		VarIn1[/"입력변수: 체의 호칭 치수"/];
		VarIn2[/"입력변수: 부순 잔골재의 체 통과량"/];
		VarIn3[/"입력변수: 부순 잔골재 이외 잔골재의 체 통과량"/];



    VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2 & VarIn3
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{체의 호칭 치수}

		D --> |표 2.1-1|F{부순 잔골재의 체 통과량}
		D --> |표 2.1-1|G{부순 잔골재 이외의 잔골재의 체 통과량}

		F --> |True|H([PASS])
		F --> |False|I([FAIL])

		G --> |True|H([PASS])
		G --> |False|I([FAIL])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def standard_particle_size_of_aggregates(fINomSiz, fIPerCru, fIPerNon) ->str :
        """잔골재의 표준입도

        Args:
            fINomSiz (float): 체의 호칭 치수
            fIPerCru (float): 부순 잔골재의 체 통과량
            fIPerNon (float): 부순 잔골재 이외 잔골재의 체 통과량

        Returns:
            sOPerCru (string): 부순 잔골재의 체 통과량
            sOIPerNon (string): 부순 잔골재 이외 잔골재의 체 통과량

        """

        if fINomSiz == 10:
            if fIPerCru == 100:
                sOPerCru = "PASS"
                if fIPerNon == 100:
                    sOIPerNon = "PASS"
                    return sOPerCru, sOIPerNon
                else:
                    sOIPerNon = "FAIL"
                    return sOPerCru, sOIPerNon
            else:
                sOPerCru = "FAIL"
                if fIPerNon == 100:
                    sOIPerNon = "PASS"
                    return sOPerCru, sOIPerNon
                else:
                    sOIPerNon = "FAIL"
                    return sOPerCru, sOIPerNon
        elif fINomSiz == 5:
            if 95 < fIPerCru < 100:
                sOPerCru = "PASS"
                if 95< fIPerNon < 100:
                    sOIPerNon = "PASS"
                    return sOPerCru, sOIPerNon
                else:
                    sOIPerNon = "FAIL"
                    return sOPerCru, sOIPerNon
            else:
                sOPerCru = "FAIL"
                if 95< fIPerNon < 100:
                    sOIPerNon = "PASS"
                    return sOPerCru, sOIPerNon
                else:
                    sOIPerNon = "FAIL"
                    return sOPerCru, sOIPerNon

        elif fINomSiz == 2.5:
            if 80 < fIPerCru < 100:
                sOPerCru = "PASS"
                if 80 < fIPerNon < 100:
                    sOIPerNon = "PASS"
                    return sOPerCru, sOIPerNon
                else:
                    sOIPerNon = "FAIL"
                    return sOPerCru, sOIPerNon
            else:
                sOPerCru = "FAIL"
                if 80 < fIPerNon < 100:
                    sOIPerNon = "PASS"
                    return sOPerCru, sOIPerNon
                else:
                    sOIPerNon = "FAIL"
                    return sOPerCru, sOIPerNon

        elif fINomSiz == 1.2:
            if 50 < fIPerCru < 90:
                sOPerCru = "PASS"
                if 50 < fIPerNon < 85:
                    sOIPerNon = "PASS"
                    return sOPerCru, sOIPerNon
                else:
                    sOIPerNon = "FAIL"
                    return sOPerCru, sOIPerNon
            else:
                sOPerCru = "FAIL"
                if 50 < fIPerNon < 85:
                    sOIPerNon = "PASS"
                    return sOPerCru, sOIPerNon
                else:
                    sOIPerNon = "FAIL"
                    return sOPerCru, sOIPerNon

        elif fINomSiz == 0.6:
            if 25 < fIPerCru < 65:
                sOPerCru = "PASS"
                if 25 < fIPerNon < 65:
                    sOIPerNon = "PASS"
                    return sOPerCru, sOIPerNon
                else:
                    sOIPerNon = "FAIL"
                    return sOPerCru, sOIPerNon
            else:
                sOPerCru = "FAIL"
                if 25 < fIPerNon < 65:
                    sOIPerNon = "PASS"
                    return sOPerCru, sOIPerNon
                else:
                    sOIPerNon = "FAIL"
                    return sOPerCru, sOIPerNon

        elif fINomSiz == 0.3:
            if 10 < fIPerCru < 35:
                sOPerCru = "PASS"
                if 10 < fIPerNon < 30:
                    sOIPerNon = "PASS"
                    return sOPerCru, sOIPerNon
                else:
                    sOIPerNon = "FAIL"
                    return sOPerCru, sOIPerNon
            else:
                sOPerCru = "FAIL"
                if 10 < fIPerNon < 30:
                    sOIPerNon = "PASS"
                    return sOPerCru, sOIPerNon
                else:
                    sOIPerNon = "FAIL"
                    return sOPerCru, sOIPerNon

        elif fINomSiz == 0.15:
            if 2 < fIPerCru < 15:
                sOPerCru = "PASS"
                if 2 < fIPerNon < 10:
                    sOIPerNon = "PASS"
                    return sOPerCru, sOIPerNon
                else:
                    sOIPerNon = "FAIL"
                    return sOPerCru, sOIPerNon
            else:
                sOPerCru = "FAIL"
                if 2 < fIPerNon < 10:
                    sOIPerNon = "PASS"
                    return sOPerCru, sOIPerNon
                else:
                    sOIPerNon = "FAIL"
                    return sOPerCru, sOIPerNon