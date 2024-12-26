import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241011_020606_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 10 11 2.6.6 (2)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-22'
    title = '설계강우강도'

    description = """
    교량 설계 일반사항(한계상태설계법)
    2. 조사 및 계획
    2.6 수문 및 수리
    2.6.6 도로배수
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 설계강우강도];
    B["KDS 24 10 11 2.6.6 (2)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarIn1[/입력변수 : 설계강우강도/];
    VarIn2[/입력변수 : 인접도로의 포장 배수설계에 적용하는 설계강우강도/];
    end

    Python_Class ~~~ C(["KDS 24 10 11 2.6.6 (2)"])
		C --> Variable_def

    F{"발주자가 규정하지 않는 경우"};
    D["설계강우강도 &ge; 인접도로의 포장 배수설계에 적용하는 설계강우강도"];
    E(["Pass or Fail"]);
    Variable_def--->F--->D--->E
    """

    @rule_method
    def Design_rainfall_intensity(fIraind,fIrainad) -> RuleUnitResult:
        """설계강우강도

        Args:
            fIraind (float): 설계강우강도
            fIrainad (float): 인접도로의 포장 배수설계에 적용하는 설계강우강도

        Returns:
            pass_fail (bool): 교량 설계 일반사항(한계상태설계법)  2.6.6 도로배수 (2)의 판단 결과
        """

        assert isinstance(fIraind, float)
        assert isinstance(fIrainad, float)

        if fIraind >= fIrainad:
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