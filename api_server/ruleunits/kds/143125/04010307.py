import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_04010307(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.3.7'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '인장과 전단 조합 시 마찰접합의 감소계수'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.3 볼트
    4.1.3.7 마찰접합에서 인장과 전단의 조합
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
    A[Title: 인장과 전단 조합 시 마찰접합의 감소계수]
    B["KDS 14 31 25 4.1.3.7"]
  	A ~~~ B
  	end

	  subgraph Variable_def
  	VarOut1[/출력변수: 인장과 전단조합시 마찰접합의 감소계수/]
    VarIn1[/입력변수: 소요인장력/]
    VarIn2[/입력변수: 설계볼트장력/]
    VarIn3[/입력변수: 인장력을 받는 볼트의 수/]
    VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
  	end

		Python_Class ~~~ C(["KDS 14 31 25 4.1.3.7"])
		C --> Variable_def

	  Variable_def --> D --> E

	  D["<img src='https://latex.codecogs.com/svg.image?K_s=1-\frac{T_u}{T_oN_b}'>-------------------------------"]
	  E(["<img src='https://latex.codecogs.com/svg.image?K_s'>----------"])
    """

    @rule_method
    def reduction_coefficient_of_friction_joint_in_tensile_and_shear_combination(fITu,fITo,fINb) -> RuleUnitResult:
        """인장과 전단 조합 시 마찰접합의 감소계수

        Args:
            fITu (float): 소요인장력
            fITo (float): 설계볼트장력
            fINb (float): 인장력을 받는 볼트의 수

        Returns:
            fOKs (float): 강구조 연결 설계기준(하중저항계수설계법)  4.1.3.7 마찰접합에서 인장과 전단의 조합의 값
        """

        assert isinstance(fITu, float)
        assert isinstance(fITo, float)
        assert fITo != 0
        assert isinstance(fINb, float)
        assert fINb != 0

        fOKs = 1-fITu/(fITo*fINb)

        return RuleUnitResult(
            result_variables = {
                "fOKs": fOKs,
            }
        )