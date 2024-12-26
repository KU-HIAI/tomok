import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040501020201(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.5.1.2.2.1'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '절점구속 가새 소요강도'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5. 기타 부재
    4.5.1 기둥과 보의 가새
    4.5.1.2 기둥 안정용 가새
    4.5.1.2.2 절점구속 가새
    4.5.1.2.2.1 소요강도
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 절점구속 가새 소요강도] ;
		B["KDS 14 31 10 4.5.1.2.2.1"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarOut1[/출력변수: 소요강도/] ;
      VarIn1[/입력변수: 하중조합으로 구해진 소요인장강도/] ;

			end
		VarOut1 ~~~ VarIn1

		Python_Class ~~~ C1(["KDS 14 31 10 4.5.1.2.2.1"]) --> Variable_def


		E["<img src=https://latex.codecogs.com/svg.image?P_{bu}=0.01P_{u}>--------------------"]



		Variable_def --> E --> D(["<img src=https://latex.codecogs.com/svg.image?P_{bu}>------------"])
    """

    @rule_method
    def required_strength_of_nodal_restraint_bracing(fIPu) -> RuleUnitResult:
        """절점구속 가새 소요강도

        Args:
            fIPu (float): 하중조합으로 구해진 소요인장강도

        Returns:
            fOPbu (float): 강구조부재설계기준(하중저항계수설계법) 4.5.1.2.2.1 소요강도의 값
        """

        assert isinstance(fIPu, float)

        fOPbu = 0.01 * fIPu

        return RuleUnitResult(
          result_variables = {
            "fOPbu": fOPbu,
          }
        )