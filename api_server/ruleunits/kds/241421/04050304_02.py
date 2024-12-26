import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04050304_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.5.3.4 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-21'
    title = '슬래브의 포스트텐션 긴장재 중심간의 간격'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.5 철근 상세
    4.5.3 철근의 간격
    4.5.3.4 슬래브에서의 프리스트레싱 강재와 덕트의 최대간격
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 슬래브의 포스트텐션 긴장재 중심간의 간격];
    B["KDS 24 14 21 4.5.3.4 (2)"];
    A ~~~ B
    end

	  subgraph Variable_def;

		VarIn1["슬래브의 포스트텐션 긴장재는 중심간의 간격"]
		VarIn2["합성슬래브 최소두께"]

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.5.3.4 (2)"])
		C --> Variable_def

		Variable_def--->D--->F
		D{"슬래브의 포스트텐션 긴장재는 중심간의 간격≤ 합성슬래브 최소두께 x4"}

		F(["Pass or fail"])
    """

    @rule_method
    def Spacing_between_centers_of_post_tensioned_tendons_of_slab(fIpotscs,fImincst) -> RuleUnitResult:
        """슬래브의 포스트텐션 긴장재 중심간의 간격

        Args:
            fIpotscs (float): 슬래브의 포스트텐션 긴장재 중심간의 간격
            fImincst (float): 합성슬래브 최소두께

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.5.3.4 슬래브에서의 프리스트레싱 강재와 덕트의 최대간격 (2)의 판단 결과
        """

        assert isinstance(fIpotscs, float)
        assert isinstance(fImincst, float)

        if fIpotscs <= fImincst * 4 :
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