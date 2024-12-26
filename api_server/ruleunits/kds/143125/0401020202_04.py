import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0401020202_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.2.2.2 (4)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '필릿용접의 길이'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.2 용접
    4.1.2.2 필릿용접
    4.1.2.2.2 제한사항
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
    A[Title: 필릿용접의 길이]
    B["KDS 14 31 25 4.1.2.2.2 (4)"]
  	A ~~~ B
  	end

	  subgraph Variable_def
	  VarIn1[/입력변수: 필릿용접의 길이/]
	  VarIn2[/입력변수: 용접의 직각방향 간격/]
	  VarIn3[/입력변수: 인장재의 유효 순단면적/]
	  VarIn1 ~~~ VarIn2 & VarIn3
	  end

		Python_Class ~~~ C(["KDS 14 31 25 4.1.2.2.2 (4)"])
		C --> Variable_def

	  Variable_def --> D & E
	  D --> G
	  E --> F --> H
	  D{"필릿용접의 길이> 용접의 직각방향 간격"}
	  E["인장재의 유효 순단면적"]
	  F{"KDS 14 31 25 4.1.2.3"}
	  G(["Pass or Fail"])
	  H([인장재의 유효 순단면적])
    """

    @rule_method
    def length_of_fillet_weld(fIlefiwe,fIpespwe) -> RuleUnitResult:
        """필릿용접의 길이

        Args:
            fIlefiwe (float): 필릿용접의 길이
            fIpespwe (float): 용접의 직각방향 간격

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)   4.1.2.2.2 제한사항 (4)의 판단 결과
        """

        assert isinstance(fIlefiwe, float)
        assert isinstance(fIpespwe, float)

        if fIlefiwe > fIpespwe :
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