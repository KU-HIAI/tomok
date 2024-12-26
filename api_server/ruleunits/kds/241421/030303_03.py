import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_030303_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 3.3.3 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '스트랜드에 대한 탄성계수의 설계값'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.3 프리스트레싱 강재
    3.3.3 설계 가정
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 스트랜드에 대한 탄성계수의 설계값];
    B["KDS 24 14 21 3.3.3 (3)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarOut1[/출력변수: 탄성계수의 설계값/];
		VarOut1

		end

	  Python_Class ~~~ C(["KDS 24 14 21 3.3.3 (3)"])
		C --> Variable_def

		Variable_def--->C--->G

		C["탄성계수의 설계값=200GPa"]

		G(["탄성계수의 설계값"])
    """

    @rule_method
    def Design_value_of_elastic_modulus_of_strand(fOEp) -> RuleUnitResult:
        """스트랜드에 대한 탄성계수의 설계값

        Args:
            fOEp (float): 탄성계수의 설계값

        Returns:
            fOEp (float): 콘크리트교 설계기준(한계상태설계법)  3.3.3 설계 가정 (3)의 값
            pass_fail (bool): 콘크리트교 설계기준(한계상태설계법)  3.3.3 설계 가정 (3)의 판단 결과
        """

        if fOEp == 0 :
          fOEp = 200
          return RuleUnitResult(
              result_variables = {
                  "fOEp": fOEp,
              }
          )
        else:
          if 185 <= fOEp <= 205 :
            return RuleUnitResult(
                result_variables = {
                    "fOEp": fOEp,
                    "pass_fail": True,
                }
            )
          else:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": False,
                }
            )