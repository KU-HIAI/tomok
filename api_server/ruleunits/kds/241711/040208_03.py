import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_040208_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.2.8 (3)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-13'
    title = '최소받침지지길이'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.2 해석 및 설계
    4.2.8 설계변위
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 최소받침지지길이]
	  B["KDS 24 17 11 4.2.8(3)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: 최소받침지지길이/]
	  VarIn1[/입력변수: 인접 신축이음부까지 또는 교량단부까지의 거리/]
	  VarIn2[/입력변수: 평균높이/]
	  VarIn3[/입력변수: 받침선과 교축직각방향의 사잇각/]

  	VarOut ~~~ VarIn1 & VarIn2 & VarIn3
	  end
	  Python_Class ~~~ C(["KDS 24 17 11 4.2.8(3)"])
		C --> Variable_def --> D --> E
	  D{"<img src='https://latex.codecogs.com/svg.image?&space;N\geq(200&plus;1.67L&plus;6.66H)(1&plus;0.000125\theta^2)(mm)'>--------------------------------------------------------------------"};
	  E([Pass or Fail])
    """

    @rule_method
    def Minimum_Support_Length(fIN, fIL, fIH, fIvarphi) -> RuleUnitResult:
        """최소받침지지길이

        Args:
            fIN (float): 최소받침지지길이
            fIL (float): 인접 신축이음부까지 또는 교량단부까지의 거리
            fIH (float): 평균높이
            fIvarphi (float): 받침선과 교축직각방향의 사잇각

        Returns:
            pass_fail (bool): 교량내진설계기준(한계상태설계법) 4.2.8 설계변위 (3)의 판단 결과
        """

        assert isinstance(fIN, float)
        assert isinstance(fIL, float)
        assert isinstance(fIH, float)
        assert isinstance(fIvarphi, float)

        if fIN >= (200 + 1.67 * fIL + 6.66 * fIH) * (1 + 0.000125 * fIvarphi ** 2):
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