import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403010201_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.1.2.1 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '국부항복 한계상태에 관한 설계강도'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.1 강관구조의 집중하중
    4.3.1.2 축직각방향 집중하중
    4.3.1.2.1 원형강관
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 국부항복 한계상태에 관한 설계강도]
	  B["KDS 14 31 25 4.3.1.2.1 (2)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn1[/입력변수: 국부항복한계상태에 관한 설계강도/]
	  VarIn2[/입력변수: 강재의 항복강도/]
	  VarIn3[/입력변수: 주강관의 두께/]
	  VarIn4[/입력변수: 접합평면과 90도를 이루는 판폭/]
	  VarIn5[/입력변수: 원형 강관의 외경/]
	  VarIn6[/입력변수: 주관-응력상관변수/]
	  VarIn7[/입력변수: 원형 강관의 외경/]
	  VarIn1 ~~~ VarIn2 & VarIn3 & VarIn4
	  VarIn3 ~~~ VarIn5 & VarIn6 & VarIn7
	  end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.1.2.1 (2)"])
		C --> Variable_def

	  Variable_def --> E --> F & G--> K
	  E{"<img src='https://latex.codecogs.com/svg.image?0.2<B_p/D\leq&space;1.0'>--------------------------------------------"}
		F{"T형 접합에 대하여 <img src='https://latex.codecogs.com/svg.image?D/t\leq&space;50'>--------------"}
	  G{"X형 접합에 대하여 <img src='https://latex.codecogs.com/svg.image?D/t\leq&space;40'>--------------"}
		K(["Pass or Fail"])
    """

    @rule_method
    def Design_strength_for_local_yield_limit_state(fID,fIt,fITcon,fIXcon) -> RuleUnitResult:
        """국부항복 한계상태에 관한 설계강도

        Args:
            fID (float): 원형 강관의 외경
            fIt (float): 주강관의 두께
            fITcon (float): T형 접합
            fIXcon (float): X형 접합

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.1.2.1 원형강관 (2)의 판단 결과
        """

        assert isinstance(fID, float)
        assert isinstance(fIt, float)
        assert fIt != 0
        assert isinstance(fITcon, float)
        assert isinstance(fIXcon, float)

        if fITcon != 0 and fIXcon == 0 :
          if fID / fIt <= 50:
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

        elif fITcon == 0 and fIXcon != 0 :
          if fID / fIt <= 40:
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