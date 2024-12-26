import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241451_03050304_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 51 3.5.3.4 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '동수경사'

    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.5 교대와 중력식 및 반중력식 옹벽
    3.5.3 극한한계상태의 지지력과 안정성
    3.5.3.4 지중 침식
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 동수경사];
    B["KDS 24 14 51 3.5.3.4 (2)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarIn1[/입력변수:동수경사/]
    end

		Python_Class ~~~ C(["KDS 24 14 51 3.5.3.4 (2)"])
		C --> Variable_def

		H[실트나 점성토]
		D[사질토]
		E([동수경사])
		F[0.2]
		G[0.3]

		Variable_def ---> H & D
		H ---> F ---> E
		D ---> G---> E
    """

    @rule_method
    def hydraulic_gradient(fIhydgrA,fIhydgrB) -> RuleUnitResult:
        """동수경사

        Args:
            fIhydgrA (float): 동수경사(실트나 점성토)
            fIhydgrB (float): 동수경사(사질토)

        Returns:
            pass_fail (bool): 교량 하부구조 설계기준 (한계상태설계법) 3.4.5.6 확대선단부의 판단 결과
        """

        assert isinstance(fIhydgrA, float)
        assert isinstance(fIhydgrB, float)

        if fIhydgrA != 0 and fIhydgrB == 0 :
          if fIhydgrA <= 0.2:
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

        elif fIhydgrA == 0 and fIhydgrB != 0 :
          if fIhydgrA <= 0.2:
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

        else:
          return RuleUnitResult(
                result_variables = {
                    "pass_fail": False,
              }
          )