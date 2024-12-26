import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_040302_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.3.2 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '피로하중조합에 의해 유발된 응력'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.3 피로한계상태
    4.3.2 철근
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 피로하중조합에 의해 유발된 응력];
    B["KDS 24 14 21 4.3.2 (1)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수: 피로하중조합에 의한 최소 활하중 응력/];
		VarOut1[/출력변수: 피로하중조합에 의해 유발된 응력/];
		VarOut1~~~VarIn1
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.3.2 (1)"])
		C --> Variable_def

		Variable_def--->D--->F
		D["<img src='https://latex.codecogs.com/svg.image?&space;f_{fat}=166-0.33f_{min}'>---------------------------------"]
		D~~~~|KDS 24 12 11 Table 4.1-1|D

		F(["피로하중조합에 의해 유발된 응력"])
    """

    @rule_method
    def Stresses_induced_by_fatigue_load_combinations(fIfmin) -> RuleUnitResult:
        """피로하중조합에 의해 유발된 응력

        Args:
            fIfmin (float): 피로하중조합에 의한 최소 활하중 응력

        Returns:
            fOffat (float): 콘크리트교 설계기준 (한계상태설계법) 4.3.2 철근 (1)의 값
        """

        assert isinstance(fIfmin, float)

        fOffat = 166 - 0.33*fIfmin

        return RuleUnitResult(
            result_variables = {
                "fOffat": fOffat,
            }
        )