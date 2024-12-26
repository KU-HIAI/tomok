import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS171000_0201_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 17 10 00 2.1 (2)'
    ref_date = '2018-12-06'
    doc_date = '2024-02-13'
    title = '기반암 전단파 속도'

    description = """
    내진설계 일반
    2. 조사 및 계획
    2.1 지반조사
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 기반암 전단파 속도];
    B["KDS 17 10 00 2.1 (2)"];
    A ~~~ B
    end
    subgraph Variable_def;
		VarIn1[/입력변수:전단파 속도/];

		VarIn1
		end


    Python_Class ~~~ C(["KDS 17 10 00 2.1 (2)"])
		C --> Variable_def

    Variable_def--->D
		D{"전단파속도≥760m/s"}
		D --->E(["Pass or Fail"])
    """

    @rule_method
    def Bedrock_shear_wave_velocity(fIVs) -> RuleUnitResult:
        """기반암 전단파 속도

        Args:
            fIVs (float): 전단파속도

        Returns:
            pass_fail (bool): 내진설계 일반  2.1 지반조사 (2)의 판단 결과
        """

        assert isinstance(fIVs, float)

        if fIVs >= 760:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": True,
                  }
              )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": True,
                  }
              )