import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010302_05(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.3.2 (5)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-21'
    title = '최소철근량 조건'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.3 비틀림
    4.1.3.2 설계
    (5)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 최소철근량 조건];
    B["KDS 24 14 21 4.1.3.2 (5)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 비틀림모멘트/];
		VarIn2[/입력변수: 전단력/];
		VarIn3[/입력변수: 단면의 복부폭/];
		VarIn4[/입력변수: 콘크리트가 기여하는 설계전단강도/];
		VarIn1 & VarIn2 & VarIn3 & VarIn4
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.3.2 (5)"])
		C --> Variable_def

		Variable_def--->F & D--->E
		F{"<img src='https://latex.codecogs.com/svg.image?T_u\leq\frac{V_ub_w}{4.5}'>---------------------------------"}
		D{"<img src='https://latex.codecogs.com/svg.image?V_u[1&plus;\frac{4.5T_u}{V_ub_w}]\leq&space;V_{cd}'>---------------------------------"}
		E(["Pass or Fail"])
    """

    @rule_method
    def minimum_reinforcement_condition(fITu,fIVu,fIbw,fIVcd) -> RuleUnitResult:
        """최소철근량 조건

        Args:
            fITu (float): 비틀림모멘트
            fIVu (float): 전단력
            fIbw (float): 단면의 복부폭
            fIVcd (float): 콘크리트가 기여하는 설계전단강도

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.1.3.2 설계 (5)의 판단 결과 1
            sOminrei (string): 콘크리트교 설계기준 (한계상태설계법)  4.1.3.2 설계 (5)의 판단 결과 2
        """

        assert isinstance(fITu, float)
        assert isinstance(fIVu, float)
        assert fIVu != 0
        assert isinstance(fIbw, float)
        assert fIbw != 0

        if fITu <= fIVu * fIbw / 4.5 and fIVu * (1 + 4.5 * fITu / (fIVu * fIbw)) <= fIVcd:
          return RuleUnitResult(
              result_variables = {
                  "sOminrei": "4.6.2.7에서 규정한 최소철근량 필요",
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "sOminrei": "4.6.2.7에서 규정한 최소철근량 필요하지 않음",
                  "pass_fail": False,
              }
          )