import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS142010_020202_07(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 14 20 10 2.2.2 (7)' # 건설기준문서
    ref_date = '2023-11-29'  # 디지털 건설문서 작성일
    doc_date = '2022-09-01'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
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
    VarOut[/출력변수: 배합강도/];
    VarIn1[/입력변수: 콘크리트 압축강도 표준편차/];
    VarIn2[/입력변수: 압축강도 시험 횟수/];

    VarOut ~~~ VarIn1 & VarIn2
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
    def concrete_mix_strength_14or_fewer_or_no_record(bIStaDev, nINumTes, fIFcn) -> float:
        """압축강도의 시험 횟수가 14회 이하이거나 기록이 없는 경우의 콘크리트 배합강도

        Args:
            bIStaDev (float): 콘크리트 압축강도 표준편차
            nINumTes (integer): 압축강도 시험 횟수
            fIFcn (float): 호칭강도

        Returns:
            fOFcr (float): 콘크리트 배합강도
        """

        if (bIStaDev == False) and (nINumTes <= 14):
            if fIFcn < 21:
              fOFcr = fIFcn + 7
            if 21 <= fIFcn <= 35:
              fOFcr = fIFcn + 8.5
            if fIFcn > 35:
              fOFcr = 1.1*(fIFcn) + 5
            return fOFcr