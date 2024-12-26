import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04060201_01_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.6.2.1 (1) ②'
    ref_date = '2021-04-12'
    doc_date = '2024-05-14'
    title = '주철근 최소 단면적'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.2 보
    4.6.2.1 주철근
    (1)
    ②
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 주철근 최소 단면적];
    B["KDS 24 14 21 4.6.2.1 (1) ②"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수:해석에 의해 필요한 철근량/];
		VarIn2[/입력변수:인장철근/];

		VarIn1 & VarIn2
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.6.2.1 (1) ②"])
		C --> Variable_def

		Variable_def--->D--->E

		D{"인장철근 ≥ 해석에 의해 필요한 철근량 X 4/3"}

		E(["Pass or Fail"])
    """

    @rule_method
    def minimum_area_of_main_reinforcement(fIrerean,fItenrei) -> RuleUnitResult:
        """주철근 최소 단면적

        Args:
            fIrerean (float): 해석에 의해 필요한 철근량
            fItenrei (float): 인장철근

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법) 4.6.2.1 극한한계상태에서의 중립축의 깊이 (1) ②의 판단 결과
        """

        assert isinstance(fIrerean, float)
        assert isinstance(fItenrei, float)

        if fItenrei >= fIrerean * 4/3 :
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