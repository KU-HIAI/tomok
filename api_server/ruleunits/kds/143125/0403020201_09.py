import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403020201_09(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.2.2.1 (9)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-25'
    title = '지강관의 폭비'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.2 강관 간의 트러스접합
    4.3.2.2 각형강관
    4.3.2.2.1 적용한계
    (9)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 지강관의 폭비]
	  B["KDS 14 31 25 4.3.2.2.1 (9)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
    VarOut1[/출력변수: 지강관의 폭비/] ;
	  VarIn1[/입력변수: 지강관의 폭비/]
		VarOut1 ~~~ VarIn1
		end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.2.2.1 (9)"])
		C --> Variable_def

	  E{"겹침 K접합에서 지강관의 폭비"} ;
    D{"0.75 ≤ 지강관의 폭비"} ;
    Variable_def -->E-->D-->Q(["PASS or Fail"])
    """

    @rule_method
    def width_of_branch_member(fIwibrme) -> RuleUnitResult:
        """지강관의 폭비

        Args:
            fIwibrme (float): 지강관의 폭비

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.2.1 적용한계 (9)의 판단 결과
        """

        assert isinstance(fIwibrme, float)

        if fIwibrme >= 0.75:
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