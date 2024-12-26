import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403020101_06(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.2.1.1 (6)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-25'
    title = '폭 비'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.2 강관 간의 트러스접합
    4.3.2.1 원형강관
    4.3.2.1.1 적용한계
    (6)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 폭 비]
	  B["KDS 14 31 25 4.3.2.1.1 (6)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
		VarIn1[/입력변수: 폭 비/] ;
	  VarIn2[/입력변수: 원형 지강관의 외경/]
	  VarIn3[/입력변수: 바깥지름/]
		end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.2.1.1 (6)"])
		C --> Variable_def

	  E{"접합형상"} ;
    D{"<img src='https://latex.codecogs.com/svg.image?0.2<D_{b}/D\leq&space;1.0'>----------------------------------------------"} ;
    F{"<img src='https://latex.codecogs.com/svg.image?0.4<D_{b}/D\leq&space;1.0'>----------------------------------------------"} ;
		Variable_def --> E
    E--T, Y, X, 겹침 K형 접합-->D
    E--간격 K형 접합-->F
		F & D --> Q(["PASS or Fail"])
    """

    @rule_method
    def width_ratio(fIbetaA,fIbetaB,fIDb,fID) -> RuleUnitResult:
        """폭 비

        Args:
            fIbetaA (float): 폭비 (T, Y, K-형 이음)
            fIbetaB (float): 폭비 (X형 접합)
            fIDb (float): 원형 지강관의 외경
            fID (float): 바깥지름

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.1.1 적용한계 (6)의 판단 결과
        """

        assert isinstance(fIbetaA, float)
        assert isinstance(fIbetaB, float)
        assert isinstance(fIDb, float)
        assert isinstance(fID, float)
        assert fID != 0

        if fIbetaA != 0 and fIbetaB == 0 :
          if 0.2 < fIDb / fID <= 1.0:
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

        if fIbetaA == 0 and fIbetaB != 0 :
          if 0.4 < fIDb / fID <= 1.0:
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

        else:
          return RuleUnitResult(
                result_variables = {
                    "pass_fail": False,
                }
            )