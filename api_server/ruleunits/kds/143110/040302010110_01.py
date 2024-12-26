import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040302010110_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.3.2.1.1.10 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '단일 ㄱ형강 항복강도'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3 휨부재
    4.3.2 형강 및 강관
    4.3.2.1 단일부재
    4.3.2.1.1 휨강도
    4.3.2.1.1.10 단일ㄱ형강
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[단일ㄱ형강]
	  B["KDS 14 31 10 4.3.2.1.1.10 (1)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수:항복강도/]
	  VarIn1[/입력변수: 압축플랜지 항복강도/]
	  VarIn2[/입력변수: 휨축에 대한 항복모멘트/]
	  VarOut ~~~ VarIn1 & VarIn2
	  end
	  Python_Class ~~~C1(["KDS 14 31 10 4.3.2.1.1.10 (1)"]) -->Variable_def --> D --> E
	  D["<img src='https://latex.codecogs.com/svg.image?&space;M_n=1.5M_y'>--------------------------"]
	  E(["<img src='https://latex.codecogs.com/svg.image?&space;M_n'>--------"])
    """

    @rule_method
    def yield_strength(fIMy)-> RuleUnitResult:
        """단일 ㄱ형강 항복강도

        Args:
            fIMy (float): 휨축에 대한 항복모멘트

        Returns:
            fOMn (float): 강구조부재설계기준(하중저항계수설계법) 4.3.2.1.1.10 단일ㄱ형강 (1)의 값
        """

        assert isinstance(fIMy, float)

        fOMn = 1.5 * fIMy

        return RuleUnitResult(
          result_variables = {
            "fOMn": fOMn,
            }
        )