import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142010_030302_08(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = True # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 14 20 10 3.3.2 (8)' # 건설기준문서
    ref_date = '2022-09-01'  # 디지털 건설문서 작성일
    doc_date = '2024-05-17'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '일반콘크리트'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    일반콘크리트
    3. 시공
    3.3 타설
    3.3.2 타설
    (8)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.3.2 타설
    (8) 콘크리트를 2층 이상으로 나누어 타설할 경우, 상층의 콘크리트 타설은 원칙적으로 하층의 콘크리트가 굳기 시작하기 전에 해야 하며, 상층과 하층이 일체가 되도록 시공한다. 또한, 콜트조인트가 발생하지 않도록 하나의 시공구획의 면적, 콘크리트의 공급능력, 이어치기 허용시간간격 등을 정하여야 한다. 이어치기 허용시간 간격은 표 3.3-1을 표준으로 한다.

표 3.3-1 허용 이어치기 시간간격의 표준

\begin{table}[]
\begin{tabular}{|
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l |}
\hline
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 외기온도}}    & \multicolumn{2}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 허용 이어치기 시간간격}} \\ \hline
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 25 ℃ 초과}} & \multicolumn{2}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 2.0시간}}        \\ \hline
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 25 ℃ 이하}} & \multicolumn{2}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 2.5시간}}        \\ \hline
\multicolumn{3}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 주) 허용 이어치기 시간간격은 하층 콘크리트 비비기 시작에서부터 콘크리트 타설 완료한 후, 상층 콘크리트가 타설되기까지의 시간}}                     \\ \hline
\end{tabular}
\end{table}

    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 허용 이어치기 시간간격"];
    B["KCS 14 20 10 3.3.2 (8)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 10 3.3.2 (8)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 허용 이어치기 시간간격"/];
		VarIn1[/"입력변수: 외기온도"/];
    VarOut1 ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{"외기온도 > 25℃"}

		D --> |True|E[2.0시간]
		D --> |False|F[2.5시간]

		E --> G([허용 이어치기 시간간격])
		F --> G([허용 이어치기 시간간격])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def splicing_time_interval(fIOutTem) -> RuleUnitResult:
        """허용 이어치기 시간간격

        Args:
            fIOutTem (float): 외기온도

        Returns:
            fOAllPou (float): 허용 이어치기 시간간격
        """
        assert isinstance(fIOutTem, float)

        if fIOutTem > 25:
            fOAllPou = 2.0
            return RuleUnitResult(
                result_variables = {
                    "fOAllPou": fOAllPou
            }
        )
        else:
            fOAllPou = 2.5
            return RuleUnitResult(
                result_variables = {
                    "fOAllPou": fOAllPou
            }
        )