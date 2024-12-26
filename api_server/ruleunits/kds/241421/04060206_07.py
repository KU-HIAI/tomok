import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04060206_07(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.6.2.6 (7)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-21'
    title = '굽힘철근의 최대 종방향 간격'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.2 보
    4.6.2.6 전단철근
    (7)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 굽힘철근의 최대 종방향 간격];
    B["KDS 24 14 21 4.6.2.6 (7)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 단면의 유효깊이/];
		VarIn2[/입력변수: 종방향 축과의 각도/]
		VarOut1[/출력변수: 전단철근의 최대 간격/]
		VarOut1~~~VarIn1 & VarIn2
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.6.2.6 (7)"])
		C --> Variable_def

		Variable_def--->F--->G

		F["<img src='https://latex.codecogs.com/svg.image?s_{max}=0.6d(1&plus;cot\alpha)'>---------------------------------"]

		G(["굽힘철근의 최대 종방향 간격"])
    """

    @rule_method
    def Maximum_longitudinal_spacing_of_bent_bars(fId,fIalpha) -> RuleUnitResult:
        """굽힘철근의 최대 종방향 간격

        Args:
            fId (float): 단면의 유효깊이
            fIalpha (float): 종방향 축과의 각도

        Returns:
            fOsmax (float): 콘크리트교 설계기준 (한계상태설계법)  4.6.2.6 전단철근 (7)의 값
        """

        assert isinstance(fId, float)
        assert isinstance(fIalpha, float)
        assert fIalpha != 0

        import math

        fOsmax = (0.6)*fId*(1+1/math.tan(math.radians(fIalpha)))

        return RuleUnitResult(
            result_variables = {
                "fOsmax": fOsmax,
            }
        )