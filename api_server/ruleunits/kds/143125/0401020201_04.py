import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0401020201_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.2.2.1 (4)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '플러그용접과 슬롯용접의 유효길이'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.2 용접
    4.1.2.2 필릿용접
    4.1.2.2.1 필릿용접의 유효면적
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
    A[Title: 플러그용접과 슬롯용접의 유효길이]
    B["KDS 14 31 25 4.1.2.2.1 (4)"]
  	A ~~~ B
  	end

	  subgraph Variable_def
	  VarOut[/출력변수: 플러그용접과 슬롯용접의 유효길이/]
	  VarIn[/입력변수: 용접중심선의 길이/]
	  VarOut ~~~ VarIn
	  end

		Python_Class ~~~ C(["KDS 14 31 25 4.1.2.2.1 (4)"])
		C --> Variable_def

	  Variable_def --> D --> E
	  D["플러그용접과 슬롯용접의 유효길이=용접중심선의 길이"]
	  E([플러그용접과 슬롯용접의 유효길이])
    """

    @rule_method
    def Effective_length_of_plug_welding_and_slot_weld(fIlenwcl) -> RuleUnitResult:
        """플러그용접과 슬롯용접의 유효길이

        Args:
            fIlenwcl (float): 용접중심선의 길이

        Returns:
            fOelpwsw (float):  강구조 연결 설계기준(하중저항계수설계법)   4.1.2.2.1 필릿용접의 유효면적 (4)의 값
        """

        assert isinstance(fIlenwcl, float)


        fOelpwsw = fIlenwcl

        return RuleUnitResult(
            result_variables = {
                "fOelpwsw": fOelpwsw,
            }
        )