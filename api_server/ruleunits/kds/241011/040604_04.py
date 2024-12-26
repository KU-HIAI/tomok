import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241011_040604_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 10 11 4.6.4 (4)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-22'
    title = '감소계수'

    description = """
    교량 설계 일반사항(한계상태설계법)
    4. 구조해석
    4.6 정적 해석
    4.6.4 슬래브교에 대한 등가 스트립 폭
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 감소계수];
    B["KDS 24 10 11 4.6.4 (4)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 감소계수/];
    VarIn1[/입력변수 : 사각/];
    end

    Python_Class ~~~ C(["KDS 24 10 11 4.6.4 (4)"])
		C --> Variable_def

    D["<img src='https://latex.codecogs.com/svg.image?r=1.05-0.25tan\theta(\leq&space;1.00)'>-------------------------------"];
    E(["감소계수"]);
    Variable_def--->D--->E
    """

    @rule_method
    def Reduction_factor(fIskeang) -> RuleUnitResult:
        """감소계수

        Args:
            fIskeang (float): 사각(도)

        Returns:
            fOr (float): 교량 설계 일반사항(한계상태설계법)  4.6.4 슬래브교에 대한 등가 스트립 폭 (4)의 값
            pass_fail (bool): 교량 설계 일반사항(한계상태설계법)  4.6.4 슬래브교에 대한 등가 스트립 폭 (4)의 판단 결과
        """

        assert isinstance(fIskeang, float)

        import math

        fOr=1.05-0.25*math.tan(math.radians(fIskeang))

        if fOr <= 1.0:
          return RuleUnitResult(
              result_variables = {
                  "fOr": fOr,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )