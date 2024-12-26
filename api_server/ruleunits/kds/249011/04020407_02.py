import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04020407_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.2.4.7 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '포트 설계'

    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.4 포트받침
    4.2.4.7 포트 설계
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 포트 설계];
    B["KDS 24 90 11 4.2.4.7 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 포트의 응력/];
		VarIn2[/입력변수: 항복강도/];

    VarIn1 & VarIn2

		end

		Python_Class ~~~ C(["KDS 24 90 11 4.2.4.7 (2)"])
		C --> Variable_def;
		Variable_def--->K--->L--->M

		K{"극한한계상태일때"}
		L{"포트의 응력≤항복강도"};
		M(["Pass or Fail"])
    """

    @rule_method
    def Stress_On_Pot(fIstrpot, fIyldstr) -> RuleUnitResult:
        """포트 설계

        Args:
            fIstrpot (float): 포트의 응력
            fIyldstr (float): 항복강도

        Returns:
            pass_fail (bool): 교량 기타시설설계기준 (한계상태설계법)  4.2.4.7 포트 설계 (2)의 판단 결과
        """

        assert isinstance(fIstrpot, float)
        assert isinstance(fIyldstr, float)

        if fIstrpot <= fIyldstr:
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