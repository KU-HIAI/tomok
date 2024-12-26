import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010205_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.2.5 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-17'
    title = '계면에 작용하는 전단응력'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.5 서로 다른 시기에 타설한 콘크리트의 계면 전단
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 계면에 작용하는 전단응력];
    B["KDS 24 14 21 4.1.2.5 (2)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 새로 친 콘크리트에 작용하는 종방향력과 총종방항력의 비/];
		VarIn2[/입력변수: 계수전단력/];
		VarIn3[/입력변수: 단면의 내부 모멘트 팔길이/];
		VarIn4[/입력변수: 계면의 폭/];
		VarOut1[/출력변수: 계면에 작용하는 전단응력/];
		VarOut1~~~VarIn1 & VarIn2 & VarIn3 & VarIn4

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.2.5 (2)"])
		C --> Variable_def

		Variable_def--->E--->D
		E["<img src='https://latex.codecogs.com/svg.image?v_u=\frac{\beta&space;V_u}{zb}'>---------------------------------"];
		D(["계면에 작용하는 전단응력"])

    """

    @rule_method
    def Shear_stress_acting_on_the_interface(fIbeta,fIVu,fIz,fIb) -> RuleUnitResult:
        """계면에 작용하는 전단응력

        Args:
            fIbeta (float): 새로 친 콘크리트에 작용하는 종방향력과 총종방항력의 비
            fIVu (float): 계수전단력
            fIz (float): 단면의 내부 모멘트 팔길이
            fIb (float): 계면의 폭

        Returns:
            fOVu (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.5 서로 다른 시기에 타설한 콘크리트의 계면 전단 (2)의 값
        """

        assert isinstance(fIbeta, float)
        assert isinstance(fIVu, float)
        assert isinstance(fIz, float)
        assert fIz != 0
        assert isinstance(fIb, float)
        assert fIb != 0

        fOVu = fIbeta*fIVu/fIz/fIb*1000

        return RuleUnitResult(
            result_variables = {
                "fOVu": fOVu,
            }
        )