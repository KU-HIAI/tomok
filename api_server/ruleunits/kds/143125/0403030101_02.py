import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403030101_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.3.1.1 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-25'
    title = '주강관벽 세장비'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.3 강관 간의 모멘트접합
    4.3.3.1 원형강관
    4.3.3.1.1 적용한계
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 주강관벽 세장비]
	  B["KDS 14 31 25 4.3.3.1.1 (2)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
    VarOut1[/출력변수: 주강관벽 세장비/] ;
    VarIn1[/입력변수: 벽지름 두께비/] ;
    end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.3.1.1 (2)"])
		C --> Variable_def

	  G{"T, Y, K형 접합"} ;
    D{"벽지름 두께비 ≤ 50"} ;
    E{"X형 접합"} ;
    F{"벽지름 두께비 ≤ 40"} ;
    Variable_def --> G -->D
    Variable_def --> E -->F
    D & F --> R["주강관벽 세장비 = 벽지름 두께비"] --> Q(["주강관벽 세장비"])
    """

    @rule_method
    def Cast_steel_pipe_wall_slenderness(fIcwslrA,fIcwslrB) -> RuleUnitResult:
        """주강관벽 세장비

        Args:
            fIcwslrA (float): 주강관벽 세장비 (T, Y, K-형 접합)
            fIcwslrB (float): 주강관벽 세장비 (X형 접합)

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.2.1 적용한계 (3)의 판단 결과
        """

        assert isinstance(fIcwslrA, float)
        assert isinstance(fIcwslrB, float)

        if fIcwslrA != 0 and fIcwslrB == 0 :
          if fIcwslrA <= 50:
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

        elif fIcwslrA == 0 and fIcwslrB != 0 :
          if fIcwslrB <= 40:
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