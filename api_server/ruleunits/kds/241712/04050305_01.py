import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241712_04050305_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 12 4.5.3.5 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-16'
    title = '단부구역에 배근되는 횡방향철근'

    description = """
    교량내진 설계기준(케이블교량)
    4. 설계
    4.5 콘크리트교의 설계
    4.5.3 주탑 및 기둥
    4.5.3.5 단부구역의 횡방향철근상세
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 단부구역에 배근되는 횡방향철근];
    B["KDS 24 17 12 4.5.3.5 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 단부구역에 배근되는 횡방향철근 지름/];
    VarIn2[/입력변수: 축방향철근지름/];

	  VarIn1 & VarIn2

		end
		Python_Class ~~~ C(["KDS 24 17 12 4.5.3.5 (1)"])
		C --> Variable_def--->E--->D

		E{"D13 철근 지름 ≤단부구역에 배근되는 횡방향철근 지름, 축방향철근 지름X2/5≤단부구역에 배근되는 횡방향철근 지름"}
		D(["Pass or Fail"])
    """

    @rule_method
    def transverse_steel_diameter_of_end_section(fItrbprz,fIaxredi) -> RuleUnitResult:
        """단부구역에 배근되는 횡방향철근

        Args:
            fItrbprz (float): 단부구역에 배근되는 횡방향철근 지름
            fIaxredi (float): 축방향철근 지름

        Returns:
            pass_fail (bool): 교량내진 설계기준(케이블교량) 4.5.3.5 단부구역의 횡방향철근상세 (1)의 판단 결과
        """

        assert isinstance(fItrbprz, float)
        assert isinstance(fIaxredi, float)

        if 12.7 <= fItrbprz and 0.4 * fIaxredi <= fItrbprz:
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