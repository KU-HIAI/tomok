import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142010_040203_02_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 10 4.2.3 (2) ③'
    ref_date = '2021-02-18'
    doc_date = '2024-10-02'
    title = '전단력과 비틀림모멘트의 강도감소계수'

    description = """
    콘크리트구조 해석과 설계 원칙
    4. 설계
    4.2 강도
    4.2.3 설계강도
    (2)
    ③
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 전단력과 비틀림모멘트의 강도감소계수];
    B["KDS 14 20 10 4.2.3 (2) ③"];
    A ~~~ B
    end

    subgraph Variable_def
    VarOut1[/출력변수: 전단력과 비틀림모멘트의 강도감소계수/];
    end

    Python_Class ~~~ C(["KDS 14 20 10 4.2.3 (2) ③"])
		C --> Variable_def


		D{"전단력과 비틀림모멘트"};
    E["강도감소계수=0.75"];
		F(["전단력과 비틀림모멘트의 강도감소계수"])

		Variable_def --> D --> E --> F
    """

    @rule_method
    def strength_reduction_factor_of_shear_force_and_torsion_moment() -> RuleUnitResult:
        """전단력과 비틀림모멘트의 강도감소계수


        Returns:
            fOphi (float): 전단력과 비틀림모멘트의 강도감소계수
        """


        fOphi = 0.75

        return RuleUnitResult(
            result_variables = {
                "fOphi": fOphi,
            }
        )