import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_04010401(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.4.1'
    ref_date = '2017-12-20'
    doc_date = '2024-02-14'
    title = '접합부재의 설계인장강도'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.4 접합부재의 설계강도
    4.1.4.1 설계인장강도
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 접합부재의 설계인장강도]
	  B["KDS 14 31 25 4.1.4.1"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: 설계전단강도/]
	  VarOut
	  end

    Python_Class ~~~ C(["KDS 14 31 25 4.1.4.1"])
		C --> Variable_def

	  Variable_def --> D --> E
	  D{"인장항복과 인장파단의 한계상태에 따라 작은 값"}
	  E(["<img src='https://latex.codecogs.com/svg.image?\phi&space;R_n'>---------------------------"])
    """

    @rule_method
    def Design_tensile_strength_of_connection(fIphiRnA,fIphiRnB) -> RuleUnitResult:
        """접합부재의 설계인장강도

        Args:
            fIphiRnA (float): 접합부재의 설계인장강도 (접합부재의 인장항복에 대하여)
            fIphiRnB (float): 접합부재의 설계인장강도 (접합부재의 인장파단에 대하여)

        Returns:
            fOphiRn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.1.4.1 설계인장강도의 값
        """

        fOphiRn = min(fIphiRnA, fIphiRnB)

        return RuleUnitResult(
            result_variables = {
                "fOphiRn": fOphiRn,
            }
        )