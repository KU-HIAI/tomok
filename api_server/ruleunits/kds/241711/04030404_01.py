import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_04030404_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.3.4.4 (1)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-19'
    title = '모드의 수'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.3 해석방법
    4.3.4 다중모드스펙트럼해석법
    4.3.4.4 모드 수
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 모드의 수]
	  B["KDS 24 17 11 4.3.4.4 (1)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn1[/입력변수: 모드의 수/]
	  VarIn2[/입력변수: 지간 수/]
	  VarIn1 & VarIn2
	  end

	  Python_Class ~~~ C(["KDS 24 17 11 4.3.4.4 (1)"])
		C --> Variable_def


	  Variable_def --> D --> E
	  D{"모드의 수 ≥ 지간 수 x3"}
	  E([Pass or Fail])
    """

    @rule_method
    def numbers_of_modes(fInuofmo,fInuofsp) -> RuleUnitResult:
        """모드의 수

        Args:
            fInuofmo (float): 모드의 수
            fInuofsp (float): 지간 수

        Returns:
            pass_fail (bool): 교량내진설계기준(한계상태설계법) 4.3.4.4 모드 수 (1)의 판단 결과 1
            sOnuofmo (string): 교량내진설계기준(한계상태설계법) 4.3.4.4 모드 수 (1)의 판단 결과 2
        """

        assert isinstance(fInuofmo, float)
        assert isinstance(fInuofsp, float)


        if fInuofmo >= fInuofsp * 3 :
          return RuleUnitResult(
              result_variables = {
                  "sOnuofmo": "잔여모드를 모두 포함하여 해석하더라도 응답이 10 % 이상 증가하지 않는 개수의 모드를 고려하여야 한다.",
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )