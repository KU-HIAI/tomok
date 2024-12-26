import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241712_04050201_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 12 4.5.2.1 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-15'
    title = '철근콘크리트 주탑 및 교각의 축방향철근'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.5 콘크리트교의 설계
    4.5.2 주탑 및 교각의 해석 및 설계강도
    4.5.2.1 일반사항
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 철근콘크리트 주탑 및 교각의 축방향철근];
    B["KDS 24 17 12 4.5.2.1 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 축방향철근의 설계기준항복강도/];
    VarIn2[/입력변수: 축방향철근의 인장강도/];
		VarIn3[/입력변수: 횡방향철근의 설계기준항복강도/];

		VarIn1 & VarIn2 & VarIn3

		end
		Python_Class ~~~ C(["KDS 24 17 12 4.5.2.1 (2)"])
		C --> Variable_def;

	  Variable_def--->D---> E & F
		D["철근콘크리트 주탑 및 교각의 축방향 철근"];
		E["설계기준항복 강도≤500MPa"];
		F["인장강도≥항복강도 X 1.25"]
		G["철근콘크리트 교각의 횡방향철근"];
		H["설계기준항복 강도≤500MPa"];
		Variable_def--->G--->H
    """

    @rule_method
    def steel_for_reinforced_concrete_pylons_and_piers(fItstaxrb,fIystaxrb,fIfyh) -> RuleUnitResult:
        """철근콘크리트 주탑 및 교각의 축방향철근

        Args:
            fItstaxrb (float): 축방향철근의 설계기준항복강도
            fIystaxrb (float): 축방향철근의 인장강도
            fIfyh (float): 횡방향철근의 설계기준항복강도

        Returns:
            pass_fail (bool): 교량내진 설계기준(케이블교량) 4.5.2.1 일반사항 (2)의 판단 결과
        """

        assert isinstance(fItstaxrb, float)
        assert isinstance(fIystaxrb, float)
        assert isinstance(fIfyh, float)

        if fItstaxrb <= 500 and fIystaxrb >= 1.25 * fItstaxrb and fIfyh <= 500 :
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