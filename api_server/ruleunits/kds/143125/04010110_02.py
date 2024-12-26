import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_04010110_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.1.10 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-14'
    title = '겹침이음의 겹침길이'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.1 일반사항
    4.1.1.10 이음부 설계세칙
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
  	subgraph Python_Class
  	A[Title: 겹침이음의 겹침길이]
  	B["KDS 14 31 25 4.1.1.10(2)"]
  	A ~~~ B
  	end

  	subgraph Variable_def
  	VarIn1[/입력변수: 겹침길이/]
  	VarIn2[/입력변수: 얇은쪽 판 두께/]
	  end

		Python_Class ~~~ C(["KDS 14 31 25 4.1.1.10(2)"])
		C --> Variable_def

	  Variable_def --> D --> E
	  D{"겹침길이 ≥ 얇은쪽 판 두께x5 and 20mm"}
  	E([Pass or Fail])
    """

    @rule_method
    def Overlap_length_of_overlapping_joint(fIovelen,fIthspth) -> RuleUnitResult:
        """겹침이음의 겹침길이

        Args:
            fIovelen (float): 겹침길이
            fIthspth (float): 얇은쪽 판 두께

        Returns:
            sOfilwel (string): 강구조 연결 설계기준(하중저항계수설계법)   4.1.1.10 이음부 설계세칙 (2)의 판단 결과 1
            pass_fail (bool):  강구조 연결 설계기준(하중저항계수설계법)   4.1.1.10 이음부 설계세칙 (2)의 판단 결과 2
        """

        assert isinstance(fIovelen, float)
        assert isinstance(fIthspth, float)

        if fIovelen >= (fIthspth * 5 or 20) :
          return RuleUnitResult(
              result_variables = {
                  "sOfilwel": "2열 이상의 필릿용접",
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "sOfilwel": "2열 이상의 필릿용접",
                  "pass_fail": False,
              }
          )