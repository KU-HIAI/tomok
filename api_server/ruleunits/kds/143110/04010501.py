import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_04010501(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.1.5.1'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '핀접합부재의 설계인장강도'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.1 인장부재
    4.1.5 핀접합부재
    4.1.5.1 인장강도
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[핀접합부재의 설계인장강도] ;
		B["KDS 14 31 10 4.1.5.1"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarOut1[/출력변수: 핀접합부재의 설계인장강도/]
    VarIn1[/입력변수: 인장파단/]
    VarIn2[/입력변수: 전단파단/]
    VarIn3[/입력변수: 지압 및 항복의 한계상태/]
		end

		Python_Class ~~~ Variable_def
  	D(["핀접합부재의 설계인장강도=min(인장파단, 전단파단, 지압 및 항복의 한계상태)"])
  	Variable_def-->D
    """

    @rule_method
    def design_tensil_strength_of_pin_joint_member(fItenrup,fIsherup,fIlsoaas) -> RuleUnitResult:
        """핀접합부재의 설계인장강도

        Args:
            fItenrup (float): 인장파단
            fIsherup (float): 전단파단
            fIlsoaas (float): 지압 및 항복의 한계상태

        Returns:
            fOphitPn (float): 강구조부재설계기준(하중저항계수설계법) 4.1.5.1 인장강도의 값
        """

        assert isinstance(fItenrup, float)
        assert isinstance(fIsherup, float)
        assert isinstance(fIlsoaas, float)

        fOphitPn = min(fItenrup,fIsherup,fIlsoaas)

        return RuleUnitResult(
            result_variables = {
              "fOphitPn": fOphitPn,
            }
        )