import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403020203_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.2.2.3 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-25'
    title = '유효 폭'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.2 강관 간의 트러스접합
    4.3.2.2 각형강관
    4.3.2.2.3 간격 K형 접합에서 압축력을 받는 지강관
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 유효 폭]
	  B["KDS 14 31 25 4.3.2.2.3 (2)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
		VarIn1[/입력변수: 유효 폭/];
		end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.2.2.3 (2)"])
		C --> Variable_def

	  E{"<img src='https://latex.codecogs.com/svg.image?B_{eff}\geq&space;0.35'>---------------------"} ;

		Variable_def --> E --> D(["PASS or Fail"])
    """

    @rule_method
    def effective_width(fIBeff) -> RuleUnitResult:
        """유효 폭

        Args:
            fIBeff (float): 유효 폭

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.2.3 간격 K형 접합에서 압축력을 받는 지강관 (2)의 판단 결과
        """

        assert isinstance(fIBeff, float)

        if fIBeff >= 0.35 :
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