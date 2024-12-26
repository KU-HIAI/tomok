import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_0401050101(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.1.5.1.1'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '인장파단에 대한 공칭인장강도'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.1 인장부재
    4.1.5 핀접합부재
    4.1.5.1.1 유효순단면적에 대한 인장파단
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[유효순단면적에 대한 인장파단] ;
		B["KDS 14 31 10 4.1.5.1.1"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarOut1[/출력변수: 인장파단에 대한 공칭인장강도/]
    VarIn1[/입력변수: 판재의 두께/]
    VarIn2[/입력변수: 유효연단거리/]
    VarIn3[/입력변수: 인장강도/]
		end

		Python_Class ~~~ D(["KDS 14 31 10 4.1.5.1.1"])---> Variable_def
	  C(["<img src='https://latex.codecogs.com/svg.image?P_{n}=2tb_{eff}F_{u}'>---------------------------------"])
	  Variable_def-->C
    """

    @rule_method
    def Nominal_tensile_strength_to_tensile_rupture(fIt,fIbeff,fIFu) -> RuleUnitResult:
        """인장파단에 대한 공칭인장강도

        Args:
            fIt (float): 판재의 두께
            fIbeff (float): 유효연단거리
            fIFu (float): 인장강도

        Returns:
            fOPn (float): 강구조부재설계기준(하중저항계수설계법)  4.1.5.1.1 유효순단면적에 대한 인장파단의 값
        """

        assert isinstance(fIt, float)
        assert isinstance(fIbeff, float)
        assert isinstance(fIFu, float)

        fOPn = 2 * fIt * fIbeff * fIFu

        return RuleUnitResult(
            result_variables = {
              "fOPn": fOPn,
            }
        )