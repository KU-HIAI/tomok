import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_04010106(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.1.6'
    ref_date = '2017-12-20'
    doc_date = '2024-02-14'
    title = '접합부의 설계강도'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.1 일반사항
    4.1.1.6 접합부의 최소강도
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
    A[Title: 접합부의 설계강도]
    B["KDS 14 31 25 4.1.1.6"]
  	A ~~~ B
  	end

	  subgraph Variable_def
	  VarIn[/입력변수: 접합부의 설계강도/]
	  end

		Python_Class ~~~ C(["KDS 14 31 25 4.1.1.6"])
		C --> Variable_def

	  Variable_def --> D --> E

	  D{"접합부의 설계강도 ≥ 45KN"}
	  E([Pass or Fail])
    """

    @rule_method
    def Design_strength_of_connection(fIdestco) -> RuleUnitResult:
        """접합부의 설계강도

        Args:
            fIdestco (float): 접합부의 설계강도

        Returns:
            sOdestco (string):  강구조 연결 설계기준(하중저항계수설계법)   4.1.1.6 접합부의 최소강도의 판단 결과 1
            pass_fail (bool):  강구조 연결 설계기준(하중저항계수설계법)   4.1.1.6 접합부의 최소강도의 판단 결과 2
        """

        assert isinstance(fIdestco, float)

        if fIdestco >= 45 :
          return RuleUnitResult(
              result_variables = {
                  "sOdestco": "연결재, 새그로드 또는 띠장은 제외",
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "sOdestco": "연결재, 새그로드 또는 띠장은 제외",
                  "pass_fail": False,
              }
          )