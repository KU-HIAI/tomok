import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241211_040102_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 11 4.1.2 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-22'
    title = '하중계수'

    description = """
    교량 설계하중조합(한계상태설계법)
    4. 설계
    4.1 하중의 종류와 하중조합
    4.1.2 가설 시 하중에 대한 하중계수
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 하중계수];
    B["KDS 24 12 11 4.1.2 (2)"];
    A ~~~ B
    end

	  subgraph Variable_def
	  VarIn1[/입력변수 : 하중계수: 다른 모든 하중계수/];
	  VarIn2[/입력변수 : 하중계수: 시공하중, 설비하중, 동적효과/];
	  VarIn3[/입력변수 : 하중계수: 풍하중/];
	  end

	  Python_Class ~~~ C(["KDS 24 12 11 4.1.2 (2)"])
		C --> Variable_def

		D{"시공하중, 설비하중, 동적효과에 대한 하중계수 ≥ 1.5"};
	  E{"풍하중에 대한 하중계수 ≥ 1.25"};
	  Variable_def --> D & E --->F(["Pass or Fail"])
    """

    @rule_method
    def Load_factor(fIloafaA,fIloafaB,fIloafaC) -> RuleUnitResult:
        """하중계수
        Args:
            fIloafaA (float): 하중계수(다른 모든 하중계수)
            fIloafaB (float): 하중계수(시공하중, 설비하중, 동적효과)
            fIloafaC (float): 하중계수(풍하중)

        Returns:
            pass_fail (bool): 교량 설계하중조합(한계상태설계법)  4.1.2 가설 시 하중에 대한 하중계수 (2)의 판단 결과
        """

        assert isinstance(fIloafaA, float)
        assert isinstance(fIloafaB, float)
        assert isinstance(fIloafaC, float)

        if fIloafaA != 0 and fIloafaB == 0 and fIloafaC == 0 :
          if fIloafaA == 1.0 :
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

        elif fIloafaA == 0 and fIloafaB != 0 and fIloafaC == 0 :
          if fIloafaB >= 1.5 :
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

        elif fIloafaA == 0 and fIloafaB == 0 and fIloafaC != 0 :
          if fIloafaC >= 1.25 :
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