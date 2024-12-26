import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403020203_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.2.2.3 (3)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-25'
    title = '갭비'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.2 강관 간의 트러스접합
    4.3.2.2 각형강관
    4.3.2.2.3 간격 K형 접합에서 압축력을 받는 지강관
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 갭비]
	  B["KDS 14 31 25 4.3.2.2.3 (3)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
		VarIn1[/입력변수: 유효폭 비/] ;
		VarIn2[/입력변수: 간격/] ;
		VarIn3[/입력변수: 접합평면과 90º를 이루는 각형 강관폭/] ;
		end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.2.2.3 (3)"])
		C --> Variable_def

	  E{"<img src='https://latex.codecogs.com/svg.image?\zeta=g/B\geq&space;0.5(1-\beta&space;_{eff})'>----------------------------------------------------------"} ;

		Variable_def --> E --> D(["PASS or Fail"])
    """

    @rule_method
    def gap_ratio(fIg,fIB,fIbetaef) -> RuleUnitResult:
        """갭비

        Args:
            fIg (float): 간격
            fIB (float): 접합평면과 90°를 이루는 각형 강관폭
            fIbetaef (float): 유효폭 비

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.2.3 간격 K형 접합에서 압축력을 받는 지강관 (3)의 판단 결과
            fOvarsig (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.2.3 간격 K형 접합에서 압축력을 받는 지강관 (3)의 값
        """

        assert isinstance(fIg, float)
        assert isinstance(fIB, float)
        assert fIB != 0
        assert isinstance(fIbetaef, float)

        fOvarsig = fIg/fIB

        if fOvarsig >= 0.5*(1-fIbetaef) :
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )