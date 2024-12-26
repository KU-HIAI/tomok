import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040501020202(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.5.1.2.2.2'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '절점구속 가새 소요강성'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5 기타 부재
    4.5.1 기둥과 보의 가새
    4.5.1.2 기둥 안정용 가새
    4.5.1.2.2 절점구속 가새
    4.5.1.2.2.2 소요강성
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 절점구속 가새 소요강성] ;
		B["KDS 14 31 10 4.5.1.2.2.2"] ;
		A ~~~ B
		end

    subgraph Variable_def
    VarOut1[/출력변수: 소요강성/] ;
    VarIn1[/입력변수: 하중조합으로 구해진 소요인장강도/] ;
    VarIn2[/입력변수: 비지지길이/] ;
    VarIn3[/입력변수: K값이 1인 기둥의 소요강도에 요구되는 최대 비지지길이/] ;

		end
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3

		Python_Class ~~~ C1(["KDS 24 90 11 4.5.1.2.2.2"]) -->Variable_def


		E["<img src=https://latex.codecogs.com/svg.image?\beta&space;_{bu}=\frac{1}{\phi}(\frac{8P_{u}}{L_{b}})>--------------------------"]
		C{"<img src=https://latex.codecogs.com/svg.image?L_{b}<L_{q}>--------------------------"}



		Variable_def --> C --"No"--> E --> D(["<img src=https://latex.codecogs.com/svg.image?\beta&space;_{bu}>----------"])
		C --"Yes"--> T["<img src=https://latex.codecogs.com/svg.image?\beta&space;_{bu}=\frac{1}{\phi}(\frac{8P_{u}}{L_{q}})>--------------------------"] --> D
    """

    @rule_method
    def required_rigid_of_nodal_restraint_bracing(fIPu,fILb,fILq) -> RuleUnitResult:
        """절점구속 가새 소요강성

        Args:
            fIPu (float): 하중조합으로 구해진 소요인장강도
            fILb (float): 비지지길이
            fILq (float): K값이 1인 기둥의 소요강도에 요구되는 최대 비지지길이

        Returns:
            fObetabu (float): 강구조부재설계기준(하중저항계수설계법) 4.5.1.2.2.2 소요강성의 값
        """

        assert isinstance(fIPu, float)
        assert isinstance(fILb, float)
        assert fILb != 0
        assert isinstance(fILq, float)
        assert fILq != 0

        if fILb > fILq:
          fObetabu = (1 / 0.75) * ((8 * fIPu / fILb))
          return RuleUnitResult(
              result_variables = {
               "fObetabu": fObetabu,
             }
            )
        else:
          fObetabu = (1 / 0.75) * ((8 * fIPu / fILq))
          return RuleUnitResult(
              result_variables = {
                "fObetabu": fObetabu,
             }
            )