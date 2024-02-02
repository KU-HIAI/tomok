import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS243000_030304_04(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 30 00 3.3.4 (4)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-14'
    title = '타입식 고장력 볼트'

    # 건설기준문서항목 (분류체계정보)
    description = """
    강교량공사
    3. 시공
    3.3 볼트접합
    3.3.4 시공
    (4)
    """

    # 건설기준문서내용(text)
    content = """
    ####(4) 타입식 고장력 볼트
    ① 타입식 고장력볼트의 와셔는 너트 측에만 1개를 사용한다.
    ② 지압접합에 타입식 고장력볼트를 이용할 경우에는 체결 시공 전에 구멍의 어긋남에 대해 확인하여 타입 작업성에 문제가 발생하지 않도록 한다. 또한 볼트 타입시 구멍 주위 연단에 유해한 손상이 가지 않도록 주의한다.
    ③ 타입식 고장력볼트 체결은 볼트의 나사부에 너트가 걸릴 때까지 타입한 후에 너트를 회전하여 볼트 속으로 끌어넣는 방법을 택한다.
    ④ 볼트의 축력은 표 3.3-2에 따른다.
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
    A[Title: 타입식 고장력 볼트];
    B["KCS 24 30 00 3.3.4 (4)"];
    B ~~~ A
    end

    KCS(["KCS 24 30 00 3.3.4 (4)"])

    subgraph Variable_def
    VarOut1[/출력변수: 설계볼트축력/];
    VarOut2[/출력변수: 조임축력/];
    VarOut3[/출력변수: 5본 이상 볼트의 평균축력 하한치/];
    VarOut4[/출력변수: 5본 이상 볼트의 평균축력 상한치/];
    VarIn1[/입력변수: 볼트등급/];
    VarIn2[/입력변수: 볼트호칭/];
    VarOut1 & VarOut2 ~~~ VarOut3 & VarOut4
    VarOut3 & VarOut4 ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> HH{"볼트등급, 볼트호칭"}
    HH --> |표 3.3-2|I[설계볼트축력, 조임축력,\n5본 이상 볼트의 평균축력 하한치\n5본 이상 볼트의 평균축력 상한치\n.]
    I --> Q(["타입식 고장력 볼트"])
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
            fILowAxi (float): 5본 이상 볼트의 평균축력 하한치
            fIUppAxi (float): 5본 이상 볼트의 평균축력 상한치
        """
        if sIBolCla == "F8T":
            if sIBolNam == "M20":
                fODesAxi = 130
                fOTigAxi = 145
                fILowAxi = 135
                fIUppAxi = 150
            elif sIBolNam == "M22":
                fODesAxi = 160
                fOTigAxi = 180
                fILowAxi = 170
                fIUppAxi = 185
            elif sIBolNam == "M24":
                fODesAxi = 190
                fOTigAxi = 210
                fILowAxi = 195
                fIUppAxi = 215
            else:
                return "M20, M22, M24 중에 선택해주세요"
        elif sIBolCla == "F10T":
            if sIBolNam == "M20":
                fODesAxi = 160
                fOTigAxi = 180
                fILowAxi = 170
                fIUppAxi = 185
            elif sIBolNam == "M22":
                fODesAxi = 200
                fOTigAxi = 220
                fILowAxi = 210
                fIUppAxi = 230
            elif sIBolNam == "M24":
                fODesAxi = 235
                fOTigAxi = 260
                fILowAxi = 245
                fIUppAxi = 270
            elif sIBolNam == "M27":
                fODesAxi = 310
                fOTigAxi = 340
                fILowAxi = 315
                fIUppAxi = 355
            elif sIBolNam == "M30":
                fODesAxi = 375
                fOTigAxi = 415
                fILowAxi = 390
                fIUppAxi = 435
            else:
                return "M20, M22, M24, M27, M30 중에 선택해주세요"
        elif sIBolCla == "F13T":
            if sIBolNam == "M20":
                fODesAxi = 215
                fOTigAxi = 235
                fILowAxi = 220
                fIUppAxi = 240
            elif sIBolNam == "M22":
                fODesAxi = 265
                fOTigAxi = 290
                fILowAxi = 275
                fIUppAxi = 300
            elif sIBolNam == "M24":
                fODesAxi = 305
                fOTigAxi = 340
                fILowAxi = 320* 입력변수, 출력변수, 출력, 조건
                fIUppAxi = 350
            else:
                return "M20, M22, M24 중에 선택해주세요"
        else:
            return "F8T, F10T, F13T 중에 선택해주세요"
        return "설계볼트축력: " + str(fODesAxi) + " kN, " + "볼트조임축력: " + str(fOTigAxi) + " kN, " + "5본 이상 볼트의 평균축력 하한치: " + str(fILowAxi) + " kN, "+ "5본 이상 볼트의 평균축력 상한치: " + str(fIUppAxi) + " kN"