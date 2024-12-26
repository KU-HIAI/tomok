import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_04060306_05(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.6.3.6 (5)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-16'
    title = '결합나선철근의 나선철근간의 중심간격'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.3 기둥
    4.6.3.6 결합나선철근
    (5)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 결합나선철근의 나선철근간의 중심간격]
	  B["KDS 24 17 11 4.6.3.6 (5)"]
	  A ~~~ B
	  end

  	subgraph Variable_def
  	VarIn1[/입력변수: 결합나선철근의 나선철근간의 중심 간격/]
	  VarIn2[/입력변수: 심부단면치수/]
	  end
	  Python_Class ~~~ C(["KDS 24 17 11 4.6.3.6 (5)"])
		C --> Variable_def --> D --> E
	  D{"<img src='https://latex.codecogs.com/svg.image?d_{int}\leq&space;0.75d_s'>---------------------"}
	  E(["PASS or Fail"])
    """

    @rule_method
    def spiral_rebar_center_spacing(fIdint,fIds) -> RuleUnitResult:
        """중심간격

        Args:
            fIdint (float): 결합나선철근의 나선철근간의 중심 간격
            fIds (float): 심부단면치수

        Returns:
            pass_fail (bool): 교량내진설계기준(한계상태설계법) 4.6.3.6 결합나선철근 (5)의 판단 결과
        """

        assert isinstance(fIdint, float)
        assert isinstance(fIds, float)

        if fIdint <= fIds * 0.75 :
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