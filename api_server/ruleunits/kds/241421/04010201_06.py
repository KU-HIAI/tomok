import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010201_06(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.2.1 (6)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '계수하중에 의한 단면의 전단력'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.1 일반
    (6)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 계수하중에 의한 단면의 전단력];
    B["KDS 24 14 21 4.1.2.1 (6)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 계수하중에 의한 단면의 전단력/];
		VarIn2[/입력변수: 콘크리트 설계전단강도/];
 		VarIn3[/입력변수: 단면 설계전단강도/];

		VarIn1 & VarIn2 & VarIn3

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.2.1 (6)"])
		C --> Variable_def

		Variable_def--->F
    F--->|yes|D--->E


		F{"<img src='https://latex.codecogs.com/svg.image?V_{cd}<V_{u}'>---------------------------------"}
		F~~~ |"KDS 24 14 21 4.1.2.3"| F
    D{"<img src='https://latex.codecogs.com/svg.image?V_{u} \leq V_{d}'>---------------------------------"}
    E(["Pass or Fail"])
    """

    @rule_method
    def Sectional_shear_force_due_to_modulus_load(fIVu,fIVcd,fIVd) -> RuleUnitResult:
        """계수하중에 의한 단면의 전단력

        Args:
            fIVu (float): 계수하중에 의한 단면의 전단력
            fIVcd (float): 콘크리트 설계전단강도
            fIVd (float): 전단철근이 배치된 부재의 설계전단강도

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.1 일반 (6)의 판단 결과
        """

        assert isinstance(fIVu, float)
        assert isinstance(fIVcd, float)
        assert isinstance(fIVd, float)



        if fIVu > fIVcd:
          if fIVd >= fIVu:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": True,
                }
            )
          else:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": False,
                }
            )