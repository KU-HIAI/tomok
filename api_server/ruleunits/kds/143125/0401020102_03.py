import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0401020102_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.2.1.2 (3)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '부분용입 그루브용접의 유효면적'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.2 용접
    4.1.2.1 그루브용접
    4.1.2.1.2 부분용입 그루브용접
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
    A[Title: 부분용입 그루브용접의 유효면적]
    B["KDS 14 31 25 4.1.2.1.2 (3)"]
  	A ~~~ B
  	end

	  subgraph Variable_def
	  VarOut[/출력변수: 부분용입그루브용접의 유효면적/]
	  VarIn1[/입력변수: 용접의 유효길이/]
	  VarIn2[/입력변수: 유효목두께/]
	  VarOut ~~~ VarIn1 & VarIn2
	  end

		Python_Class ~~~ C(["KDS 14 31 25 4.1.2.1.2 (3)"])
		C --> Variable_def

	  Variable_def --> D --> E
	  D["부분용입 그루브용접의 유효면적=용접의 유효두께 x 유효목두께"]
	  E([부분용입 그루브용접의 유효면적])
    """

    @rule_method
    def Effective_area_of_partial_joint_penetration_groove_weld(fIeflewe,fIefthth) -> RuleUnitResult:
        """부분용입 그루브용접의 유효면적

        Args:
            fIeflewe (float): 용접의 유효길이
            fIefthth (float): 유효목두께

        Returns:
            fOefaPJP (float):  강구조 연결 설계기준(하중저항계수설계법)   4.1.2.1.2 부분용입 그루브용접 (3)의 값
        """

        assert isinstance(fIeflewe, float)
        assert isinstance(fIefthth, float)

        fOefaPJP = fIeflewe*fIefthth

        return RuleUnitResult(
            result_variables = {
                "fOefaPJP": fOefaPJP,
            }
        )