import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403020201_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.2.2.1 (4)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-25'
    title = '인장 지강관벽의 세장비'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.2 강관 간의 트러스접합
    4.3.2.2 각형강관
    4.3.2.2.1 적용한계
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 인장 지강관벽의 세장비]
	  B["KDS 14 31 25 4.3.2.2.1 (4)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut1[/입력변수: 인장 지강관벽 세장비/]
    VarIn1[/입력변수: 벽의 폭두께비/]
		end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.2.2.1 (4)"])
		C --> Variable_def

	  E{"인장 지강관벽 세장비 = 벽의 폭두께비 ≤ 35"} ;
		Variable_def --> E --> D(["Pass or Fail"])
    """

    @rule_method
    def Slenderness_ratio_of_tension_branch_member_wall(fIsrtbmw) -> RuleUnitResult:
        """인장 지강관벽의 세장비

        Args:
            fIsrtbmw (float): 인장 지강관벽 세장비

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.2.1 적용한계 (4)의 판단 결과
        """

        assert isinstance(fIsrtbmw, float)

        if fIsrtbmw <= 35:
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