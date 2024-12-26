import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241431_040303_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 31 4.3.3 (2)'
    ref_date = '2018-08-30'
    doc_date = '2024-02-20'
    title = '폐단면리브의 두께'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.3 부재에 관한 일반사항
    4.3.3 강재의 최소두께
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 폐단면리브의 두께];
    B["KDS 24 14 31 4.3.3 (2)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarIn1[/입력변수: 폐단면리브의 두께/];
    end

		Python_Class ~~~ C(["KDS 24 14 31 4.3.3 (2)"])
		C --> Variable_def

		D{"폐단면리브의 두께 &ge; 7mm"};
    D --> H([PASS or Fail]);
    Variable_def -->D
    """

    @rule_method
    def Closed_section_ribs_thickness(fIcsrith) -> RuleUnitResult:
        """폐단면리브의 두께

        Args:
            fIcsrith (float): 폐단면리브의 두께

        Returns:
            pass_fail (bool): 강교 설계기준(한계상태설계법)  4.3.3 강재의 최소두께 (2)의 판단 결과
        """

        assert isinstance(fIcsrith, float)

        if fIcsrith >= 7.0 :
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