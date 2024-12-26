import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142022_040201_01_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 22 4.2.1 (1) ①'
    ref_date = '2022-01-11'
    doc_date = '2024-06-27'
    title = '전단력과 휨모멘트만을 받는 부재의 전단강도'

    description = """
    콘크리트구조 전단 및 비틀림 설계기준
    4. 설계
    4.2 콘크리트에 의한 전단강도
    4.2.1 철근콘크리트 부재의 콘크리트에 의한 전단강도
    (1)
    ①
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 전단력과 휨모멘트만을 받는 부재의 전단강도];
    B["KDS 14 20 22 4.2.1 (1) ①"];
    A ~~~ B
    end

    subgraph Variable_def
    VarOut1[/출력변수: 전단강도/];
    VarIn1[/입력변수: 경량콘크리트계수/];
    VarIn2[/입력변수: 콘크리트의 설계기준압축강도/];
    VarIn3[/입력변수: 복부의 폭/];
    VarIn4[/입력변수: 종방향 인장철근의 중심에서 압축콘크리트 연단까지 거리/];

    VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4

    end

    Python_Class ~~~ C(["KDS 14 20 22 4.2.1 (1) ①"])
		C --> Variable_def

		Variable_def --> D --> E --> F

		D{"전단력과 휨모멘트만을 받는 부재의 경우"}
    E["<img src='https://latex.codecogs.com/svg.image? V_{c}=\frac{1}{6}\lambda \sqrt{f_{ck}}b_{w}d'>-----------------------------"];

		F(["전단강도"])
    """

    @rule_method
    def Shear_strength_of_a_member_subjected_to_shear_force_and_bending_moment_only(fIlambda,fIfck,fIbw,fId) -> RuleUnitResult:
        """전단력과 휨모멘트만을 받는 부재의 전단강도

        Args:
            fIlambda (float): 경량콘크리트계수
            fIfck (float): 콘크리트의 설계기준압축강도
            fIbw (float): 복부의 폭
            fId (float): 종방향 인장철근의 중심에서 압축콘크리트 연단까지 거리


        Returns:
            fOVc (float): 전단강도
        """

        assert isinstance(fIlambda, float)
        assert isinstance(fIfck, float)
        assert fIfck > 0
        assert isinstance(fIbw, float)
        assert isinstance(fId, float)


        fOVc = 1 / 6 * fIlambda * (fIfck ** 0.5) * fIbw * fId

        return RuleUnitResult(
            result_variables = {
                "fOVc": fOVc,
            }
        )