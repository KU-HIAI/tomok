import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241011_04060202_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.6.2.2 (2)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-13'
    title = '바닥판 설계기준강도'

    description = """
    교량 설계 일반사항(한계상태설계법)
    4. 구조해석
    4.6 정적 해석
    4.6.2 바닥판의 해석방법
    4.6.2.2 설계일반
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 바닥판 설계기준강도];
    B["KDS 24 10 11 4.6.2.2 (2)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarIn1[/입력변수 : 콘크리트의 설계기준강도/];
    end

    Python_Class ~~~ C(["KDS 24 10 11 4.6.2.2 (2)"])
		C --> Variable_def

    D{"콘크리트의 설계기준강도 &ge; 27MPa"};
    E(["Pass or Fail"]);
    Variable_def--->D--->E
    """

    @rule_method
    def specified_design_strength_of_floor(fIfck) -> RuleUnitResult:
        """바닥판 설계기준강도

        Args:
            fIfck (float): 콘크리트의 설계기준강도

        Returns:
            pass_fail (bool): 교량 설계 일반사항(한계상태설계법) 4.6.2.2 설계일반 (2)의 판단 결과
        """

        assert isinstance(fIfck, float)

        if fIfck >= 27 :
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