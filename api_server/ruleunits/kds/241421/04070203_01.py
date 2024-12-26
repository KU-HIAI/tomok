import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04070203_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.7.2.3 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-22'
    title = '콘크리트 거더의 구성 요소 두께'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.7 구조 형식에 따른 추가 규정
    4.7.2 거더 교량
    4.7.2.3 현장타설 거더 교량
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 콘크리트 거더의 구성 요소 두께];
    B["KDS 24 14 21 4.7.2.3 (1)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수:상부 플랜지/];
		VarIn2[/입력변수:정착과 피복두께에 필요한 두께/];
		VarIn3[/입력변수:인접 거더 사이의 순간격/];


	  VarIn1 & VarIn2
	  ~~~~VarIn3

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.7.2.3 (1)"])
		C --> Variable_def

		Variable_def--->D & E--->I

		D{"상부플랜지의 두께>정착과 피복두께에 필요한 두께"}
		E{"인접 거더사이의 순간격X1/20≤ 상부플렌지의 두께"}
		I(["Pass or Fail"])
    """

    @rule_method
    def cast_in_place_concrete_girder_bridge(fIupflth, fIthreft, fIingadg) -> RuleUnitResult:
        """현장타설 거더 교량

        Args:
            fIupflth (float): 상부 플랜지 두께
            fIthreft (float): 정착과 피복두께에 필요한 두께
            fIingadg (float): 인접 거더 사이의 순간격

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.7.2.3 현장타설 거더 교량 (1)의 판단 결과
        """

        assert isinstance(fIupflth, float)
        assert isinstance(fIthreft, float)
        assert isinstance(fIingadg, float)

        if fIupflth > fIthreft and fIupflth >= fIingadg/20 :
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