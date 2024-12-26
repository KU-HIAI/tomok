import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_040303_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.3.3 (1)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-19'
    title = '등가정적 지진하중'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.3 해석방법
    4.3.3 단일모드스펙트럼해석법
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 등가정적 지진하중]
	  B["KDS 24 17 11 4.3.3 (1)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: 등가정적 지진하중/]
	  VarIn1[/입력변수: 스펙트럼 가속도/]
	  VarIn2[/입력변수: 교량의 등가정적 지진하중을 계산하는데 사용되는 계수/]
	  VarIn3[/입력변수: 교량의 주기를 계산하는데 사용되는 계수/]
	  VarIn4[/입력변수: 교량 상부구조와 이의 동적거동에 영향을 주는 하부구조의 단위길이당 고정하중/]
	  VarIn5[/입력변수: 균일한 등분포 하중 po에의한 정적처짐/]

	  VarOut ~~~ VarIn1 & VarIn3 & VarIn5
	  VarIn1 & VarIn3 & VarIn5 ~~~	 VarIn2 & VarIn4
	  end

	  Python_Class ~~~ C(["KDS 24 17 11 4.3.3 (1)"])
		C --> Variable_def


	  Variable_def ---> D --> E
	  D["<img src='https://latex.codecogs.com/svg.image?\rho&space;_e(x)=\frac{\beta&space;S_a}{\gamma}w(x)v_s(x)'>------------------------------------------------------"]
	  E(["<img src='https://latex.codecogs.com/svg.image?\rho&space;_e(x)'>------------"])
    """

    @rule_method
    def Equivalent_static_seismic_load(fISa,fIbeta,fIgamma,fIwx,fIvsx) -> RuleUnitResult:
        """등가정적 지진하중

        Args:
            fISa (float): 스펙트럽가속도
            fIbeta (float): 교량의 등가정적 지진하중을 계산하는데 사용되는 계수
            fIgamma (float): 교량의 주기를 계산하는데 사용되는 계수
            fIwx (float): 교량 상부구조와 이의 동적거동에 영향을 주는 하부구조의 단위길이당 고정하중
            fIvsx (float): 균일한 등분포 하중 po에 의한 정적처짐

        Returns:
            fOpex (float): 교량내진설계기준(한계상태설계법)  4.3.3 단일모드스펙트럼해석법 (1)의 값
        """

        assert isinstance(fISa, float)
        assert isinstance(fIbeta, float)
        assert isinstance(fIgamma, float)
        assert fIgamma != 0
        assert isinstance(fIwx, float)
        assert isinstance(fIvsx, float)


        fOpex = ((fIbeta * fISa) / fIgamma) * fIwx * fIvsx

        return RuleUnitResult(
            result_variables = {
                "fOpex": fOpex,
            }
        )