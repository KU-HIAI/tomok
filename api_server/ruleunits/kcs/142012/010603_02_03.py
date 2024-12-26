import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142012_010603_02_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 20 12 1.6.3 (2) ③'
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
    ③ 상기의 고정하중과 활하중을 합한 연직하중은 슬래브두께에 관계없이 최소 5.0 kN/㎡ 이상, 전동식 카트를 사용할 경우에는 최소 6.25 kN/㎡ 이상
    을 고려하여 거푸집 및 동바리를 설계한다.
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 거푸집 및 동바리의 연직하중];
    B["KCS 14 20 12 1.6.3 (2) ③"];
    B ~~~ A
    end

    KCS(["KCS 14 20 12 1.6.3 (2) ③"])

    subgraph Variable_def
    VarOut[/출력변수: 연직하중/];
    VarIn1[/입력변수: 전동식 카트 장비 사용 여부/];
    VarIn2[/입력변수: 고정하중/];
    VarIn3[/입력변수: 활하중/];
    VarOut ~~~ VarIn1 & VarIn2 & VarIn3
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> Q{"전동식 카트 장비 사용 여부"}
    Q --> |False|R{"연직하중 = \n max(고정하중 + 활하중, 5.0 kN/㎡)"}
    Q --> |True|S{"연직하중 = \n max(고정하중 + 활하중, 6.25 kN/㎡)"}
    R & S --> End([거푸집 및 동바리의 연직하중])
    """

    @rule_method
    def gravity_load(bIEleCar,fIDeaLoa, fILivLoa)-> RuleUnitResult:
        """
        Args:
            bIEleCar (bool): 전동식 카트 장비 사용 여부
            fIDeaLoa (float): 고정하중
            fILivLoa (float): 활하중

        Returns:
            fOGraLoa (float): 연직하중
        """
        assert isinstance(bIEleCar, bool)
        assert isinstance(fIDeaLoa, float)
        assert isinstance(fILivLoa, float)


        if bIEleCar:
            fOGraLoa = max(6.25, fIDeaLoa + fILivLoa)
        else:
            fOGraLoa = max(5.0, fIDeaLoa + fILivLoa)

        return RuleUnitResult(
            result_variables = {
                "fOGraLoa": fOGraLoa,
                })