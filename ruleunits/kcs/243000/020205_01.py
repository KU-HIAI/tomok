import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS243000_020205_01(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 30 00 2.2.5 (1)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-08'
    title = '스터드의 치수 및 허용오차'

    # 건설기준문서항목 (분류체계정보)
    description = """
    강교량공사
    2. 자재
    2.2 사용재료
    2.2.5 스터드형 전단연결재
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    ####(1) 형상, 치수 및 허용오차는 표 2.2-3에 따른다.
    표 2.2-3 스터드의 형상, 치수 및 허용오차
    (단위 : mm)
    \begin{table}[]
    \begin{tabular}{llllllll}
    \multirow{2}{*}{호칭} & \multicolumn{2}{l}{직경(d)}    & \multicolumn{2}{l}{머리직경}     & \multirow{2}{*}{최소머리두께(T)} & \multirow{2}{*}{\begin{tabular}[c]{@{}l@{}}헌치부\\ 반지름(r)\end{tabular}} & \multirow{2}{*}{표준형상 및 치수 표시기호} \\
                        & 기준치수 & 허용오차                  & 기준치수 & 허용오차                  &                            &                                                                       &                                 \\
    13                  & 13.0 & \multirow{2}{*}{±0.3} & 22.0 & \multirow{5}{*}{±0.4} & \multirow{5}{*}{10}        & \multirow{5}{*}{2∼3}                                                  & \multirow{5}{*}{<img src='http://drive.google.com/uc?export=view&id=1ZhDZZxAaR5U2jNHs6zuG1CHVZDI9fbrf_link' /><br>}               \\
    16                  & 16.0 &                       & 29.0 &                       &                            &                                                                       &                                 \\
    19                  & 19.0 & \multirow{3}{*}{±0.4} & 32.0 &                       &                            &                                                                       &                                 \\
    22                  & 22.0 &                       & 35.0 &                       &                            &                                                                       &                                 \\
    25                  & 25.0 &                       & 38.0 &                       &                            &                                                                       &                                 \\
    \multicolumn{8}{l}{주 1) 길이(L)의 허용오차는 ±1.6 ㎜를 기준으로 함.}
    \end{tabular}
    \end{table}
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 스터드의 치수 및 허용오차];
    B["KCS 24 30 00 2.2.5 (1)"];
    B ~~~ A
    end

    KCS(["KCS 24 30 00 2.2.5 (1)"])

    subgraph Variable_def
    VarOut[/출력변수: 스터드의 치수 및 허용오차/];
    VarIn0[/입력변수: 호칭/]
    VarIn1[/입력변수: 직경/];
    VarIn2[/입력변수: 머리직경/];
    VarIn3[/입력변수: 최소머리두께/];
    VarIn4[/입력변수: 현치부 반지름/];
    VarIn5[/입력변수: 길이/];
    VarOut ~~~ VarIn0 & VarIn1 & VarIn2
    VarIn0 & VarIn1 & VarIn2  ~~~ VarIn3 & VarIn4 & VarIn5
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"교량구조용 압연강재"}
    C --> D{"직경, 머리직경 \n 최소머리두께 \n 헌치부 반지름\n 길이\n."}
    D --> |표3.2-3|S(["스터드의 치수 및 허용오차"])
    """

    @rule_method
    def dimension_stud(nINomDia, bID,bIHeaDia,bIT,bIR,bIL)-> str:
        """
        Args:
            nINomDia (integer): 호칭
            bID (boolean): 직경
            bIHeaDia (boolean): 머리직경
            bIT (boolean): 최소머리두께
            bIR (boolean): 헌치부 반지름
            bIL (boolean): 길이
        Returns:
            sODimStu (string): 스터드의 치수 및 허용오차
        """
        if bID:
            if nINomDia == 13:
                sODimStu = "13.0±0.3 mm"
            elif nINomDia == 16:
                sODimStu = "16.0±0.3 mm"
            elif nINomDia == 19:
                sODimStu = "19.0±0.4 mm"
            elif nINomDia == 22:
                sODimStu = "22.0±0.4 mm"
            elif nINomDia == 25:
                sODimStu = "25.0±0.4 mm"
            else:
                return "호칭은 13, 16, 19, 22, 25 중에 선택해주세요"
        elif bIHeaDia:
            if nINomDia == 13:
                sODimStu = "22.0±0.4 mm"
            elif nINomDia == 16:
                sODimStu = "29.0±0.4 mm"
            elif nINomDia == 19:
                sODimStu = "32.0±0.4 mm"
            elif nINomDia ==22:
                sODimStu = "35.0±0.4 mm"
            elif nINomDia == 25:
                sODimStu = "38.0±0.4 mm"
            else:
                return "호칭은 13, 16, 19, 22, 25 중에 선택해주세요"
        elif bIT:
            sODimStu = "10 mm"
        elif bIR:
            sODimStu = "2~3 mm"
        elif bIL:
            sODimStu =  "허용오차: ±1.6 ㎜"
        else:
            return "직경, 머리직경, 최소머리두께, 헌치부 반지름, 길이 중에 선택해주세요"
        return sODimStu