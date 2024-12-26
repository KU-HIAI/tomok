import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241710_0203_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 10 2.3 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-20'
    title = '등가정적 지진하중 및 교량의 주기'

    description = """
    교량 내진설계기준(일반설계법)
    2. 설계
    2.3 해석방법
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 등가정적 지진하중 및 교량의 주기]
	  B["KDS 24 17 10 2.3 (3)"]
	  A ~~~ B
	  end

	  subgraph Variable_def;
		VarOut1[/출력변수:등가정적 지진하중/]
		VarIn1[/입력변수:탄성지진 응답계수/]
		VarIn2[/입력변수:중력가속도/]
		VarIn3[/입력변수:교량상부구조와 이의 동적거동에 영향을 주는 하부구조의 단위길이당 고정하중/]
		VarIn4[/입력변수:균일한 등분포하중 po에 의한 정적처짐/]

		VarOut1 ~~~
		VarIn1 & VarIn2 &	VarIn3 & VarIn4

    end

	  Python_Class ~~~ C(["KDS 24 17 10 2.3 (3)"])
		C --> Variable_def


	  H["<img src='https://latex.codecogs.com/svg.image?p_{e}(x)=\frac{\beta&space;C_{s}}{r}w(x)v_{s}(x)'>---------------------------------"]
		D["<img src='https://latex.codecogs.com/svg.image?T=2\pi\sqrt{\frac{r}{p_{o}q\alpha}}'>---------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?\beta=\int&space;w(x)v_{s}(x)dx'>---------------------------------"]
		F["<img src='https://latex.codecogs.com/svg.image?r=\int&space;w(x)v_{s}(x)^{2}dx'>---------------------------------"]
		G([등가정적 지진하중])
		I([교량의 주기])
		D~~~ |"KDS 24 12 10 2.3(2) 식 2.3-1"| D

		Variable_def ---> E & F
		F ---> D ---> I
		E ---> H ---> G
    """

    @rule_method
    def Elastic_seismic_response_coefficient_and_period_of_bridge(fICs,fIg,fIw,fIVs,fIalpha,fIbeta,fIgamma,fIpo) -> RuleUnitResult:
        """등가정적 지진하중 및 교량의 주기

        Args:
            fICs (float): 탄성지진 응답계수
            fIg (float): 중력가속도
            fIw (float): 교량상부구조와 이의 동적거동에 영향을 주는 하부구조의 단위길이당 고정하중
            fIVs (float): 균일한 등분포하중 po에 의한 정적처짐
            fIalpha (float): 설계변수 ɑ
            fIbeta (float): 교량의 등가정적 지진하중을 계산하는데 사용되는 계수
            fIgamma (float): 교량의 주기를 계산하는데 사용되는 계수
            fIpo (float): 균일한 등분포하중

        Returns:
            fOPe (float): 교량 내진설계기준(일반설계법)  2.3 해석방법 (3)의 값 1
            fOT (float): 교량 내진설계기준(일반설계법)  2.3 해석방법 (3)의 값 2
        """

        assert isinstance(fICs, float)
        assert isinstance(fIg, float)
        assert fIg != 0
        assert isinstance(fIw, float)
        assert isinstance(fIVs, float)
        assert isinstance(fIalpha, float)
        assert fIalpha != 0
        assert isinstance(fIbeta, float)
        assert isinstance(fIgamma, float)
        assert fIgamma != 0
        assert isinstance(fIpo, float)
        assert fIpo != 0

        import math

        fOPe = fIbeta * fICs / fIgamma * fIw * fIVs
        fOT = 2 * math.pi * (fIgamma / (fIpo * fIg * fIalpha))**0.5

        return RuleUnitResult(
            result_variables = {
                "fOPe": fOPe,
                "fOT": fOT,
            }
        )