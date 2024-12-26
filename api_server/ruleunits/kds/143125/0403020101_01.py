import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403020101_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.2.1.1 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-25'
    title = 'K형 접합에 대한 접합부 편심'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.2 강관 간의 트러스접합
    4.3.2.1 원형강관
    4.3.2.1.1 적용한계
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: K형 접합에 대한 접합부 편심]
	  B["KDS 14 31 25 4.3.2.1.1 (1)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
		VarOut1[/출력변수: 접합부 편심/] ;
	  VarIn1[/입력변수: 바깥지름/]
		VarIn2[/입력변수: 지강관에서 떨어진 거리/]
		VarOut1 ~~~ VarIn1 & VarIn2
		end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.2.1.1 (1)"])
		C --> Variable_def

	  E{"<img src='https://latex.codecogs.com/svg.image?-0.55D\leq&space;e\leq0.25D'>----------------------------------"} ;
    D([접합부 편심])

		Variable_def --> E --> D
    """

    @rule_method
    def junction_eccentricity(fID,fIe) -> RuleUnitResult:
        """K형 접합에 대한 접합부 편심

        Args:
            fID (float): 바깥지름
            fIe (float): 지강관에서 떨어진 거리

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.1.1 적용한계 (1)의 판단 결과
        """

        assert isinstance(fID, float)
        assert isinstance(fIe, float)

        if -0.55*fID <= fIe <= 0.25*fID:
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