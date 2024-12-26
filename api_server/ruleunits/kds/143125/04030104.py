import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_04030104(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.1.4'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '판재의 항복강도'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.1 강관구조의 집중하중
    4.3.1.4 강관폭의 중심에 종방향으로 분포된 종방향 집중하중
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 판재의 항복강도]
	  B["KDS 14 31 25 4.3.1.4"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn1[/입력변수: 판재의 항복강도/]
	  VarIn2[/입력변수: 판재의 두께/]
	  VarIn3[/입력변수: 강재의 최소인장강도/]
	  VarIn4[/입력변수: 주강관의 두께/]
	  VarIn1 ~~~ VarIn2 & VarIn3 & VarIn4
	  end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.1.4"])
		C --> Variable_def

	  Variable_def --> E --> D(["PASS or Fail"])
	  E{"<img src='https://latex.codecogs.com/svg.image?F_{yp}t_p\leq&space;F_yt'>--------------------"}
    """

    @rule_method
    def yield_strength_of_plate(fIFyp,fItp,fIFu,fIt) -> RuleUnitResult:
        """판재의 항복강도

        Args:
            fIFyp (float): 판재의 항복강도
            fItp (float): 판재의 두께
            fIFu (float): 강재의 최소인장강도
            fIt (float): 주강관의 두께

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.1.4 강관폭의 중심에 종방향으로 분포된 종방향 집중하중의 판단 결과
        """

        assert isinstance(fIFyp, float)
        assert isinstance(fItp, float)
        assert isinstance(fIFu, float)
        assert isinstance(fIt, float)

        if fIFyp * fItp <= fIFu * fIt:
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