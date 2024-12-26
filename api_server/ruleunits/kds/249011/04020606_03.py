import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04020606_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.2.6.6 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-14'
    title = '유도궤도'

    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.6 받침 마찰요소의 설계
    4.2.6.6 미끄럼요소 설계
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 유도궤도];
    B["KDS 24 90 11 4.2.6.6 (3)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarIn1[/입력변수: 미끄럼요소간의 틈/];
		VarIn2[/입력변수: PTFE의 직경/];
    VarIn1 & VarIn2
    end

    Python_Class ~~~ C(["KDS 24 90 11 4.2.6.6 (3)"])
		C --> Variable_def;
		Variable_def--->K--->M


    K{"<img src='https://latex.codecogs.com/svg.image?c\leq&space;1.0mm&plus;\frac{L}{1000}mm'>--------------------------------------------------------"};

    M(["Pass or Fail"])
    """

    @rule_method
    def Gaps_Between_Sliding_Elements(fIc,fIL) -> RuleUnitResult:
        """유도궤도
        Args:
            fIc (float): 미끄럼요소간의 틈
            fIL (float): PTFE의 직경

        Returns:
            pass_fail (bool): 교량 기타시설설계기준 (한계상태설계법) 4.2.6.6 미끄럼요소 설계 (3)의 판단 결과
        """

        assert isinstance(fIc, float)
        assert isinstance(fIL, float)

        if fIc <= 1.0 + fIL / 1000 :
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