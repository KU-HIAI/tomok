import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040303020201_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.3.3.2.2.1 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '수평보강재가 없는 웨브의 단면비'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.2 박스거더
    4.3.3.2.2 단면비 요구조건
    4.3.3.2.2.1 웨브 단면비
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 수평보강재가 없는 웨브의 단면비] ;
		B["KDS 14 31 10 4.3.3.2.2.1 (2)"] ;
		A ~~~ B
		end

    subgraph Variable_def
    VarIn1[/입력변수: 수평보강재 안의 최대 웨브 높이/] ;
    VarIn2[/입력변수: 웨브 두께/] ;
		end

		Python_Class ~~~ C(["KDS 14 31 10 4.3.3.2.2.1 (2)"])
		C --> Variable_def

		D{"<img src=https://latex.codecogs.com/svg.image?\frac{D}{t_{w}}\leq&space;150>------------------------"}
		Variable_def --> D --> E(["PASS or Fail"])
    """

    @rule_method
    def Section_ratio_of_web_without_horizontal_stiffener(fID,fItw) -> RuleUnitResult:
        """수평보강재가 없는 웨브의 단면비

        Args:
            fID (float): 수평보강재 안의 최대 웨브 높이
            fItw (float): 웨브두께

        Returns:
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법)  4.3.3.2.2.1 웨브 단면비 (2)의 판단 결과
        """

        assert isinstance(fID, float)
        assert isinstance(fItw, float)
        assert fItw > 0

        if fID / fItw <= 150:
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