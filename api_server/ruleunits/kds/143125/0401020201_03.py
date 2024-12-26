import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0401020201_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.2.2.1 (3)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '필릿용접의 유효목두께'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.2 용접
    4.1.2.2 필릿용접
    4.1.2.2.1 유효길이
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
    A[Title: 필릿용접의 유효목두께]
    B["KDS 14 31 25 4.1.2.2.1 (3)"]
  	A ~~~ B
  	end

	  subgraph Variable_def
	  VarOut[/출력변수: 필릿용접의 유효목두께/]
	  VarIn1[/입력변수: 용접치수/]
	  VarOut ~~~ VarIn1
	  end

		Python_Class ~~~ C(["KDS 14 31 25 4.1.2.2.1 (3)"])
		C --> Variable_def

	  Variable_def --> G --yes--> D --> F
  	G --no--> E --> F
  	G --"no(용접 다리의 크기가 서로 다른 경우)" --> H --> F
  	G{"두부재사이의 각도 90°"}
  	D["필릿용접의 유효목두께=용접치수x0.7"]
  	E["필릿용접의 유효목두께=용접루트를 꼭지점으로 하는 내접삼각형의 높이"]
	  F([필릿용접의 유효목두께])
	  H["필릿용접의 유효목두께=용접외측면을 밑변으로 하는 내접삼각형의 높이"]
    """

    @rule_method
    def Effective_throat_thickness_of_fillet_weld(fIweldim) -> RuleUnitResult:
        """필릿용접의 유효목두께

        Args:
            fIweldim (float): 용접치수

        Returns:
            fOetthfw (float):  강구조 연결 설계기준(하중저항계수설계법)   4.1.2.2.1 필릿용접의 유효면적 (3)의 값
        """

        assert isinstance(fIweldim, float)


        fOetthfw = fIweldim*0.7

        return RuleUnitResult(
            result_variables = {
                "fOetthfw": fOetthfw,
            }
        )