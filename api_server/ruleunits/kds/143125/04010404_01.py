import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_04010404_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.4.4 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-15'
    title = '접합부재의 압축강도'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.4 접합부재의 설계강도
    4.1.4.4 설계압축강도
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 접합부재의 압축강도]
	  B["KDS 14 31 25 4.1.4.4(1)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: 압축강도/]
	  VarIn1[/입력변수: 유효좌굴길이계수/]
	  VarIn2[/입력변수: 지간길이/]
	  VarIn3[/입력변수: 좌굴축에 대한 단면2차반경/]
	  VarIn4[/입력변수: 핀의 항복강도/]
	  VarIn5[/입력변수: 부재의 총단면적/]
	  VarOut ~~~ VarIn1 & VarIn2 & VarIn3
	  VarIn2 ~~~ VarIn4 & VarIn5

	  end

    Python_Class ~~~ C(["KDS 14 31 25 4.1.4.4(1)"])
		C --> Variable_def

	  Variable_def --> D --Yes--> E --> F

	  D{"<img src='https://latex.codecogs.com/svg.image?KL/r\leq&space;25'>----------------------"}
	  E["<img src='https://latex.codecogs.com/svg.image?P_n=F_yA_g'>------------------------------------------"]
	  F(["<img src='https://latex.codecogs.com/svg.image?P_n'>-----------"])
    """

    @rule_method
    def Compressive_strength_of_joint(fIK,fIL,fIr,fIFy,fIAg) -> RuleUnitResult:
        """접합부재의 압축강도

        Args:
            fIK (float): 유효좌굴길이계수
            fIL (float): 지간길이
            fIr (float): 좌굴축에 대한 단면2차반경
            fIFy (float): 핀의 항복강도
            fIAg (float): 부재의 총단면적

        Returns:
            fOPn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.1.4.4 접합부재의 압축강도 (1)의 값
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.1.4.4 접합부재의 압축강도 (1)의 판단 결과
        """

        assert isinstance(fIK, float)
        assert isinstance(fIL, float)
        assert isinstance(fIr, float)
        assert fIr > 0
        assert isinstance(fIFy, float)
        assert isinstance(fIAg, float)

        if fIK * fIL / fIr <= 25 :
          fOPn = fIFy * fIAg
          return RuleUnitResult(
              result_variables = {
                  "fOPn": fOPn,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )