import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040501030202(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.5.1.3.2.2'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '비보강 웨브의 뒤틀림강성도'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5. 기타 부재
    4.5.1 기둥과 보의 가새
    4.5.1.3 보 안정용 가새
    4.5.1.3.2 비틀림좌굴 가새
    4.5.1.3.2.2 연속 비틀림좌굴 가새
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 비보강 웨브의 뒤틀림강성도] ;
		B["KDS 14 31 10 4.5.1.3.2.2"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarOut1[/출력변수: 비보강 웨브의 뒤틀림강성도/] ;
      VarIn1[/입력변수: 강재의 탄성계수/] ;
      VarIn2[/입력변수: 플랜지 도심간의 거리/] ;
      VarIn3[/입력변수: 보 웨브의 두께/] ;

			end
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3

		Python_Class ~~~ C1(["KDS 14 31 10 4.5.1.3.2.2"])--> Variable_def

		E["<img src=https://latex.codecogs.com/svg.image?\beta&space;_{sec}=\frac{3.3Et_{w}^{3}}{12h_{o}}>--------------------------------"]

		Variable_def --> E --> D(["<img src=https://latex.codecogs.com/svg.image?\beta&space;_{sec}>----------"])
    """

    @rule_method
    def Torsional_stiffness_of_unreinforced_web(fIE,fIho,fItw) -> RuleUnitResult:
        """비보강 웨브의 뒤틀림강성도

        Args:
            fIE (float): 강재의 탄성계수
            fIho (float): 플랜지 도심간의 거리
            fItw (float): 보 웨브의 두께

        Returns:
            fObetasec (float): 강구조부재설계기준(하중저항계수설계법) 4.5.1.3.2.2 연속 비틀림좌굴 가새의 값
        """

        assert isinstance(fObetasec, float)
        assert isinstance(fIE, float)
        assert isinstance(fIho, float) and fIho != 0

        assert isinstance(fItw, float)


        fObetasec = (3.3 * fIE * fItw ** 3) / (12 * fIho)


        return RuleUnitResult(
            result_variables = {
              "fObetasec": fObetasec,
            }
          )