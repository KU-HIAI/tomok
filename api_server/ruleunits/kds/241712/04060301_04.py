import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241712_04060301_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 12 4.6.3.1 (4)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-16'
    title = '압력지반운동 시간이력 수'

    description = """
    교량내진 설계기준(케이블교량)
    4. 설계
    4.6 붕괴방지수준의 내진성능 검증
    4.6.3 응답(시간)이력해석법
    4.6.3.1 해석방법
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 압력지반운동 시간이력 수];
    B["KDS 24 17 12 4.6.3.1 (4)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 압력지반운동 시간이력 수/];

	  VarIn1

		end
		Python_Class ~~~ C(["KDS 24 17 12 4.6.3.1 (4)"])
		C --> Variable_def--->E

		E{"4세트≤압력지반운동 시간이력 수"}
    E ---> F(["Pass or Fail"])
    """

    @rule_method
    def interpretation_method(fInumpgm) -> RuleUnitResult:
        """압력지반운동 시간이력 수

        Args:
            fInumpgm (float): 압력지반운동 시간이력 수

        Returns:
            pass_fail (bool): 교량내진 설계기준(케이블교량) 4.6.3.1 (4)의 판단 결과
        """

        assert isinstance(fInumpgm, float)

        if fInumpgm >= 4 :
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