import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04060203_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.6.2.3 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-21'
    title = '정착 영역에 작용하는 힘'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.2 보
    4.6.2.3 단부 하부 철근의 정착
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 정착 영역에 작용하는 힘];
    B["KDS 24 14 21 4.6.2.3 (2)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수:작용하는 계수하중에 의한 단면 전단력/];
		VarIn2[/입력변수: 철근의 인장력 분포의 이동거리/];
		VarIn3[/입력변수: 단면의 내부 모멘트 팔길이/]
		VarIn4[/입력변수: 축력/]
		VarOut1[/출력변수: 인장력/]
		VarOut1~~~VarIn1 & VarIn2 & VarIn3 & VarIn4
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.6.2.3 (2)"])
		C --> Variable_def

		Variable_def--->F--->G

		F["<img src='https://latex.codecogs.com/svg.image?T=\frac{V_ua_l}{z}&plus;N_u'>---------------------------------"]

		G(["인장력"])
    """

    @rule_method
    def force_acting_on_the_anchorage_area(fIVu,fIai,fIz,fINu) -> RuleUnitResult:
        """정착 영역에 작용하는 힘

        Args:
            fIVu (float): 작용하는 계수하중에 의한 단면 전단력
            fIai (float): 철근의 인장력 분포의 이동거리
            fIz (float): 단면의 내부 모멘트 팔길이
            fINu (float): 축력

        Returns:
            fOT (float): 콘크리트교 설계기준 (한계상태설계법)  4.6.2.3 단부 하부 철근의 정착 (2)의 값
        """

        assert isinstance(fIVu, float)
        assert isinstance(fIai, float)
        assert isinstance(fIz, float)
        assert fIz != 0
        assert isinstance(fINu, float)

        fOT = fIVu * fIai / fIz + fINu

        return RuleUnitResult(
            result_variables = {
                "fOT": fOT,
            }
        )