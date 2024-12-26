import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241211_040102_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 11 4.1.2 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-22'
    title = '구조물과 부속물의 중량에 대한 하중계수'

    description = """
    교량 설계하중조합(한계상태설계법)
    4. 설계
    4.1 하중의 종류와 하중조합
    4.1.2 가설 시 하중에 대한 하중계수
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 구조물과 부속물의 중량에 대한 하중계수];
    B["KDS 24 12 11 4.1.2 (1)"];
    A ~~~ B
    end

	  subgraph Variable_def
    Varin[/입력변수 : 구조물과 부속물의 중량에 대한 하중계수/];
    end

	  Python_Class ~~~ C(["KDS 24 12 11 4.1.2 (1)"])
		C --> Variable_def

		D{"구조물과 부속물의 중량에 대한 하중계수 ≥ 1.25"};
    Variable_def --> D--->E(["Pass or Fail"])
    """

    @rule_method
    def Load_factor_for_the_weight_of_structure(fIweifac) -> RuleUnitResult:
        """구조물과 부속물의 중량에 대한 하중계수
        Args:
            fIweifac (float): 구조물과 부속물의 중량에 대한 하중계수

        Returns:
            pass_fail (bool): 교량 설계하중조합(한계상태설계법)  4.1.2 가설 시 하중에 대한 하중계수 (1)의 판단 결과
        """

        assert isinstance(fIweifac, float)

        if fIweifac>=1.25:
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