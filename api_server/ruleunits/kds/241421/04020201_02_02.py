import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04020201_02_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.2.2.1 (2) ②'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '강재의 응력'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.2 사용한계상태
    4.2.2 응력 한계
    4.2.2.1 기본 사항
    (2)
    ②
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 강재의 응력];
    B["KDS 24 14 21 4.2.2.1 (2) ②"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 프리스트레스 강재의 응력/];
		VarIn2[/입력변수: 프리스트레스 강재의 인장강도/];

		VarIn1 & VarIn2

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.2.2.1 (2) ②"])
		C --> Variable_def

		Variable_def--->G
		G{"하중조합에 따라"}
		G--유효 프리스트레스와 사용한계상태 하중조합V 일때--->E
		E{"프리스트레스 강재의 응력≤<img src='https://latex.codecogs.com/svg.image?0.65f_{pu}'>---------------------------------"}
		E-->F
		F(["Pass or Fail"])
    """

    @rule_method
    def steel_stress(fIstrpst,fIfpu) -> RuleUnitResult:
        """강재의 응력

        Args:
            fIstrpst (float): 프리스트레스 강재의 응력
            fIfpu (float): 프리스트레스 강재의 인장강도

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법) 4.2.2.1 기본 사항 (2) ②의 판단 결과
        """

        assert isinstance(fIstrpst, float)
        assert isinstance(fIfpu, float)

        if fIstrpst <= 0.65 * fIfpu :
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