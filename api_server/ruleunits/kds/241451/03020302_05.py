import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241451_03020302_05(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 51 3.2.3.2 (5)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '하중편심량'

    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.2 확대기초
    3.2.3 극한한계상태의 지지력
    3.2.3.2 암반 지지력
    (5)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 하중편심량];
    B["KDS 24 14 51 3.2.3.2 (5)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarIn1[/입력변수: 편심량/];
		VarIn2[/입력변수: 기초의 크기 B/];
		VarIn3[/입력변수: 기초의 크기 L/];

		VarIn1
		VarIn2
		VarIn3

    end

    Python_Class ~~~ C(["KDS 24 14 51 3.2.3.2 (5)"])
		C --> Variable_def;

		F{기초크기 B or L 의 3/8 > 편심량}
		D{기초크기 B or L 의 4/10 > 편심량}

		Variable_def --하중에대한 편심량 ---> F
		Variable_def --지진하중을 고려하는 극단상황한계상태 ---> D

		E([Pass or Fail])

		F & D ---> E
    """

    @rule_method
    def load_eccentricity(fIeccenA,fIeccenB,fIB,fIL) -> RuleUnitResult:
        """하중편심량

        Args:
            fIeccenA (float): 편심량
            fIeccenB (float): 편심량 (지진하중을 고려하는 극단상황한계상태)
            fIB (float): 기초의 B 크기
            fIL (float): 기초의 L 크기

        Returns:
            pass_fail (bool): 교량 하부구조 설계기준 (한계상태설계법)  3.2.3.2 암반 지지력 (5)의 판단 결과
        """

        assert isinstance(fIeccenA, float)
        assert isinstance(fIeccenB, float)
        assert isinstance(fIB, float)
        assert isinstance(fIL, float)

        if fIeccenA != 0 and  fIeccenB == 0 :
          if fIeccenA <= min(3/8 * fIB, 3/8 * fIL) :
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

        elif fIeccenA == 0 and  fIeccenB != 0 :
          if fIeccenB <= min(4/10 * fIB, 4/10 * fIL) :
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

        else :
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )