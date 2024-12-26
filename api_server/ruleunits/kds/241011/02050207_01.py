import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241011_02050207_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 10 11 2.5.2.7 (1)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-22'
    title = '외측거더의 내하력'

    description = """
    교량 설계 일반사항(한계상태설계법)
    2. 조사 및 계획
    2.5 설게 목적
    2.5.2 사용성
    2.5.2.7 향후 확폭의 고려
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 외측거더의 내하력];
    B["KDS 24 10 11 2.5.2.7 (1)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarIn1[/입력변수 : 외측거더의 내하력/];
    VarIn2[/입력변수 : 내측거더의 내하력/];
    end

    Python_Class ~~~ C(["KDS 24 10 11 2.5.2.7 (1)"])
		C --> Variable_def

    D{"외측거더 내하력&ge; 내측거더 내하력"};
    E(["Pass or Fail"]);
    Variable_def--->D--->E
    """

    @rule_method
    def Load_capacity_of_outer_girder(fILoutgd,fILingd) -> RuleUnitResult:
        """외측거더의 내하력

        Args:
            fILoutgd (float): 외측거더의 내하력
            fILingd (float): 내측거더의 내하력

        Returns:
            pass_fail (bool): 교량 설계 일반사항(한계상태설계법)  2.5.2.7 향후 확폭의 고려 (1)의 판단 결과
        """

        assert isinstance(fILoutgd, float)
        assert isinstance(fILingd, float)

        if fILoutgd>=fILingd:
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