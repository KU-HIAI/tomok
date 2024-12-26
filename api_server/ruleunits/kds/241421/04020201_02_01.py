import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04020201_02_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.2.2.1 (2) ①'
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
    ①
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 강재의 응력];
    B["KDS 24 14 21 4.2.2.1 (2) ①"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 철근의 인장응력/];
		VarIn2[/입력변수: 철근의 기준항복강도/];

		VarIn1 & VarIn2

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.2.2.1 (2) ①"])
		C --> Variable_def

		Variable_def--->G
		G{"하중조합에 따라"}
		G--사용하중조합1 일때--->D
		D{"철근의 인장응력≤<img src='https://latex.codecogs.com/svg.image?0.8f_{y}'>---------------------------------"}
		D-->F
		F(["Pass or Fail"])
    """

    @rule_method
    def steel_stress(fItensrb,fIfy) -> RuleUnitResult:
        """강재의 응력

        Args:
            fItensrb (float): 철근의 인장응력
            fIfy (float): 철근의 기준항복강도

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법) 4.2.2.1 기본 사항 (2) ①의 판단 결과
        """

        assert isinstance(fItensrb, float)
        assert isinstance(fIfy, float)

        if fItensrb <= 0.8 * fIfy :
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