import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142010_02010403_01(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = False # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 14 20 10 2.1.4.3 (1)' # 건설기준문서
    ref_date = '2022-09-01'  # 디지털 건설문서 작성일
    doc_date = '2024-02-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '일반콘크리트'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    일반콘크리트
    2. 자재
    2.1 구성재료
    2.1.4 굵은 골재
    2.1.4.3 입도
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    #### 2.1.4.3 입도
    (1) 굵은 골재는 크고 작은 입자가 알맞게 혼합되어 있는 것으로, 그 입도는 표 2.1-3의 범위를 표준으로 한다. 골재의 체가름 시험은 KS F 2502에 따른다.

표 2.1-3 굵은 골재의 표준 입도
\begin{table}[]
\begin{tabular}{|
>{\columncolor[HTML]{FFFFFF}}l |
>{\columncolor[HTML]{FFFFFF}}l |
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l |}
\hline
\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }                       & \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }                                                                                       & \multicolumn{13}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 체를 통과하는 것의 질량 백분율(\%)}}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           \\ \cline{3-15}
\multirow{-2}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 골재번호}} & \multirow{-2}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}체의 호칭\\ 치수(mm)\\ 체의\\ 크기(mm)\end{tabular}}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 100}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 90}}          & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 75}}  & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 65}}          & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 50}}          & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 40}}          & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 25}}          & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 20}}          & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 13}}          & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 10}}          & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 5}}          & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 2.5}}       & {\color[HTML]{333333} 1.2}      \\ \hline
{\color[HTML]{333333} 1}                                              & {\color[HTML]{333333} 90$\sim$40}                                                                                                     & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 100}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 90$\sim$100}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 25$\sim$60}}  & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0$\sim$15}}   & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0$\sim$5}}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}           & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}          & {\color[HTML]{333333} }         \\ \hline
{\color[HTML]{333333} 2}                                              & {\color[HTML]{333333} 65$\sim$40}                                                                                                     & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 100}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 90$\sim$100}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 35$\sim$70}}  & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0$\sim$15}}   & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0$\sim$5}}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}           & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}          & {\color[HTML]{333333} }         \\ \hline
{\color[HTML]{333333} 3}                                              & {\color[HTML]{333333} 50$\sim$25}                                                                                                     & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 100}}         & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 90$\sim$100}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 35$\sim$70}}  & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0$\sim$15}}   & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0$\sim$5}}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}           & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}          & {\color[HTML]{333333} }         \\ \hline
{\color[HTML]{333333} 357}                                            & {\color[HTML]{333333} 50$\sim$5}                                                                                                      & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 100}}         & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 95$\sim$100}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 35$\sim$70}}  & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 10$\sim$30}}  & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0$\sim$5}}   & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}          & {\color[HTML]{333333} }         \\ \hline
{\color[HTML]{333333} 4}                                              & {\color[HTML]{333333} 40$\sim$20}                                                                                                     & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 100}}         & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 90$\sim$100}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 20$\sim$55}}  & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0$\sim$15}}   & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0$\sim$5}}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}           & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}          & {\color[HTML]{333333} }         \\ \hline
{\color[HTML]{333333} 467}                                            & {\color[HTML]{333333} 40$\sim$5}                                                                                                      & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 100}}         & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 95$\sim$100}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 35$\sim$70}}  & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 10$\sim$30}}  & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0$\sim$5}}   & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}          & {\color[HTML]{333333} }         \\ \hline
{\color[HTML]{333333} 5}                                              & {\color[HTML]{333333} 25$\sim$13}                                                                                                     & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 100}}         & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 90$\sim$100}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 20$\sim$55}}  & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0$\sim$10}}   & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0$\sim$5}}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}           & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}          & {\color[HTML]{333333} }         \\ \hline
{\color[HTML]{333333} 57}                                             & {\color[HTML]{333333} 25$\sim$5}                                                                                                      & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 100}}         & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 95$\sim$100}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 25$\sim$60}}  & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0$\sim$10}}  & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0$\sim$5}}  & {\color[HTML]{333333} }         \\ \hline
{\color[HTML]{333333} 6}                                              & {\color[HTML]{333333} 20$\sim$13}                                                                                                     & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 100}}         & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 90$\sim$100}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0$\sim$10}}   & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0$\sim$5}}   & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}          & {\color[HTML]{333333} }         \\ \hline
{\color[HTML]{333333} 67}                                             & {\color[HTML]{333333} 20$\sim$5}                                                                                                      & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 100}}         & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 90$\sim$100}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 20$\sim$55}}  & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0$\sim$10}}  & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0$\sim$5}}  & {\color[HTML]{333333} }         \\ \hline
{\color[HTML]{333333} 7}                                              & {\color[HTML]{333333} 13$\sim$5}                                                                                                      & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 100}}         & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 90$\sim$100}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 40$\sim$70}}  & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0$\sim$15}}  & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0$\sim$5}}  & {\color[HTML]{333333} }         \\ \hline
{\color[HTML]{333333} 78}                                             & {\color[HTML]{333333} 13$\sim$2.5}                                                                                                    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 100}}         & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 90$\sim$100}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 40$\sim$75}}  & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 5$\sim$25}}  & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0$\sim$10}} & {\color[HTML]{333333} 0$\sim$5} \\ \hline
{\color[HTML]{333333} 8}                                              & {\color[HTML]{333333} 10$\sim$2.5}                                                                                                    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}            & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 100}}         & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 85$\sim$100}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 10$\sim$30}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0$\sim$10}} & {\color[HTML]{333333} 0$\sim$5} \\ \hline
\end{tabular}
\end{table}

    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 굵은 골재의 표준입도"];
    B["KCS 14 31 30 2.1.4.3 (1)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 30 2.1.4.3 (1)"])

    subgraph Variable_def
		VarIn1[/"입력변수: 골재 번호"/];
		VarIn2[/"입력변수: 체의 호칭 치수"/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{골재번호, 체의 호칭 치수}

		D --> |표 2.1-3|F([체를 통과하는 것의 질량 백분율])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def standard_coarse_aggregate_particle_size(nINumAgg, fINomSiz) -> RuleUnitResult:
        """굵은 골재의 표준입도

        Args:
            nINumAgg (int): 골재 번호
            fINomSiz (float): 체의 호칭 치수

        Returns:
            sOPerPas (str): 체를 통과하는 것의 질량 백분율

        """
        assert isinstance(nINumAgg, int)
        assert isinstance(fINomSiz, float)

        if nINumAgg == 1:
            if fINomSiz == 100:
                sOPerPas = "100"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 90:
                sOPerPas = "90~100"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 65:
                sOPerPas = "25~60"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 40:
                sOPerPas = "0~15"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 20:
                sOPerPas = "0~5"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            else:
                assert 1 != 1
        if nINumAgg == 2:
            if fINomSiz == 75:
                sOPerPas = "100"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 65:
                sOPerPas = "90~100"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 50:
                sOPerPas = "35~70"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 40:
                sOPerPas = "0~15"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 20:
                sOPerPas = "0~5"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            else:
                assert 1 != 1
        if nINumAgg == 3:
            if fINomSiz == 65:
                sOPerPas = "100"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 50:
                sOPerPas = "90~100"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 40:
                sOPerPas = "35~70"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 25:
                sOPerPas = "0~15"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 13:
                sOPerPas = "0~5"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            else:
                assert 1 != 1
        if nINumAgg == 357:
            if fINomSiz == 65:
                sOPerPas = "100"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 50:
                sOPerPas = "95~100"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 25:
                sOPerPas = "35~70"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 13:
                sOPerPas = "10~30"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 5:
                sOPerPas = "0~5"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            else:
                assert 1 != 1
        if nINumAgg == 4:
            if fINomSiz == 50:
                sOPerPas = "100"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 40:
                sOPerPas = "90~100"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 25:
                sOPerPas = "20~55"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 20:
                sOPerPas = "0~15"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 10:
                sOPerPas = "0~5"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            else:
                assert 1 != 1
        if nINumAgg == 467:
            if fINomSiz == 50:
                sOPerPas = "100"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 40:
                sOPerPas = "95~100"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 20:
                sOPerPas = "35~70"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 10:
                sOPerPas = "10~30"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 5:
                sOPerPas = "0~5"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            else:
                assert 1 != 1
        if nINumAgg == 5:
            if fINomSiz == 40:
                sOPerPas = "100"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 25:
                sOPerPas = "90~100"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 20:
                sOPerPas = "20~55"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 13:
                sOPerPas = "0~10"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 10:
                sOPerPas = "0~5"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            else:
                assert 1 != 1
        if nINumAgg == 57:
            if fINomSiz == 40:
                sOPerPas = "100"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 25:
                sOPerPas = "95~100"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 13:
                sOPerPas = "25~60"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 5:
                sOPerPas = "0~10"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 2.5:
                sOPerPas = "0~5"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            else:
                assert 1 != 1
        if nINumAgg == 6:
            if fINomSiz == 25:
                sOPerPas = "100"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 20:
                sOPerPas = "90~100"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 10:
                sOPerPas = "0~10"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 5:
                sOPerPas = "0~5"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            else:
                assert 1 != 1
        if nINumAgg == 67:
            if fINomSiz == 25:
                sOPerPas = "100"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 20:
                sOPerPas = "90~100"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 10:
                sOPerPas = "20~55"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 5:
                sOPerPas = "0~10"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 2.5:
                sOPerPas = "0~5"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            else:
                assert 1 != 1
        if nINumAgg == 7:
            if fINomSiz == 20:
                sOPerPas = "100"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 13:
                sOPerPas = "90~100"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 10:
                sOPerPas = "40~70"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 5:
                sOPerPas = "0~15"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 2.5:
                sOPerPas = "0~5"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            else:
                assert 1 != 1
        if nINumAgg == 78:
            if fINomSiz == 20:
                sOPerPas = "100"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 13:
                sOPerPas = "90~100"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 10:
                sOPerPas = "40~75"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 5:
                sOPerPas = "5~25"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 2.5:
                sOPerPas = "0~10"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 1.2:
                sOPerPas = "0~5"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            else:
                assert 1 != 1
        if nINumAgg == 8:
            if fINomSiz == 13:
                sOPerPas = "100"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 10:
                sOPerPas = "85~100"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 5:
                sOPerPas = "10~30"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 2.5:
                sOPerPas = "0~10"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            if fINomSiz == 1.2:
                sOPerPas = "0~5"
                return RuleUnitResult(
                    result_variables = {
                        "sOPerPas": sOPerPas,
                    }
                )
            else:
                assert 1 != 1
        else:
            assert 1 != 1