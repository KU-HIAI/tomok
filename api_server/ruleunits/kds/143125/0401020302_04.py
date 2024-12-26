import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0401020302_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.2.3.2 (4)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '슬롯용접의 제한사항'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.2 용접
    4.1.2.3 플러그 및 슬롯용접
    4.1.2.3.2 제한사항
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
    A[Title: 슬롯용접의 제한사항]
    B["KDS 14 31 25 4.1.2.3.2 (4)"]
  	A ~~~ B
  	end

	  subgraph Variable_def
	  VarIn1[/입력변수: 슬롯용접의 슬롯길이/]
	  VarIn2[/입력변수: 용접두께/]
	  VarIn3[/입력변수: 슬롯의 폭/]
	  VarIn4[/입력변수: 슬롯이 있는 판의 두께/]
	  end

		Python_Class ~~~ C(["KDS 14 31 25 4.1.2.3.2 (4)"])
		C --> Variable_def

	  Variable_def --> D & E
	  D --> F
	  E --> F

	  D{"슬롯용접의 슬롯길이 ≤ 용접두께+8mm "}
	  E{"슬롯이 있는 판의 두께+8mm ≤ 슬롯의 폭 ≤ 용접두께x2.25"}
	  F([PASS or Fail])
    """

    @rule_method
    def Restricton_for_solt_welding(fIsllesw,fIwelthi,fIslowid,fIthipla) -> RuleUnitResult:
        """슬롯용접의 제한사항

        Args:
            fIsllesw (float): 슬롯용접의 슬롯길이
            fIwelthi (float): 용접두께
            fIslowid (float): 슬롯의 폭
            fIthipla (float): 슬롯이 있는 판의 두께

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)   4.1.2.3.2 제한사항 (4)의 판단 결과
        """

        assert isinstance(fIsllesw, float)
        assert isinstance(fIwelthi, float)
        assert isinstance(fIslowid, float)
        assert isinstance(fIthipla, float)

        if fIsllesw <= 10*fIwelthi and (fIthipla+8) <= fIslowid <= (2.25*fIwelthi) :
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