import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_04060504_11(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.6.5.4 (11)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-16'
    title = '보강 띠철근간의 수평간격'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.5 중공원형 교각
    4.6.5.4 소성힌지구역에서의 심부구속 방향
    (11)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 보강 띠철근간의 수평간격];
    B["KDS 24 17 11 4.6.5.4 (11)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarIn1[/입력변수: 보강 띠철근간의 수평간격/] ;
    VarIn2[/입력변수: 심부구속 후프철근 호칭지름/];
    end

    Python_Class ~~~ C(["KDS 24 17 11 4.6.5.4 (11)"])
		C --> Variable_def

    Variable_def -->H
    H{"심부구속 후프철근 호칭지름 x30 &ge; 보강 띠철근간의 수평간격"};
   	I([Pass or Fail])

		H -->I
    """

    @rule_method
    def horizontal_rebar_spacing(fIhosprb,fInddrhr) -> RuleUnitResult:
        """보강 띠철근간의 수평간격

        Args:
            fIhosprb (float): 보강 띠철근간의 수평간격
            fInddrhr (float): 심부구속 후프철근 호칭지름

        Returns:
            pass_fail (bool): 교량내진설계기준(한계상태설계법) 4.6.5.4 중공원형 교각 (11)의 값
        """

        assert isinstance(fIhosprb, float)
        assert isinstance(fInddrhr, float)

        if fIhosprb <= 30 * fInddrhr:
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