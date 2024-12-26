import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04020403_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.2.4.3 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-14'
    title = '회전수용능력'

    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.4 포트받침
    4.2.4.3 회전수용능력
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 회전수용능력];
    B["KDS 24 90 11 4.2.4.3 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 포트받침에 발생하는 최대 회전각/];
		VarIn2[/입력변수: 활하중에 의한 회전각 변동/];

		VarIn1 & VarIn2
		end

		Python_Class ~~~ C(["KDS 24 90 11 4.2.4.3 (1)"])
		C --> Variable_def;

		Variable_def--> F & D--->E

		F{"포트받침에 발생하는 최대 회전각≤0.03rad"}
		D{"활하중에 의한 회전각 변동≤0.005rad"}

		E(["Pass or Fail"])
    """

    @rule_method
    def Maximum_Rotation_Angle_For_Potholders (fIalphadmax,fIdeltaalphad2) -> RuleUnitResult:
        """회전수용능력
        Args:
            fIalphadmax (float): 포트받침에 발생하는 최대 회전각
            fIdeltaalphad2 (float): 활하중에 의한 회전각 변동

        Returns:
            pass_fail (bool): 교량 기타시설설계기준 (한계상태설계법) 4.2.4.3 회전수용능력 (1)의 판단 결과
        """
        assert isinstance(fIalphadmax, float)
        assert isinstance(fIdeltaalphad2, float)

        if fIalphadmax <= 0.03 and fIdeltaalphad2 <= 0.005 :
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