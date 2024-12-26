import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241712_04050303_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 12 4.5.3.3 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-16'
    title = '축방향철근 단면적'

    description = """
    교량내진 설계기준(케이블교량)
    4. 설계
    4.5 콘크리트교의 설계
    4.5.3 주탑 및 기둥
    4.5.3.3 축방향철근과 횡방향철근
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 축방향철근 단면적];
    B["KDS 24 17 12 4.5.3.3 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 축방향철근 단면적/];
    VarIn2[/입력변수: 기둥 전체 단면적/];


	 VarIn1 & VarIn2

		end
		Python_Class ~~~ C(["KDS 24 17 12 4.5.3.3 (1)"])
		C --> Variable_def--->E--->F

		E{"기둥전체 단면적X0.01≤축방향철근 단면적≤기둥 전체 단면적X0.06"}
		F(["Pass or Fail"])
    """

    @rule_method
    def axial_steal_cross_sectional_area(fIaxrcsa,fIctcrsa) -> RuleUnitResult:
        """축방향철근 단면적

        Args:
            fIaxrcsa (float): 축방향철근 단면적
            fIctcrsa (float): 기둥 전체 단면적


        Returns:
            pass_fail (bool): 교량내진 설계기준(케이블교량) 4.5.3.3 축방향철근과 횡방향철근 (1)의 판단 결과
        """

        assert isinstance(fIaxrcsa, float)
        assert isinstance(fIctcrsa, float)

        if fIctcrsa * 0.01 <= fIaxrcsa <= fIctcrsa * 0.06  :
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