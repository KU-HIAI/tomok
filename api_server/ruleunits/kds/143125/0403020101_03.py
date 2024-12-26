import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403020101_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.2.1.1 (3)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-25'
    title = '주강관벽 세장비'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.2 강관 간의 트러스접합
    4.3.2.1 원형강관
    4.3.2.1.1 적용한계
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 주강관벽 세장비]
	  B["KDS 14 31 25 4.3.2.1.1 (3)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn1[/입력변수: 주강관벽 세장비/]
		VarIn1
		end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.2.1.1 (3)"])
		C --> Variable_def

	  F{"벽지름 두께비≤50"} ;
    D{"벽지름 두께비≤40"} ;
    E{"접합형상"} ;
		Variable_def --> E
    E--T, Y, K형 이음-->F
    E--X형 접합-->D
		F & D --> Q(["PASS or Fail"])
    """

    @rule_method
    def chord_wall_slenderness_ratio(fIcwslrA,fIcwslrB) -> RuleUnitResult:
        """주강관벽 세장비

        Args:
            fIcwslrA (float): 주강관벽 세장비 (T, Y, K-형 이음)
            fIcwslrB (float): 주강관벽 세장비 (X형 접합)

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.1.1 적용한계 (3)의 판단 결과
        """

        assert isinstance(fIcwslrA, float)
        assert isinstance(fIcwslrB, float)

        if fIcwslrA != 0 and fIcwslrB == 0 :
          if fIcwslrA <= 50 :
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

        if fIcwslrA == 0 and fIcwslrB != 0 :
          if fIcwslrB <= 40 :
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