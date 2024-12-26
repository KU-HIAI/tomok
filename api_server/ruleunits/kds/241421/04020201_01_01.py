import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04020201_01_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.2.2.1 (1) ①'
    ref_date = '2021-04-12'
    doc_date = '2024-05-14'
    title = '콘크리트 압축응력'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.2 사용한계상태
    4.2.2 응력 한계
    4.2.2.1 기본 사항
    (1)
    ①
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 콘크리트 압축응력];
    B["KDS 24 14 21 4.2.2.1 (1) ①"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 유효 프리스트레스와 사용한계상태 하중조합-V에 의한 콘크리트 압축응력/];
		VarIn2[/입력변수: 설계기준 압축강도/];
		VarIn1 & VarIn2

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.2.2.1 (1) ①"])
		C --> Variable_def

		Variable_def--->D--->E
		D{"유효 프리스트레스와 사용한계상태 하중조합-V에 의한 콘크리트 압축응력 ≤ 0.45fck"}
		E(["Pass or Fail"])
    """

    @rule_method
    def concrete_compressive_stress(fIcocost,fIfck) -> RuleUnitResult:
        """설계전단강도

        Args:
            fIcocost (float): 유효 프리스트레스와 사용한계상태 하중조합-V에 의한 콘크리트 압축응력
            fIfck (float): 설계기준 압축강도


        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.2.2.1 기본 사항 (1) ①의 판단 결과
        """
        assert isinstance(fIcocost, float)
        assert isinstance(fIfck, float)


        if fIcocost <= 0.45 * fIfck:
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