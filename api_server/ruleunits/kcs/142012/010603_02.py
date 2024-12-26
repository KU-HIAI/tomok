import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142012_010603_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 20 12 1.6.3 (2)'
    ref_date = '2022-09-01'
    doc_date = '2023-09-25'
    title = '거푸집 및 동바리의 연직하중'

    description = """
    거푸집 및 동바리
    1. 일반사항
    1.6 거푸집 및 동바리 설계
    1.6.3 거푸집 및 동바리 구조계산
    (2)
    """
    content = """
    #### 1.6.3 거푸집 및 동바리 구조계산
    (2) 연직하중은 고정하중 및 공사 중 발생하는 활하중으로 다음의 값을 적용한다.
    ① 고정하중은 철근콘크리트와 거푸집의 중량을 고려하여 합한 하중이며, 콘크리트의 단위 중량은 철근의 중량을 포함하여 보통 콘크리트 24 kN/㎥,
     제1종 경량골재 콘크리트 20 kN/㎥ 그리고 2종 경량골재 콘크리트 17 kN/㎥을 적용하여야 한다. 거푸집 하중은 최소 0.4 kN/㎡ 이상을 적용하며, 특
     수 거푸집의 경우에는 그 실제의 중량을 적용하여 설계한다.
    ② 활하중은 구조물의 수평투영면적(연직방향으로 투영시킨 수평면적)당 최소 2.5 kN/㎡ 이상으로 하여야 하며, 전동식 카트 장비를 이용하여 콘크
    리트를 타설할 경우에는 3.75 kN/㎡의 활하중을 고려하여 설계한다. 단, 콘크리트 분배기 등의 특수 장비를 이용할 경우에는 실제 장비하중을 적용
    하고, 거푸집 및 동바리에 대한 안전 여부를 확인한다.
    ③ 상기의 고정하중과 활하중을 합한 연직하중은 슬래브두께에 관계없이 최소 5.0 kN/㎡ 이상, 전동식 카트를 사용할 경우에는 최소 6.25 kN/㎡ 이상
    을 고려하여 거푸집 및 동바리를 설계한다.
    """
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
    VarIn1[/입력변수: 콘크리트 종류/];
    VarIn2[/입력변수: 슬래브 두께/];
    VarIn3[/입력변수: 특수 거푸집/];
    VarIn4[/입력변수: 특수 거푸집의 중량/];
    end
    subgraph V2
    VarOut4[/출력변수: 활하중/];
    VarIn6[/입력변수: 전동식 카트/];
    VarIn7[/입력변수: 특수장비/];
    VarIn8[/입력변수: 특수장비의 하중/];
    end
    subgraph V3
    VarOut5[/출력변수: 연직하중/];
    VarIn10[/입력변수: 전동식 카트/];
    end
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"고정하중\n활하중\n고정하중과 활하중을 합한 연직하중"}
    C --> |"고정하중"|F{"콘크리트 종류"}
    F --> |보통 콘크리트|G["콘크리트 단위 중량 = 24 kN/㎥"]
    F --> |제1종 경량골재 콘크리트|H["콘크리트 단위 중량 = 20 kN/㎥"]
    F --> |제2종 경량골재 콘크리트|I["콘크리트 단위 중량 = 17 kN/㎥"]
    C --> |"고정하중"|D{"특수 거푸집"}
    D --> |False|E[거푸집 하중 = 0.4 kN/㎡]
    D --> |True|EE[거푸집 하중 = 특수 거푸집의 중량]
    G & H & I & E & EE --> J["고정하중 = 콘크리트 단위 중량 * 슬래브 두께 + 거푸집 하중"]
    C --> |"활하중"|M{"전동식 카트 장비\n 특수장비"}
    M --> |False|N["활하중 = 2.5 kN/㎡"]
    M --> |전동식 카트 장비|O["활하중 = 3.75 kN/㎡"]
    M --> |특수장비|P["활하중 = 2.5 kN/㎡ + 특수장비의 하중"]
    N & O & P --> K(["활하중"])
    J & K --> |"연직하중"|Q{"전동식 카트"}
    Q --> |False|R{"연직하중 = \n max(고정하중 + 활하중, 5.0 kN/㎡)"}
    Q --> |True|S{"연직하중 = \n max(고정하중 + 활하중, 6.25 kN/㎡)"}
    R & S --> End([거푸집 및 동바리의 연직하중])
    """

    @rule_method
    def gravity_load(sIConTyp, fISlaThi,bISpeFor, fIWeiFor, bIEleCar,bISpeEqu, fIWeiEqu)-> RuleUnitResult:
        """
        Args:
            sIConTyp (str): 콘크리트 종류
            fISlaThi (float): 슬래브 두께
            bISpeFor (bool): 특수 거푸집
            fIWeiFor (float): 특수 거푸집의 중량
            bIEleCar (bool): 전동식 카트 장비
            bISpeEqu (bool): 특수장비
            fIWeiEqu (float): 특수장비의 하중

        Returns:
            fODeaLoa (float)): 고정하중
            fOLivLoa (float): 활하중
            fOGraLoa (float): 연직하중

        """
        assert isinstance(sIConTyp, str)
        assert sIConTyp in ["보통 콘크리트","제1종 경량골재 콘크리트","제2종 경량골재 콘크리트"]
        assert isinstance(fISlaThi, float)
        assert isinstance(bISpeFor, bool)
        assert isinstance(fIWeiFor, float)

        assert isinstance(bIEleCar, bool)
        assert isinstance(bISpeEqu, bool)
        assert (bIEleCar+bISpeEqu) != 2


        if sIConTyp == "보통 콘크리트":
            temp_1 = 24*fISlaThi
        elif sIConTyp == "제1종 경량골재 콘크리트":
            temp_1 = 20*fISlaThi
        elif sIConTyp == "제2종 경량골재 콘크리트":
            temp_1 = 17*fISlaThi
        if bISpeFor:
            temp_2 = fIWeiFor
        else:
            temp_2 = 0.4
        fODeaLoa = temp_1 + temp_2

        if bIEleCar:
            fOLivLoa = 3.75
        elif bISpeEqu:
            fOLivLoa = 2.5 + fIWeiEqu
        else:
            fOLivLoa = 2.5

        if bIEleCar:
            fOGraLoa = max(6.25, fODeaLoa + fOLivLoa)
        else:
            fOGraLoa = max(5.0, fODeaLoa + fOLivLoa)

        return RuleUnitResult(
            result_variables = {
                "fODeaLoa": fODeaLoa,
                "fOLivLoa": fOLivLoa,
                "fOGraLoa": fOGraLoa,
                })