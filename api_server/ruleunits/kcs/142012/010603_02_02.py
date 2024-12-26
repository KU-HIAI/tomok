import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142012_010603_02_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 20 12 1.6.3 (2) ②'
    ref_date = '2022-09-01'
    doc_date = '2023-09-25'
    title = '거푸집 및 동바리의 연직활하중'

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
    ② 활하중은 구조물의 수평투영면적(연직방향으로 투영시킨 수평면적)당 최소 2.5 kN/㎡ 이상으로 하여야 하며, 전동식 카트 장비를 이용하여 콘크
    리트를 타설할 경우에는 3.75 kN/㎡의 활하중을 고려하여 설계한다. 단, 콘크리트 분배기 등의 특수 장비를 이용할 경우에는 실제 장비하중을 적용
    하고, 거푸집 및 동바리에 대한 안전 여부를 확인한다.
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 거푸집 및 동바리의 연직활하중];
    B["KCS 14 20 12 1.6.3 (2) ②"];
    B ~~~ A
    end

    KCS(["KCS 14 20 12 1.6.3 (2) ②"])

    subgraph Variable_def
    VarOut[/출력변수: 활하중/];
    VarIn6[/입력변수: 전동식 카트 장비 사용 여부/];
    VarIn7[/입력변수: 특수장비 사용 여부/];
    VarIn8[/입력변수: 특수장비의 하중/];
    VarOut ~~~ VarIn6 & VarIn7 & VarIn8
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> M{"전동식 카트 장비 사용 여부\n 특수장비 사용 여부"}
    M --> |False|N["활하중 = 2.5 kN/㎡"]
    M --> |전동식 카트 장비 사용 여부|O["활하중 = 3.75 kN/㎡"]
    M --> |특수장비 사용 여부|P["활하중 = 2.5 kN/㎡ + 특수장비의 하중"]
    N & O & P --> K(["활하중"])
    K --> End([거푸집 및 동바리의 연직하중])
    """

    @rule_method
    def gravity_live_load(bIEleCar,bISpeEqu, fIWeiEqu)-> RuleUnitResult:
        """
        Args:
            bIEleCar (bool): 전동식 카트 장비 사용 여부
            bISpeEqu (bool): 특수장비 사용 여부
            fIWeiEqu (float): 특수장비의 하중

        Returns:
            fOLivLoa (float): 활하중
        """

        assert isinstance(bIEleCar, bool)
        assert isinstance(bISpeEqu, bool)
        assert (bIEleCar+bISpeEqu) != 2


        if bIEleCar:
            fOLivLoa = 3.75
        elif bISpeEqu:
            fOLivLoa = 2.5 + fIWeiEqu
        else:
            fOLivLoa = 2.5

        return RuleUnitResult(
            result_variables = {
                "fOLivLoa": fOLivLoa,
                })