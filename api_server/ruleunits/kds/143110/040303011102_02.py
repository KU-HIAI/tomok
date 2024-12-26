import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040303011102_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.3.3.1.11.2 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '지압보강재의 돌출폭'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.1 플레이트거더
    4.3.3.1.11 보강재
    4.3.3.1.11.2 하중집중점 지압보강재
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 지압보강재의 돌출폭] ;
		B["KDS 14 31 10 4.3.3.1.11.2 (2)"] ;
		A ~~~ B
		end

    subgraph Variable_def
		VarIn1[/입력변수: 지압보강재의 돌출폭/] ;
    VarIn2[/입력변수: 지압보강재의 두께/] ;
    VarIn3[/입력변수: 강재의 탄성계수/] ;
    VarIn4[/입력변수: 지압보강재의 최소항복강도/] ;
    end

    Python_Class ~~~ C(["KDS 14 31 10 4.3.3.1.11.2 (2)"])
		C --> Variable_def

    D{"<img src=https://latex.codecogs.com/svg.image?b_{t}\leq&space;0.48t_{p}\sqrt{\frac{E}{F_{ys}}}>------------------------"}
    Variable_def --> D --> E(["PASS or Fail"])
    """

    @rule_method
    def entrapment_width_of_bearing_stiffener(fIbt,fItp,fIE,fIFys) -> RuleUnitResult:
        """지압보강재의 돌출폭

        Args:
            fIbt (float): 지압보강재의 돌출폭
            fItp (float): 지압보강재의 두께
            fIE (float): 강재의 탄성계수
            fIFys (float): 지압보강재의 최소항복강도

        Returns:
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법)  4.3.3.1.11.2 중간수직보강재 (2)의 판단 결과
        """

        assert isinstance(fIbt, float)
        assert isinstance(fItp, float)
        assert isinstance(fIE, float)
        assert fIE > 0
        assert isinstance(fIFys, float)
        assert fIFys > 0

        if fIbt <= 0.48 * fItp * (fIE / fIFys) ** 0.5 :
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