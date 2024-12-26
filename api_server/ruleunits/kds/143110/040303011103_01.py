import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040303011103_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 4.3.3.1.11.3 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '수평보강재의 휨응력'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.1 플레이트거더
    4.3.3.1.11 보강재
    4.3.3.1.11.3 수평보강재
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 수평보강재의 휨응력] ;
		B["KDS 14 31 10 4.3.3.1.11.3 (1)"] ;
		A ~~~ B
		end

    subgraph Variable_def
      VarIn1[/입력변수: 수평보강재의 휨응력/] ;
      VarIn2[/입력변수: 휨에 대한 강도저항계수/] ;
      VarIn3[/입력변수: 보강재의 최소항복강도/] ;
      VarIn4[/입력변수: 하이브리드 단면의 응력감소계수/] ;
    end
    VarIn1 & VarIn2 ~~~ VarIn3 & VarIn4

    Python_Class ~~~ C1(["KDS 14 31 10 4.3.3.1.11.3 (1)"]) -->Variable_def

    C["<img src=https://latex.codecogs.com/svg.image?f_{s}\leq\phi&space;_{f}R_{h}F_{ys}>------------------------"]
    Variable_def --> C --> D(["PASS or Fail"])
    """

    @rule_method
    def Bending_stress_of_horizontal_stiffeners(fIfs,fIphif,fIFys,fIRh) -> RuleUnitResult:
        """수평보강재의 휨응력

        Args:
            fIfs (float): 수평보강재의 휨응력
            fIphif (float): 휨에 대한 강도저항계수
            fIFys (float): 보강재의 최소항복강도
            fIRh (float): 하이브리드 단면의 응력감소계수

        Returns:
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법)  4.3.3.1.11.3 수평보강재 (1)의 통과여부
        """

        assert isinstance(fIfs, float)
        assert isinstance(fIphif, float)
        assert isinstance(fIFys, float)
        assert isinstance(fIRh, float)

        if fIfs <= fIphif * fIRh * fIFys:
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