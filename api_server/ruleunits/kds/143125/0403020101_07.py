import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403020101_07(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.2.1.1 (7)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-25'
    title = '적용한계'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.2 강관 간의 트러스접합
    4.3.2.1 원형강관
    4.3.2.1.1 적용한계
    (7)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 적용한계]
	  B["KDS 14 31 25 4.3.2.1.1 (7)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn1[/입력변수: 갭 K이음에서 용접부를 무시한 지강관 끝 사이의 간격/]
	  VarIn2[/입력변수: 벽두께 총합/]
		end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.2.1.1 (7)"])
		C --> Variable_def

	  D{"g ≥ 벽두께 총합"} ;
		Variable_def --"간격 K접합"--> D
    D-->F(["PASS or Fail"])
    """

    @rule_method
    def application_limit(fIg,fItowath) -> RuleUnitResult:
        """적용한계

        Args:
            fIg (float): 갭 K이음에서 용접부를 무시한 지강관 끝 사이의 간격
            fItowath (float): 벽두께 총합

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.1.1 적용한계 (7)의 판단 결과
        """

        assert isinstance(fIg, float)
        assert isinstance(fItowath, float)

        if fIg >= fItowath:
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