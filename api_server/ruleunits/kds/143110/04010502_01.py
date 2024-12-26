import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_04010502_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.1.5.2 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '일반 강구조물의 핀접합부재 구조제한'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.1 인장부재
    4.1.5 핀접합부재
    4.1.5.2 핀접합부재의 구조제한
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[일반 강구조물의 핀접합부재 구조제한] ;
		B["KDS 14 31 10 4.1.5.2 (1)"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarIn1[/입력변수: 핀구멍의 직경/]
    VarIn2[/입력변수: 핀직경/]
    VarIn3[/입력변수: 핀구멍이 있는 플레이트의 폭/]
    VarIn4[/입력변수: 유효연단거리/]
    VarIn5[/입력변수: 재축에 평행한 핀구멍의 연단거리/]
		end

		Python_Class ~~~ Variable_def
	  C["핀구멍의 직경"] ;
    D(["핀구멍의 직경 ≤ 핀직경+1mm"]) ;
	  E["핀구멍이 있는 플레이트의 폭"] ;
    F(["핀구멍이 있는 플레이트폭<img src='https://latex.codecogs.com/svg.image?\geq&space;2b_{eff}&plus;d'>-------------------------------- "]) ;
	  G["재축에 평행한 핀구멍의 연단거리a"] ;
    H(["<img src='https://latex.codecogs.com/svg.image?a\geq&space;1.33b_{eff}'>---------------------------"])

	  Variable_def-->C-->D
	  Variable_def-->E-->F
	  Variable_def-->G-->H
	  D & F & H --> I([PASS or Fail]);
    """

    @rule_method
    def structure_limit_of_pin_member(fIdipiho,fId,fIwiplpH,fIbeff,fIa) -> RuleUnitResult:
        """일반 강구조물의 핀접합부재 구조제한

        Args:
            fIdipiho (float): 핀구멍의 직경
            fId (float): 핀직경
            fIwiplpH (float): 핀구멍이 있는 플레이트의 폭
            fIbeff (float): 유효연단거리
            fIa (float): 재축에 평행한 핀구멍의 연단거리

        Returns:
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법)  4.1.5.2 핀접합부재의 구조제한 (1)의 통과여부
        """

        assert isinstance(fIdipiho, float)
        assert isinstance(fId, float)
        assert isinstance(fIwiplpH, float)
        assert isinstance(fIbeff, float)
        assert isinstance(fIa, float)

        if fIdipiho <= (fId+1) and fIwiplpH >= (2*fIbeff + fId) and fIa >= 1.33*fIbeff:
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