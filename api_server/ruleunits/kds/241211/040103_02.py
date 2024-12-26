import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241211_040103_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 11 4.1.3 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-22'
    title = '포스트텐션의 정착부에 대한 설계력'

    description = """
    교량 설계하중조합(한계상태설계법)
    4. 설계
    4.1 하중의 종류와 하중조합
    4.1.3 받침인상과 포스트텐션힘을 위한 하중계수
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 포스트텐션의 정착부에 대한 설계력];
    B["KDS 24 12 11 4.1.3 (2)"];
    A ~~~ B
    end

	  subgraph Variable_def
	  VarOut1[/출력변수 : 포스트텐션의 정착부에 대한 설계력/];
	  VarIn1[/입력변수 : 최대 긴장력/];

  	end

	  Python_Class ~~~ C(["KDS 24 12 11 4.1.3 (2)"])
		C --> Variable_def

		D{"포스트텐션의 정착부에 대한 설계력 = 최대긴장력 x 1.2"};
  	E{"포스트텐션의 정착부에 대한 설계력"};
  	Variable_def --> D --> E
    """

    @rule_method
    def design_force_of_post_tension_anchorage(fImaxten) -> RuleUnitResult:
        """포스트텐션의 정착부에 대한 설계력
        Args:
            fImaxten (float): 최대 긴장력

        Returns:
            fOdesfor (float): 교량 설계하중조합(한계상태설계법)  4.1.3 받침인상과 포스트텐션힘을 위한 하중계수 (2)의 값
        """

        assert isinstance(fImaxten, float)

        fOdesfor = 1.2 * fImaxten

        return RuleUnitResult(
            result_variables = {
                "fOdesfor": fOdesfor,
            }
        )