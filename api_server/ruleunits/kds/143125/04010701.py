import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_04010701(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.7.1'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '공칭지압강도'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.7 지압강도
    4.1.7.1 공장가공면, 핀의 구멍, 지압보강재 등의 지압
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 공칭지압강도]
	  B["KDS 14 31 25 4.1.7.1"]
	  A ~~~ B
	  end

	  subgraph Variable_def
    VarOut[/출력변수: 공칭지압강도/]
	  VarIn1[/입력변수: 항복강도/]
	  VarIn2[/입력변수: 투영된 지압면적/]
	  VarOut ~~~ VarIn1 & VarIn2
	  end

    Python_Class ~~~ C(["KDS 14 31 25 4.1.7.1"])
		C --> Variable_def

	  Variable_def --> E --> D
	  E["<img src='https://latex.codecogs.com/svg.image?R_n=1.8F_yA_{pb}'>-------------------------------------"]
	  D(["<img src='https://latex.codecogs.com/svg.image?R_n'>--------------"])
    """

    @rule_method
    def nominal_bearing_strength(fIFy,fIApb) -> RuleUnitResult:
        """공칭지압강도

        Args:
            fIFy (float): 항복강도
            fIApb (float): 투영된 지압면적

        Returns:
            fORn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.1.7.1 공장가공면, 핀의 구멍, 지압보강재 등의 지압의 값
        """

        assert isinstance(fIFy, float)
        assert isinstance(fIApb, float)

        fORn = (1.8)*fIFy*fIApb

        return RuleUnitResult(
            result_variables = {
                "fORn": fORn,
            }
        )