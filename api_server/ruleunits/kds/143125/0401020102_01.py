import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0401020102_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.2.1.2 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '부분용입 그루브용접의 유효목두께'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.2 용접
    4.1.2.1 그루브용접
    4.1.2.1.2 부분용입 그루브용접
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
    A[Title: 부분용입 그루브용접의 유효목두께]
    B["KDS 14 31 25 4.1.2.1.2 (1)"]
  	A ~~~ B
  	end

	  subgraph Variable_def
	  VarIn1[/입력변수: 부분용입 그루브용접의 유효목두께/]
	  VarIn2[/입력변수: 접합부의 두꺼운 쪽 판의 두께/]
  	VarIn3[/입력변수: 얇은 쪽 판의 두께/]
	  end

		Python_Class ~~~ C(["KDS 14 31 25 4.1.2.1.2 (1)"])
		C --> Variable_def

	  Variable_def --> D --> E

	  D{"얇은 쪽 판의두께≥부분용입 그루브용접의 유효목두께 ≥ <img src='https://latex.codecogs.com/svg.image?\sqrt{2t}(mm)'>"}
	  E([Pass or Fail])
    """

    @rule_method
    def Effective_throat_thickness_of_partial_joint_penetration_groove_weld(fIettPJP,fIt,fItsplth) -> RuleUnitResult:
        """부분용입 그루브용접의 유효목두께

        Args:
            fIettPJP (float): 부분용입 그루브용접의 유효목두께
            fIt (float): 접합부의 두꺼운 쪽 판의 두께
            fItsplth (float): 얇은 쪽 판의 두께

        Returns:
            pass_fail (bool):  강구조 연결 설계기준(하중저항계수설계법)   4.1.2.1.2 부분용입 그루브용접 (1)의 판단 결과 1
        """

        assert isinstance(fIettPJP, float)
        assert isinstance(fIt, float)
        assert fIt > 0
        assert isinstance(fItsplth, float)

        if (fIt*2)**0.5 <= fIettPJP <= fItsplth :
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