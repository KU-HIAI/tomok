import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040303011202_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.3.3.1.12.2 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '단면변화를 준 덮개판 끝의 폭'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.1 플레이트거더
    4.3.3.1.12 덮개판
    4.3.3.1.12.2 단부 요구조건
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 단면변화를 준 덮개판 끝의 폭] ;
		B["KDS 14 31 10 4.3.3.1.12.2 (1)"] ;
		A ~~~ B
		end

    subgraph Variable_def
      VarIn1[/입력변수: 단면변화를 준 덮개판 끝의 폭/] ;
    end

    Python_Class ~~~ C1(["KDS 24 90 11 4.2.3.9"]) --> Variable_def

    C["단면변화를 준 덮개판 끝의 폭 &ge; 75mm"]

    Variable_def --> C --> D(["PASS or Fail"])
    """

    @rule_method
    def Cover_plate_tip_width_with_cross_section_change(fIcptwcc) -> RuleUnitResult:
        """단면변화를 준 덮개판 끝의 폭

        Args:
            fIcptwcc (float): 단면변화를 준 덮개판 끝의 폭

        Returns:
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법) 4.3.3.1.12.2 단부 요구조건 (1)의 통과여부
        """

        assert isinstance(fIcptwcc, float)


        if fIcptwcc >= 75:
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