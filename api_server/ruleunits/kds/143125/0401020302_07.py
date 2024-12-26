import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0401020302_07(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.2.3.2 (7)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '플러그 및 슬롯용접의 두께'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.2 용접
    4.1.2.3 플러그 및 슬롯용접
    4.1.2.3.2 제한사항
    (7)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
    A[Title: 플러그 및 슬롯용접의 두께]
    B["KDS 14 31 25 4.1.2.3.2 (7)"]
  	A ~~~ B
  	end

	  subgraph Variable_def
	  VarOut1[/출력변수: 플러그/]
	  VarOut2[/출력변수: 슬롯용접의 두께/]
	  VarIn[/입력변수: 판 두께/]
	  VarOut1 & VarOut2 ~~~ VarIn
	  end

		Python_Class ~~~ C(["KDS 14 31 25 4.1.2.3.2 (7)"])
		C --> Variable_def

	  Variable_def --> D
	  D --Yes--> F
	  D --No--> G

  	D{"판 두께 ≤ 16mm"}
	  F[플러그 및 슬롯용접의 두께 = 판 두께]
	  G{"플러그 및 슬롯용접의 두께 ≥ 판 두께x1/2 and 16mm"}
		F & G ---> H([플러그 및 슬롯용접의 두께])
    """

    @rule_method
    def Thickness_of_plug_and_slot_welding(fIthipla) -> RuleUnitResult:
        """플러그 및 슬롯용접의 두께

        Args:
            fIthipla (float): 판 두께

        Returns:
            fOthpswe (bool): 강구조 연결 설계기준(하중저항계수설계법)   4.1.2.3.2 제한사항 (7)의 값
        """

        assert isinstance(fIthipla, float)

        if fIthipla <= 16 :
          fOthpswe = fIthipla

        else:
          fOthpswe = max(fIthipla*0.5,16)

        return RuleUnitResult(
            result_variables = {
                "fOthpswe": fOthpswe,
            }
        )