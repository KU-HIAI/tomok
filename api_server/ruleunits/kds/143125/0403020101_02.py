import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403020101_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.2.1.1 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-25'
    title = '지강관 각도'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.2 강관 간의 트러스접합
    4.3.2.1 원형강관
    4.3.2.1.1 적용한계
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 지강관 각도]
	  B["KDS 14 31 25 4.3.2.1.1 (2)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn1[/입력변수: 지강관 각도/]
		VarIn1
		end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.2.1.1 (2)"])
		C --> Variable_def

	  E{"<img src='https://latex.codecogs.com/svg.image?\Theta\geq&space;30^{\circ}'>-------------------"} ;
    D([접합부 편심])

		Variable_def --> E --> D
    """

    @rule_method
    def branch_member_degree(fIhrmede) -> RuleUnitResult:
        """지강관 각도

        Args:
            fIhrmede (float): 지강관 각도

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.1.1 적용한계 (2)의 판단 결과
        """

        assert isinstance(fIhrmede, float)

        if fIhrmede >= 30:
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