import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_04010204_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.2.4 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-14'
    title = '용접의 단위길이당 설계강도'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.2 용접
    4.1.2.4 설계강도
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 용접의 단위길이당 설계강도]
	  B["KDS 14 31 25 4.1.2.4(1)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: 용접의 단위길이당 설계강도/]
	  VarIn1[/입력변수: 용접 단위길이당 소요강도/]
	  VarIn2[/입력변수: 저항계수/]
	  VarIn3[/입력변수: 공칭강도/]
	  VarOut ~~~ VarIn1 & VarIn2 & VarIn3
	  end

    Python_Class ~~~ C(["KDS 14 31 25 4.1.2.4(1)"])
		C --> Variable_def

	  Variable_def --> D --> E --> F


	  D["<img src='https://latex.codecogs.com/svg.image?\phi&space;R_n=\phi&space;F_{nw}A_w'>------------------------------------"]
	  E["<img src='https://latex.codecogs.com/svg.image?\phi&space;R_n\geq&space;P_u'>----------------------------"]
		F(["<img src='https://latex.codecogs.com/svg.image?\phi&space;R_n'>----------------------------"])
    """

    @rule_method
    def Design_strength_per_unit_length_of_weld(fIPu,fIphi,fIFnw,fIAw) -> RuleUnitResult:
        """용접의 단위길이당 설계강도

        Args:
            fIPu (float): 용접 단위길이당 소요강도
            fIphi (float): 저항계수
            fIFnw (float): 공칭강도
            fIAw (float): 웨브의 단면적

        Returns:
            fOphiRn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.1.2.4 설계강도 (1)의 값
        """

        assert isinstance(fIPu, float)
        assert isinstance(fIphi, float)
        assert isinstance(fIFnw, float)
        assert isinstance(fIAw, float)

        fOphiRn = max(fIphi*fIFnw*fIAw, fIPu)

        return RuleUnitResult(
            result_variables = {
                "fOphiRn": fOphiRn,
            }
        )