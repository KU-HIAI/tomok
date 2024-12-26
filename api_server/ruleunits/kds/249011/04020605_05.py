import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04020605_05(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.2.6.5 (5)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-14'
    title = '알루미늄 합금'

    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.6 받침 마찰요소의 설계
    4.2.6.5 재료
    (5)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 알루미늄 합금];
    B["KDS 24 90 11 4.2.6.5 (5)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 코팅의 최소 평균두께/];
		VarIn2[/입력변수: 최소 국부두께/];
		VarIn3[/입력변수: 거칠기/];

	  VarIn1 & VarIn2 & VarIn3


		end

		Python_Class ~~~ C(["KDS 24 90 11 4.2.6.5 (5)"])
		C --> Variable_def;
		Variable_def--->L
		Variable_def--->K
		Variable_def--->M

		L(["코팅의 최소 평균두께=15μm"])
		M(["최소 국부두께=14μm"])
		K(["거칠기<3μm"])
		K~~~ |"KS B ISO 4287"| K
    """

    @rule_method
    def Minimum_Average_Thickness_Of_The_Coating(fIminavg,fIminlth,fIRy5i) -> RuleUnitResult:
        """알루미늄 합금
        Args:
            fIminavg (float): 코팅의 최소 평균두께
            fIminlth (float): 최소 국부두께
            fIRy5i (float): 거칠기

        Returns:
            pass_fail (bool): 교량 기타시설설계기준 (한계상태설계법)  4.2.6.5 재료 (5)의 판단 결과 1
            sOfilwel (string): 교량 기타시설설계기준 (한계상태설계법)  4.2.6.5 재료 (5)의 판단 결과 2
        """

        assert isinstance(fIminavg, float)
        assert isinstance(fIminlth, float)
        assert isinstance(fIRy5i, float)
        assert 0 <= fIminlth

        if fIminavg >= 15 and fIminlth >= 14 and fIRy5i <= 3 :
          return RuleUnitResult(
              result_variables = {
                  "sOfilwel": "미끄럼면의 표면은 균열, 공극이 없어야 한다",
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "sOfilwel": "미끄럼면의 표면은 균열, 공극이 없어야 한다",
                  "pass_fail": False,
              }
          )