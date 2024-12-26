import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0401020202_05(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.2.2.2 (5)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '필릿용접의 유효길이'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.2 용접
    4.1.2.2 필릿용접
    4.1.2.2.2 제한사항
    (5)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
    A[Title: 필릿용접의 유효길이]
    B["KDS 14 31 25 4.1.2.2.2 (5)"]
  	A ~~~ B
  	end

	  subgraph Variable_def
	  VarIn1[/입력변수: 부재단부에 용접된 필릿용접의 길이/]
	  VarIn2[/입력변수: 용접치수/]
	  VarIn3[/입력변수: 실제 용접된 길이/]
	  VarIn4[/입력변수: 유효길이/]
	  VarIn5[/입력변수: 감소계수/]
	  VarIn6[/입력변수: 필릿용접의 유효길이/]
	  VarIn7[/입력변수: 용접길이/]
	  VarIn5 ~~~ VarIn1 & VarIn2
	  VarIn1 & VarIn2 ~~~ VarIn3 & VarIn4
  	end

		Python_Class ~~~ C(["KDS 14 31 25 4.1.2.2.2 (5)"])
		C --> Variable_def

	  Variable_def --> D & E & F
	  D --> H
	  E --> G
	  F --> J
	  H --> K
	  G--> I --> K
	  J --> K
	  D{"용접길이 ≤ 용접치수x100"}
	  E{"용접치수x100 < 용접길이 ≤용접치수x300"}
	  F{"용접길이 > 용접치수x300"}
	  G["<img src='https://latex.codecogs.com/svg.image?\beta=1.2-0.002\left(\frac{l}{z}\right)\leq&space;1.0'>-------------------------------------------------------"]
	  H["실제 용접된 길이= 유효길이"]
	  I["용접길이 x β =필릿용접의 유효길이"]
	  J["용접치수x180=필릿용접의 유효길이"]
  	K([필릿용접의 유효길이])
    """

    @rule_method
    def Effective_length_of_fillet_weld(fIl,fIz,fIacwele,fIwellen) -> RuleUnitResult:
        """필릿용접의 유효길이

        Args:
            fIl (float): 부재 단부에 용접된 필릿용접의 길이
            fIz (float): 용접치수
            fIacwele (float): 실제 용접된 길이
            fIwellen (float): 용접길이

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)   4.1.2.2.2 제한사항 (5)의 판단 결과
            fOeflefw (float): 강구조 연결 설계기준(하중저항계수설계법)   4.1.2.2.2 제한사항 (5)의 값 1
            fObeta (float): 강구조 연결 설계기준(하중저항계수설계법)   4.1.2.2.2 제한사항 (5)의 값 2
        """

        assert isinstance(fIl, float)
        assert isinstance(fIz, float)
        assert fIz != 0
        assert isinstance(fIacwele, float)
        assert isinstance(fIwellen, float)

        fObeta = 1.2-0.002*(fIl/fIz)

        if fIl <= 100*fIz :
          fOeflefw = fIacwele

        if 100*fIz < fIwellen <= 300*fIz :
          if fObeta <= 1.0 :
            fOeflefw = fIacwele*fObeta
            return RuleUnitResult(
                result_variables = {
                    "fOeflefw": fOeflefw,
                    "pass_fail": True,
                }
            )
          else:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": False,
                }
            )

        if 300*fIz < fIwellen  :
          fOeflefw = fIz*180

        return RuleUnitResult(
            result_variables = {
                "fOeflefw": fOeflefw,
            }
        )