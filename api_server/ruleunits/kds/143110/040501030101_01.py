import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040501030101_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.5.1.3.1.1 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '상대구속 가새 소요강도'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5 기타 부재
    4.5.1 기둥과 보의 가새
    4.5.1.3 보 안정용 가새
    4.5.1.3.1 횡좌굴 가새
    4.5.1.3.1.1 상대구속 가새
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 상대구속 가새 소요강도] ;
		B["KDS 14 31 10 4.5.1.3.1.1 (1)"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarOut1[/출력변수: 상대구속 가새 소요강도/] ;
      VarIn1[/입력변수: 소요휨강도/] ;
      VarIn2[/입력변수: 변곡점에 가장 가까운 가새에 적용/] ;
      VarIn3[/입력변수: 플랜지 도심간의 거리/] ;

			end
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3

		Python_Class ~~~ C1(["KDS 14 31 10 4.5.1.3.1.1 (1)"]) -->Variable_def


		E["<img src=https://latex.codecogs.com/svg.image?P_{bu}=0.008M_{u}C_{d}/h_{o}>--------------------------------"]


		Variable_def --> E --> D(["<img src=https://latex.codecogs.com/svg.image?P_{bu}>----------"])
    """

    @rule_method
    def required_strength_of_relative_restraint_bracing(fIMu,fICd,fIho) -> RuleUnitResult:
        """상대구속 가새 소요강도

        Args:
            fIMu (float): 소요휨강도
            fICd (float): 변곡점에 가장 가까운 가새에 적용
            fIho (float): 플랜지 도심간의 거리

        Returns:
            fOPbu (float): 강구조부재설계기준(하중저항계수설계법) 4.5.1.3.1.1 상대구속 가새 (1)의 값
        """

        assert isinstance(fIMu, float)
        assert isinstance(fICd, float)
        assert isinstance(fIho, float)

        fOPbu = 0.008 * fIMu * fICd / fIho


        return RuleUnitResult(
            result_variables = {
                "fOPbu": fOPbu,
            }
        )