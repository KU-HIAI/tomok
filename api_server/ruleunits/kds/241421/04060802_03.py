import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04060802_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.6.8.2 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-22'
    title = '두 수직 철근 사이의 간격'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.8 벽체
    4.6.8.2 수직 철근
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 두 수직 철근 사이의 간격];
    B["KDS 24 14 21 4.6.8.2 (3)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수:두 수직 철근 사이의 간격/];
		VarIn2[/입력변수:벽체두께/];

		VarIn1 & VarIn2
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.6.8.2 (3)"])
		C --> Variable_def

		Variable_def--->C
		C{"두 수직 철근 사이의 간격≤ min(벽체두께X3,400mm)"}
    H(["Pass or Fail"])
    """

    @rule_method
    def Spacing_between_two_vertical_reinforcing_bars(fIspbtvr, fIwalthi) -> RuleUnitResult:
        """두 수직 철근 사이의 간격

        Args:
            fIspbtvr (float): 두 수직 철근 사이의 간격
            fIwalthi (float): 벽체 두께

        Returns:
            pass_fail (bool):  콘크리트교 설계기준 (한계상태설계법)  4.6.8.2 수직 철근 (3)의 판단 결과
        """

        assert isinstance(fIspbtvr, float)
        assert isinstance(fIwalthi, float)

        if fIspbtvr <= min(3*fIwalthi, 400):
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