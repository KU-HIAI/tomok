import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS143125_030102_05(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 14 31 25 3.1.2 (5)' # 건설기준문서
    ref_date = '2023-09-11'  # 디지털 건설문서 작성일
    doc_date = '2019-05-20'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '볼트 접합 및 핀 연결'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    볼트 접합 및 핀 연결
    3. 시공
    3.1.2 마찰면의 준비
    (5)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.1.2 마찰면의 준비
    (5) 품질관리 구분 ‘라’의 교량에서 마찰이음부의 마찰면에 도장을 할 경우에는 표 3.1-1에 준하여 무기질 아연말 프라이머(징크리치 페인트)를 사용한다.

표 3.1-1 무기질 아연말 프라이머를 도장할 경우의 조건

\begin{table}[]
\begin{tabular}{|
>{\columncolor[HTML]{FFFFFF}}l |
>{\columncolor[HTML]{FFFFFF}}l |}
\hline
{\color[HTML]{333333} 항목}                 & {\color[HTML]{333333} 조건}            \\ \hline
{\color[HTML]{333333} 접촉면 편면당 최소건조 도막두께}  & {\color[HTML]{333333} 30 ㎛ 이상}       \\ \hline
{\color[HTML]{333333} 접촉면의 합계 건조 도막두께}    & {\color[HTML]{333333} 90$\sim$200 ㎛} \\ \hline
{\color[HTML]{333333} 건조 도막 중 아연함유량}      & {\color[HTML]{333333} 80\% 이상}       \\ \hline
{\color[HTML]{333333} 아연분말 입경(50\% 평균입경)} & {\color[HTML]{333333} 10 ㎛ 이상}       \\ \hline
\end{tabular}
\end{table}



    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A[Title: 무기질 아연말 프라이머를 도장할 경우의 조건];
    B["KCS 14 31 25 3.1.2 (5)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 25 3.1.2 (5)"])

    subgraph Variable_def
    VarOut[/출력변수: 무기질 아연말 프라이머를 도장할 경우의 조건/];
    VarIn1[/입력변수: 접촉면 편면당 최소건조 도막두께/];
    VarIn2[/입력변수: 접촉면의 합계 건조 도막두께/];
    VarIn3[/입력변수: 건조 도막 중 아연함유량/];
    VarIn4[/입력변수: 아연분말 입경_50% 평균입경/];
    VarOut ~~~ VarIn1 &  VarIn2 & VarIn3 & VarIn4
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> M{교량에서 마찰이음부의 마찰면에 도장을 할 경우}
		M-->C{항목}
    C --> |접촉면 편면당 최소건조 도막두께|D["30 ㎛ 이상"]
    C --> |접촉면의 합계 건조 도막두께|E["90~200 ㎛"]
    C --> |"건조 도막 중 아연함유량"|F["80% 이상"]
    C --> |"아연분말 입경(50% 평균입경)"|G["10 ㎛ 이상"]


    D --> L(["무기질 아연말 프라이머를 도장할 경우의 조건"])
    E --> L(["무기질 아연말 프라이머를 도장할 경우의 조건"])
    F --> L(["무기질 아연말 프라이머를 도장할 경우의 조건"])
    G --> L(["무기질 아연말 프라이머를 도장할 경우의 조건"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def conditions_for_inorganic_zinc_primer_coating(bIUniThi, bITotThi, bIZinPai, bIParSiz) ->str :
        """마찰면의 무기질 아연말 프라이머 도장 조건

        Args:
            bIUniThi (boolean): 접촉면 편면당 최소건조 도막두께
            bITotThi (boolean): 접촉면의 합계 건조 도막두께
            bIZinPai (boolean): 건조 도막 중 아연함유량
            bIParSiz (boolean): 아연분말 입경(50% 평균입경)

        Returns:
            sOZinCoa (string): 마찰면의 무기질 아연말 프라이머 도장 조건


        """

        if bIUniThi == True:
            sOZinCoa = "30 ㎛ 이상"
            return sOZinCoa
        elif bITotThi == True:
            sOZinCoa = "90~200 ㎛"
            return sOZinCoa
        elif bIZinPai == True:
            sOZinCoa = "80% 이상"
            return sOZinCoa
        elif bIParSiz == True:
            sOZinCoa = "10 ㎛ 이상"
            return sOZinCoa