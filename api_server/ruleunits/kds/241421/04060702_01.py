import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04060702_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.6.7.2 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-22'
    title = '철근 간격'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.7 속빈 사각형 단면 압축부재의 보강철근
    4.6.7.1 일반사항
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 철근 간격];
    B["KDS 24 14 21 4.6.7.2 (1)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수:종방향 철근의 중심간격/];
		VarIn2[/입력변수:벽체두께/];
		VarIn3[/입력변수:횡방향 철근의 수직방향으로의 중심간격/];

		VarIn1 & VarIn2 & VarIn3
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.6.7.2 (1)"])
		C --> Variable_def

		Variable_def--->E & D--->H
		E{"종방향 철근의 중심간격≤ min(벽체두께 X1.5 or 450mm)"}
		D{"횡방향철근의 수직방향으로의 중심간격≤min(벽체두께X1.25 or 300mm)"}
    H(["Pass or Fail"])
    """

    @rule_method
    def reinforcement_distance(fIcenslb, fIwalthi, fIcspvdl) -> RuleUnitResult:
        """철근 간격

        Args:
            fIcenslb (float): 종방향 철근의 중심간격
            fIwalthi (float): 벽체두께
            fIcspvdl (float): 횡방향 철근의 수직방향으로의 중심간격

        Returns:
            pass_fail (bool):  콘크리트교 설계기준 (한계상태설계법)  4.6.7.1 철근 간격 (1)의 판단 결과
        """

        assert isinstance(fIcenslb, float)
        assert isinstance(fIwalthi, float)
        assert isinstance(fIcspvdl, float)

        if fIcenslb <= min(1.5*fIwalthi, 450) and fIcspvdl <= min(1.25*fIwalthi, 300):
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