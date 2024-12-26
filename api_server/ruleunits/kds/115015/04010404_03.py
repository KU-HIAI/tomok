import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS115015_04010404_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 11 50 15 4.1.4.4 (3)'
    ref_date = '2021-05-12'
    doc_date = '2024-02-07'
    title = '강말뚝의 단기 허용압축응력'

    description = """
    깊은기초 설계기준(일반설계법)
    4. 설계
    4.1 말뚝기초
    4.1.4 말뚝재료의 허용응력
    4.1.4.4 강말뚝
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 강말뚝의 단기 허용압축응력];
    B["KDS 11 50 15 4.1.4.4 (3)"];
    A ~~~ B
    end

		subgraph Variable_def;

		VarOut1[/출력변수: 강말뚝의 단기 허용압축응력/]
    VarIn1[/입력변수: 강말뚝의 장기 허용압축응력/] ;

		VarOut1~~~VarIn1

		end
		Python_Class ~~~ C(["KDS 11 50 15 4.1.4.4 (3)"])
		C --> Variable_def;

		E["강말뚝의 단기 허용압축응력 = 강말뚝의 장기 허용압축응력X1.5"]

		Variable_def --> E
	  E--->D
    D(["강말뚝의 단기 허용압축응력"])
    """

    @rule_method
    def short_term_allowable_compressive_stress_of_steel_pile(fIlacssp) -> RuleUnitResult:
        """강말뚝의 단기 허용압축응력

        Args:
            fIlacssp (float): 강말뚝의 장기 허용압축응력

        Returns:
            fOsacssp (float): 깊은기초 설계기준(일반설계법)  4.1.4.4 강말뚝 (3)의 값
        """

        assert isinstance(fIlacssp, float)

        fOsacssp = fIlacssp * 1.5

        return RuleUnitResult(
            result_variables = {
                "fOsacssp": fOsacssp,
            }
        )