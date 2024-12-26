import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142012_010603_03_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 20 12 1.6.3 (3) ①'
    ref_date = '2022-09-01'
    doc_date = '2023-09-25'
    title = '동바리의 수평하중'

    description = """
    거푸집 및 동바리
    1. 일반사항
    1.6 거푸집 및 동바리 설계
    1.6.3 거푸집 및 동바리 구조계산
    (3)
    """
    content = """
    #### 1.6.3 거푸집 및 동바리 구조계산
    (3) 수평하중은 고정하중 및 공사 중 발생하는 활하중으로 다음의 값을 적용한다.
    ① 동바리에 작용하는 수평하중으로는 고정하중의 2% 이상 또는 동바리 상단의 수평방향 단위 길이 당 1.5 kN/m 이상 중에서 큰 쪽의 하중이 동바리 머리 부분에 수평방향으로 작용하는 것으로 가정하여 가새설치 여부를 검토한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 동바리의 수평하중];
    B["KCS 14 20 12 1.6.3 (3) ①"];
    B ~~~ A
    end

    KCS(["KCS 14 20 12 1.6.3 (3) ①"])

    subgraph Variable_def
    VarOut[/출력변수: 동바리에 작용하는 수평하중/];
    VarIn1[/입력변수: 동바리 상단의 수평방향 길이/];
    VarIn2[/입력변수: 수평 고정하중/];
    VarOut ~~~ VarIn1 & VarIn2
    end


    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"동바리 상단의 수평방향 길이* 수평 고정하중*2% > 1.5"}
    C --> |True|D[수평 고정하중*2%]
    C --> |False|E[1.5/동바리 상단의 수평방향 길이]
    D & E --> End([동바리의 수평하중])
    """

    @rule_method
    def horizontal_load_shore(fILenSho, fIDeaLoa)-> RuleUnitResult:
        """
        Args:
            fILenSho (float): 동바리 상단의 수평방향 길이
            fIDeaLoa (float): 수평 고정하중

        Returns:
            fOLoaSho (float): 동바리에 작용하는 수평하중
        """
        assert isinstance(fILenSho, float)
        assert isinstance(fIDeaLoa, float)
        assert fILenSho > 0

        if fILenSho*0.02*fIDeaLoa <1.5:
            fOLoaSho = 1.5/fILenSho
        else:
            fOLoaSho = fIDeaLoa*0.02

        return RuleUnitResult(
            result_variables = {
                "fOLoaSho": fOLoaSho,
                })