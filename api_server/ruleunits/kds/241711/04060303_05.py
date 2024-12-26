import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_04060303_05(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.6.3.3 (5)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-16'
    title = '최대간격'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.3 기둥
    4.6.3.3 축방향철근과 횡방향철근
    (5)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 최대간격]
	  B["KDS 24 17 11 4.6.3.3 (5)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn1[/입력변수: 최대간격/]
	  VarIn2[/입력변수: 부재 최소 단면치수/]
	  VarIn3[/입력변수: 축방향철근지름/]
	  end

	  Python_Class ~~~ C(["KDS 24 17 11 4.6.3.3 (5)"])
		C --> Variable_def

   	Variable_def--> I

    I-->J
	  I{"min(부재 최소 단면치수x1/4,축방향철근지름x6) &ge; 최대간격"}
	  J([Pass or Fail])
    """

    @rule_method
    def maximum_spacing(fImaxspa,fImicsdm,fIaxredi) -> RuleUnitResult:
        """최대간격

        Args:
            fImaxspa (float): 최대간격
            fImicsdm (float): 부재 최소 단면치수
            fIaxredi (float): 축방향철근지름

        Returns:
            pass_fail (bool): 교량내진설계기준(한계상태설계법) 4.6.3.3 축방향철근과 횡방향철근 (5)의 판단 결과
        """

        assert isinstance(fImaxspa, float)
        assert isinstance(fImicsdm, float)
        assert isinstance(fIaxredi, float)

        if min(fImicsdm * 0.25, fIaxredi * 6) >= fImaxspa:
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