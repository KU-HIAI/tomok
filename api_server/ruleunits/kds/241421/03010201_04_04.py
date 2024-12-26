import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_03010201_04_04(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 3.1.2.1 (4) ④'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '평균인장강도'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.1 콘크리트
    3.1.2 재료특성
    3.1.2.1 강도
    (4)
    ④
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 평균인장강도];
    B["KDS 24 14 21 3.1.2.1 (4) ④"];
    A ~~~ B
    end
	  subgraph Variable_def;

		VarIn1[/평균인장강도/];

		VarOut1[/출력변수: 기준인장강도/];


	  VarOut1~~~VarIn1
		end

	  Python_Class ~~~ C(["KDS 24 14 21 3.1.2.1 (4) ④"])
		C --> Variable_def

		I(["콘크리트의 기준인장강도"]);
		H["<img src='https://latex.codecogs.com/svg.image?&space;f_{ctk}=0.7f_{ctm}'>-------------------"]
		Variable_def---->H--->I

    """

    @rule_method
    def Concrete_tensile_strength(fIfctm) -> RuleUnitResult:
        """평균인장강도

        Args:
            fIfctm (float): 재령 28일 평균인장강도

        Returns:
            fOfctk (float): 콘크리트교 설계기준(한계상태설계법) 3.1.2.1 강도 (4) ④의 값
        """

        assert isinstance(fIfctm, float)

        fOfctk = 0.7 * (fIfctm)

        return RuleUnitResult(
            result_variables = {
                "fOfctk": fOfctk,
          }
        )