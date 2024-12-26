import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040303011103_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.3.3.1.11.3 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '수평보강재의 돌출폭'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.1 플레이트거더
    4.3.3.1.11 보강재
    4.3.3.1.11.3 수평보강재
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 수평보강재의 돌출폭] ;
		B["KDS 14 31 10 4.3.3.1.11.3 (2)"] ;
		A ~~~ B
		end

    subgraph Variable_def
    VarIn1[/입력변수: 수평보강재의 돌출폭/] ;
    VarIn2[/입력변수: 보강재의 두께/] ;
    VarIn3[/입력변수: 강재의 탄성계수/] ;
    VarIn4[/입력변수: 보강재의 최소항복강도/] ;
    end
    VarIn1 & VarIn2 ~~~ VarIn3 & VarIn4

		Python_Class ~~~ C(["KDS 14 31 10 4.3.3.1.11.3 (2)"])
		C --> Variable_def

    D{"<img src=https://latex.codecogs.com/svg.image?b_{l}\leq&space;0.48t_{s}\sqrt{\frac{E}{F_{ys}}}>-----------------------------"}
    Variable_def --> D --> E(["PASS or Fail"])
    """

    @rule_method
    def Projection_width_of_horizontal_stiffener(fIbl,fIts,fIE,fIFys) -> RuleUnitResult:
        """수평보강재의 돌출폭

        Args:
            fIbl (float): 수평보강재의 돌출폭
            fIts (float): 보강재의 두께
            fIE (float): 강재의 탄성계수
            fIFys (float): 보강재의 최소항복강도

        Returns:
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법)  4.3.3.1.11.3 수평보강재 (2)의 판단 결과
        """

        assert isinstance(fIbl, float)
        assert isinstance(fIts, float)
        assert isinstance(fIE, float)
        assert fIE > 0
        assert isinstance(fIFys, float)
        assert fIFys > 0

        if fIbl <= 0.48 * fIts * (fIE / fIFys) ** 0.5:
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