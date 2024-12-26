import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010203_10(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.2.3 (10)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-17'
    title = '경량콘크리트의 유효강도계수'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.3 전단보강철근이 배치된 부재
    (10)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 경량콘크리트의 유효강도계수];
    B["KDS 24 14 21 4.1.2.3 (10)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 콘크리트의 유효강도계수/];
		VarIn2[/입력변수: 경량콘크리트 계수/];
		VarIn3[/입력변수: 28일 콘크리트 공시체의 기준압축강도/];
		VarIn1 & VarIn2 & VarIn3

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.2.3 (10)"])
		C --> Variable_def

		Variable_def--->D
		D["<img src='https://latex.codecogs.com/svg.image? v=0.5\eta _{l}\left ( 1-\frac{f_{ck}}{250} \right )'>-----------------------------------"] ;

		D-->E(["콘크리트 유효강도계수"])
    """

    @rule_method
    def Effective_strength_factor_of_lightweight_concrete(fIetal,fIfck) -> RuleUnitResult:
        """경량콘크리트의 유효강도계수

        Args:
            fIetal (float): 경량콘크리트 계수
            fIfck (float): 28일 콘크리트 공시체의 기준압축강도

        Returns:
            fOnu (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.3 전단보강철근이 배치된 부재 (10)의 값
        """

        assert isinstance(fIetal, float)
        assert isinstance(fIfck, float)

        fOnu = 0.5 * fIetal * ( 1- fIfck / 250 )

        return RuleUnitResult(
            result_variables = {
                "fOnu": fOnu,
            }
        )