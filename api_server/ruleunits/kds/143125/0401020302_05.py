import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0401020302_05(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.2.3.2 (5)'
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
    (5)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
    A[Title: 슬롯용접의 제한사항]
    B["KDS 14 31 25 4.1.2.3.2 (5)"]
  	A ~~~ B
  	end

	  subgraph Variable_def
  	VarOut1[/출력변수: 슬롯용접 길이에 횡방향인 슬롯용접선의 최소간격/]
  	VarOut2[/출력변수: 슬롯용접 길이방향의 최소 중심간격/]
  	VarIn1[/입력변수: 슬롯의 폭/]
  	VarIn2[/입력변수: 슬롯 길이/]

  	end

		Python_Class ~~~ C(["KDS 14 31 25 4.1.2.3.2 (5)"])
		C --> Variable_def

	  Variable_def --> D & E

  	D["횡뱡향인 슬롯용접선의 최소간격= 슬롯 폭x4 "]
  	E["슬롯용접선의 길이방향 최소중심간격= 슬롯길이x2"]
    """

    @rule_method
    def Restricton_for_solt_welding(fIslowid,fIslolen) -> RuleUnitResult:
        """슬롯용접의 제한사항

        Args:
            fIslowid (float): 슬롯의 폭
            fIslolen (float): 슬롯 길이

        Returns:
            fOmsswtl (bool): 강구조 연결 설계기준(하중저항계수설계법)   4.1.2.3.2 제한사항 (5)의 값 1
            fOmcldsw (bool): 강구조 연결 설계기준(하중저항계수설계법)   4.1.2.3.2 제한사항 (5)의 값 2
        """

        assert isinstance(fIslowid, float)
        assert isinstance(fIslolen, float)

        fOmsswtl = 4*fIslowid
        fOmcldsw = 2*fIslolen

        return RuleUnitResult(
            result_variables = {
                "fOmsswtl": fOmsswtl,
                "fOmcldsw": fOmcldsw,
            }
        )