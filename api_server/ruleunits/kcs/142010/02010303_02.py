import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142010_02010303_02(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = False # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 14 20 10 2.1.3.3 (2)' # 건설기준문서
    ref_date = '2022-09-01'  # 디지털 건설문서 작성일
    doc_date = '2024-02-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '일반콘크리트'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    일반콘크리트
    2. 자재
    2.1 구성재료
    2.1.3 잔골재
    2.1.3.3 입도
    (2)
    """

    # 건설기준문서내용(text)
    content = """
    #### 2.1.3.3 입도
    (2) 표 2.1-1의 입도 범위 내의 잔골재를 사용하여야 하며, 입도가 이 범위를 벗어난 잔골재를 쓰는 경우에는, 두 종류 이상의 잔골재를 혼합하여 입도를 조정해서 사용하여야 한다. 혼합 잔골재의 경우 부순 잔골재 이외의 잔골재의 표준입도에 따른다. 또한, 표 2.1-1에 표시된 연속된 두 개의 체 사이를 통과하는 양의 백분율이 45 %를 넘지 않아야 한다.


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
    A["Title: 혼합잔골재의 입도"];
    B["KCS 14 31 30 2.1.3.3 (2)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 30 2.1.3.3 (2)"])

    subgraph Variable_def
		VarIn1[/"입력변수: 체의 호칭 치수"/];
		VarIn2[/"입력변수: 혼합잔골재의 체 통과량"/];
		VarIn3[/"입력변수: 연속하는 두개의 체 사이 통과양의 백분율"/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{연속하는 두개의 체 사이\n 통과양의 백분율< 45%}
		Variable_def --> D{체의 호칭 치수}
		
		D --> E([혼합잔골재의 체 통과량])
		C --> J([PASS or Fail])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def non_standard_aggregate_particle_size(fIPasPer,fINomSiz) -> RuleUnitResult:
        """혼합잔골재의 표준 입도

        Args:
            fIPasPer (float): 연속하는 두개의 체 사이 통과양의 백분율
            fINomSiz (float): 체의 호칭 치수

        Returns:
            sOPerMix (str): 혼합잔골재의 체 통과량
            pass_fail (bool): 일반콘크리트 2.1.3.3 입도 (2)의 연속된 두 개의 체 사이를 통과하는 양의 백분율 판단 결과

        """
        assert isinstance(fINomSiz, float)
        assert isinstance(fIPasPer, float)
        assert 0 <= fIPasPer <= 100
        if fIPasPer <= 45:
            pass_fail = True
            if fINomSiz == 10:
                sOPerMix = "100"
                return RuleUnitResult(
                    result_variables = {
                        "pass_fail": pass_fail,
                        "sOPerMix": sOPerMix
                    }
                )
            if fINomSiz == 5:
                sOPerMix = "95-100"
                return RuleUnitResult(
                    result_variables = {
                        "pass_fail": pass_fail,
                        "sOPerMix": sOPerMix
                    }
                )
            if fINomSiz == 2.5:
                sOPerMix = "80-100"
                return RuleUnitResult(
                    result_variables = {
                        "pass_fail": pass_fail,
                        "sOPerMix": sOPerMix
                    }
                )
            if fINomSiz == 1.2:
                sOPerMix = "50-85"
                return RuleUnitResult(
                    result_variables = {
                        "pass_fail": pass_fail,
                        "sOPerMix": sOPerMix
                    }
                )
            if fINomSiz == 0.6:
                sOPerMix = "25-60"
                return RuleUnitResult(
                    result_variables = {
                        "pass_fail": pass_fail,
                        "sOPerMix": sOPerMix
                    }
                )
            if fINomSiz == 0.3:
                sOPerMix = "10-35"
                return RuleUnitResult(
                    result_variables = {
                        "pass_fail": pass_fail,
                        "sOPerMix": sOPerMix
                    }
                )
            if fINomSiz == 0.15:
                sOPerMix = "2-15"
                return RuleUnitResult(
                    result_variables = {
                        "pass_fail": pass_fail,
                        "sOPerMix": sOPerMix
                    }
                )
            else:
                assert 1 != 1
        else:
            pass_fail = False
            if fINomSiz == 10:
                sOPerMix = "100"
                return RuleUnitResult(
                    result_variables = {
                        "pass_fail": pass_fail,
                        "sOPerMix": sOPerMix
                    }
                )
            if fINomSiz == 5:
                sOPerMix = "95-100"
                return RuleUnitResult(
                    result_variables = {
                        "pass_fail": pass_fail,
                        "sOPerMix": sOPerMix
                    }
                )
            if fINomSiz == 2.5:
                sOPerMix = "80-100"
                return RuleUnitResult(
                    result_variables = {
                        "pass_fail": pass_fail,
                        "sOPerMix": sOPerMix
                    }
                )
            if fINomSiz == 1.2:
                sOPerMix = "50-85"
                return RuleUnitResult(
                    result_variables = {
                        "pass_fail": pass_fail,
                        "sOPerMix": sOPerMix
                    }
                )
            if fINomSiz == 0.6:
                sOPerMix = "25-60"
                return RuleUnitResult(
                    result_variables = {
                        "pass_fail": pass_fail,
                        "sOPerMix": sOPerMix
                    }
                )
            if fINomSiz == 0.3:
                sOPerMix = "10-35"
                return RuleUnitResult(
                    result_variables = {
                        "pass_fail": pass_fail,
                        "sOPerMix": sOPerMix
                    }
                )
            if fINomSiz == 0.15:
                sOPerMix = "2-15"
                return RuleUnitResult(
                    result_variables = {
                        "pass_fail": pass_fail,
                        "sOPerMix": sOPerMix
                    }
                )
            else:
                assert 1 != 1