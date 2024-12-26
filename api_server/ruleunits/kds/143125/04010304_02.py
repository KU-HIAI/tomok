import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_04010304_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.3.4 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '볼트의 설계전단응력'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.3 볼트
    4.1.3.4 지압접합에서 인장과 전단의 조합
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
    A[Title: 볼트의 설계전단응력]
    B["KDS 14 31 25 4.1.3.4 (2)"]
  	A ~~~ B
  	end

	  subgraph Variable_def
  	VarIn1[/입력변수: 설계전단응력/]
    VarIn2[/입력변수: 전단소요응력/]
  	end

		Python_Class ~~~ C(["KDS 14 31 25 4.1.3.4 (2)"])
		C --> Variable_def

	  Variable_def --> D --> E

	  D{"볼트의 설계전단응력 ≥ fv"}
	  E(["Pass or Fail"])
    """

    @rule_method
    def design_shear_stress_of_bolt(fIdeshst,fIfv) -> RuleUnitResult:
        """볼트의 설계전단응력

        Args:
            fIdeshst (float): 설계전단응력
            fIfv (float): 전단소요응력

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.1.3.4 지압접합에서 인장과 전단의 조합 (2)의 판단 결과
        """

        assert isinstance(fIdeshst, float)
        assert isinstance(fIfv, float)

        if fIdeshst >= fIfv :
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