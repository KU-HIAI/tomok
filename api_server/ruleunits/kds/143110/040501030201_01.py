import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040501030201_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.5.1.3.2.1 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '상대구속 가새 소요모멘트'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5 기타 부재
    4.5.1 기둥과 보의 가새
    4.5.1.3 보 안정용 가새
    4.5.1.3.2 비틀림좌굴 가새
    4.5.1.3.2.1 상대구속 가새
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 상대구속 가새 소요모멘트] ;
		B["KDS 14 31 10 4.5.1.3.2.1 (1)"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarOut1[/출력변수: 소요모멘트/] ;
      VarIn1[/입력변수: 소요휨강도/] ;
      VarIn2[/입력변수: 부재길이/] ;
      VarIn3[/입력변수: 경간 내에서 가새 지점의 수/] ;
      VarIn4[/입력변수: 모멘트 분포에 따른 보정계수/] ;
      VarIn5[/입력변수: 횡적 비지지길이/] ;

			end
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
	  VarIn2 ~~~ VarIn4 & VarIn5

		Python_Class ~~~ C1(["KDS 14 31 10 4.5.1.3.2.1 (1)"]) --> Variable_def

		E["<img src=https://latex.codecogs.com/svg.image?M_{bu}=\frac{0.024M_{u}L}{nC_{b}L_{b}}>--------------------------------"]



		Variable_def --> E --> D(["<img src=https://latex.codecogs.com/svg.image?M_{bu}>----------"])
    """

    @rule_method
    def required_moment_of_relative_restraint_bracing(fIMu,fIL,fIn,fICb,fILb) -> RuleUnitResult:
        """상대구속 가새 소요모멘트

        Args:
            fIMu (float): 소요휨강도
            fIL (float): 부재길이
            fIn (float): 경간 내에서 가새 지점의 수
            fICb (float): 모멘트 분포에 따른 보정계수
            fILb (float): 횡적 비지지길이

        Returns:
            fOMbu (float): 강구조부재설계기준(하중저항계수설계법) 4.5.1.3.2.1 상대구속 가새 (1)의 값
        """

        assert isinstance(fIMu, float)
        assert isinstance(fIL, float)
        assert isinstance(fIn, float)
        assert fIn != 0
        assert isinstance(fICb, float)
        assert fICb != 0
        assert isinstance(fILb, float)
        assert fILb != 0

        fOMbu = (0.024 * fIMu * fIL) / (fIn * fICb * fILb)


        return RuleUnitResult(
            result_variables = {
              "fOMbu": fOMbu,
            }
          )