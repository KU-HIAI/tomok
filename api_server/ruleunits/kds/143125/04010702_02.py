import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_04010702_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.7.2 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '공칭지압강도'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.7 지압강도
    4.1.7.2 확장롤러 및 확장록커
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 공칭지압강도]
	  B["KDS 14 31 25 4.1.7.2 (2)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
    VarOut[/출력변수: 공칭지압강도/]
  	VarIn1[/입력변수: 항복강도/]
  	VarIn2[/입력변수: 투영된 지압면적/]
  	VarOut ~~~ VarIn1 & VarIn2
  	end

    Python_Class ~~~ C(["KDS 14 31 25 4.1.7.2 (2)"])
		C --> Variable_def

	  Variable_def --> G --> D --Pass--> E --> F
  	G["<img src='https://latex.codecogs.com/svg.image?d>635mm'>---------------"]
  	D["Pass or Fail"]
  	E["<img src='https://latex.codecogs.com/svg.image?R_n=30.2(F_y-90)l\sqrt{d}/20'>------------------------------------"]
	  F(["<img src='https://latex.codecogs.com/svg.image?R_n'>---------------"])
    """

    @rule_method
    def nominal_bearing_strength(fIFy,fId,fIl) -> RuleUnitResult:
        """공칭지압강도

        Args:
            fIFy (float): 항복강도
            fId (float): 직경
            fIl (float): 지압길이

        Returns:
            fORn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.1.7.2 확장롤러 및 확장록커 (2)의 값
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.1.7.2 확장롤러 및 확장록커 (2)의 판단 결과
        """

        assert isinstance(fIFy, float)
        assert isinstance(fId, float)
        assert fId > 0
        assert isinstance(fIl, float)

        if fId > 635 :
          fORn = (30.2)*(fIFy-90)*fIl*(fId**0.5)/20

          return RuleUnitResult(
              result_variables = {
                  "fORn": fORn,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )