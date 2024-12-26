import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04060208_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.6.2.8 (4)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-21'
    title = '표피철근량'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.2 보
    4.6.2.8 표피철근
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 표피철근량];
    B["KDS 24 14 21 4.6.2.8 (4)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수:피복두께/];
		VarIn2[/입력변수: 표피철근량/];
		VarIn3[/입력변수:횡방향철근 외측의 인장콘크리트 면적/];
		VarIn1 & VarIn2 &  VarIn3
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.6.2.8 (4)"])
		C --> Variable_def

		Variable_def--->F--->G--->H

		F{"피복두께 70mm 초과하는 경우"}

		G{"표피철근량 <img src='https://latex.codecogs.com/svg.image?\geq&space;0.005A_{ct,ext}'>---------------------------------"}

		H(["Pass or fail"])
    """

    @rule_method
    def amount_of_skin_reinforcement(fIcovthi,fIamoski,fIActext) -> RuleUnitResult:
        """표피철근량

        Args:
            fIcovthi (float): 피복두께
            fIamoski (float): 표피철근량
            fIActext (float): 횡방향철근 외측의 인장콘크리트 면적

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.6.2.8 표피철근 (4)의 판단 결과
        """

        assert isinstance(fIcovthi, float)
        assert isinstance(fIamoski, float)
        assert isinstance(fIActext, float)

        if fIcovthi > 70:
          if fIamoski >= 0.005*fIActext:
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