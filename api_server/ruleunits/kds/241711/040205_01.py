import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_040205_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.2.5 (1)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-19'
    title = '최대지반가속도'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.2 해석 및 설계
    4.2.5 단경간교의 설계규정
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 최대지반가속도]
	  B["KDS 24 17 11 4.2.5 (1)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
		VarOut[/출력변수: 수평지진력/] ;
		VarIn1[/입력변수: 최대지반가속도/] ;
		VarIn2[/입력변수: 유효수평지반가속도/] ;
		VarIn3[/입력변수: 단주기 지반증폭계수/] ;
		VarIn4[/입력변수: 고정하중반력/] ;
		VarOut ~~~ VarIn1
		VarOut ~~~ VarIn2
		VarOut ~~~ VarIn3
		VarOut ~~~ VarIn4
		end

	  Python_Class ~~~ C(["KDS 24 17 11 4.2.5 (1)"])
		C --> Variable_def


	  K["최대지반가속도"] ;
		D{지반 분류} ;
		E["암반지반"] ;
		F["토사지반"] ;
		G["최대지반가속도 = <img src='https://latex.codecogs.com/svg.image?S'>"] ;
		H["최대지반가속도 = <img src='https://latex.codecogs.com/svg.image?S\times&space;F_a'>"] ;
		I["수평지진력 = 고정하중반력 x 최대지반가속도"] ;
		J(["수평지진력"]) ;
		Variable_def --> K --> D --> E & F
		E --> G
		F --> H
		G & H --> I --> J
    """

    @rule_method
    def Peak_ground_acceleration(fIPGA,fIPGB,fIS,fIFa) -> RuleUnitResult:
        """최대지반가속도

        Args:
            fIPGA (float): 최대지반가속도 (암반지반 S1)
            fIPGB (float): 최대지반가속도 (토사지반 S2~S5)
            fIS (float): 유효수평지반가속도
            fIFa (float): 단주기 지반증폭계수

        Returns:
            fOPG (float): 교량내진설계기준(한계상태설계법)  4.2.5 단경간교의 설계규정 (1)의 값
            sOnone (string): 건축물 설계하중  3.5.3 제한사항 (2)의 판단 결과
        """

        assert isinstance(fIS, float)
        assert isinstance(fIFa, float)

        if fIPGA != 0 and fIPGB == 0 :
          fOPG = fIS
          return RuleUnitResult(
              result_variables = {
                  "fOPG": fOPG,
              }
          )

        elif fIPGA != 0 and fIPGB == 0 :
          fOPG = fIS * fIFa
          return RuleUnitResult(
              result_variables = {
                  "fOPG": fOPG,
              }
          )

        else :
          return RuleUnitResult(
              result_variables = {
                  "sOnone": "해당없음",
              }
          )