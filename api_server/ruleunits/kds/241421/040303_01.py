import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_040303_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.3.3 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '프리스트레싱 긴장재의 피로영역범위'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.3 피로한계상태
    4.3.3 프리스트레싱 긴장재
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 프리스트레싱 긴장재의 피로영역범위];
    B["KDS 24 14 21 4.3.3 (1)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수: 피로응력/];
		VarIn2[/입력변수: 곡률 반경/];
		VarIn1 & VarIn2
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.3.3 (1)"])
		C --> Variable_def

		Variable_def--->F
		F{"곡률반경"}
		F-->G{곡률 반경≥9000mm}--->D
		D["피로응력=125MPa"]
		F-->H{곡률 반경<3600mm}--->E
		E["피로응력=70MPa"]
    """

    @rule_method
    def Fatigue_area_range_of_prestressing_tendon(fIfatstr,fIradcuv) -> RuleUnitResult:
        """프리스트레싱 긴장재의 피로영역범위

        Args:
            fIfatstr (float): 피로응력
            fIradcuv (float): 곡률 반경

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법) 4.3.3 프리스트레싱 긴장재 (1)의 판단 결과
        """

        assert isinstance(fIradcuv, float)

        if fIradcuv >= 9000:
          if fIfatstr <= 125:
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
        elif fIradcuv <= 3600:
          if fIfatstr <= 70:
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