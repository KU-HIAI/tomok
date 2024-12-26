import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_04060303_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.6.3.3 (2)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-16'
    title = '횡방향철근'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.3 기둥
    4.6.3.3 축방향철근과 횡방향철근
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 횡방향철근]
	  B["KDS 24 17 11 4.6.3.3(2)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn1[/입력변수: 축방향철근/]
	  VarIn2[/입력변수: 축방향철근 지름/]
	  end

	  Python_Class ~~~ C(["KDS 24 17 11 4.6.3.3(2)"])
		C --> Variable_def--> D --> E --> F

   	D{"단부구역에 배근되는 횡방향철근 ≥ D13"}
	  E{"지름 ≥ 축방향 철근 지름 x 2/5"}
	  F([Pass or Fail])
    """

    @rule_method
    def transverse_reinforcement_diameter(fItrarei,fIaxredi) -> RuleUnitResult:
        """횡방향철근

        Args:
            fItrarei (float): 횡방향철근
            fIaxredi (float): 축방향철근 지름


        Returns:
            pass_fail (bool): 교량내진설계기준(한계상태설계법) 4.6.3.3 축방향철근과 횡방향철근 (2)의 판단 결과
        """

        assert isinstance(fItrarei, float)
        assert isinstance(fIaxredi, float)

        if fItrarei >= 13 and fItrarei >= fIaxredi * 0.4 :
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