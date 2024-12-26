import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241451_03030203_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 51 3.3.2.3 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-17'
    title = '말뚝기초의 침하'

    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.3 타입말뚝
    3.3.2 사용한계상태의 변위와 지지력
    3.3.2.3 침하
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 말뚝기초의 침하];
    B["KDS 24 14 51 3.3.2.3 (1)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarIn1[입력변수:말뚝기초의 침하]
		VarIn2[입력변수:허용침하량]

    end
    Python_Class ~~~ E(["KDS 24 14 51 3.2.3.1 (5)"])
		E --> Variable_def;

		C{"말뚝기초의 침하 ≤ 허용침하량"}
		C~~~ |"KDS 24 14 51 3.2.2.2"| C

		Variable_def ---> C ---> D([Pass or Fail])
    """

    @rule_method
    def the_sinking_of_the_foundation_of_a_stake(fIsinsta,fIallsub) -> RuleUnitResult:
        """말뚝기초의 침하

        Args:
            fIsinsta (float): 말뚝기초의 침하
            fIallsub (float): 허용침하량

        Returns:
            pass_fail (bool): 교량 하부구조 설계기준 (한계상태설계법) 3.3.2.3 침하(1)의 판단 결과
        """

        assert isinstance(fIsinsta, float)
        assert isinstance(fIallsub, float)

        if fIsinsta <= fIallsub :
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": True,
                  }
              )
        else :
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
                  }
              )