import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_040609_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.6.9 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '철근망의 두 인접한 철근 사이의 간격'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.9 깊은 보
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 철근망의 두 인접한 철근 사이의 간격];
    B["KDS 24 14 21 4.6.9 (2)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수:철근 사이의 간격/];
		VarIn2[/입력변수:깊은 보 두께/];

		VarIn1 & VarIn2
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.6.9 (2)"])
		C --> Variable_def

		Variable_def--->D

		D{"철근 사이의 간격≤min(깊은 보 두께x2, 300mm)"}
		D ---> E(["Pass or Fail"])
    """

    @rule_method
    def Spacing_between_rebars(fIspbere,fIdebeth) -> RuleUnitResult:
        """깊은보의 최소 철근량

        Args:
            fIspbere (float): 철근 사이의 간격
            fIdebeth (float): 깊은 보 두께

        Returns:
            pass_fail (bool): 깊은기초 설계기준(일반설계법)  4.1.1.1 말뚝기초의 축방향 허용지지력과 허용변위 (2)의 판단 결과
        """

        assert isinstance(fIspbere, float)
        assert isinstance(fIdebeth, float)

        if fIspbere <= min( 2*fIdebeth, 300 ):
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