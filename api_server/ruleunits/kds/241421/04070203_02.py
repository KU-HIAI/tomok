import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04070203_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.7.2.3 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-22'
    title = '현장타설 거더 교량의 하부 플랜지 두께'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.7 구조 형식에 따른 추가 규정
    4.7.2 거더 교량
    4.7.2.3 현장타설 거더 교량
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 현장타설 거더 교량의 하부 플랜지 두께];
    B["KDS 24 14 21 4.7.2.3 (2)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수:거더의 하부플랜지 두께/];
		VarIn2[/입력변수:철근콘크리트 거더 사이 순간격/];
		VarIn3[/입력변수:프리스트레스트 거더 사이 순간격/];

		VarIn1 & VarIn2 & VarIn3

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.7.2.3 (2)"])
		C --> Variable_def

		Variable_def--->D & E--->I

		D{"거더의 하부플랜지 두께>140mm"}
		E{"거더의 하부플랜지 두께≥철근콘크리트 거더 사이 순간격x1/16 or 프리스트레스트 거더 사이 순간격x1/30 "}
		I(["Pass or Fail"])
    """

    @rule_method
    def Lower_flange_thickness_of_cast_in_place_concrete_girder_bridge(fIloflth, fIcdbrcg, fIcdbprg) -> RuleUnitResult:
        """현장타설 거더 교량의 하부 플랜지 두께

        Args:
            fIloflth (float): 거더의 하부플랜지 두께
            fIcdbrcg (float): 철근콘크리트 거더 사이 순간격
            fIcdbprg (float): 프리스트레스트 거더 사이 순간격

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.7.2.3 현장타설 거더 교량 (2)의 판단 결과
        """

        assert isinstance(fIloflth, float)
        assert isinstance(fIcdbrcg, float)
        assert isinstance(fIcdbprg, float)

        if fIloflth > 140 and fIloflth >= max(fIcdbrcg/16, fIcdbprg/30) :
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