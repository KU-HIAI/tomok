import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_040303_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.3.3 (2)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-19'
    title = '교량의 주기'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.3 해석방법
    4.3.3 단일모드스펙트럼해석법
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 교량의 주기]
	  B["KDS 24 17 11 4.3.3 (2)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  arOut[/출력변수: 교량의 주기/]
  	VarIn1[/입력변수: 중력가속도/]
  	VarIn2[/입력변수: 교량 상부구조와 이의 동적거동 영향을 주는 하부구조의 단위길이당 고정하중/]
  	VarIn3[/입력변수: 균일한 등분포하중/]
  	VarIn4[/입력변수: 설계변수/]

  	VarOut ~~~ VarIn1 & VarIn2 ~~~ VarIn3 & VarIn4
  	end

	  Python_Class ~~~ C(["KDS 24 17 11 4.3.3 (2)"])
		C --> Variable_def


	  Variable_def --> E & G --> D --> H
  	D["<img src='https://latex.codecogs.com/svg.image?T=2\pi\sqrt{\frac{\gamma}{\rho&space;_0g\alpha}}'>--------------------"]
  	E["<img src='https://latex.codecogs.com/svg.image?\alpha=\int&space;v_s(x)dx'>--------------------"]
  	G["<img src='https://latex.codecogs.com/svg.image?\gamma=\int&space;w(x)v_s(x)^2dx'>-----------------------"]
  	H([교량의 주기 T])
    """

    @rule_method
    def Bridge_cycle(fIg,fIwx,fIpo,fIalpha,fIgamma) -> RuleUnitResult:
        """교량의 주기

        Args:
            fIg (float): 중력가속도
            fIwx (float): 교량 상부구조와 이의 동적거동에 영향을 주는 하부구조의 단위길이당 고정하중
            fIpo (float): 균일한 등분포하중
            fIalpha (float): 설계변수 ɑ
            fIgamma (float): 설계변수 r

        Returns:
            fOT (float): 교량내진설계기준(한계상태설계법)  4.3.3 단일모드스펙트럼해석법 (2)의 값
        """

        assert isinstance(fIg, float)
        assert fIg > 0
        assert isinstance(fIwx, float)
        assert isinstance(fIpo, float)
        assert fIpo > 0
        assert isinstance(fIalpha, float)
        assert fIalpha > 0
        assert isinstance(fIgamma, float)

        import math

        fOT = 2 * math.pi * (fIgamma / (fIpo * fIg * fIalpha))**0.5

        return RuleUnitResult(
            result_variables = {
                "fOT": fOT,
            }
        )