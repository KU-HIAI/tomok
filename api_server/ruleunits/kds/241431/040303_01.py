import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241431_040303_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 31 4.3.3 (1)'
    ref_date = '2018-08-30'
    doc_date = '2024-02-20'
    title = '강재의 최소두께'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.3 부재에 관한 일반사항
    4.3.3 강재의 최소두께
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 강재의 최소두께];
    B["KDS 24 14 31 4.3.3 (1)"];
    A ~~~ B
    end

    subgraph Variable_def
		VarIn1[/입력변수: 강재의 최소두께/] ;
		end

		Python_Class ~~~ C(["KDS 24 14 31 4.3.3 (1)"])
		C --> Variable_def

		Variable_def -->D
    D{"강재의 최소두께 &ge; 8mm"};
    D --> H([PASS or Fail]);
    """

    @rule_method
    def Steel_minimum_thickness(fIstmith) -> RuleUnitResult:
        """강재의 최소두께

        Args:
            fIstmith (float): 강재의 최소두께

        Returns:
            pass_fail (bool): 강교 설계기준(한계상태설계법)  4.3.3 강재의 최소두께 (1)의 판단 결과 1
            sOstmith (string): 강교 설계기준(한계상태설계법)  4.3.3 강재의 최소두께 (1)의 판단 결과 2
        """

        assert isinstance(fIstmith, float)

        if fIstmith >= 8 :
          return RuleUnitResult(
              result_variables = {
                  "sOstmith": "단, 압연형강의 복부판, 강바닥판의 폐단면리브, 채움재 및 난간용 재료는 이 규정을 따르지 않아도 좋다.",
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "sOstmith": "단, 압연형강의 복부판, 강바닥판의 폐단면리브, 채움재 및 난간용 재료는 이 규정을 따르지 않아도 좋다.",
                  "pass_fail": False,
              }
          )