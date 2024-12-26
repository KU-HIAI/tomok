import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS243000_030304_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 30 00 3.3.4 (3)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-14'
    title = '용융아연도금 고장력 볼트'

    description = """
    강교량공사
    3. 시공
    3.3 볼트접합
    3.3.4 시공
    (3)
    """
    content = """
    #### 3.3.4 시공
    (3) 용융아연도금 고장력 볼트
    ① 볼트의 본조임 방법은 너트 회전법에 따르고 1차 조임은 프리-세트형 토크렌치를 사용한다.
    ② 1차 조임 후 볼트, 너트, 와셔 및 부재에는 금메김을 하고 본조임은 1차 조임 후 금메김 위치에서 너트가 120°±30°(1/3회전)의 위치까지 회전시켜 조임 시공한다.
    ③ 연결되는 판의 접합면 거칠기는 50S 정도로 마무리하고 미끄럼 계수는 역시 0.4 이상이 되어야 한다.
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

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 용융아연도금 고장력 볼트];
    B["KCS 24 30 00 3.3.4 (3)"];
    B ~~~ A
    end

    KCS(["KCS 24 30 00 3.3.4 (3)"])

    subgraph Variable_def
    subgraph V2
    VarIn21[/입력변수: 50S 정도의 거칠기/];
    VarIn22[/입력변수: 미끄럼계수/];
    end
    subgraph V3
    VarOut3[/출력변수: 볼트의 축력/];
    VarIn31[/"출력변수: 설계볼트축력"/];
    VarIn32[/"출력변수: 조임축력"/];
    VarIn33[/입력변수: 5본 이상 볼트의 평균축력 하한치/];
    VarIn34[/입력변수: 5본 이상 볼트의 평균축력 상한치/];
    VarIn41[/"입력변수: 볼트등급"/];
    VarIn42[/"입력변수: 볼트호칭"/];
    end
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> |연결되는 판의 접합면|F{"50S 정도의 거칠기 = True\n 미끄럼계수>=0.4 \n."}
    F --> End([Pass or Fail])
    Variable_def --> |볼트의 축력|HH{"볼트등급, 볼트호칭"}
    HH --> |표 3.3-2|I[설계볼트축력,조임축력,\n5본 이상 볼트의 평균축력 하한치\n5본 이상 볼트의 평균축력 상한치\n.]
    I --> Q(["용융아연도금 고장력 볼트"])
    """

    @rule_method

    def bolt_axial_force(bIRou50,fIMinSli,sIBolCla,sIBolNam) -> RuleUnitResult:
        """
        Args:
            bIRou50 (bool): 50S 정도의 거칠기
            fIMinSli (float): 미끄럼계수
            sIBolCla (str): 볼트등급
            sIBolNam (str): 볼트호칭

        Returns:
            pass_fail (bool): 강교량공사 3.3.4 시공 (3) ③의 판단 결과
            fODesAxi (float): 설계볼트축력
            fOTigAxi (float): 볼트조임축력
            fILowAxi (float): 5본 이상 볼트의 평균축력 하한치
            fIUppAxi (float): 5본 이상 볼트의 평균축력 상한치
        """
        assert isinstance(sIBolCla,str)
        assert isinstance(sIBolNam,str)
        assert sIBolCla in ["F8T", "F10T","F13T"]

        if bIRou50 == True and fIMinSli>=0.4:
            pass_fail = True
        else:
            pass_fail = False

        if sIBolCla == "F8T":
            assert sIBolNam in ["M20","M22","M24"]
        elif sIBolCla == "F10T":
            assert sIBolNam in ["M20","M22","M24","M27","M30"]
        elif sIBolCla == "F13T":
            assert sIBolNam in ["M20","M22","M24"]


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
                fILowAxi = 320
                fIUppAxi = 350

        return RuleUnitResult(
            result_variables = {
                "pass_fail":pass_fail,
                "fODesAxi": fODesAxi,
                "fOTigAxi": fOTigAxi,
                "fILowAxi": fILowAxi,
                "fIUppAxi": fIUppAxi,
                })