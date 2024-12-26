import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142012_010603_02_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 20 12 1.6.3 (2) ①'
    ref_date = '2022-09-01'
    doc_date = '2023-09-25'
    title = '거푸집 및 동바리의 연직고정하중'

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
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 거푸집 및 동바리의 연직고정하중];
    B["KCS 14 20 12 1.6.3 (2) ①"];
    B ~~~ A
    end

    KCS(["KCS 14 20 12 1.6.3 (2) ①"])

    subgraph Variable_def
    VarOut[/출력변수: 고정하중/];
    VarIn1[/입력변수: 콘크리트 종류/];
    VarIn2[/입력변수: 슬래브 두께/];
    VarIn3[/입력변수: 특수 거푸집 여부/];
    VarIn4[/입력변수: 특수 거푸집의 중량/];
    VarOut ~~~ VarIn1 & VarIn2
    VarIn1 & VarIn2 ~~~ VarIn1 & VarIn2 & VarIn3
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> F{"콘크리트 종류"}
    F --> |보통 콘크리트|G["4 kN/㎥"]
    F --> |제1종 경량골재 콘크리트|H["20 kN/㎥"]
    F --> |제2종 경량골재 콘크리트|I["17 kN/㎥"]
    G & H & I --> II[콘크리트 단위 중량]
    Variable_def --> D{"특수 거푸집"}
    D --> |False|E[0.4 kN/㎡]
    D --> |True|EE[특수 거푸집의 중량]
    E & EE --> FF[거푸집 하중]
    II & FF --> J["고정하중 = 콘크리트 단위 중량 * 슬래브 두께 + 거푸집 하중"]
    J --> End([거푸집 및 동바리의 연직고정하중])
    """

    @rule_method
    def gravity_dead_load(sIConTyp, fISlaThi,bISpeFor, fIWeiFor)-> RuleUnitResult:
        """
        Args:
            sIConTyp (str): 콘크리트 종류
            fISlaThi (float): 슬래브 두께
            bISpeFor (bool): 특수 거푸집 여부
            fIWeiFor (float): 특수 거푸집의 중량

        Returns:
            fODeaLoa (float)): 고정하중

        """
        assert isinstance(sIConTyp, str)
        assert sIConTyp in ["보통 콘크리트","제1종 경량골재 콘크리트","제2종 경량골재 콘크리트"]
        assert isinstance(fISlaThi, float)
        assert isinstance(bISpeFor, bool)
        assert isinstance(fIWeiFor, float)


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

        return RuleUnitResult(
            result_variables = {
                "fODeaLoa": fODeaLoa,
                })