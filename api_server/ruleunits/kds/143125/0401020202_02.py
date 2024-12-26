import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0401020202_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.2.2.2 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '겹침이음의 필릿용접 최대치수'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.2 용접
    4.1.2.2 필릿용접
    4.1.2.2.2 제한사항
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
    A[Title: 겹침이음의 필릿용접 최대치수]
    B["KDS 14 31 25 4.1.2.2.2 (2)"]
  	A ~~~ B
  	end

	  subgraph Variable_def
	  VarOut[/출력변수: 겹침이음의 필릿용접 최대치수/]
	  VarIn[/입력변수: 연단이 용접되는 판의 두께/]
	  VarOut ~~~ VarIn
	  end

		Python_Class ~~~ C(["KDS 14 31 25 4.1.2.2.2 (2)"])
		C --> Variable_def

	  Variable_def --> D
	  D--yes-->E
	  D--no-->F
	  E & F --> G
	  D{"<img src='https://latex.codecogs.com/svg.image?t<6(mm)'>-------------"}
	  E["<img src='https://latex.codecogs.com/svg.image?s=t'>---------"]
	  F["<img src='https://latex.codecogs.com/svg.image?s=t-2(mm)'>-----------------"]
	  G([겹침이음의 필릿용접 최대치수 s])
    """

    @rule_method
    def maximum_fillet_welding_dimensions_of_overlapping_joints(fIt) -> RuleUnitResult:
        """겹침이음의 필릿용접 최대치수

        Args:
            fIt (float): 연단이 용접되는 판의 두께

        Returns:
            fOs (float):  강구조 연결 설계기준(하중저항계수설계법)   4.1.2.2.2 제한사항 (2)의 값
        """

        assert isinstance(fIt, float)


        if fIt < 6 :
          fOs = fIt
          return RuleUnitResult(
              result_variables = {
                  "fOs": fOs,
              }
          )
        else:
          fOs = fIt - 2
          return RuleUnitResult(
              result_variables = {
                  "fOs": fOs,
              }
          )