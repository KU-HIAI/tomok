import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403020201_06(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.2.2.1 (6)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-25'
    title = '폭 비'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.2 강관 간의 트러스접합
    4.3.2.2 각형강관
    4.3.2.2.1 적용한계
    (6)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 폭 비]
	  B["KDS 14 31 25 4.3.2.2.1 (6)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn1[/입력변수: 폭비/]
		end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.2.2.1 (6)"])
		C --> Variable_def

	  C{"폭비 &ge; 0.25"} ;
   	D{"폭비 &ge; 0.35"} ;

    Variable_def --T,Y,X와 겹침K형 접합-->C
    Variable_def --간격 K형 접합-->D
		C & D --> Q(["Pass or Fail"])
    """

    @rule_method
    def width(fIbetaA,fIbetaB) -> RuleUnitResult:
        """폭 비

        Args:
            fIbetaA (float): 폭 비 (K, T, Y, X형 접합)
            fIbetaB (float): 폭 비 (겹침 K형 접합)

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.2.1 적용한계 (6)의 판단 결과
        """

        assert isinstance(fIbetaA, float)
        assert isinstance(fIbetaB, float)

        if fIbetaA != 0 and fIbetaB == 0 :
          if fIbetaA >= 0.25:
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

        elif fIbetaA == 0 and fIbetaB != 0 :
          if fIbetaB >= 0.35:
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