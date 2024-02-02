import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS142012_010603_02(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 14 20 12 1.6.3 (2)'
    ref_date = '2022-09-01'
    doc_date = '2023-09-25'
    title = '거푸집 및 동바리의 연직하중'

    # 건설기준문서항목 (분류체계정보)
    description = """
    거푸집 및 동바리
    1. 일반사항
    1.6 거푸집 및 동바리 설계
    1.6.3 거푸집 및 동바리 구조계산
    (2)
    """

    # 건설기준문서내용(text)
    content = """
    ####(2) 연직하중은 고정하중 및 공사 중 발생하는 활하중으로 다음의 값을 적용한다.

    ① 고정하중은 철근콘크리트와 거푸집의 중량을 고려하여 합한 하중이며, 콘크리트의 단위 중량은 철근의 중량을 포함하여 보통 콘크리트 24 kN/㎥,
     제1종 경량골재 콘크리트 20 kN/㎥ 그리고 2종 경량골재 콘크리트 17 kN/㎥을 적용하여야 한다. 거푸집 하중은 최소 0.4 kN/㎡ 이상을 적용하며, 특
     수 거푸집의 경우에는 그 실제의 중량을 적용하여 설계한다.

    ② 활하중은 구조물의 수평투영면적(연직방향으로 투영시킨 수평면적)당 최소 2.5 kN/㎡ 이상으로 하여야 하며, 전동식 카트 장비를 이용하여 콘크
    리트를 타설할 경우에는 3.75 kN/㎡의 활하중을 고려하여 설계한다. 단, 콘크리트 분배기 등의 특수 장비를 이용할 경우에는 실제 장비하중을 적용
    하고, 거푸집 및 동바리에 대한 안전 여부를 확인한다.

    ③ 상기의 고정하중과 활하중을 합한 연직하중은 슬래브두께에 관계없이 최소 5.0 kN/㎡ 이상, 전동식 카트를 사용할 경우에는 최소 6.25 kN/㎡ 이상
    을 고려하여 거푸집 및 동바리를 설계한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 거푸집 및 동바리의 연직하중];
    B["KCS 14 20 12 1.6.3 (2)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 12 1.6.3 (2)"])

    subgraph Variable_def
    subgraph V1
    VarOut1[/출력변수: 고정하중/];
    VarOut2[/출력변수: 콘크리트 단위 중량/];
    VarOut3[/출력변수: 거푸집 하중/];
    VarIn1[/입력변수: 철근콘크리트 중량/];
    VarIn2[/입력변수: 거푸집 중량/];
    VarIn3[/입력변수: 보통 콘크리트/];
    VarIn4[/입력변수: 제1종 경량골재 콘크리트/];
    VarIn5[/입력변수: 제2종 경량골재 콘크리트/];
    VarIn6[/입력변수: 특수 거푸집/];
    end
    subgraph V2
    VarOut4[/출력변수: 활하중/];
    VarIn7[/입력변수: 전동식 카트 장비/];
    VarIn8[/입력변수: 특수장비/];
    end
    subgraph V3
    VarOut5[/출력변수: 고정하중과 활하중을 합한 연직하중/];
    VarIn9[/입력변수: 고정하중과 활하중을 합한 연직하중/];
    VarIn10[/입력변수: 전동식 카트/];
    end
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"고정하중\n활하중\n고정하중과 활하중을 합한 연직하중"}
    C --> |"고정하중"|D["고정하중\n 콘크리트 단위 중량\n거푸집 하중"]
    D --> |고정하중|E["고정하중 = 철근콘크리트 중량+거푸집 중량"]
    D --> |콘크리트 단위 중량|F["보통 콘크리트\n제1종 경량골재 콘크리트\n제2종 경량골재 콘크리트"]
    F --> |보통 콘크리트|G["콘크리트 단위 중량 = 24 kN/㎥"]
    F --> |제1종 경량골재 콘크리트|H["콘크리트 단위 중량 = 20 kN/㎥"]
    F --> |제2종 경량골재 콘크리트|I["콘크리트 단위 중량 = 17 kN/㎥"]
    D --> |거푸집 하중|J{"특수 거푸집"}
    J --> |False|K["최소 0.4 kN/㎡ 이상"]
    J --> |True|L["실제의 중량을 적용"]
    C --> |"활하중"|M{"전동식 카트 장비\n 특수장비"}
    M --> N["구조물의 수평투영면적\n(연직방향으로 투영시킨 수평면적)당 \n 최소 2.5 kN/㎡ 이상"]
    M --> |전동식 카트 장비|O["구조물의 수평투영면적\n(연직방향으로 투영시킨 수평면적)당 \n 최소 3.75 kN/㎡ 이상"]
    M --> |특수장비|P["실제 장비하중을 적용하고, \n 거푸집 및 동바리에 대한 \n 안전 여부를 확인"]
    D & E & F & G & H & I & K & L & N & O & P --> End(["철근가공의 허용오차"])
    C --> |"고정하중과 활하중을 합한 연직하중"|Q{"전동식 카트"}
    Q --> |False|R{"고정하중과 활하중을 합한 연직하중 \n ≥ 5.0 kN/㎡"}
    Q --> |True|S{"고정하중과 활하중을 합한 연직하중 \n ≥ 6.25 kN/㎡"}
    R & S --> |True|Pass([Pass])
    R & S --> |False|Fail([Fail])
    """

    @rule_method
    def dead_load(fIWeiRei, fIWeiFo,bINorCon, bILigCon_1, bILigCon_2, bIWeiSpe):
        """
        Args:
            fIWeiRei (float): 철근콘크리트 중량
            fIWeiFor (float): 거푸집 중량
            bINorCon (boolean): 보통 콘크리트
            bILigCon_1 (boolean): 제1종 경량골재 콘크리트
            bILigCon_2 (boolean): 제2종 경량골재 콘크리트
            bIWeiSpe (boolean): 특수 거푸집
        Returns:
            fODeaLoa (float): 고정하중
            fOConSpe (float): 콘크리트 단위 중량
            sOForLoa (string): 거푸집 하중
        """
        fODeaLoa = fIWeiRei + fIWeiFor
        if bINorCon:
            fOConSpe = 24
        elif bILigCon_1:
            fOConSpe = 20
        elif bILigCon_2:
            fOConSpe = 17
        if bIWeiSpe:
            sOForLoa = "실제의 중량을 적용"
        else:
            sOForLoa = "최소 0.4 kN/㎡ 이상을 적용"
        return "고정하중: ", fODeaLoa, "콘크리트 단위 중량: ", fOConSpe, "거푸집 하중: ", sOForLoa

    def live_load(self,bIEleCar,bISpeEqu) -> str:
        """
        Args:
            bIEleCar (boolean): 전동식 카트 장비
            bISpeEqu (boolean): 특수장비
        Returns:
            sOLivLoa (string): 활하중
        """
        if bIEleCar == False and bISpeEqu == False:
            sOLivLoa = "구조물의 수평투영면적(연직방향으로 투영시킨 수평면적)당 최소 2.5 kN/㎡ 이상"
        elif bIEleCar == True:
            sOLivLoa = "3.75 kN/㎡의 활하중을 고려"
        elif bISpeEqu == True:
            sOLivLoa = "실제 장비하중을 적용하고, 거푸집 및 동바리에 대한 안전 여부를 확인"
        return sOLivLoa


    def gravity_load(self,fIGraLoa,bIEleCar) -> str:
        """
        Args:
            fIGraLoa (float): 고정하중과 활하중을 합한 연직하중
            bIEleCar (boolean): 전동식 카트
        Returns:
            sOGraLoa (string): 고정하중과 활하중을 합한 연직하중
        """
        if bIEleCar == False:
            if fIGraLoa >= 5:
                sOGraLoa = "Pass"
            else:
                sOGraLoa = "Fail"
        else:
            if fIGraLoa >= 6.25:
               sOGraLoa = "Pass"
            else:
                sOGraLoa = "Fail"
        return sOGraLoa