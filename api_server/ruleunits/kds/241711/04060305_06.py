import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_04060305_06(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.6.3.5 (6)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-16'
    title = '수평간격과 보강띠철근 간의 수평간격'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.3 기둥
    4.6.3.5 심부구속 횡방향철근상세
    (6)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 수평간격과 보강띠철근 간의 수평간격]
	  B["KDS 24 17 11 4.6.3.5 (6)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn1[/입력변수: 후프띠철근과 보강띠철간의 수평간격/]
	  VarIn2[/입력변수: 보강띠철근 간의 수평간격/]
	  end

	  Python_Class ~~~ C(["KDS 24 17 11 4.6.3.5 (6)"])
		C --> Variable_def --> D --> E
	  D{"후프띠철근과 보강띠철근의 수평간격, 보강띠철근 간의 수평간격 ≤ 350mm"}
	  E(["PASS or Fail"])
    """

    @rule_method
    def horizontal_spacing(fIhosphore,fIhosprere) -> RuleUnitResult:
        """수평간격과 보강띠철근 간의 수평간격

        Args:
            fIhosphore (float): 후프띠철근과 보강띠철간의 수평간격
            fIhosprere (float): 보강띠철근 간의 수평간격

        Returns:
            pass_fail (bool): 교량내진설계기준(한계상태설계법) 4.6.3.5 심부구속 횡방향철근상세 (6)의 판단 결과
        """

        assert isinstance(fIhosphore, float)
        assert isinstance(fIhosprere, float)

        if fIhosphore <= 350 and fIhosprere <= 350 :
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