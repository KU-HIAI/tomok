import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241712_04050306_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 12 4.5.3.6 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-16'
    title = '축방향철근 중심간 수평간격'

    description = """
    교량내진 설계기준(케이블교량)
    4. 설계
    4.5 콘크리트교의 설계
    4.5.3 주탑 및 기둥
    4.5.3.6 결합나선철근
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 축방향철근 중심간 수평간격];
    B["KDS 24 17 12 4.5.3.6 (3)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 축방향철근 중심간 수평간격/];

	  VarIn1

		end
		Python_Class ~~~ C(["KDS 24 17 12 4.5.3.6 (3)"])
		C --> Variable_def--->E & D

		E{"축방향철근 중심간 수평간격≤200mm"}
		D{"4개 이상 축방향 철근(결합부분)≤축방향철근 중심간 수평간격 "}
    D & E ---> F(["Pass or Fail"])
    """

    @rule_method
    def combined_spiral_rebar(fIhorscl) -> RuleUnitResult:
        """축방향철근 중심간 수평간격

        Args:
            fIhorscl (float): 축방향철근 중심간 수평간격

        Returns:
            pass_fail (bool): 교량내진 설계기준(케이블교량) 4.5.3.6 결합나선철근 (3)의 판단 결과 1
            sOfilwel (string): 교량내진 설계기준(케이블교량) 4.5.3.6 결합나선철근 (3)의 판단 결과 2
        """

        assert isinstance(fIhorscl, float)

        if fIhorscl <= 200 :
          return RuleUnitResult(
              result_variables = {
                  "sOfilwel": "결합부분에는 최소한 4개 이상의 축방향철근을 배근",
                  "pass_fail": True,
                  }
              )
        else:
          return RuleUnitResult(
              result_variables = {
                  "sOfilwel": "결합부분에는 최소한 4개 이상의 축방향철근을 배근",
                  "pass_fail": False,
              }
          )