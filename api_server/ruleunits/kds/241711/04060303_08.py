import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_04060303_08(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.6.3.3 (8)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-16'
    title = '횡방향 철근의 간격'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.3 기둥
    4.6.3.3 축방향철근과 횡방향철근
    (8)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 횡방향 철근의 간격]
	  B["KDS 24 17 11 4.6.3.3 (8)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn1[/입력변수: 횡방향철근의 간격/]
	  VarIn2[/입력변수: 부재 단면 최소치수/]
	  end

	  Python_Class ~~~ C(["KDS 24 17 11 4.6.3.3 (8)"])
		C --> Variable_def

   	D["단부구역 이외의 위치에 배근되는 횡방향철근"]
	  E["축방향 철근이 겹침이음된 구간"]
	  F{"횡방향 철근의 간격 ≤ 100mm or 부재단면 최소치수x 1/4"}
	  G["4.6.3.5 철근상세 만족필요 X"]
	  H([횡방향철근의 간격])
	  Variable_def ---> D & E
	  D ---> G ---> H
	  E ---> F ---> H
    """

    @rule_method
    def transeverse_reinforcement_spacing(fIdistan,fImicsdm) -> RuleUnitResult:
        """횡방향 철근의 간격

        Args:
            fIdistan (float): 횡방향 철근의 간격
            fImicsdm (float): 부재 최소 단면치수

        Returns:
            pass_fail (bool): 교량내진설계기준(한계상태설계법) 4.6.3.3 축방향철근과 횡방향철근 (8)의 판단 결과
        """

        assert isinstance(fIdistan, float)
        assert isinstance(fImicsdm, float)

        if fIdistan <= 100 and fIdistan <= 0.25 * fImicsdm:
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