import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04020605_07(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.2.6.5 (7)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-14'
    title = '접착제'

    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.6 받침 마찰요소의 설계
    4.2.6.5 재료
    (7)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 접착제];
    B["KDS 24 90 11 4.2.6.5 (7)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 겹침전단강도/];
		end

		Python_Class ~~~ C(["KDS 24 90 11 4.2.6.5 (7)"])
		C --> Variable_def;
		Variable_def--->L--->K

		L{"25MPa≤겹침전단강도"}
    K(["Pass or Fail"])
    """

    @rule_method
    def Overlap_Shear_Strength(fIovshst) -> RuleUnitResult:
        """접착제
        Args:
            fIovshst (float): 겹침전단강도

        Returns:
            pass_fail (bool): 교량 기타시설설계기준 (한계상태설계법)  4.2.6.5 재료 (7)의 판단 결과
        """

        assert isinstance(fIovshst, float)

        if fIovshst >= 25 :
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