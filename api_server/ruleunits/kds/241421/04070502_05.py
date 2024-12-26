import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04070502_05(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.7.5.2 (5)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-22'
    title = '현장타설 속빈 슬래브교의 교량 받침'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.7 구조 형식에 따른 추가 규정
    4.7.5 슬래브교
    4.7.5.2 현장타설 속빈 슬래브교
    (5)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 현장타설 속빈 슬래브교의 교량 받침];
    B["KDS 24 14 21 4.7.5.2 (5)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수:교량 받침/];
		VarIn2[/입력변수:상부구조의 횡방향 회전각/];


		VarIn1 & VarIn2

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.7.5.2 (5)"])
		C --> Variable_def

		Variable_def--->D & E---> I(["Pass or Fail"])

		D["교량받침≥2개"]
		E["상부구조의 횡방향 회전각≤0.005"]
    """

    @rule_method
    def bearing_of_cast_in_place_hollow_slab_bridge(fIbearig, fItranrs) -> RuleUnitResult:
        """현장타설 속빈 슬래브교의 교량 받침

        Args:
            fIbearig (float): 교량 받침
            fItranrs (float): 상부구조의 횡방향 회전각

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.7.5.2 현장타설 속빈 슬래브교 (5)의 판단 결과
        """

        assert isinstance(fIbearig, float)
        assert isinstance(fItranrs, float)

        if fIbearig >= 2 and fItranrs <= 0.005:
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