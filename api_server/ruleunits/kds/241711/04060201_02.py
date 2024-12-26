import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_04060201_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.6.2.1 (2)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-19'
    title = '설계기준항복강도'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.2 교각의 해석 및 설계 강도
    4.6.2.1 일반사항
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 설계기준항복강도]
	  B["KDS 24 17 11 4.6.2.1(2)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn1[/입력변수: 설계기준항복강도/]
	  VarIn2[/입력변수: 인장강도/]
	  VarIn3[/입력변수: 항복강도/]
	  VarIn1 & VarIn2 & VarIn3
	  end

	  Python_Class ~~~ C(["KDS 24 17 11 4.6.2.1(2)"])
		C --> Variable_def --> D & E

	  D --> G --> H --> I
	  E --> F --> I
	  D{"축방향 철근"}
	  E{"횡방향 철근"}
	  F{"설계기준항복강도 ≤ 500Mpa"}
	  G{"설계기준항복강도 ≤ 500Mpa"}
  	H{"인장강도 ≥ 항복강도 x 1.25"}
	  I([Pass or Fail])
    """

    @rule_method
    def pier_rebar_strengh_consideration(fIspyist,fItenstr,fIyiestr,) -> RuleUnitResult:
        """설계기준항복강도

        Args:
            fIspyist (float): 설계기준항복강도
            fItenstr (float): 인장강도
            fIyiestr (float): 항복강도


        Returns:
            pass_fail (bool): 교량내진설계기준(한계상태설계법) 4.4.2.1 일반사항 (2)의 판단 결과
        """

        assert isinstance(fIspyist, float)
        assert isinstance(fItenstr, float)
        assert isinstance(fIyiestr, float)


        if fIspyist <= 500  and fItenstr >= fIyiestr * 1.25 :
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