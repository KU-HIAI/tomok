import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04070307_05(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.7.3.7 (5)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-22'
    title = '압출용 받침판의 측면 가이드에 작용하는 수평력'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.7 구조 형식에 따른 추가 규정
    4.7.3 세그멘탈 공법 교량
    4.7.3.7 연속압출공법 교량
    (5)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 압출용 받침판의 측면 가이드에 작용하는 수평력];
    B["KDS 24 14 21 4.7.3.7 (5)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수:수평력/];
		VarIn2[/입력변수:수직반력/];

		VarIn1 & VarIn2

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.7.3.7 (5)"])
		C --> Variable_def

		Variable_def--->D--->E

		D{"수평력≥수직반력X1%"}
		E(["Pass or Fail"])
    """

    @rule_method
    def lateral_force_acting_on_the_side_guide_of_the_extrusion_support_plate(fIlatfor, fIverref) -> RuleUnitResult:
        """압출용 받침판의 측면 가이드에 작용하는 수평력

        Args:
            fIlatfor (float): 수평력
            fIverref (float): 수직반력

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.7.3.7 연속압출공법 교량 (5)의 판단 결과
        """

        assert isinstance(fIlatfor, float)
        assert isinstance(fIverref, float)

        if fIlatfor >= fIverref*0.01 :
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