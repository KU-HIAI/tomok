import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142022_041102_05(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 22 4.11.2 (5)'
    ref_date = '2022-01-11'
    doc_date = '2024-08-02'
    title = '콘크리트에 의한 공칭전단강도'

    description = """
    콘크리트구조 전단 및 비틀림 설계기준
    4. 설계
    4.11 슬래브와 기초판에 대한 전단 설계
    4.11.2 2방향 거동에 대한 전단강도
    (5)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 콘크리트에 의한 공칭전단강도];
    B["KDS 14 20 22 4.11.2 (5)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarIn1[/입력변수: 콘크리트에 의한 공칭전단강도/];
    VarIn2[/입력변수: 설계기준 압축강도/];
    VarIn3[/입력변수: 슬래브와 기초판에서 2방향 전단에 대한 위험단면의 둘레/];
    VarIn4[/입력변수: 압축철근의 영향을 무시하고 계산된 슬래브 위험단면의 압축대 깊이의 평균값/];
    end

    VarIn1 & VarIn2 ~~~ VarIn3 & VarIn4

    Python_Class ~~~ C(["KDS 14 20 22 4.11.2 (5)"])
		C --> Variable_def

    D{"<img src='https://latex.codecogs.com/svg.image? V_{c}\leq 0.58f_{ck}b_{o}c_{u}'>------------------"};

		Variable_def --> D --> E(["콘크리트에 의한 공칭전단강도"])
    """

    @rule_method
    def Nominal_shear_strength_by_concrete(fIVc,fIfck,fIbo,fIcu) -> RuleUnitResult:
        """콘크리트에 의한 공칭전단강도

        Args:
            fIVc (float): 콘크리트에 의한 공칭전단강도
            fIfck (float): 설계기준 압축강도
            fIbo (float): 슬래브와 기초판에서 2방향 전단에 대한 위험단면의 둘레
            fIcu (float): 압축철근의 영향을 무시하고 계산된 슬래브 위험단면의 압축대 깊이의 평균값


        Returns:
            fOVc (float): 콘크리트에 의한 공칭전단강도
        """

        assert isinstance(fIVc, float)
        assert isinstance(fIfck, float)
        assert isinstance(fIbo, float)
        assert isinstance(fIcu, float)

        fOVc = min(fIVc, 0.58 * fIfck * fIbo * fIcu)

        return RuleUnitResult(
            result_variables = {
                "fOVc": fOVc,
            }
        )