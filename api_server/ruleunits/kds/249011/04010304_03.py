import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04010304_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.1.3.4 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-14'
    title = '중심 간격'

    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.1 신축이음
    4.1.3 설계
    4.1.3.4 설계상세
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 중심 간격];
    B["KDS 24 90 11 4.1.3.4 (3)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 중심간격/];
		VarIn2[/입력변수: 공기 배출 구멍 직경/];

		end
		Python_Class ~~~ C(["KDS 24 90 11 4.1.3.4 (3)"])
		C --> Variable_def--->E--->F

		E{"중심간격≤460mm, 20mm≤공기 배출 구멍 직경"}
		F(["Pass or Fail"])
    """

    @rule_method
    def Centre_To_Centre_Distance (fIcencdi, fIairodi) -> RuleUnitResult:
        """중심 간격
        Args:
            fIcencdi (float): 중심 간격
            fIairodi (float): 공기 배출 구멍 직경

        Returns:
            pass_fail (bool): 교량 기타시설설계기준 (한계상태설계법)  4.1.3.4 설계상세 (3)의 판단 결과
        """

        assert isinstance(fIcencdi, float)
        assert isinstance(fIairodi, float)

        if fIcencdi <= 460 and fIairodi >= 20 :
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