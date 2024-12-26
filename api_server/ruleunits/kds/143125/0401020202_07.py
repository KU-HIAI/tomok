import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0401020202_07(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.2.2.2 (7)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '겹침이음의 최소 겹침길이'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.2 용접
    4.1.2.2 필릿용접
    4.1.2.2.2 제한사항
    (7)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
    A[Title: 겹침이음의 최소 겹침길이]
    B["KDS 14 31 25 4.1.2.2.2 (7)"]
  	A ~~~ B
  	end

	  subgraph Variable_def
	  VarOut[/출력변수: 최소 겹침길이/]
	  VarIn[/입력변수: 연결부의 얇은 쪽 판두께/]
	  VarOut ~~~ VarIn
	  end

		Python_Class ~~~ C(["KDS 14 31 25 4.1.2.2.2 (7)"])
		C --> Variable_def

	  Variable_def --> D --> E

	  D["최소 겹침길이= 연결부의 얇은 쪽 판 두께x5 or 25mm"]
  	E([최소 겹침길이])
    """

    @rule_method
    def Minimum_overlapped_length_of_overlap_joint(fIthtspj) -> RuleUnitResult:
        """겹침이음의 최소 겹침길이

        Args:
            fIthtspj (float): 연결부의 앏은 쪽 판 두께

        Returns:
            fOmiovle (float): 강구조 연결 설계기준(하중저항계수설계법)   4.1.2.2.2 제한사항 (7)의 값
        """

        assert isinstance(fIthtspj, float)

        if 5*fIthtspj <= 25 :
          fOmiovle = 25
          return RuleUnitResult(
              result_variables = {
                  "fOmiovle": fOmiovle,
              }
          )

        else:
          fOmiovle = 5 * fIthtspj
          return RuleUnitResult(
              result_variables = {
                  "fOmiovle": fOmiovle,
              }
          )