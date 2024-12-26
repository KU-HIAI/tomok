import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04060206_08(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.6.2.6 (8)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-21'
    title = '전단철근의 최대 폭방향 간격'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.2 보
    4.6.2.6 전단철근
    (8)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 전단철근의 최대 폭방향 간격];
    B["KDS 24 14 21 4.6.2.6 (8)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 단면의 유효깊이/];
		VarOut1[/출력변수: 전단철근의 최대 간격/]
		VarOut1~~~VarIn1
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.6.2.6 (8)"])
		C --> Variable_def

		Variable_def--->F--->G

		F["<img src='https://latex.codecogs.com/svg.image?s_{max}=0.75d\leq&space;600mm'>---------------------------------"]

		G(["Pass or Fail & 전단철근의 최대 폭방향 간격"])
    """

    @rule_method
    def Maximum_spacing_of_shear_bars(fId) -> RuleUnitResult:
        """전단철근의 최대 폭방향 간격

        Args:
            fId (float): 단면의 유효깊이

        Returns:
            fOsmax (float): 콘크리트교 설계기준 (한계상태설계법)  4.6.2.6 전단철근 (8)의 값
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.6.2.6 전단철근 (8)의 판단 결과
        """

        assert isinstance(fId, float)

        fOsmax = 0.75 * fId

        if fOsmax <= 600 :
          return RuleUnitResult(
              result_variables = {
                  "fOsmax": fOsmax,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )