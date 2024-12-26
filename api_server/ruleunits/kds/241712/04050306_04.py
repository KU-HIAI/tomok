import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241712_04050306_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 12 4.5.3.6 (4)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-16'
    title = '결합나선철근의 나선철근간의 중심간격'

    description = """
    교량내진 설계기준(케이블교량)
    4. 설계
    4.5 콘크리트교의 설계
    4.5.3 주탑 및 기둥
    4.5.3.6 결합나선철근
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 결합나선철근의 나선철근간의 중심간격];
    B["KDS 24 17 12 4.5.3.6 (4)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 결합나선철근의 나선철근간의 중심간격/];
		VarIn2[/입력변수: 심부단면치수/];

	  VarIn1 & VarIn2

		end
		Python_Class ~~~ C(["KDS 24 12 21 4.5.3.6 (4)"])
		C --> Variable_def--->E

		E{"결합나선철근의 나선철근간의 중심간격≤심부단면치수x0.75"}
    E ---> F(["Pass or Fail"])
    """

    @rule_method
    def Combined_spiral_rebar(fIdint,fIds) -> RuleUnitResult:
        """결합나선철근의 나선철근간의 중심간격

        Args:
            fIdint (float): 결합나선철근의 나선철근간의 중심간격
            fIds (float): 심부단면치수

        Returns:
            pass_fail (bool): 교량내진 설계기준(케이블교량) 4.5.3.6 결합나선철근 (4)의 판단 결과
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