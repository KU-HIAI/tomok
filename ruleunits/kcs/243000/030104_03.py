import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS243000_030104_03(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 30 00 3.1.4 (3)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-08'
    title = '구멍 뚫기'

    # 건설기준문서항목 (분류체계정보)
    description = """
    강교량공사
    3. 시공
    3.1 제작
    3.1.4 시공
    (3)
    """

    # 건설기준문서내용(text)
    content = """
    ####(3) 구멍 뚫기
    ① 2차부재에서 판두께 16 mm 이하 강재에 구멍을 뚫을 때는 눌러뚫기에 의하여 소정의 지름으로 뚫을 수 있으나 구멍 주변에 생긴 손상부는 깎아서 제거하여야 한다.
    ② 볼트 구멍의 중심에서 연단까지의 최소거리는 설계도에 특별히 지정한 경우를 제외하고는 표 3.1-2에 따른다.
    표 3.1-2 볼트 구멍중심에서 연단까지의 최소거리
    \begin{table}[]
    \begin{tabular}{lll}
    \multicolumn{3}{l}{(단위: mm)}                                  \\
    \multirow{2}{*}{볼트의 호칭} & \multicolumn{2}{l}{구멍중심에서 연단까지의 거리} \\
                            & 전단연     & 자동가스 전단연, 압연연 및 다듬질한 연    \\
    M8                      & 18      & 15                        \\
    M10                     & 20      & 17                        \\
    M12                     & 22      & 19                        \\
    M16                     & 27      & 23                        \\
    M20                     & 32      & 28                        \\
    M22                     & 37      & 32                        \\
    M24                     & 42      & 37                        \\
    M27                     & 50      & 45                        \\
    M30                     & 55      & 50
    \end{tabular}
    \end{table}
    ③ 볼트 구멍의 공칭치수는 표 3.1-3 및 표 3.1-4에 표시한 것으로 한다.
    표 3.1-3 볼트 구멍의 지름표
    \begin{table}[]
    \begin{tabular}{lll}
    \multicolumn{3}{l}{(단위: mm)}                                                                                                                                                                                                                                             \\
    볼트의 호칭                                                                                 & 고장력볼트                                                                                & 일반볼트                                                                                     \\
    M8                                                                                     & -                                                                                    & 10.0                                                                                     \\
    M10                                                                                    & -                                                                                    & 12.0                                                                                     \\
    M12                                                                                    & -                                                                                    & 14.0                                                                                     \\
    M16                                                                                    & 18.0                                                                                 & 18.0(17.5)                                                                               \\
    M20                                                                                    & 22.5                                                                                 & 22.5(21.5)                                                                               \\
    M22                                                                                    & 24.5                                                                                 & 24.5(23.5)                                                                               \\
    M24                                                                                    & 26.5                                                                                 & 26.5(25.5)                                                                               \\
    M27                                                                                    & 30.5                                                                                 & 30.5(29.5)                                                                               \\
    M30                                                                                    & 33.5                                                                                 & 33.5(32.5)                                                                               \\
    \multicolumn{3}{l}{\begin{tabular}[c]{@{}l@{}}주 1) 고장력볼트에는 T/S 볼트, 방청처리 고장력볼트, 용융 아연도금 고장력볼트, 내후성 고장력볼트를 포함한다.\\ 2) (  ) 안은 공사용 거더 등 주요부재에 일반볼트를 지압접합으로 사용한 경우이고, 이 경우의 볼트품질은 마무리 볼트로 한다.\\ 3) M20 이상의 볼트에 대하여는 AASHTO LRFD 교량설계기준보다 0.5 ㎜의 여유를 두고 정한 것이다.\end{tabular}}
    \end{tabular}
    \end{table}
    표 3.1-4 접시머리형 볼트구멍의 형상 및 치수
    \begin{table}[]
    \begin{tabular}{llllllllll}
    \multicolumn{10}{l}{(단위: mm)}                                                                                                                         \\
    호칭  & \begin{tabular}[c]{@{}l@{}}타입식고장력 접시\\ 머리형 볼트\end{tabular} &      &      &      & 보통접시 머리형 볼트          &    &      &      & \multirow{2}{*}{도해} \\
        & θ                                                          & h    & D    & d    & θ                    & h  & D    & d    &                     \\
    M12 &                                                            &      &      &      & \multirow{3}{*}{90°} & 5  & 24.0 & 14.0 & \multirow{4}{*}{<img src='http://drive.google.com/uc?export=view&id=11T5Di7eJy2ukwdr-LfAzScOOlHzbLvi2_link' /><br>}   \\
    M16 &                                                            &      &      &      &                      & 6  & 30.0 & 18.0 &                     \\
    M20 & \multirow{2}{*}{60°}                                       & 9.5  & 32.2 & 21.2 &                      & 7  & 36.5 & 22.5 &                     \\
    M22 &                                                            & 11.0 & 35.9 & 23.2 & 60°                  & 10 & 36.0 & 24.5 &
    \end{tabular}
    \end{table}
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 구멍 뚫기];
    B["KCS 24 30 00 3.1.4 (3)"];
    B ~~~ A
    end

    KCS(["KCS 24 30 00 3.1.4 (3)"])

    subgraph Variable_def
    subgraph V1
    VarOut1[/출력변수: 강재에 구멍 뚫기/];
    VarIn11[/입력변수: 2차부재/];
    VarIn12[/입력변수: 판두께/];
    end
    subgraph V2
    VarOut2[/출력변수: 볼트 구멍중심에서 연단까지의 거리/];
    VarIn21[/입력변수: 설계도에 특별히 지정/];
    VarIn22[/입력변수: 볼트의 호칭/];
    VarIn23[/입력변수: 전단연/];
    VarIn24[/입력변수: 자동가스 전단연, 압연연 및 다듬질한 연/];
    end
    subgraph V3
    VarOut31[/출력변수: 볼트 구멍의 공칭치수/];
    VarOut32[/출력변수: 볼트 구멍의 공칭치수/];
    VarIn31[/입력변수: 볼트 구멍의 지름/];
    VarIn32[/입력변수: 볼트의 호칭/];
    VarIn33[/입력변수: 고장력볼트/];
    VarIn34[/입력변수: 일반볼트/];
    VarIn35[/입력변수: 주요부재에 일반볼트를 지압접합으로 사용/];
    VarIn36[/입력변수: 접시머리형 볼트구멍의 치수/];
    VarIn37[/입력변수: 타입식고장력 접시머리형 볼트/];
    VarIn38[/입력변수: 보통접시 머리형 볼트/];
    VarIn39[/입력변수: 각도/];
    VarIn40[/입력변수: 높이/];
    VarIn41[/입력변수: 큰 직경/];
    VarIn42[/입력변수: 작은 직경/];
    end
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"강재에 구멍 뚫기 \n 볼트 구멍중심에서 연단까지의 거리 \n 볼트 구멍의 공칭치수 \n."}
    C --> |"강재에 구멍 뚫기"|D{"2차부재"}
    D --> |"True"|E{판두께}
    E --> |"≤ 16mm"|F["눌러뚫기에 의하여 소정의 지름으로 뚫을 수 있으나 \n 구멍 주변에 생긴 손상부는 깎아서 제거"]
    C --> |"볼트 구멍중심에서 연단까지의 거리"|G{"설계도에 특별히 지정"}
    G --> |False|H{"볼트의 호칭, 전단연 \n 자동가스 전단연, 압연연 및 다듬질한 연"}
    H --> |표 3.1-2|I[볼트 구멍중심에서 연단까지의 거리]
    C --> |"볼트 구멍의 공칭치수"|J{"볼트 구멍의 지름 \n 접시머리형 볼트구멍의 치수"}
    J --> |볼트 구멍의 지름|K{볼트의 호칭\n고장력볼트, 일반볼트 \n 주요부재에 일반볼트를 지압접합으로 사용}
    K --> |표 3.1-3|L[볼트 구멍의 공칭치수]
    J --> |접시머리형 볼트구멍의 치수|M{접시머리형 볼트구멍의 치수\n타입식고장력 접시머리형 볼트 \n보통접시 머리형 볼트 \n 각도, 높이, 큰직경, 작은직경 \n. }
    M --> |표 3.1-4|N[볼트 구멍의 공칭치수]
    F & I & L & N --> End([구멍 뚫기])
    """

    @rule_method
    def drilling_hole(bISecMem,fIPlaThi)-> str:
        """
        Args:
            bISecMem (boolean): 2차부재
            fIPlaThi (float): 판두께
        Returns:
            sODriSte (string): 강재에 구멍 뚫기
        """
        if bISecMem == True and fIPlaThi <=16:
            sODriSte = "눌러뚫기에 의하여 소정의 지름으로 뚫을 수 있으나 구멍 주변에 생긴 손상부는 깎아서 제거하여야 한다."
        else:
            sODriSte = None
        return sODriSte


    def distance_center_edge(self, bISpeDra,sIBolNam,bISheSte,bIRolSte)-> str:
        """
        Args:
            bISpeDra (boolean): 설계도에 특별히 지정
            sIBolNam (string): 볼트의 호칭
            bISheSte (boolean): 전단연
            bIRolSte (boolean): 자동가스 전단연, 압연연 및 다듬질한 연
        Returns:
            sOBolEdg (string): 볼트 구멍중심에서 연단까지의 거리
        """
        if bISpeDra:
            sOBolEdg = "설계도를 확인"
        else:
            if bISheSte:
                if sIBolNam == "M8":
                    sOBolEdg = "18 mm"
                elif sIBolNam == "M10":
                    sOBolEdg = "20 mm"
                elif sIBolNam == "M12":
                    sOBolEdg = "22 mm"
                elif sIBolNam == "M16":
                    sOBolEdg = "27 mm"
                elif sIBolNam == "M20":
                    sOBolEdg = "32 mm"
                elif sIBolNam == "M22":
                    sOBolEdg = "37 mm"
                elif sIBolNam == "M24":
                    sOBolEdg = "42 mm"
                elif sIBolNam == "M27":
                    sOBolEdg = "50 mm"
                elif sIBolNam == "M30":
                    sOBolEdg = "55 mm"
            elif bIRolSte:
                if sIBolNam == "M8":
                    sOBolEdg = "15 mm"
                elif sIBolNam == "M10":
                    sOBolEdg = "17 mm"
                elif sIBolNam == "M12":
                    sOBolEdg = "19 mm"
                elif sIBolNam == "M16":
                    sOBolEdg = "23 mm"
                elif sIBolNam == "M20":
                    sOBolEdg = "28 mm"
                elif sIBolNam == "M22":
                    sOBolEdg = "32 mm"
                elif sIBolNam == "M24":
                    sOBolEdg = "37 mm"
                elif sIBolNam == "M27":
                    sOBolEdg = "45 mm"
                elif sIBolNam == "M30":
                    sOBolEdg = "50 mm"
        return sOBolEdg

    def bolt_hole_dimension(self,sIBolNam,bIHigBol,bIGenBol,bIDriFla,bIGenFla,bIBeaMaj)->str:
        """
        Args:
            sIBolNam (string): 볼트의 호칭
            bIHigBol (boolean): 고장력볼트
            bIGenBol (boolean): 일반볼트
            bIDriFla (boolean): 타입식고장력 접시머리형 볼트
            bIGenFla (boolean): 보통접시 머리형 볼트
            bIBeaMaj (boolean): 주요부재에 일반볼트를 지압접합으로 사용
        Returns:
            sODimHol (string): 볼트 구멍의 공칭치수
        """
        if bIHigBol ==True:
            if sIBolNam == "M16":
                sODimHol = "18.0 mm"
            elif sIBolNam == "M20":
                sODimHol = "22.5 mm"
            elif sIBolNam == "M22":
                sODimHol = "24.5 mm"
            elif sIBolNam == "M24":
                sODimHol = "26.5 mm"
            elif sIBolNam == "M27":
                sODimHol = "30.5 mm"
            elif sIBolNam == "M30":
                sODimHol = "33.5 mm"
            else:
                return "M16, M20, M22, M24, M27, M30 중에 선택해주세요"
        elif bIGenBol:
            if sIBolNam == "M8":
                sODimHol = "10.0 mm"
            elif sIBolNam == "M10":
                sODimHol = "12.0 mm"
            elif sIBolNam == "M12":
                sODimHol = "14.0 mm"
            if sIBolNam == "M16":
                if bIBeaMaj == False:
                    sODimHol = "18.0 mm"
                else:
                    sODimHol = "17.5 mm"
            elif sIBolNam == "M20":
                if bIBeaMaj == False:
                    sODimHol = "22.5 mm"
                else:
                    sODimHol = "21.5 mm"
            elif sIBolNam == "M22":
                if bIBeaMaj == False:
                    sODimHol = "24.5 mm"
                else:
                    sODimHol = "23.5 mm"
            elif sIBolNam == "M24":
                if bIBeaMaj == False:
                    sODimHol = "26.5 mm"
                else:
                    sODimHol = "25.5 mm"
            elif sIBolNam == "M27":
                if bIBeaMaj == False:
                    sODimHol = "30.5 mm"
                else:
                    sODimHol = "29.5 mm"
            elif sIBolNam == "M30":
                if bIBeaMaj == False:
                    sODimHol = "33.5 mm"
                else:
                    sODimHol = "32.5 mm"
            else:
                return "M8, M10, M12, M16, M20, M22, M24, M27, M30 중에 선택해주세요"
        elif bIDriFla:
            if sIBolNam == "M20":
                sODimHol = "θ=60°,h=9.5 mm, D=32.2 mm, d= 21.2 mm"
            elif sIBolNam == "M22":
                sODimHol = "θ=60°,h=11.0 mm, D=35.9 mm, d= 23.2 mm"
            else:
                return "M20, M22 중에 선택해주세요"
        elif bIGenFla:
            if sIBolNam == "M12":
                sODimHol = "θ=90°,h=5 mm, D=24.0 mm, d= 14.0 mm"
            elif sIBolNam == "M16":
                sODimHol = "θ=90°,h=6 mm, D=30.0 mm, d=18.0 mm"
            elif sIBolNam == "M20":
                sODimHol = "θ=90°,h=7 mm, D=36.5 mm, d= 22.5 mm"
            elif sIBolNam == "M22":
                sODimHol = "θ=60°,h=10 mm, D=36.0 mm, d= 24.5 mm"
            else:
                return "M12, M16, M20, M22 중에 선택해주세요"
        else:
            return "고장력볼트, 일반볼트, 타입식고장력 접시머리형 볼트, 보통접시 머리형 볼트 중에 하나를 선택해주세요"
        return sODimHol