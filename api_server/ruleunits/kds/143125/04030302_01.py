import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_04030302_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.3.2 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-25'
    title = '응력상관계수'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.3 강관 간의 모멘트접합
    4.3.3.2 각형강관
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 응력상관계수]
	  B["KDS 14 31 25 4.3.3.2 (1)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
    VarOut1[/출력변수: 응력상관계수/] ;
    end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.3.2 (1)"])
		C --> Variable_def

    E["주강관이 인장인 경우"] ;
    D(["<img src='https://latex.codecogs.com/svg.image?Q_{f}=1.0'>---------------------"]) ;

    Variable_def-->E-->D
    """

    @rule_method
    def stress_correlation_coefficient(fOQf) -> RuleUnitResult:
        """응력상관계수

        Args:
            fOQf (float): 응력상관계수

        Returns:
            fOQf (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.2 각형강관의 값
        """

        fOQf = 1.0

        return RuleUnitResult(
            result_variables = {
                "fOQf": fOQf,
            }
        )