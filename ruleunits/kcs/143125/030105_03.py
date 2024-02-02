import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS143125_030105_03(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 14 31 25 3.1.5 (3)' # 건설기준문서
    ref_date = '2023-09-11'  # 디지털 건설문서 작성일
    doc_date = '2019-05-20'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '볼트 접합 및 핀 연결'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    볼트 접합 및 핀 연결
    3. 시공
    3.1.5 볼트조임
    (3)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.1.5 볼트조임
    (3) 볼트조임 순서
    ③ 1차조임은 프리세트형 토크렌치, 전동 임펙트렌치 등을 사용하여 표 3.1-5에 명시한 토크로 너트를 회전시켜 조인다. 다만 품질관리 구분 ‘라’ 교량 접합부의 볼트 1차조임은 표준볼트장력의 60%에 해당하는 토크를 적용한다.

표 3.1-5 1차조임 토크
(단위 : N·m)
\begin{table}[]
\begin{tabular}{|
>{\columncolor[HTML]{FFFFFF}}l |ll|}
\hline
\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }                                                 & \multicolumn{2}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 1차조임 토크}}                                                                            \\ \cline{2-3}
\multirow{-2}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 고장력볼트의 호칭}}                      & \multicolumn{1}{l|}{품질관리 구분 ‘나’, ‘다’}                                                                                                   & 품질관리 구분 ‘라’  \\ \hline
{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}M16\\ M20, M22\\ M24\\ M27\\ M30\end{tabular}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}100\\ 150\\ 200\\ 300\\ 400\end{tabular}}} & 표준볼트장력의 60\% \\ \hline
\end{tabular}
\end{table}
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A[Title: 볼트에 따른 1차조임 토크값];
    B["KCS 14 31 25 3.1.5 (3)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 25 3.1.5 (3)"])

    subgraph Variable_def
    VarOut[/출력변수: 1차조임 토크/];
    VarIn1[/입력변수: 품질관리 구분/];
    VarIn2[/입력변수: 고장력볼트의 호칭/];

    VarOut ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"품질관리 구분"}
    C --> |"품질관리 구분 = '나' or '다'"|D{"고장력볼트의 호칭"}
    C --> |"품질관리 구분 = '라'"|E{"고장력볼트의 호칭"}

    D --> |"'M16'"|F["100"]
    D --> |"'M20' or 'M22'"|G["150"]
    D --> |"'M24'"|H["200"]
    D --> |"'M27'"|I["300"]
    D --> |"'M30'"|J["400"]

    E --> |"'M16'"|K["100 * 0.6"]
    E --> |"'M20' or 'M22'"|L["150 * 0.6"]
    E --> |"'M24'"|M["200 * 0.6"]
    E --> |"'M27'"|N["300 * 0.6"]
    E --> |"'M30'"|O["400 * 0.6"]


		F  & G & H & I & J & K & L & M & N & O--> End([1차조임 토크])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def primary_tightening_torque_values_of_bolts(sIQuaCla, sIHigBol) ->float :
        """볼트에 따른 1차조임 토크값

        Args:
            sIQuaCla (string): 품질관리 구분
            sIHigBol (string): 고장력볼트의 호칭

        Returns:
            fOTigTor (float): 1차조임 토크
        """

        if (sIQuaCla == "나") or (sIQuaCla == "다"):
            if sIHigBol == "M16":
                fOTigTor = 100
            if (sIHigBol == "M20") or (sIHigBol == "M22"):
                fOTigTor = 150
            if sIHigBol == "M24":
                fOTigTor = 200
            if sIHigBol == "M27":
                fOTigTor = 300
            if sIHigBol == "M30":
                fOTigTor = 400
        if sIQuaCla == "라":
            if sIHigBol == "M16":
                fOTigTor = 100*0.6
            if (sIHigBol == "M20") or (sIHigBol == "M22"):
                fOTigTor = 150*0.6
            if sIHigBol == "M24":
                fOTigTor = 200*0.6
            if sIHigBol == "M27":
                fOTigTor = 300*0.6
            if sIHigBol == "M30":
                fOTigTor = 400*0.6
        return fOTigTor