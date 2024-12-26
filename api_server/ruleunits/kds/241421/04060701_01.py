import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04060701_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.6.7.1 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-22'
    title = '종방향 철근의 총단면적'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.7 속빈 사각형 단면 압축부재의 보강철근
    4.6.7.1 일반사항
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 종방향 철근의 총단면적];
    B["KDS 24 14 21 4.6.7.1 (1)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수:종방향 철근의 총단면적/];
		VarIn2[/입력변수:콘크리트 단면적/];

		VarIn1 & VarIn2
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.6.7.1 (1)"])
		C --> Variable_def

		Variable_def--->E--->H

		E{"종방향 철근의 총단면적<img src='https://latex.codecogs.com/svg.image?\inline&space;\LARGE&space;\geq&space;0.01A_c'>---------------------------------"}
    H(["Pass or Fail"])
    """

    @rule_method
    def Total_cross_sectional_area_of_longitudinal_reinforcing_bars(fItoclrb, fIAc) -> RuleUnitResult:
        """종방향 철근의 총단면적

        Args:
            fItoclrb (float): 종방향 철근의 총단면적
            fIAc (float): 콘크리트 단면적

        Returns:
            pass_fail (bool):  콘크리트교 설계기준 (한계상태설계법)  4.6.7.1 일반사항 (1)의 판단 결과
        """

        assert isinstance(fItoclrb, float)
        assert isinstance(fIAc, float)

        if fItoclrb >= 0.01*fIAc:
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