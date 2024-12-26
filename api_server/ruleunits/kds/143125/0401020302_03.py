import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0401020302_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.2.3.2 (3)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '플러그용접의 최소 중심간격'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.2 용접
    4.1.2.3 플러그 및 슬롯용접
    4.1.2.3.2 제한사항
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
    A[Title: 플러그용접의 최소 중심간격]
    B["KDS 14 31 25 4.1.2.3.2 (3)"]
  	A ~~~ B
  	end

	  subgraph Variable_def
  	VarOut[/출력변수: 플러그용접의 최소 중심간격/]
	  VarIn[/입력변수: 공칭구멍직경/]
	  VarOut ~~~ VarIn
	  end

		Python_Class ~~~ C(["KDS 14 31 25 4.1.2.3.2 (3)"])
		C --> Variable_def

	  Variable_def --> D --> F

  	D["플러그용접의 최소 중심간격 = 공칭구멍직경x4"]
	  F([플러그용접의 최소 중심간격])
    """

    @rule_method
    def Minimum_center_spacing_for_plug_welding(fInohodi) -> RuleUnitResult:
        """플러그용접의 최소 중심간격

        Args:
            fInohodi (float): 공칭구멍직경

        Returns:
            fOmicspw (float): 강구조 연결 설계기준(하중저항계수설계법)   4.1.2.3.2 제한사항 (3)의 값
        """

        assert isinstance(fInohodi, float)

        fOmicspw = 4 * fInohodi

        return RuleUnitResult(
            result_variables = {
                "fOmicspw": fOmicspw,
            }
        )