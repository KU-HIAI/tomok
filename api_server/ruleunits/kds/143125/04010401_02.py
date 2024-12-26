import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_04010401_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.4.1 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-14'
    title = '접합부재의 인장파단에 대하여 설계인장강도'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.4 접합부재의 설계강도
    4.1.4.1 설계인장강도
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 접합부재의 인장파단에 대하여 설계인장강도]
	  B["KDS 14 31 25 4.1.4.1(2)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: 설계전단강도/]
	  VarIn1[/입력변수: 피접합재의 공칭인장강도/]
	  VarIn2[/입력변수: 유효단면적/]

	  VarOut ~~~ VarIn1 & VarIn2
	  end

    Python_Class ~~~ C(["KDS 14 31 25 4.1.4.1(2)"])
		C --> Variable_def

	  Variable_def --> D --> E
  	D["<img src='https://latex.codecogs.com/svg.image?R_n=F_uA_e'>-------------------------------"]
  	E(["<img src='https://latex.codecogs.com/svg.image?\phi&space;R_n'>--------------"])
    """

    @rule_method
    def Design_tensile_strength_for_tensile_rupture_of_connection(fIFu,fIAe) -> RuleUnitResult:
        """접합부재의 인장파단에 대하여 설계인장강도

        Args:
            fIFu (float): 피접합재의 공칭항복강도
            fIAe (float): 총 단면적

        Returns:
            fORn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.1.4.1 설계인장강도 (2)의 값 1
            fOphi (float): 강구조 연결 설계기준(하중저항계수설계법)  4.1.4.1 설계인장강도 (2)의 값 2
        """

        assert isinstance(fIFu, float)
        assert isinstance(fIAe, float)

        fORn = fIFu * fIAe
        fOphi = 0.75

        return RuleUnitResult(
            result_variables = {
                "fORn": fORn,
            }
        )