import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS243000_030304_02(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 30 00 3.3.4 (2)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-14'
    title = '고장력 볼트'

    # 건설기준문서항목 (분류체계정보)
    description = """
    강교량공사
    3. 시공
    3.3 볼트접합
    3.3.4 시공
    (2)
    """

    # 건설기준문서내용(text)
    content = """
    ####(2) 고장력 볼트
    ① 볼트의 조임을 위한 기구(機具)의 보정은 작업개시 전 그 정밀도를 확인한다.
    ② 볼트의 조임은, 특별한 제한 사유가 있는 경우를 제외하고는 너트를 돌려서 축력을 도입한다. 볼트돌림을 할 때는 토크 계수값의 변화를 확인한다. 볼트의 조임을 토크법에 따라 할 때에는 표준 볼트축력이 균일하게 도입되도록 조임 토크를 조절한다.
    ③ 마찰접합 및 지압접합의 볼트는 표 3.3-2에 표시된 볼트의 설계축력을 얻을 수 있도록 조여야 한다.
    ④ 볼트의 조임축력은 설계축력에 10%를 증가시킨 값으로 한다.
    표 3.3-2 볼트축력 및 볼트조임축력
    \begin{table}[]
    \begin{tabular}{llllll}
    \multicolumn{6}{r}{(단위: kN)}                                                                                                                                                      \\
    \multirow{2}{*}{등급}   & \multirow{2}{*}{볼트호칭} & \multirow{2}{*}{\begin{tabular}[c]{@{}l@{}}설계볼트\\ 축력\end{tabular}} & \multirow{2}{*}{조임축력} & \multicolumn{2}{l}{5본 이상 볼트의 평균축력1)} \\
                        &                       &                                                                    &                       & 하한치               & 상한치              \\
    \multirow{3}{*}{F8T}  & M20                   & 130                                                                & 145                   & 135               & 150              \\
                        & M22                   & 160                                                                & 180                   & 170               & 185              \\
                        & M24                   & 190                                                                & 210                   & 195               & 215              \\
    \multirow{5}{*}{F10T} & M20                   & 160                                                                & 180                   & 170               & 185              \\
                        & M22                   & 200                                                                & 220                   & 210               & 230              \\
                        & M24                   & 235                                                                & 260                   & 245               & 270              \\
                        & M27                   & 310                                                                & 340                   & 315               & 355              \\
                        & M30                   & 375                                                                & 415                   & 390               & 435              \\
    \multirow{3}{*}{F13T} & M20                   & 215                                                                & 235                   & 220               & 240              \\
                        & M22                   & 265                                                                & 290                   & 275               & 300              \\
                        & M24                   & 305                                                                & 340                   & 320               & 350              \\
    \multicolumn{6}{l}{주:1) 시공 전 시험시공 검사값의 상ㆍ하한치}
    \end{tabular}
    \end{table}
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 고장력 볼트];
    B["KCS 24 30 00 3.3.4 (2)"];
    B ~~~ A
    end

    KCS(["KCS 24 30 00 3.3.4 (2)"])

    subgraph Variable_def
    VarOut1[/출력변수: 설계볼트축력/];
    VarOut2[/출력변수: 볼트조임축력/];
    VarIn1[/입력변수: 볼트등급/];
    VarIn2[/입력변수: 볼트호칭/];
    VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"검토항목"}
    C --> |"마찰접합 및 지압접합의 볼트 설계축력"|D{"볼트등급\n볼트호칭"}
    C --> |"볼트의 조임축력"|E{"볼트등급\n볼트호칭"}
    D --> |표3.3-2|Z(["설계볼트축력"])
    E --> |표3.3-2|ZZ(["볼트조임축력"])
    """

    @rule_method
    def bolt_axial_force(sIBolCla,sIBolNam):
        """
        Args:
            sIBolCla (string): 볼트등급
            sIBolNam (string): 볼트호칭
        Returns:
            fODesAxi (float): 설계볼트축력
            fOTigAxi (float): 볼트조임축력
        """
        if sIBolCla == "F8T":
            if sIBolNam == "M20":
                fODesAxi = 130
                fOTigAxi = 145
            elif sIBolNam == "M22":
                fODesAxi = 160
                fOTigAxi = 180
            elif sIBolNam == "M24":
                fODesAxi = 190
                fOTigAxi = 210
            else:
                return "M20, M22, M24 중에 선택해주세요"
        elif sIBolCla == "F10T":
            if sIBolNam == "M20":
                fODesAxi = 160
                fOTigAxi = 180
            elif sIBolNam == "M22":
                fODesAxi = 200
                fOTigAxi = 220
            elif sIBolNam == "M24":
                fODesAxi = 235
                fOTigAxi = 260
            elif sIBolNam == "M27":
                fODesAxi = 310
                fOTigAxi = 340
            elif sIBolNam == "M30":
                fODesAxi = 375
                fOTigAxi = 415
            else:
                return "M20, M22, M24, M27, M30 중에 선택해주세요"
        elif sIBolCla == "F13T":
            if sIBolNam == "M20":
                fODesAxi = 215
                fOTigAxi = 235
            elif sIBolNam == "M22":
                fODesAxi = 265
                fOTigAxi = 290
            elif sIBolNam == "M24":
                fODesAxi = 305
                fOTigAxi = 340
            else:
                return "M20, M22, M24 중에 선택해주세요"
        else:
            return "F8T, F10T, F13T 중에 선택해주세요"
        return "설계볼트축력: " + str(fODesAxi) + " kN, " + "볼트조임축력" + str(fOTigAxi) + " kN"