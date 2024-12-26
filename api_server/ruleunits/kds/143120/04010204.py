import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143120_04010204(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 20 4.1.2.4'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '용접지단 사이의 간격'

    description = """
    강구조 피로 및 파단 설계기준(하중저항계수설계법)
    4. 설계(피로 및 파단)
    4.1 피로
    4.1.2 하중유발피로
    4.1.2.4 구속을 줄이기 위한 상세
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 용접지단 사이의 간격];
    B["KDS 14 31 20 4.1.2.4"];
    A ~~~ B
    end

    subgraph Variable_def
    VarIn1[/입력변수: 용접지단 사이의 간격/];

    end

    Python_Class ~~~ C(["KDS 14 31 20 4.1.2.4"])
		C --> Variable_def

		Variable_def --> H

    E([PASS or Fail])

		H{"용접지단 사이의 간격<img src='https://latex.codecogs.com/svg.image?\geq&space;25mm'>-----------------------------"};
	  H-->E
    """

    @rule_method
    def spacing_between_the_welded_joints(fIdiwejo) -> RuleUnitResult:
        """용접지단 사이의 간격

        Args:
            fIdiwejo (float): 용접지단 사이의 간격

        Returns:
            pass_fail (bool): 강구조 피로 및 파단 설계기준(하중저항계수설계법)  4.1.2.4 구속을 줄이기 위한 상세의 판단 결과
        """

        assert isinstance(fIdiwejo, float)

        if fIdiwejo >= 25:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )