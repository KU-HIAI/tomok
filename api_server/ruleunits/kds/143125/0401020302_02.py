import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0401020302_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.2.3.2 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '플러그용접을 위한 구멍의 직경'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.2 용접
    4.1.2.3 플러그 및 슬롯용접
    4.1.2.3.2 제한사항
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
    A[Title: 플러그용접을 위한 구멍의 직경]
    B["KDS 14 31 25 4.1.2.3.2 (2)"]
  	A ~~~ B
  	end

	  subgraph Variable_def
	  VarIn1[/입력변수: 플러그용접을 위한 구멍의 직경/]
	  VarIn2[/입력변수: 구멍이 있는 판의 두께/]
	  VarIn3[/입력변수: 용접두께/]
	  VarIn4[/입력변수: 최소직경/]
  	end

		Python_Class ~~~ C(["KDS 14 31 25 4.1.2.3.2 (2)"])
		C --> Variable_def

	  Variable_def --> D --> F

  	D{"구멍이 있는 판의 두께+8mm ≤ 플러그용접을 위한 구멍의 직경 ≤ 용접두께x2.25 or 최소직경+3mm"}
  	F(["Pass or Fail"])
    """

    @rule_method
    def diameter_of_holes_for_plug_welding(fIdihopw,fIthpepl,fIwelthi,fImindia) -> RuleUnitResult:
        """플러그용접을 위한 구멍의 직경

        Args:
            fIdihopw (float): 플러그용접을 위한 구멍의 직경
            fIthpepl (float): 구멍이 있는 판의 두께
            fIwelthi (float): 용접 두께
            fImindia (float): 최소 직경

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)   4.1.2.3.2 제한사항 (2)의 판단 결과
        """

        assert isinstance(fIdihopw, float)
        assert isinstance(fIthpepl, float)
        assert isinstance(fIwelthi, float)
        assert isinstance(fImindia, float)

        if (fIthpepl+8) <= fIdihopw <= (fIwelthi*2.25 or fImindia+3) :
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