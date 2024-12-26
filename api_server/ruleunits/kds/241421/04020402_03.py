import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04020402_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.2.4.2 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '보정값'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.2 사용한계상태
    4.2.4 처짐
    4.2.4.2 직접 처짐 계산을 생략하는 경우
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 보정값];
    B["KDS 24 14 21 4.2.4.2 (3)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 플랜지 폭/];
		VarIn2[/입력변수: 복부폭/];
		VarIn3[/입력변수: 지간/];
		VarIn4[/입력변수: 단면의 유효깊이/];

		VarIn1 & VarIn2  & VarIn3  & VarIn4

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.2.4.2 (3)"])
		C --> Variable_def

		Variable_def--->D--->E

		D["플랜지폭>복부폭 x3"]
		E["0.8 x l/d"]

    """

    @rule_method
    def correction_value(fIld,fIflawid,fIabdwid) -> RuleUnitResult:
        """보정값

        Args:
            fIld (float): 한계 지간/깊이-비
            fIflawid (float): 플랜지 폭
            fIabdwid (float): 복부폭

        Returns:
            fOld (float): 콘크리트교 설계기준 (한계상태설계법) 4.2.4.2 직접 처짐 계산을 생략하는 경우 (3)의 값
        """

        assert isinstance(fIld, float)
        assert isinstance(fIflawid, float)
        assert isinstance(fIabdwid, float)

        if fIflawid > 3 * fIabdwid :
          fOld = 0.8 * fIld
          return RuleUnitResult(
              result_variables = {
                  "fOld": fOld,
              }
          )
        else:
          fOld = fIld
          return RuleUnitResult(
              result_variables = {
                  "fOld": fOld,
              }
          )