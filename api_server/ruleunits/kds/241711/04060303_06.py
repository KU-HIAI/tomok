import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_04060303_06(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.6.3.3 (6)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-16'
    title = '횡방향철근의 연장길이'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.3 기둥
    4.6.3.3 축방향철근과 횡방향철근
    (6)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 횡방향철근의 연장길이]
	  B["KDS 24 17 11 4.6.3.3 (6)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn1[/입력변수: 횡방향철근의 연장길이/]
	  VarIn2[/입력변수: 기둥치수/]
	  end

	  Python_Class ~~~ C(["KDS 24 17 11 4.6.3.3 (6)"])
		C --> Variable_def

   	Variable_def---> D
	  D{"심부구속 횡방향철근과 단부구역의 횡방향철근 설치 ≥ max(기둥치수 x0.5, 380mm)"}
	  E(["PASS or Fail"])

	  D-->E
    """

    @rule_method
    def additional_length_of_horizontal_rebar(fIadlehr,fIcolsiz) -> RuleUnitResult:
        """횡방향철근의 연장길이

        Args:
            fIadlehr (float): 횡방향철근의 연장길이
            fIcolsiz (float): 기둥치수

        Returns:
            pass_fail (bool): 교량내진설계기준(한계상태설계법) 4.6.3.3 축방향철근과 횡방향철근 (6)의 판단 결과
        """

        assert isinstance(fIadlehr, float)
        assert isinstance(fIcolsiz, float)

        if fIadlehr >= max(0.5 * fIcolsiz, 380):
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