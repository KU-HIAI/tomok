import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241451_03030105(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 51 3.3.1.5'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '말뚝 간격, 여유 거리, 관입 깊이'

    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.3 타입말뚝
    3.3.1 일반사항
    3.3.1.5 말뚝 간격, 여유 거리, 관입 깊이
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 말뚝 간격, 여유 거리, 관입 깊이];
    B["KDS 24 14 51 3.3.1.5"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarIn1[/입력변수: 말뚝 중심 간의 거리/];
		VarIn2[/입력변수: 말뚝 직경/];
		VarIn3[/입력변수: 말뚝 폭/];
		VarIn4[/입력변수: 확대기초의 모서리 면까지의 여유거리/];

		VarIn1

    end

    Python_Class ~~~ C(["KDS 24 14 51 3.3.1.5"])
		C --> Variable_def;

		E{말뚝의 중심간의 거리 > 750mm, 말뚝직경 또는 폭의 2.5배 중 큰 값};
		D{확대기초의 모서리 면까지 여유거리 > 225mm};

		Variable_def ---> E & D ---> F([Pass or Fail])
    """

    @rule_method
    def pile_distance_and_free_distance_penetration_depth(fIdiscep,fIdispil,fIwidpil,fIFredis) -> RuleUnitResult:
        """말뚝 간격, 여유 거리, 관입 깊이

        Args:
            fIdiscep (float): 말뚝 중심 간의 거리
            fIdispil (float): 말뚝 직경
            fIwidpil (float): 말뚝 폭
            fIFredis (float): 확대기초의 모서리 면까지의 여유 거리

        Returns:
            pass_fail (bool): 교량 하부구조 설계기준 (한계상태설계법)  3.3.1.5 말뚝 간격, 여유 거리, 관입 깊이의 판단 결과
        """

        assert isinstance(fIdiscep, float)
        assert isinstance(fIdispil, float)
        assert isinstance(fIwidpil, float)
        assert isinstance(fIFredis, float)

        if fIdiscep > max(750, fIdispil * 2.5, fIwidpil * 2.5) and fIFredis > 225 :
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