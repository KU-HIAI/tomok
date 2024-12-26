import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_040208(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.2.8'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '지압응력'

    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.8 철도교 수평분산장치(크리프커플러) 및 스토퍼
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 지압응력];
    B["KDS 24 90 11 4.2.8"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 지압응력/];
		VarIn2[/입력변수: 설계기준압축강도/];
		VarIn1 & VarIn2

		end

		Python_Class ~~~ Variable_def;
		Variable_def---> C--->E
		C["지압응력≤0.8 x 설계기준압축강도"]

		E(["Pass or Fail"])
    """

    @rule_method
    def Bearing_Stress (fIfc,fIfck) -> RuleUnitResult:
        """지압응력
        Args:
            fIfc (float): 지압응력
            fIfck (float): 설계기준압축강도

        Returns:
            pass_fail (bool): 교량 기타시설설계기준 (한계상태설계법)  4.2.8 철도교 수평분산장치(크리프커플러) 및 스토퍼의 판단 결과
        """

        assert isinstance(fIfc, float)
        assert isinstance(fIfck, float)

        if fIfc <= 0.8*fIfck:
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