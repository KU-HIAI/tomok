import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010203_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.2.3 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-17'
    title = '복부의 스트럿 경사각'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.3 전단보강철근이 배치된 부재
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 복부의 스트럿 경사각];
    B["KDS 24 14 21 4.1.2.3 (1)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 복부의 스트럿 경사각/];

		VarIn1

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.2.3 (1)"])
		C --> Variable_def

		Variable_def--->D--->E

		D{"<img src='https://latex.codecogs.com/svg.image?1\leq&space;cot\theta\leq&space;2.5'>---------------------------------"}
    E(["Pass or Fail"])
    """

    @rule_method
    def The_angle_of_inclination_of_the_strut_in_the_abdomen(fItheta) -> RuleUnitResult:
        """복부의 스트럿 경사각

        Args:
            fItheta (float): 복부의 스트럿 경사각

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.3 전단보강철근이 배치된 부재 (1)의 판단 결과
        """

        assert isinstance(fItheta, float)
        assert fItheta != 0

        import math

        fItheta = math.radians(fItheta)

        if 1.0 <= 1/(math.tan(fItheta)) <= 2.5:
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