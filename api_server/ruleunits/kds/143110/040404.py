import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040404(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '구멍이 있는 플랜지의 인장파단'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.4. 조합력과 비틀림부재
    4.4.4 구멍이 있는 플랜지의 인장파단
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 구멍이 있는 플랜지의 인장파단] ;
		B["KDS 14 31 10 4.4.4"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarIn1[/입력변수: 플랜지의 인장파단강도/] ;
      VarIn2[/입력변수: 하중조합으로 구해진 소요인장강도/] ;
      VarIn3[/입력변수: 인장파단의 한계상태에 대한 설계인장강도/] ;
      VarIn4[/입력변수: 하중조합으로 구한 소요휨강도/] ;
      VarIn5[/입력변수: 설계휨강도/] ;
      VarIn6[/입력변수: 인장파단에 대한 강도저항계수/] ;
      VarIn7[/입력변수: 휨에 대한 강도저항계수/] ;

			end
		VarIn1 & VarIn2 & VarIn3 ~~~ VarIn4 & VarIn5 & VarIn6 & VarIn7

		Python_Class ~~~ C1(["KDS 14 31 10 4.4.4"]) --> Variable_def

		E["<img src=https://latex.codecogs.com/svg.image?\frac{P_{u}}{P_{r}}&plus;\frac{M_{ux}}{M_{rx}}\leq&space;1.0>--------------------------------"]


		Variable_def --> E --> D(["PASS or Fail"])
    """

    @rule_method
    def Tensile_rupture_strength_of_hole_flange(fIPu,fIPt,fIMu,fIMrx,fIphit,fIphib) -> RuleUnitResult:
        """구멍이 있는 플랜지의 인장파단

        Args:
            fIPu (float): 하중조합으로 구해진 소요인장강도
            fIPt (float): 인장파단의 한계상태에 대한 설계인장강도
            fIMu (float): 하중조합으로 구한 소요휨강도
            fIMrx (float): 설계휨강도
            fIphit (float): 인장파단에 대한 강도저항계수
            fIphib (float): 휨에 대한 강도저항계수

        Returns:
            fOtebrsf (float): 강구조부재설계기준(하중저항계수설계법) 4.4.4 구멍이 있는 플랜지의 인장파단의 값
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법) 4.4.4 구멍이 있는 플랜지의 인장파단의 통과여부
        """

        assert isinstance(fIPu, float)
        assert isinstance(fIPt, float)
        assert fIPt !=0
        assert isinstance(fIMu, float)
        assert isinstance(fIMrx, float)
        assert fIMrx !=0
        assert isinstance(fIphit, float)
        assert isinstance(fIphib, float)

        if fIPu / fIPt + fIMu / fIMrx <= 1.0:
          fOtebrsf = fIPu / fIPt + fIMu / fIMrx
          return RuleUnitResult(
             result_variables = {
               "pass_fail": True,
               "fOtebrsf": fOtebrsf,
              }
            )

        else:
          fOtebrsf = fIPu / fIPt + fIMu / fIMrx
          return RuleUnitResult(
            result_variables = {
              "pass_fail": False,
              "fOtebrsf": fOtebrsf,
             }
           )