import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040303020202(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.3.3.2.2.2'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '압축 또는 인장을 받는 U형 단면의 상부플랜지 단면비'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.2 박스거더
    4.3.3.2.2 단면비 요구조건
    4.3.3.2.2.2 플랜지 단면비
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 압축 또는 인장을 받는 U형 단면의 상부플랜지 단면비] ;
		B["KDS 14 31 10 4.3.3.2.2.2"] ;
		A ~~~ B
		end

    subgraph Variable_def
    VarIn1[/입력변수: 압축 또는 인장을 받는 U형 단면의 상부플랜지 단면비/] ;
    VarIn2[/입력변수: 플랜지의 폭/] ;
    VarIn3[/입력변수: 플랜지의 두께/] ;
		VarIn4[/입력변수: 웨브 두께/] ;
    VarIn5[/입력변수: 웨브 높이/] ;
		end

		Python_Class ~~~ C(["KDS 14 31 10 4.3.3.2.2.2"])
		C --> Variable_def

		D{"<img src=https://latex.codecogs.com/svg.image?\frac{b_{f}}{2t_{f}}\leq&space;12.0>------------------------"}
		E{"<img src=https://latex.codecogs.com/svg.image?b_{f}\geq&space;D/6>------------------------"}
		F{"<img src=https://latex.codecogs.com/svg.image?t_{f}\geq&space;1.1t_{w}>------------------------"}

		Variable_def --> D --> E --> F --> G(["PASS or Fail"])
    """

    @rule_method
    def Upper_flange_section_ratio_of_U_shaped_section_under_compression_or_tension(fIbf,fItf,fItw,fId) -> RuleUnitResult:
        """압축 또는 인장을 받는 U형 단면의 상부플랜지 단면비

        Args:
            fIbf (float): 플랜지의 폭
            fItf (float): 플랜지의 두께
            fItw (float): 웨브 두께
            fId (float): 웨브 높이

        Returns:
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법)  4.3.3.2.2.2의 판단 결과
        """

        assert isinstance(fIbf, float)
        assert isinstance(fItf, float)
        assert fItf > 0
        assert isinstance(fItw, float)
        assert isinstance(fId, float)

        if fIbf / (2 * fItf) <= 12.0 and fIbf >= fId / 6 and fItf >= 1.1 * fItw:
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