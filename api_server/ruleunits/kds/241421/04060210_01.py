import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04060210_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.6.2.10 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-21'
    title = '곡선 긴장재의 영향을 고려한 부재 상세'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.2 보
    4.6.2.10 곡선 긴장재의 영향을 고려한 부재 상세
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 곡선 긴장재의 영향을 고려한 부재 상세];
    B["KDS 24 14 21 4.6.2.10 (1)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수:철근응력/];
		VarIn2[/입력변수:철근의 기준항복강도/];
		VarIn3[/입력변수:횡구속철근의 간격/];
		VarIn4[/입력변수: 덕트 외측지름/];

		VarIn1 & VarIn2 & VarIn3 & VarIn4

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.6.2.10 (1)"])
		C --> Variable_def

		Variable_def---> G & H ---> I

		G{"철근응력 <img src='https://latex.codecogs.com/svg.image?\leq&space;0.6f_y'>---------------------------------"}

		H{"횡구속철근간격≤덕트 외측지름X3 or 600mm"}

		I(["Pass or fail"])
    """

    @rule_method
    def Details_of_member_considering_the_effects_of_curved_tension(fIrebstr,fIfy,fIspatcb,fIduoudi) -> RuleUnitResult:
        """곡선 긴장재의 영향을 고려한 부재 상세

        Args:
            fIrebstr (float): 철근응력
            fIfy (float): 철근의 기준항복강도
            fIspatcb (float): 횡구속철근의 간격
            fIduoudi (float): 덕트 외측지름

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.6.2.10 곡선 긴장재의 영향을 고려한 부재 상세 (1)의 판단 결과
        """

        assert isinstance(fIrebstr, float)
        assert isinstance(fIfy, float)
        assert isinstance(fIspatcb, float)
        assert isinstance(fIduoudi, float)

        if fIrebstr <= 0.6 * fIfy and fIfy <= 420 and fIspatcb <= min(3 * fIduoudi, 600):
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