import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0401020201_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.2.2.1 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '필릿용접의 유효길이'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.2 용접
    4.1.2.2 필릿용접
    4.1.2.2.1 유효길이
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
    A[Title: 필릿용접의 유효길이]
    B["KDS 14 31 25 4.1.2.2.1 (2)"]
  	A ~~~ B
  	end

	  subgraph Variable_def
	  VarOut[/출력변수: 필릿용접의 유효길이/]
	  VarIn1[/입력변수: 필릿용접의 총길이/]
	  VarIn2[/입력변수: 용접치수/]
	  VarOut ~~~ VarIn1 & VarIn2
	  end

		Python_Class ~~~ C(["KDS 14 31 25 4.1.2.2.1 (2)"])
		C --> Variable_def

	  Variable_def --> D --> E
	  D["필릿용접의 유효길이=필용접의 총길이 - 용접치수x2"]
	  E([필릿용접의 유효길이])
    """

    @rule_method
    def Effective_length_of_fillet_weld(fItolefw,fIweldim) -> RuleUnitResult:
        """필릿용접의 유효길이

        Args:
            fItolefw (float): 필릿용접의 총길이
            fIweldim (float): 용접치수

        Returns:
            fOeflefw (float):  강구조 연결 설계기준(하중저항계수설계법)   4.1.2.2.1 필릿용접의 유효면적 (2)의 값
        """

        assert isinstance(fItolefw, float)
        assert isinstance(fIweldim, float)

        fOeflefw = fItolefw-(2*fIweldim)

        return RuleUnitResult(
            result_variables = {
                "fOeflefw": fOeflefw,
            }
        )