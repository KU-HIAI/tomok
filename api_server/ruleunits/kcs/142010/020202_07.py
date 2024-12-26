import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142010_020202_07(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = True # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 14 20 10 2.2.2 (7)' # 건설기준문서
    ref_date = '2022-09-01'  # 디지털 건설문서 작성일
    doc_date = '2024-02-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '일반콘크리트'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    일반콘크리트
    2. 자재
    2.2 배합
    2.2.2 배합강도
    (7)
    """

    # 건설기준문서내용(text)
    content = """
    #### 2.2.2 배합강도
    (7) 콘크리트 압축강도의 표준편차를 알지 못할 때, 또는 압축강도의 시험 횟수가 14회 이하인 경우 콘크리트의 배합강도는 표 2.2-3과 같이 정할 수 있다.

표 2.2-3 압축강도의 시험 횟수가 14회 이하이거나 기록이 없는 경우의 배합강도
\begin{table}[]
\begin{tabular}{|
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l |}
\hline
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 호칭강도(MPa)}}                                                           & {\color[HTML]{333333} 배합강도(MPa)}                                                                 \\ \hline
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}21 미만\\ 21 이상 35 이하\\ 35 초과\end{tabular}}} & {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}fcn  + 7\\ fcn + 8.5\\ 1.1fcn + 5\end{tabular}} \\ \hline
\multicolumn{2}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}                                                                                                                                                                       \\ \hline
\end{tabular}
\end{table}
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A[Title: 압축강도의 시험 횟수가 14회 이하이거나 기록이 없는 경우의 콘크리트 배합강도];
    B["KCS 14 20 10 2.2.2 (7)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 10 2.2.2 (7)"])

    subgraph Variable_def
    VarIn1[/입력변수: 콘크리트 압축강도 표준편차/];
    VarIn2[/입력변수: 압축강도 시험 횟수/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"콘크리트 압축강도 표준편차 = False \n or \n 압축강도의 시험 횟수 ≤ 14 \n\n"}
    C --> |True|D{"호칭강도 < 21 \n 21≤호칭강도≤35 \n 호칭강도>35 \n\n "}

    D -->  |호칭강도 < 21|F["<img src='https://latex.codecogs.com/png.image?\dpi{500} f_{cr}=f_{cn}&plus;7'>-----------------------"]
    D -->  |21≤호칭강도≤35|G["<img src='https://latex.codecogs.com/png.image?\dpi{500} f_{cr}=f_{cn}&plus;8.5'>-------------------------"]
    D -->  |호칭강도>35|H["<img src='https://latex.codecogs.com/png.image?\dpi{500} 1.1*f_{cr}=f_{cn}&plus;8.5'>-------------------------------"]

		F & G & H  --> End(["배합강도"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def concrete_mix_strength_14or_fewer_or_no_record(bIStaDev, nINumTes, fINomStr) -> RuleUnitResult:
        """압축강도의 시험 횟수가 14회 이하이거나 기록이 없는 경우의 콘크리트 배합강도

        Args:
            bIStaDev (bool): 콘크리트 압축강도 표준편차
            nINumTes (int): 압축강도 시험 횟수
            fINomStr (float): 호칭강도

        Returns:
            fOStrPro (float): 콘크리트 배합강도
        """
        assert isinstance(bIStaDev, bool)
        assert isinstance(nINumTes, int)
        assert isinstance(fINomStr, float)
        assert bIStaDev == False
        assert 0 <= nINumTes <= 14
        assert 0 <= fINomStr

        if (bIStaDev == False) and (nINumTes <= 14):
            if fINomStr < 21:
                fOStrPro = fINomStr + 7
                return RuleUnitResult(
                    result_variables = {
                        "fOStrPro": fOStrPro
                    }
                )
            if 21 <= fINomStr <= 35:
                fOStrPro = fINomStr + 8.5
                return RuleUnitResult(
                    result_variables = {
                        "fOStrPro": fOStrPro
                    }
                )
            if fINomStr > 35:
                fOStrPro = 1.1*(fINomStr) + 5
                return RuleUnitResult(
                    result_variables = {
                        "fOStrPro": fOStrPro
                    }
                )