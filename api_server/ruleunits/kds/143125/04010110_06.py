import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_04010110_06(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.1.10 (6)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-14'
    title = '고장력볼트의 구멍중심에서 볼트머리 또는 너트가 접하는 부재의 연단까지의 최대거리'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.1 일반사항
    4.1.1.10 이음부 설계세칙
    (6)
    """
    content = """
    """
    flowchart = """
    flowchart TD
  	subgraph Python_Class
  	A[Title: 고장력볼트의 구멍중심에서 볼트머리 또는 너트가 접하는 부재의 연단까지의 최대거리]
	  B["KDS 14 31 25 4.1.1.10(6)"]
  	A ~~~ B
  	end

	  subgraph Variable_def
	  VarOut[/출력변수: 부재의 연단까지의 최대거리/]
	  VarIn[/입력변수: 판 두께/]
	  VarOut ~~~ VarIn
	  end

    Python_Class ~~~ C(["KDS 14 31 25 4.1.1.10(6)"])
		C --> Variable_def

	  Variable_def --> D --> E
	  D{"부재의 연단까지의 최대거리 ≤ 판두께x12 and 150mm"}
	  E([Pass or Fail])
    """

    @rule_method
    def Maximum_distance_from_the_center_of_the_hole_in_the_high_strength_bolt_to_the_edge_of_the_member_in_contact_with_the_bolt_head_or_nut(fIdiplme,fIplathi) -> RuleUnitResult:
        """고장력볼트의 구멍중심에서 볼트머리 또는 너트가 접하는 부재의 연단까지의 최대거리

        Args:
            fIdiplme (float): 부재의 연단까지의 거리
            fIplathi (float): 판 두께

        Returns:
            pass_fail (bool): 깊은기초 설계기준(일반설계법)  4.1.1.10 이음부 설계세칙 (6)의 판단 결과
        """

        assert isinstance(fIdiplme, float)
        assert isinstance(fIplathi, float)

        if fIdiplme <= (fIplathi*12 or 150) :
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