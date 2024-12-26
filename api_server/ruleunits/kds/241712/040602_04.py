import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241712_040602_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 12 4.6.2 (4)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-16'
    title = '콘크리트 및 철근의 실제강도'

    description = """
    교량내진 설계기준(케이블교량)
    4. 설계
    4.6 붕괴방지수준의 내진성능 검증
    4.6.2 입력재료강도
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 콘크리트 및 철근의 실제강도];
    B["KDS 24 17 12 4.6.2 (4)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 콘크리트의 실제강도/];
		VarIn2[/입력변수: 철근의 실제강도/];
		VarIn3[/입력변수: 기준강도/];

	  VarIn1 & VarIn2 & VarIn3

		end

		Python_Class ~~~ C(["KDS 24 17 12 4.6.2 (4)"])
		C --> Variable_def--->E & F

		E{"기준강도x1.7≤콘크리트의 실제강도"}
		F{"기준강도x1.3≤철근의 실제강도"}
    E & F ---> G(["Pass or Fail"])
    """

    @rule_method
    def interpretation_method(fIacstco,fIacstrb,fIspcstr) -> RuleUnitResult:
        """콘크리트 및 철근의 실제강도

        Args:
            fIacstco (float): 콘크리트의 실제 강도
            fIacstrb (float): 철근의 실제 강도
            fIspcstr (float): 기준강도

        Returns:
            pass_fail (bool): 교량내진 설계기준(케이블교량) 4.6.2 입력재료강도 (4)의 판단 결과
        """

        assert isinstance(fIacstco, float)
        assert isinstance(fIacstrb, float)
        assert isinstance(fIspcstr, float)

        if fIacstco >= 1.7 * fIspcstr and fIacstrb >= 1.3 * fIspcstr:
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