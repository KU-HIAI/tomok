import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_04010402_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.4.2 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-14'
    title = '접합부재의 전단항복에 대하여 설계전단강도'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.4 접합부재의 설계강도
    4.1.4.2 설계전단강도
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 접합부재의 전단항복에 대하여 설계전단강도]
	  B["KDS 14 31 25 4.1.4.2 (1)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: 설계전단강도/]
	  VarIn1[/입력변수: 저항계수/]
	  VarIn2[/입력변수: 핀의 항복강도/]
	  VarIn3[/입력변수: 전단력을 받는 총단면적/]
	  VarOut & VarIn1 ~~~ VarIn2 & VarIn3
	  end

    Python_Class ~~~ C(["KDS 14 31 25 4.1.4.2 (1)"])
		C --> Variable_def

	  Variable_def --> D
	  D["<img src='https://latex.codecogs.com/svg.image?R_n=0.60F_yA_{gv}'>-------------------------------"]
    """

    @rule_method
    def Design_shear_strength_for_shear_yielding_of_connection(fIFy,fIAgv) -> RuleUnitResult:
        """접합부재의 전단항복에 대하여 설계전단강도

        Args:
            fIFy (float): 핀의 항복강도
            fIAgv (float): 전단력을 받는 총단면적

        Returns:
            fORn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.1.4.2 설계전단강도 (1)의 값 1
            fOphi (float): 강구조 연결 설계기준(하중저항계수설계법)  4.1.4.2 설계전단강도 (1)의 값 2
        """

        assert isinstance(fIFy, float)
        assert isinstance(fIAgv, float)

        fORn = 0.60 * fIFy * fIAgv
        fOphi = 1.0

        return RuleUnitResult(
            result_variables = {
                "fORn": fORn,
                "fOphi": fOphi,
            }
        )