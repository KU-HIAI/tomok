import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS171000_04020104_04(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 17 10 00 4.2.1.4 (4)'
    ref_date = '2018-12-06'
    doc_date = '2024-02-13'
    title = '유효수평지반가속도'

    description = """
    내진설계 일반
    4. 설계
    4.2 지진재해
    4.2.1 지반운동
    4.2.1.4 설계지반운동의 특성 표현
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 유효수평지반가속도];
    B["KDS 17 10 00 4.2.1.4 (4)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut1[/출력변수 : 유효수평지반가속도/];
    VarIn1[/입력변수 : 행정구역에 따라 결정한 값/];
    end

    Python_Class ~~~ C(["KDS 17 10 00 4.2.1.4 (4)"])
		C --> Variable_def

    D{"국가지진 위험지도 이용"};
    E["S"]
    F{"S &ge; 행정구역에 따라 결정한 값x0.8"};
    G(["유표수평지반가속도"]);
    Variable_def--->D--Yes--->E--->G
    D--No--->F--->G
    """

    @rule_method
    def Effective_Lateral_Ground_Acceleration(fIS,fIdivis) -> RuleUnitResult:
        """유효수평지반가속도

        Args:
            fIS (float): 유효수평지반가속도.
            fIdivis (float): 행정구역에 따라 결정한 값.

        Returns:
            pass_fail (bool): 내진설계 일반  4.2.1.4 설계지반운동의 특성 표현 (4)의 판단 결과
        """

        assert isinstance(fIS, float)
        assert isinstance(fIdivis, float)

        if fIS >= fIdivis * 0.8:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": True,
                  }
              )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": True,
                  }
              )