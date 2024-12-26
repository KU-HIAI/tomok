import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040501030101_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.5.1.3.1.1 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '상대구속 가새 소요강성'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5 기타 부재
    4.5.1 기둥과 보의 가새
    4.5.1.3 보 안정용 가새
    4.5.1.3.1 횡좌굴 가새
    4.5.1.3.1.1 상대구속 가새
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 상대구속 가새 소요강성] ;
		B["KDS 14 31 10 4.5.1.3.1.1 (2)"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarOut1[/출력변수: 상대구속 가새 소요강성/] ;
      VarIn1[/입력변수: 강도저항계수/] ;
      VarIn2[/입력변수: 소요휨강도/] ;
      VarIn3[/입력변수: 변곡점에 가장 가까운 가새에 적용/] ;
      VarIn4[/입력변수: 횡적 비지지길이/] ;
      VarIn5[/입력변수: 플랜지 도심간의 거리/] ;

			end
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3 ~~~ VarIn4 & VarIn5

		Python_Class ~~~ C1(["KDS 14 31 10 4.5.1.3.1.1 (2)"]) --> Variable_def

		E["<img src=https://latex.codecogs.com/svg.image?\beta&space;_{bu}=\frac{1}{\phi}\left(\frac{4M_{u}C_{d}}{L_{b}h_{o}}\right)>--------------------------------"]

		Variable_def --> E --> D(["<img src=https://latex.codecogs.com/svg.image?\beta&space;_{bu}>----------"])
    """

    @rule_method
    def required_rigid_of_relative_restraint_bracing(fIphi,fIMu,fICd,fILb,flho) -> RuleUnitResult:
        """상대구속 가새 소요강성

        Args:
            fIphi (float): 강도저항계수
            fIMu (float): 소요휨강도
            fICd (float): 변곡점에 가장 가까운 가새에 적용
            fILb (float): 횡적 비지지길이
            flho (float): 플랜지 도심간의 거리

        Returns:
            fObetabu (float): 강구조부재설계기준(하중저항계수설계법) 4.5.1.3.1.1 상대구속 가새 (2)의 값
        """

        assert isinstance(fIphi, float)
        assert fIphi != 0
        assert isinstance(fIMu, float)
        assert isinstance(fICd, float)
        assert isinstance(fILb, float)
        assert fILb != 0
        assert isinstance(flho, float)
        assert flho != 0

        fObetabu = (1 / fIphi) * ((4 * fIMu * fICd) / (fILb * flho))


        return RuleUnitResult(
              result_variables = {
               "fObetabu": fObetabu,
             }
        )