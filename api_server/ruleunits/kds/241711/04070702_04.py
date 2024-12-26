import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_04070702_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.7.7.2 (4)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-14'
    title = '유효주기'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.7 지진격리교량의 설계
    4.7.7 해석방법
    4.7.7.2 등가정적하중법
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 유효주기]
	  B["KDS 24 17 11 4.7.7.2 (4)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: 유효주기/]
	  VarIn1[/입력변수: 지진격리받침의 유효강성/]
	  VarIn2[/입력변수: 중력가속도/]
	  VarIn3[/입력변수: 상부구조물의 총중량/]
	  VarOut ~~~ VarIn1 & VarIn2 & VarIn3
	  end

	  Python_Class ~~~ C(["KDS 24 17 11 4.7.7.2 (4)"])
		C --> Variable_def

	  E["<img src='https://latex.codecogs.com/svg.image?T_{eff}=2\pi\sqrt{\frac{W}{K_{eff}g}}'>-------------------------------------"];
	  D(["<img src='https://latex.codecogs.com/svg.image?T_{eff}'>"]);

	  Variable_def --> E --> D
    """

    @rule_method
    def validity_period(fIkeff,fIg,fIW) -> RuleUnitResult:
        """유효주기

        Args:
            fIkeff (float): 지진격리교량의 유효강성
            fIg (float): 중력가속도
            fIW (float): 상부구조물의 총중량

        Returns:
            fOTeff (float): 교량내진설계기준(한계상태설계법) 4.7.7.2 등가정적하중법 (4)의 값
        """

        assert isinstance(fIkeff, float)
        assert fIkeff > 0
        assert isinstance(fIg, float)
        assert fIg > 0
        assert isinstance(fIW, float)
        assert fIW > 0

        import math
        fOTeff = 2 * math.pi * (fIW / fIkeff / fIg) ** 0.5

        return RuleUnitResult(
            result_variables = {
                "fOTeff": fOTeff,
                }
            )